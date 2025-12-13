# ⏱️ systemd Timers – Advanced Alternative to Cron

> **systemd timers** are the modern, reliable replacement for cron.
> Used heavily in production and cloud environments.

---

## 1️⃣ What is a systemd Timer?

A **timer** is a systemd unit that schedules the execution of a **service unit**.

🔁 Relationship:

```
Timer  ➜  Service  ➜  Command / Script
```

Example:

* `backup.timer` → runs `backup.service`

---

## 2️⃣ Why Timers Are Better Than Cron

| Cron                   | systemd Timer             |
| ---------------------- | ------------------------- |
| No dependency handling | Dependency-aware          |
| Missed jobs ignored    | Can run missed jobs       |
| Poor logging           | Built-in journald logs    |
| Time-only              | Time + boot + event based |

👉 **Production systems prefer timers**

---

## 3️⃣ Types of Timers

### ⏰ Calendar-based (like cron)

Runs at specific times.

### 🚀 Monotonic timers

Run relative to an event (boot, service start).

Examples:

* After boot
* After service starts

---

## 4️⃣ Basic Example (Hands-on)

### Step 1: Create Service Unit

📄 `/etc/systemd/system/backup.service`

```ini
[Unit]
Description=Daily Backup Service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

---

### Step 2: Create Timer Unit

📄 `/etc/systemd/system/backup.timer`

```ini
[Unit]
Description=Run backup daily at 1 AM

[Timer]
OnCalendar=*-*-* 01:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

---

### Step 3: Reload & Enable

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now backup.timer
```

---

## 5️⃣ Understanding Timer Options (IMPORTANT)

### `OnCalendar`

Cron-like scheduling.

Examples:

| Schedule     | OnCalendar           |
| ------------ | -------------------- |
| Every minute | `*-*-* *:*:00`       |
| Daily 2 AM   | `*-*-* 02:00:00`     |
| Weekly Sun   | `Sun *-*-* 03:00:00` |

---

### `Persistent=true`

✔ If system was OFF at scheduled time → runs when system boots.

Cron ❌ cannot do this reliably.

---

## 6️⃣ Listing & Monitoring Timers

List all timers:

```bash
systemctl list-timers
```

Check specific timer:

```bash
systemctl status backup.timer
```

---

## 7️⃣ Logs & Debugging (Huge Advantage)

```bash
journalctl -u backup.service
```

Live logs:

```bash
journalctl -u backup.service -f
```

---

## 8️⃣ Common Timer Patterns

### Run 10 minutes after boot

```ini
OnBootSec=10min
```

### Run every 15 minutes

```ini
OnUnitActiveSec=15min
```

### Replace cron job

Cron:

```bash
0 1 * * * backup.sh
```

Timer:

```ini
OnCalendar=*-*-* 01:00:00
```

---

## 🔥 Production Best Practices

✔ Use `Type=oneshot` for scripts
✔ Always set `Persistent=true`
✔ Keep service and timer names same
✔ Log via journald

---

## 🎯 Quick Summary

| Concept    | Meaning            |
| ---------- | ------------------ |
| Timer      | Scheduler          |
| Service    | Executes task      |
| OnCalendar | Time-based         |
| Persistent | Catch-up execution |

---
