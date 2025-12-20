# 🌐 Nginx Directory Structure & Virtual Hosts (Production Guide)

> Nginx is lightweight, fast, and widely used in production. Understanding its directory layout is **critical** for deployment and troubleshooting.

---

## 1️⃣ `/etc/nginx/` – Nginx Configuration Root

This directory contains **all Nginx configuration files**.

```text
/etc/nginx/
 ├── nginx.conf              # Main Nginx config
 ├── sites-available/        # Virtual host configs (inactive)
 ├── sites-enabled/          # Enabled sites (symlinks)
 ├── conf.d/                 # Extra config files
 └── snippets/               # Reusable config snippets
```

---

## 2️⃣ `/etc/nginx/sites-available/`

### What it is

* Stores **server block (virtual host) configs**
* One file per website (best practice)

### Example vhost file

📄 `/etc/nginx/sites-available/example.com`

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    root /var/www/example.com/public;
    index index.php index.html;

    access_log /var/log/nginx/example-access.log;
    error_log  /var/log/nginx/example-error.log;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
    }
}
```

---

## 3️⃣ `/etc/nginx/sites-enabled/`

### What it is

* Contains **enabled (active) websites**
* Uses **symbolic links** to `sites-available`

Example:

```text
sites-enabled/example.com -> ../sites-available/example.com
```

### Enable a site

```bash
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```

### Disable a site

```bash
sudo rm /etc/nginx/sites-enabled/example.com
```

---

## 4️⃣ Testing Configuration – `nginx -t` (CRITICAL)

Before reloading or restarting Nginx:

```bash
sudo nginx -t
```

### Successful output

```text
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

### If error exists

* Nginx will **not reload**
* Error line and file are shown

---

## 5️⃣ Reload vs Restart (Important)

### Reload (preferred)

```bash
sudo systemctl reload nginx
```

* Applies config changes
* No downtime

### Restart

```bash
sudo systemctl restart nginx
```

* Stops + starts Nginx
* Brief downtime

---

## 6️⃣ Common Nginx Problems & Fixes

### Site not loading

```bash
nginx -t
systemctl status nginx
```

### 403 Forbidden

```bash
chown -R www-data:www-data /var/www/example.com
chmod -R 755 /var/www/example.com
```

### Port already in use

```bash
ss -tulpn | grep :80
```

---

## 🔥 Production Best Practices

✔ One site = one config file
✔ Always run `nginx -t` before reload
✔ Use reload, not restart
✔ Separate access & error logs per site

---

## 🎯 Quick Summary

| Path / Command                | Purpose       |
| ----------------------------- | ------------- |
| `/etc/nginx/sites-available/` | Site configs  |
| `/etc/nginx/sites-enabled/`   | Active sites  |
| `nginx -t`                    | Test config   |
| reload                        | Zero downtime |

---
