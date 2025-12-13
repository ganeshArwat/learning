# ⏰ Cron Jobs – Scheduling Tasks in Linux (Practical Guide)

> Cron is used everywhere: backups, cleanup jobs, reports, SSL renewals, log rotation, scripts.

---

## 1️⃣ What is Cron?

**Cron** is a Linux **job scheduler** that runs commands or scripts **automatically at specified times**.

Examples of cron usage:

* Daily database backups
* Clearing old logs
* Running reports every hour
* SSL certificate renewal

The cron service runs in the background as a **daemon**.

Check cron status:

```bash
systemctl status cron
```

---

## 2️⃣ `crontab -e` – Edit Cron Jobs

Each user has their own cron table (**crontab**).

Edit your cron jobs:

```bash
crontab -e
```

List cron jobs:

```bash
crontab -l
```

Remove all cron jobs (⚠️ dangerous):

```bash
crontab -r
```

---

## 3️⃣ Cron Timing Syntax (MOST IMPORTANT)

Cron format:

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0–7) (Sun)
│ │ │ └─── Month (1–12)
│ │ └───── Day of month (1–31)
│ └─────── Hour (0–23)
└───────── Minute (0–59)
```

---

### Common Timing Examples

| Schedule          | Cron Expression |
| ----------------- | --------------- |
| Every minute      | `* * * * *`     |
| Every 5 minutes   | `*/5 * * * *`   |
| Every hour        | `0 * * * *`     |
| Daily at 2 AM     | `0 2 * * *`     |
| Weekly (Sunday)   | `0 3 * * 0`     |
| Monthly (1st day) | `0 0 1 * *`     |

---

### Special Characters

| Symbol | Meaning         |
| ------ | --------------- |
| `*`    | Every value     |
| `*/n`  | Every n units   |
| `,`    | Multiple values |
| `-`    | Range           |

Example:

```bash
0 9-17 * * 1-5 command
```

Runs **every hour from 9–5, Mon–Fri**.

---

## 4️⃣ Writing a Cron Job (Real Example)

### Backup script every day at 1 AM

```bash
0 1 * * * /usr/bin/mysqldump dbname > /backup/db.sql
```

### Run PHP script every 5 minutes

```bash
*/5 * * * * /usr/bin/php /var/www/app/artisan schedule:run
```

---

## 5️⃣ Environment & Path Issues (VERY IMPORTANT)

Cron runs with **minimal environment**.

❌ This may fail:

```bash
php script.php
```

✅ Always use full paths:

```bash
/usr/bin/php /var/www/script.php
```

Check paths:

```bash
which php
```

---

## 6️⃣ Checking Cron Logs

### Ubuntu / Debian

```bash
grep CRON /var/log/syslog
```

Live logs:

```bash
tail -f /var/log/syslog | grep CRON
```

---

### RHEL / CentOS

```bash
grep CRON /var/log/cron
```

---

## 7️⃣ Debugging Cron Jobs 🔧

### Redirect output to log

```bash
* * * * * /path/script.sh >> /tmp/cron.log 2>&1
```

### Test script manually

```bash
bash /path/script.sh
```

---

## 8️⃣ System-wide Cron Locations

| File/Dir            | Purpose     |
| ------------------- | ----------- |
| `/etc/crontab`      | System cron |
| `/etc/cron.hourly/` | Hourly jobs |
| `/etc/cron.daily/`  | Daily jobs  |
| `/etc/cron.weekly/` | Weekly jobs |

---

## 🔥 Production Best Practices

✔ Always log output
✔ Use absolute paths
✔ Test scripts manually
✔ Avoid heavy jobs during peak hours

---

## 🎯 Quick Summary

| Topic         | Key Point       |
| ------------- | --------------- |
| cron          | Job scheduler   |
| crontab -e    | Edit jobs       |
| Timing syntax | 5 fields        |
| Logs          | /var/log/syslog |

---
