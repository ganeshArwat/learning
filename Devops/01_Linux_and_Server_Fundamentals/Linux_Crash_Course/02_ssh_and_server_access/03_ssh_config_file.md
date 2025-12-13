# 🔐 SSH Client Config (`~/.ssh/config`) – Practical Guide

> This file saves time, avoids mistakes, and is **heavily used in DevOps & cloud environments**.

---

## 1️⃣ What is `~/.ssh/config`?

It is a **client-side SSH configuration file** that lets you:

* Create short host aliases
* Define custom ports
* Specify which SSH key to use
* Avoid typing long SSH commands repeatedly

Without config:

```bash
ssh -i ~/.ssh/id_ed25519 -p 2222 ganesh@192.168.1.10
```

With config:

```bash
ssh ganeshpc
```

---

## 2️⃣ Create / Edit SSH Config File

```bash
nano ~/.ssh/config
```

Ensure correct permissions:

```bash
chmod 600 ~/.ssh/config
```

---

## 3️⃣ Basic SSH Config Entry (Host Alias)

### Example: `ganeshpc`

```text
Host ganeshpc
  HostName 192.168.1.10
  User ganesh
  Port 22
```

Now connect using:

```bash
ssh ganeshpc
```

---

## 4️⃣ Using Custom SSH Key (IdentityFile)

### Example: Production server with ed25519 key

```text
Host prod-server
  HostName 203.0.113.10
  User deploy
  IdentityFile ~/.ssh/id_ed25519
```

👉 SSH will **automatically use this key**.

---

## 5️⃣ Custom SSH Port

```text
Host prod-custom
  HostName prod.example.com
  User deploy
  Port 2222
  IdentityFile ~/.ssh/id_ed25519
```

Equivalent to:

```bash
ssh deploy@prod.example.com -p 2222 -i ~/.ssh/id_ed25519
```

---

## 6️⃣ Multiple Servers (Real DevOps Example)

```text
Host dev
  HostName 10.0.0.10
  User ganesh

Host staging
  HostName 10.0.1.10
  User deploy
  IdentityFile ~/.ssh/id_ed25519

Host prod
  HostName 203.0.113.10
  User deploy
  Port 2222
  IdentityFile ~/.ssh/prod_key
```

Usage:

```bash
ssh dev
ssh staging
ssh prod
```

---

## 7️⃣ Advanced Options (Very Useful)

### Forward SSH Agent

```text
ForwardAgent yes
```

### Keep connection alive

```text
ServerAliveInterval 60
```

### Disable password auth for this host

```text
PasswordAuthentication no
```

---

## 8️⃣ Wildcards (Power Feature ⭐)

Apply settings to all servers:

```text
Host *
  ServerAliveInterval 60
  IdentitiesOnly yes
```

---

## 9️⃣ Test SSH Config

Verbose mode:

```bash
ssh -v ganeshpc
```

Check which config is used:

```bash
ssh -G ganeshpc
```

---

## 🔥 Common Mistakes

❌ Wrong file permissions

```bash
chmod 600 ~/.ssh/config
```

❌ Wrong key path in `IdentityFile`

❌ Using IP instead of Host alias

---

## 🎯 Quick Summary

| Feature      | Benefit            |
| ------------ | ------------------ |
| Host alias   | Short SSH commands |
| IdentityFile | Correct key usage  |
| Port         | Custom SSH ports   |
| Wildcards    | Global settings    |

---
