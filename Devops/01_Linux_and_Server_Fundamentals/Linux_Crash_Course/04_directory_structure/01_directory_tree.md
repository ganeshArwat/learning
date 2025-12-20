# 📁 Linux Directory Tree – Important Paths Explained (Production View)

> Understanding the Linux directory structure is **critical** for server management, debugging, and DevOps work.

---

## 1️⃣ `/var/www/` – Web Applications

### What it is

* Default location for **web application files**
* Used by **Apache** and **Nginx**

### Typical structure

```text
/var/www/
 ├── html/          # Default site
 ├── myapp/         # Custom web app
 │   ├── public/
 │   ├── index.php
 │   └── .env
```

### Real usage

* PHP (Laravel, CI)
* Node.js static builds
* React/Vue build output

### Permissions (important)

```bash
chown -R www-data:www-data /var/www/myapp
chmod -R 755 /var/www/myapp
```

---

## 2️⃣ `/etc/nginx/` – Nginx Configuration

### What it contains

* All **Nginx configuration files**

### Important files & folders

```text
/etc/nginx/
 ├── nginx.conf            # Main config
 ├── sites-available/      # Virtual hosts
 ├── sites-enabled/        # Active sites (symlinks)
 └── conf.d/
```

### Real workflow

```bash
/etc/nginx/sites-available/myapp.conf
ln -s sites-available/myapp.conf sites-enabled/
nginx -t
systemctl reload nginx
```

---

## 3️⃣ `/etc/apache2/` – Apache Configuration

### What it contains

* Apache server configuration

### Important files & folders

```text
/etc/apache2/
 ├── apache2.conf
 ├── ports.conf
 ├── sites-available/
 ├── sites-enabled/
 ├── mods-available/
 └── mods-enabled/
```

### Enable site (example)

```bash
a2ensite myapp.conf
systemctl reload apache2
```

---

## 4️⃣ `/var/log/` – System & Application Logs

### What it is

* Central place for **logs**

### Common logs

```text
/var/log/
 ├── syslog
 ├── auth.log
 ├── nginx/access.log
 ├── nginx/error.log
 ├── apache2/error.log
 └── mysql/error.log
```

### Debugging commands

```bash
tail -f /var/log/nginx/error.log
grep ERROR /var/log/syslog
```

👉 **First place to check when something breaks**

---

## 5️⃣ `/home/` – User Data

### What it contains

* Home directories for users

```text
/home/
 ├── ganesh/
 │   ├── .ssh/
 │   ├── downloads/
 │   └── scripts/
```

### Important hidden files

* `~/.ssh/` → SSH keys & config
* `~/.bashrc` → shell config
* `~/.profile`

---

## 🔥 Production Tips (Very Important)

✔ Never edit configs directly in `/lib`
✔ Always test config (`nginx -t`, `apachectl configtest`)
✔ Logs live in `/var/log` — not in app folders
✔ Web servers run as `www-data`

---

## 🎯 Quick Summary Table

| Directory       | Purpose        |
| --------------- | -------------- |
| `/var/www/`     | Web apps       |
| `/etc/nginx/`   | Nginx configs  |
| `/etc/apache2/` | Apache configs |
| `/var/log/`     | Logs           |
| `/home/`        | User data      |

---
