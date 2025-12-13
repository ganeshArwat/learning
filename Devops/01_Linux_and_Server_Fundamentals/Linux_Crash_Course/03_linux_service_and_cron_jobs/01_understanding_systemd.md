# ⚙️ Understanding systemd – Services, Daemons & Unit Files

> **systemd** is the heart of modern Linux servers. If you manage services (Nginx, MySQL, Node, PHP-FPM), you must understand this.

---

## 1️⃣ What is systemd?

**systemd** is the **init system and service manager** used by most modern Linux distributions (Ubuntu, Debian, CentOS, RHEL).

It is responsible for:

* Booting the system
* Starting system services
* Managing background processes (daemons)
* Restarting failed services
* Logging (via `journald`)

Check if systemd is running:

```bash
ps -p 1 -o comm=
```

Output:

```text
systemd
```

---

## 2️⃣ What is a Service?

A **service** is a program managed by systemd.

Examples:

* `nginx`
* `apache2`
* `mysql`
* `php8.1-fpm`
* Custom Node / Python apps

Service lifecycle commands:

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
```

---

## 3️⃣ What is a Daemon?

A **daemon** is a program that:

* Runs in the background
* Starts at boot or on demand
* Listens for requests

Examples:

* `sshd` → SSH daemon
* `nginx` → web server daemon
* `mysqld` → database daemon

👉 **systemd manages daemons as services**

---

## 4️⃣ `systemctl` – Core Commands (MUST KNOW)

### Check service status

```bash
systemctl status nginx
```

Important fields:

* Active (running / failed)
* PID
* Logs & errors

---

### Enable / Disable service at boot

```bash
sudo systemctl enable nginx
sudo systemctl disable nginx
```

---

### List services

Running services:

```bash
systemctl list-units --type=service
```

All services:

```bash
systemctl list-unit-files --type=service
```

---

## 5️⃣ systemd Unit Files

A **unit file** tells systemd **how to start, stop, and manage a service**.

### Common unit types

| Type    | Extension  |
| ------- | ---------- |
| Service | `.service` |
| Timer   | `.timer`   |
| Socket  | `.socket`  |

---

## 6️⃣ Where Unit Files Live 📂

### System-provided (DO NOT EDIT)

```text
/lib/systemd/system/
```

### Custom / Override services (YOU SHOULD USE)

```text
/etc/systemd/system/
```

Priority:

```
/etc/systemd/system  >  /lib/systemd/system
```

---

## 7️⃣ Example Unit File (Very Important)

📄 `/etc/systemd/system/myapp.service`

```ini
[Unit]
Description=My Node App
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/myapp
ExecStart=/usr/bin/node app.js
Restart=always
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

---

## 8️⃣ Reload systemd (CRITICAL STEP)

Whenever you create/edit unit files:

```bash
sudo systemctl daemon-reload
```

Then:

```bash
sudo systemctl start myapp
sudo systemctl enable myapp
```

---

## 9️⃣ Service Logs (systemd way)

```bash
journalctl -u myapp
```

Live logs:

```bash
journalctl -u myapp -f
```

---

## 🔥 Real Production Scenarios

### Service fails to start

```bash
systemctl status myapp
journalctl -u myapp
```

### Service restarts automatically

```text
Restart=always
```

---

## 🎯 Quick Summary

| Concept   | Meaning                |
| --------- | ---------------------- |
| systemd   | Init & service manager |
| Service   | Managed process        |
| Daemon    | Background process     |
| systemctl | Control tool           |
| Unit file | Service definition     |

---
