# 🔐 Linux Permissions & Ownership – Complete Guide

> This is **one of the MOST IMPORTANT Linux topics** for servers, security, DevOps, and production issues.

---

## 🧠 1. Understanding `rwx` Permissions

Each file/directory has **3 permission sets**:

```
[rwx] [rwx] [rwx]
 user  group others
```

| Symbol | Meaning | File              | Directory           |
| ------ | ------- | ----------------- | ------------------- |
| `r`    | Read    | View file content | List directory      |
| `w`    | Write   | Modify file       | Create/Delete files |
| `x`    | Execute | Run file          | Enter directory     |

---

## 👥 2. Users, Groups, Others

When you run:

```bash
ls -l
```

**Output**

```text
-rw-r--r-- 1 ganesh developers 1024 app.php
```

Breakdown:

```
- rw- r-- r--
| |   |   |
| |   |   └─ Others
| |   └──── Group
| └──────── User (owner)
└─────────── File type
```

---

## 🔢 3. Numeric (Octal) Permissions

| Permission | Value |
| ---------- | ----- |
| r          | 4     |
| w          | 2     |
| x          | 1     |

**Common combinations**

| Number | Meaning |
| ------ | ------- |
| 7      | rwx     |
| 6      | rw-     |
| 5      | r-x     |
| 4      | r--     |

**Example**

```bash
chmod 644 file.txt
```

```
User: 6 (rw-)
Group: 4 (r--)
Others: 4 (r--)
```

---

## 🛠 4. `chmod` – Change Permissions

### Symbolic Mode

```bash
chmod u+x script.sh
chmod g+w file.txt
chmod o-r secret.txt
chmod a+r file.txt
```

| Symbol | Meaning     |
| ------ | ----------- |
| `u`    | User        |
| `g`    | Group       |
| `o`    | Others      |
| `a`    | All         |
| `+`    | Add         |
| `-`    | Remove      |
| `=`    | Set exactly |

---

### Numeric Mode

```bash
chmod 755 app.sh
```

**Very common server permissions**

| Permission | Usage        |
| ---------- | ------------ |
| 644        | Files        |
| 755        | Directories  |
| 600        | Private keys |
| 700        | Scripts      |

---

### Recursive Permission Change

```bash
chmod -R 755 /var/www/html
```

---

## 👑 5. `chown` – Change Owner

```bash
chown user file.txt
```

Change owner and group:

```bash
chown ganesh:developers app.php
```

Recursive:

```bash
chown -R www-data:www-data /var/www/html
```

**Important (Web servers)**

| Server | User     |
| ------ | -------- |
| Apache | www-data |
| Nginx  | www-data |

---

## 👥 6. `chgrp` – Change Group

```bash
chgrp developers file.txt
```

Recursive:

```bash
chgrp -R developers project/
```

---

## 🎭 7. `umask` – Default Permissions

`umask` decides **default permission** when files/directories are created.

Check current umask:

```bash
umask
```

**Output**

```text
0022
```

### How umask works

| Type | Base | umask | Result |
| ---- | ---- | ----- | ------ |
| File | 666  | 022   | 644    |
| Dir  | 777  | 022   | 755    |

---

### Set umask (temporary)

```bash
umask 027
```

| umask | File | Directory |
| ----- | ---- | --------- |
| 022   | 644  | 755       |
| 027   | 640  | 750       |
| 077   | 600  | 700       |

---

## 🚨 8. Special Permissions (Interview + Real World)

### SUID (4)

```bash
chmod 4755 file
```

Runs as **file owner**

---

### SGID (2)

```bash
chmod 2755 dir
```

Files inherit **group ownership**

---

### Sticky Bit (1)

```bash
chmod 1777 /tmp
```

Only owner can delete files

---

## 🔥 9. Real Production Examples

### Web App Permissions

```bash
chown -R www-data:www-data /var/www/app
chmod -R 755 /var/www/app
chmod -R 775 storage uploads
```

### Log Access

```bash
grep error /var/log/nginx/error.log
```

(permission issues → use sudo)

---

## 🎯 10. Quick Summary

| Command | Purpose             |
| ------- | ------------------- |
| chmod   | Change permissions  |
| chown   | Change owner        |
| chgrp   | Change group        |
| umask   | Default permissions |

---
