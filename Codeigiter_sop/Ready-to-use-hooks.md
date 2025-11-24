Good — when the attacker **rotates public IPs** rapidly, IP-blocking alone becomes ineffective. You need to combine **edge protection, behavioral fingerprinting, and challenge-based checks** so bots fail even when IPs change.

Below is a practical, prioritized playbook plus ready-to-drop CodeIgniter code (a **hook**) that implements **Redis-backed behavioral fingerprinting + rate limits + temporary bans**, and a simple **JS challenge** idea. Apply the items in order — each step raises the bar the attacker must clear.

# 1) Highest-impact, easiest first (do this now)

1. Put the endpoint behind Cloudflare (or any CDN/WAF) and enable:

   * Bot Management / JS Challenge / “Under Attack” mode.
   * Rate-limiting rules for the path (e.g. 20 req/min per IP) with challenge.
     These force bots to run JS and stop many rotating-IP attackers.

2. Add an app-level **fingerprint + rate-limit** (not IP-only). Fingerprint combines IP, UA, headers and request body hash — rotating IPs won’t hide identical request patterns.

3. Add a **JavaScript token challenge** for non-API pages: serve a page that requires a JS fetch to get a short-lived token (stored in cookie or header). Bots that don’t run JS will fail.

# 2) Defensive layers (add when possible)

* Require API keys or HMAC signatures for non-public endpoints.
* CAPTCHA (reCAPTCHA v2/v3 or hCaptcha) for forms or heavy endpoints.
* Use Redis for counters and temporary bans (fast and scalable).
* Use WAF rules to block suspicious patterns, countries or ASNs if relevant.
* Add behavior analytics: throttle requests by fingerprint, not IP.

# 3) Monitoring & mitigation

* Log `fingerprint, IP, UA, path, body-hash, timestamp` to analyze patterns.
* Use Fail2Ban for log-scan-based bans if you still see abusive single-IP bursts.
* If attacks escalate, consider progressive challenges (first 1 req triggers JS token, more reqs triggers CAPTCHA).

---

# Ready-to-use CodeIgniter Hook (Redis): fingerprint + rate limit + temp ban

Drop this as an application hook (call it `application/hooks/anti_bot.php`). It:

* builds a fingerprint (UA + accept-language + body hash)
* counts requests per fingerprint in Redis with sliding window
* if threshold exceeded, sets a temporary ban for that fingerprint (and optionally the IP)
* rejects with 429 or 403

```php
<?php
// application/hooks/anti_bot.php

defined('BASEPATH') OR exit('No direct script access allowed');

class Anti_bot_hook
{
    protected $ci;
    protected $redis;
    protected $limit = 60;     // allowed requests
    protected $window = 60;    // seconds
    protected $ban_ttl = 600;  // seconds to ban when exceeded

    public function __construct()
    {
        // get CodeIgniter instance
        $this->ci =& get_instance();

        // connect to Redis (phpredis)
        $this->redis = new Redis();
        try {
            $this->redis->connect('127.0.0.1', 6379);
            // auth if needed: $this->redis->auth('password');
        } catch (Exception $e) {
            // Redis down: fail open or fallback to DB / allow small rate limiting
            return;
        }
    }

    public function protect()
    {
        // only protect certain URIs (tweak as needed)
        $uri = uri_string();
        // e.g. protect /api/submit or a specific controller/method
        $protected_paths = [
            'api/submit',
            'login',
            'register',
        ];
        $is_protected = false;
        foreach ($protected_paths as $p) {
            if (strpos($uri, $p) === 0) {
                $is_protected = true; break;
            }
        }
        if (!$is_protected) return;

        $ip = $this->ci->input->ip_address();
        $ua = $this->ci->input->user_agent();
        $al = $this->ci->input->server('HTTP_ACCEPT_LANGUAGE') ?: '';
        $body = file_get_contents('php://input');
        $body_hash = $body ? hash('sha256', $body) : '';

        // fingerprint: UA + accept-language + body-hash (omit IP to handle rotating IPs)
        $finger = substr(hash('sha256', $ua . '|' . $al . '|' . $body_hash), 0, 32);

        $ban_key = "ban:f:$finger";       // ban by fingerprint
        $count_key = "rl:f:{$finger}";

        // If fingerprint is banned, reject immediately
        if ($this->redis->exists($ban_key)) {
            $this->reject(403, "Forbidden");
        }

        // Increment request counter (atomic)
        $cur = $this->redis->incr($count_key);
        if ($cur == 1) {
            $this->redis->expire($count_key, $this->window);
        }

        // If limit exceeded, set ban and optionally ban IP for shorter time
        if ($cur > $this->limit) {
            $this->redis->setex($ban_key, $this->ban_ttl, time());
            // optional: ban ip too (shorter)
            $ip_ban_key = "ban:ip:{$ip}";
            $this->redis->setex($ip_ban_key, min($this->ban_ttl, 120), time());

            // Optionally log to DB or file for analysis
            log_message('warning', "AntiBot: fingerprint {$finger} exceeded limit; ip {$ip} temporarily banned.");

            $this->reject(429, "Too many requests");
        }

        // Optional: if UA contains suspicious token like 'curl' block and set small ban
        $lower_ua = strtolower($ua ?: '');
        $bad_ua_tokens = ['curl', 'wget', 'python-requests', 'libwww-perl', 'httpclient'];
        foreach ($bad_ua_tokens as $t) {
            if (strpos($lower_ua, $t) !== false) {
                $this->redis->setex($ban_key, 3600, time());
                $this->reject(403, "Forbidden");
            }
        }
    }

    protected function reject($code = 429, $msg = "Too many requests")
    {
        // Respect JSON responses for API endpoints
        $this->ci->output
            ->set_content_type('application/json')
            ->set_status_header($code)
            ->set_output(json_encode(['error' => $msg]));
        // send immediately
        $this->ci->output->_display();
        exit;
    }
}
```

