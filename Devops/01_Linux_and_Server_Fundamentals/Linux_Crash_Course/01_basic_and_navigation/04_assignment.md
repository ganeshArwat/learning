Perfect 👍
Here’s a **hands-on lab** you can run **step by step on any Linux VM/server**.
This is exactly how DevOps/Linux training is done.

---

# 🧪 Linux Practice Lab (Hands-On)

## ✅ TASK 1: Create 5 folders & manipulate permissions

### 1️⃣ Create 5 directories

```bash
mkdir dir1 dir2 dir3 dir4 dir5
```

Verify:

```bash
ls -ld dir*
```

---

### 2️⃣ Apply different permissions

```bash
chmod 755 dir1   # rwx r-x r-x (common for directories)
chmod 700 dir2   # rwx --- --- (private)
chmod 777 dir3   # rwx rwx rwx (NOT recommended in prod)
chmod 750 dir4   # rwx r-x ---
chmod 644 dir5   # ❌ wrong for directory (cannot cd)
```

Check permissions:

```bash
ls -ld dir*
```

👉 **Important learning**

* Directory **must have `x`** permission to enter
* `644` on a directory = you **cannot cd into it**

Test:

```bash
cd dir5
# Permission denied
```

Fix it:

```bash
chmod 755 dir5
```

---

## ✅ TASK 2: Create a new user & switch using `su` and `sudo`

### 1️⃣ Create a new user

```bash
sudo adduser testuser
```

(Set password when prompted)

---

### 2️⃣ Switch user using `su`

```bash
su - testuser
```

Check:

```bash
whoami
pwd
```

Exit back:

```bash
exit
```

---

### 3️⃣ Give sudo access (IMPORTANT)

```bash
sudo usermod -aG sudo testuser
```

Verify:

```bash
groups testuser
```

---

### 4️⃣ Login as user and use sudo

```bash
su - testuser
sudo ls /root
```

👉 You’ll be asked for **testuser’s password**

**Difference you MUST remember**

| Command | Meaning                                   |
| ------- | ----------------------------------------- |
| `su`    | Switch user (needs target password)       |
| `sudo`  | Run command as root (needs your password) |

---

## ✅ TASK 3: Monitor system usage

### 1️⃣ Monitor CPU & processes

```bash
top
```

Inside `top`:

* `P` → sort by CPU
* `M` → sort by memory
* `q` → quit

---

### 2️⃣ Check memory usage

```bash
free -m
```

Example output:

```text
              total   used   free  buff/cache available
Mem:           7834   5100    420       2314      2500
```

👉 **Key rule**

* Ignore `free`
* Focus on **available**

---

## 🔥 BONUS (Production mindset)

Simulate load:

```bash
yes > /dev/null &
```

Now check:

```bash
top
free -m
```

Kill it:

```bash
killall yes
```

---

## 🎯 What you’ve learned (VERY IMPORTANT)

✔ Directory permission logic
✔ Why `x` matters on folders
✔ User creation & privilege control
✔ `su` vs `sudo` (real production usage)
✔ CPU & memory monitoring

---

## 🚀 Next Practice (Recommended)

1️⃣ `ps aux`, `kill`, `nice`
2️⃣ `systemctl status`, `restart`, `logs`
3️⃣ Disk full troubleshooting (`df + du`)
4️⃣ Web server permission issues (Apache/Nginx)
