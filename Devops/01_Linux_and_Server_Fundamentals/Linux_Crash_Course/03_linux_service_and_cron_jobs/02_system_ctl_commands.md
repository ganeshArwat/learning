# ⚙️ systemctl Commands – Practical Usage Guide

> `systemctl` is the **daily command** you’ll use to manage services on Linux servers.

---

## 1️⃣ `systemctl status apache2`

### Command

```bash
systemctl status apache2
```

### What it does

* Shows whether **Apache** is running, stopped, or failed
* Displays recent logs
* Shows main PID and resource usage

### Sample Output (important parts)

```text
● apache2.service - The Apache HTTP Server
   Active: active (running)
   Main PID: 1234 (apache2)
```

### How to read it

| Field    | Meaning            |
| -------- | ------------------ |
| Active   | Service state      |
| running  | Service is healthy |
| failed   | Service crashed    |
| inactive | Service stopped    |

👉 **First command to run when a service is not working**

---

## 2️⃣ `systemctl restart nginx`

### Command

```bash
sudo systemctl restart nginx
```

### What it does

* Stops nginx completely
* Starts it again
* Reloads config and binaries

### When to use

* Config changes
* Service is stuck
* After SSL or vhost changes

### ⚠️ Production warning

* Causes **brief downtime**
* Prefer `reload` when possible

```bash
sudo systemctl reload nginx
```

---

## 3️⃣ `systemctl enable --now redis`

### Command

```bash
sudo systemctl enable --now redis
```

### What it does (VERY IMPORTANT)

This is **two commands in one**:

```bash
sudo systemctl enable redis   # start at boot
sudo systemctl start redis    # start now
```

### Why this is powerful

* Ensures Redis survives reboots
* Saves time
* Common DevOps best practice

Verify:

```bash
systemctl status redis
systemctl is-enabled redis
```

---

## 🔑 Related systemctl Commands (MUST KNOW)

| Command    | Purpose         |
| ---------- | --------------- |
| start      | Start service   |
| stop       | Stop service    |
| restart    | Stop + start    |
| reload     | Reload config   |
| enable     | Start at boot   |
| disable    | Disable at boot |
| status     | Service health  |
| is-enabled | Boot status     |

---

## 🔥 Real Production Scenarios

### Website down

```bash
systemctl status nginx
journalctl -u nginx
```

### Redis not starting after reboot

```bash
systemctl enable --now redis
```

### Apache config change

```bash
apachectl configtest
systemctl reload apache2
```

---

## 🎯 Quick Summary

| Command                      | Meaning                   |
| ---------------------------- | ------------------------- |
| systemctl status apache2     | Check Apache health       |
| systemctl restart nginx      | Restart Nginx             |
| systemctl enable --now redis | Start Redis now + on boot |

---
