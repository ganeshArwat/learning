# 🔐 SSH Basics – Complete Practical Guide

> SSH is the **foundation of Linux server access**. If you manage production servers, you use SSH every single day.

---

## 1️⃣ What is SSH?

**SSH (Secure Shell)** is a secure protocol used to:

* Log in to remote servers
* Execute commands remotely
* Transfer files securely (scp, sftp)

### Why SSH is important

* Encrypted communication (no plain-text passwords)
* Prevents man-in-the-middle attacks
* Standard for Linux servers, cloud, DevOps

Example:

```bash
ssh user@server_ip
```

---

## 2️⃣ Default SSH Port

* **Default port:** `22`

```bash
ssh user@server_ip -p 22
```

### Why people change SSH port

* Reduce brute-force attacks
* Hide from automated bots

Example (custom port):

```bash
ssh user@server_ip -p 2222
```

> ⚠️ Security note: Changing port alone is **NOT enough** — key-based auth is required.

---

## 3️⃣ SSH Configuration Files

### 🔹 Server-side (MOST IMPORTANT)

📄 **`/etc/ssh/sshd_config`**

Controls:

* Which users can log in
* Authentication methods
* Port number
* Root login

Open file:

```bash
sudo nano /etc/ssh/sshd_config
```

---

## 4️⃣ Important `sshd_config` Settings (YOU MUST KNOW)

### 🔸 Port

```text
Port 22
```

Change example:

```text
Port 2222
```

---

### 🔸 Root Login (CRITICAL)

```text
PermitRootLogin yes
```

Best practice:

```text
PermitRootLogin no
```

---

### 🔸 Password Authentication

```text
PasswordAuthentication yes
```

Production best practice:

```text
PasswordAuthentication no
```

(use SSH keys instead)

---

### 🔸 Allow / Deny Users

```text
AllowUsers ganesh deploy
```

OR

```text
DenyUsers test guest
```

---

### 🔸 Public Key Authentication

```text
PubkeyAuthentication yes
```

---

## 5️⃣ Restart SSH Service (VERY IMPORTANT)

After ANY change:

```bash
sudo systemctl restart ssh
```

Check status:

```bash
systemctl status ssh
```

⚠️ **WARNING**

> Always keep **one SSH session open** while testing changes.

---

## 6️⃣ Client-side SSH Config (Optional but Powerful)

📄 `~/.ssh/config`

Example:

```text
Host prod
  HostName 192.168.1.10
  User deploy
  Port 2222
```

Usage:

```bash
ssh prod
```

---

## 7️⃣ Common SSH Troubleshooting

### Connection refused

```text
ssh: connect to host x.x.x.x port 22: Connection refused
```

Causes:

* SSH service stopped
* Wrong port
* Firewall blocked

Fix:

```bash
systemctl status ssh
```

---

### Permission denied

```text
Permission denied (publickey,password)
```

Causes:

* Wrong user
* Wrong key permissions
* Password login disabled

---

## 8️⃣ Basic SSH Security Checklist ✅

✔ Disable root login
✔ Use SSH keys
✔ Change default port
✔ Limit users
✔ Use firewall

---

## 🎯 Quick Summary

| Topic           | Value                 |
| --------------- | --------------------- |
| Protocol        | SSH                   |
| Default port    | 22                    |
| Server config   | /etc/ssh/sshd_config  |
| Restart service | systemctl restart ssh |
