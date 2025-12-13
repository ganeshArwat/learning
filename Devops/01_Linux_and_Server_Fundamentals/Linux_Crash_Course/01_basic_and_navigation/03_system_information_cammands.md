# 🖥️ Linux System Information Commands – Complete Guide

> These commands are **critical for production servers**, troubleshooting slowness, memory leaks, disk-full issues, and downtime.

---

## 📊 1. `top` – Real-Time System Monitor

```bash
top
```

### Sample Output (important columns)

```
PID USER   %CPU %MEM   TIME+ COMMAND
1245 root   95.2  1.2   10:22 node
2311 mysql  35.4 15.1   45:10 mysqld
```

### Key Fields Explained

| Field   | Meaning      |
| ------- | ------------ |
| PID     | Process ID   |
| %CPU    | CPU usage    |
| %MEM    | Memory usage |
| TIME+   | CPU time     |
| COMMAND | Process name |

### Useful Keys (while inside top)

| Key | Action            |
| --- | ----------------- |
| `q` | Quit              |
| `P` | Sort by CPU       |
| `M` | Sort by memory    |
| `k` | Kill process      |
| `1` | Show per-core CPU |

### Common Flags

| Flag      | Purpose              |
| --------- | -------------------- |
| `-u user` | Show user processes  |
| `-p PID`  | Monitor specific PID |

```bash
top -u www-data
```

---

## 📈 2. `htop` – Enhanced top (if installed)

```bash
htop
```

### Advantages over top

* Colorful UI
* Mouse support
* Easier process killing
* Tree view of processes

### Important Keys

| Key | Action       |
| --- | ------------ |
| F6  | Sort         |
| F9  | Kill process |
| F10 | Exit         |

> 📌 Install:

```bash
sudo apt install htop
```

---

## 💾 3. `df -h` – Disk Space Usage

```bash
df -h
```

### Sample Output

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        40G   32G  6.5G  83% /
```

### Important Flags

| Flag | Meaning              |
| ---- | -------------------- |
| `-h` | Human readable       |
| `-T` | Show filesystem type |
| `-i` | Inode usage          |

```bash
df -hT
```

---

## 📁 4. `du -sh` – Directory Size

```bash
du -sh /var/www/html
```

### Flags

| Flag            | Meaning           |
| --------------- | ----------------- |
| `-s`            | Summary only      |
| `-h`            | Human readable    |
| `--max-depth=1` | Folder-wise usage |

```bash
du -h --max-depth=1 /var/log
```

---

## 🧠 5. `free -m` – Memory Usage

```bash
free -m
```

### Sample Output

```
              total   used   free  shared buff/cache available
Mem:           7834   5120    450     120       2264      2450
Swap:          2048    200   1848
```

### Understand this clearly

| Column     | Meaning             |
| ---------- | ------------------- |
| used       | Memory in use       |
| free       | Unused memory       |
| buff/cache | Cache (reclaimable) |
| available  | Real usable memory  |

### Flags

| Flag | Meaning        |
| ---- | -------------- |
| `-m` | MB             |
| `-g` | GB             |
| `-h` | Human readable |

---

## 🏷️ 6. `hostnamectl` – Host Information

```bash
hostnamectl
```

### Output Example

```
Static hostname: prod-web-01
Operating System: Ubuntu 22.04 LTS
Kernel: Linux 5.15.0
Architecture: x86-64
```

### Change Hostname

```bash
sudo hostnamectl set-hostname web-server-01
```

---

## 🔥 7. Real Production Scenarios

### Server is slow

```bash
top
free -m
df -h
```

### Disk full issue

```bash
df -h
du -h --max-depth=1 /
```

### High memory usage

```bash
htop
free -m
```

---

## 🎯 8. Interview & DevOps Tips

* High CPU → `top` / `htop`
* Disk 100% → `df -h` + `du`
* OOM errors → `free -m`
* Identify server → `hostnamectl`

---

## ✅ Quick Summary

| Command     | Purpose               |
| ----------- | --------------------- |
| top         | CPU & process monitor |
| htop        | Enhanced top          |
| df -h       | Disk usage            |
| du -sh      | Directory size        |
| free -m     | Memory usage          |
| hostnamectl | Host info             |

---