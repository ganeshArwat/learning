# 🧪 Linux Production Troubleshooting Labs (Real-World)

> These labs simulate **actual production issues** you WILL face as a developer handling DevOps work.

---

## 🔴 LAB 1: Process Management (`ps`, `kill`, `nice`)

### 1️⃣ View all running processes

```bash
ps aux
```

Important columns:

| Column  | Meaning       |
| ------- | ------------- |
| USER    | Process owner |
| PID     | Process ID    |
| %CPU    | CPU usage     |
| %MEM    | Memory usage  |
| COMMAND | Process name  |

Filter a process:

```bash
ps aux | grep nginx
```

---

### 2️⃣ Kill a process

Graceful stop:

```bash
kill PID
```

Force kill (last option):

```bash
kill -9 PID
```

Kill by name:

```bash
killall node
```

---

### 3️⃣ Control priority using `nice`

Start with low priority:

```bash
nice -n 10 node app.js
```

Change running process priority:

```bash
renice -5 -p PID
```

👉 Lower number = higher priority

---

## 🔴 LAB 2: Service Management (`systemctl` + logs)

### 1️⃣ Check service status

```bash
systemctl status nginx
```

Key things to read:

* Active / failed
* Error messages
* PID

---

### 2️⃣ Restart & reload service

```bash
sudo systemctl restart nginx
sudo systemctl reload nginx
```

| Command | Effect                       |
| ------- | ---------------------------- |
| restart | Stops + starts service       |
| reload  | Reloads config (no downtime) |

---

### 3️⃣ View service logs

```bash
journalctl -u nginx
```

Live logs:

```bash
journalctl -u nginx -f
```

---

## 🔴 LAB 3: Disk Full Troubleshooting (`df` + `du`)

### 1️⃣ Identify disk usage

```bash
df -h
```

Find large directories:

```bash
du -h --max-depth=1 /
```

Common space hogs:

* `/var/log`
* `/var/lib/docker`
* `/home`

---

### 2️⃣ Find large files

```bash
find /var -type f -size +500M
```

Clean logs safely:

```bash
truncate -s 0 /var/log/nginx/access.log
```

---

## 🔴 LAB 4: Web Server Permission Issues (Apache / Nginx)

### Problem

Website shows:

```
403 Forbidden
Permission denied
```

### Fix (MOST COMMON)

```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

Uploads folder:

```bash
sudo chmod -R 775 uploads storage
```

Check user:

```bash
ps aux | grep nginx
```

---

## 🔴 LAB 5: Server is Slow 🚨

### Step-by-step diagnosis

```bash
top
```

Look for:

* High CPU process
* Zombie processes

```bash
free -m
```

If `available` is low → memory issue

```bash
df -h
```

Disk 100% = system slows/crashes

---

### Fix examples

High CPU:

```bash
kill PID
```

High memory:

```bash
systemctl restart mysql
```

Disk full:

```bash
rm -rf /var/log/*.gz
```

---

## 🎯 Golden Production Checklist

When server is slow/down:

```bash
top
free -m
df -h
systemctl status nginx
```