Then configure the hook in `application/config/hooks.php`:

```php
$hook['post_controller_constructor'][] = array(
    'class'    => 'Anti_bot_hook',
    'function' => 'protect',
    'filename' => 'anti_bot.php',
    'filepath' => 'hooks',
    'params'   => array()
);
```

Notes:

* This **does not rely on IP** alone — it fingerprints the request content and UA, so rotating IPs won't help if the requests are identical.
* Tune `$limit`, `$window`, and `$ban_ttl` to your traffic profile.
* Optionally extend fingerprint with `Accept` header, cookies, or other headers you trust.

---

# JS challenge approach (simple, effective)

1. When a client requests a sensitive endpoint page, serve a lightweight page that runs:

```html
<script>
fetch('/get-js-token', {credentials:'include'})
  .then(r => r.json())
  .then(j => {
     document.cookie = "js_token=" + j.token + ";path=/";
     // continue with normal app behavior (or redirect)
  });
</script>
```

2. `/get-js-token` issues a short-lived token (store in Redis keyed to fingerprint) and sets it in response JSON. The server will **only accept requests** that include the `js_token` cookie or header. Bots that don’t execute JS won’t have the token.

3. Make `/get-js-token` run a mild cost (random delay, small CPU work) to deter cheap bots.

This is easy to pair with the CodeIgniter hook: in the hook, if token missing and endpoint requires JS challenge, reject with 403 or a redirect to challenge page.

---

# Extra techniques (if attacker persists)

* **Proof-of-work**: require client to compute a hash with some difficulty (rare, used in heavy DDoS).
* **HMAC-signed requests**: require clients to sign payloads — works when you control clients.
* **Behavioral throttling**: if many different IPs use same fingerprint, throttle by fingerprint and increase challenge frequency.
* **Geo/ASN blocking**: if traffic originates from suspicious regions or ASNs, block/challenge at CDN/WAF.

---

# TL;DR — Concrete next steps to implement **right now**

1. If you have Cloudflare/any CDN: enable JS challenge and create a rate-limit rule for the endpoint. (Best instant reduction.)
2. Drop the provided `anti_bot.php` hook into `application/hooks/` and register it in `hooks.php`. Ensure Redis is available.
3. Add a simple JS token flow for public pages and require the token on writes.
4. Monitor logs for fingerprint clusters and tune limits.

---

If you want, I can:

* produce a **hook variant** that also logs each fingerprint to DB for offline analysis,
* convert the hook to **use Memcached** if you don’t have Redis, or
* give you the exact `nginx` + `fail2ban` config to pair with this (tell me which webserver you run).

Pick one and I’ll drop the exact configs/snippets now.
