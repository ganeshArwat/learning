# 🔐 SSH Key-Based Login – Step-by-Step Practical Guide

> SSH key-based authentication is **mandatory in production**. Password login is insecure and often disabled.

---

## 1️⃣ What is SSH Key-Based Login?

SSH keys use **public–private key cryptography**:

* **Private key** → stays on your local machine (secret)
* **Public key** → stored on server

When you connect:

* Server checks your public key
* You prove ownership using your private key
* ✅ No password needed

---

## 2️⃣ Generate SSH Keys (Client Side)

### Recommended algorithm: **ed25519**

```bash
ssh-keygen -t ed25519
```

### What you will see

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519):
```

👉 Press **Enter** (default is best)

```
Enter passphrase (empty for no passphrase):
```

👉 Optional but recommended for laptops

### Resulting files

```text
~/.ssh/id_ed25519        (PRIVATE KEY)
~/.ssh/id_ed25519.pub    (PUBLIC KEY)
```

⚠️ **Never share private key**

---

## 3️⃣ Copy Public Key to Server (Method 1 – Recommended)

```bash
ssh-copy-id user@server_ip
```

Example:

```bash
ssh-copy-id ganesh@192.168.1.10
```

You will be asked for the **user password ONCE**.

After this:

```bash
ssh user@server_ip
```

➡️ Login without password 🎉

---

## 4️⃣ Copy Public Key Manually (Method 2)

### 1️⃣ Display public key

```bash
cat ~/.ssh/id_ed25519.pub
```

### 2️⃣ On server

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
```

Paste the public key inside.

Set correct permissions:

```bash
chmod 600 ~/.ssh/authorized_keys
```

---

## 5️⃣ Verify Permissions (VERY IMPORTANT)

Wrong permissions = SSH key login fails ❌

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

Owner must be the user:

```bash
chown -R user:user ~/.ssh
```

---

## 6️⃣ Test SSH Key Login

Open **new terminal**:

```bash
ssh user@server_ip
```

If login works **without password**, you are ready to harden SSH.

---

## 7️⃣ Disable Password Login (Optional but STRONGLY Recommended)

### Edit SSH config (server side)

```bash
sudo nano /etc/ssh/sshd_config
```

Change / ensure:

```text
PasswordAuthentication no
PubkeyAuthentication yes
```

Optional hardening:

```text
PermitRootLogin no
```

Restart SSH:

```bash
sudo systemctl restart ssh
```

⚠️ **IMPORTANT SAFETY RULE**

> Keep one SSH session open while testing.

---

## 8️⃣ Common Errors & Fixes

### ❌ Permission denied (publickey)

Causes:

* Wrong file permissions
* Wrong user
* Key not copied correctly

Fix:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

### ❌ Still asks for password

Check:

```bash
ssh -v user@server_ip
```

Look for:

```text
Offering public key
```

---

## 9️⃣ Production Best Practices ✅

✔ Use ed25519 keys
✔ Disable password login
✔ Disable root login
✔ Use sudo users only
✔ Backup private keys securely

---

## 🎯 Quick Summary

| Step             | Command                   |
| ---------------- | ------------------------- |
| Generate key     | ssh-keygen -t ed25519     |
| Copy key         | ssh-copy-id user@server   |
| Authorized keys  | ~/.ssh/authorized_keys    |
| Disable password | PasswordAuthentication no |

---
