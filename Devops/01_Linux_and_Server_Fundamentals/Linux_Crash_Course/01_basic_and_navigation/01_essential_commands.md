# 🐧 Essential Linux Commands – Detailed Guide

> Beginner‑friendly but **DevOps / production‑ready** explanations with **flags + examples + sample output**.

---

## 📂 Navigation Commands

### 1️⃣ `pwd` – Print Working Directory

Shows your **current directory path**.

```bash
pwd
```

**Output**

```text
/home/ganesh/projects
```

**Flags**

| Flag | Meaning                           |
| ---- | --------------------------------- |
| `-P` | Physical path (resolves symlinks) |
| `-L` | Logical path (default)            |

```bash
pwd -P
```

---

### 2️⃣ `ls` – List Directory Contents

```bash
ls
```

**Output**

```text
file1.txt  file2.log  src
```

#### Common Flags

| Flag | Description         | Example  |
| ---- | ------------------- | -------- |
| `-l` | Long listing        | `ls -l`  |
| `-a` | Show hidden files   | `ls -a`  |
| `-h` | Human‑readable size | `ls -lh` |
| `-R` | Recursive listing   | `ls -R`  |
| `-t` | Sort by time        | `ls -lt` |
| `-S` | Sort by size        | `ls -lS` |

```bash
ls -lah
```

**Output**

```text
drwxr-xr-x 2 ganesh ganesh 4.0K src
-rw-r--r-- 1 ganesh ganesh 1.2K file1.txt
```

---

### 3️⃣ `cd` – Change Directory

```bash
cd /var/log
```

**Special Paths**

| Command | Meaning            |
| ------- | ------------------ |
| `cd ..` | One level up       |
| `cd ~`  | Home directory     |
| `cd -`  | Previous directory |

---

## 📁 File & Directory Operations

### 4️⃣ `mkdir` – Create Directory

```bash
mkdir test
```

**Flags**

| Flag | Description               |
| ---- | ------------------------- |
| `-p` | Create parent directories |
| `-v` | Verbose output            |

```bash
mkdir -pv app/logs/nginx
```

---

### 5️⃣ `touch` – Create Empty File

```bash
touch file.txt
```

**Flags**

| Flag | Meaning            |
| ---- | ------------------ |
| `-c` | Do not create file |
| `-t` | Set timestamp      |

---

### 6️⃣ `cp` – Copy Files & Directories

```bash
cp source.txt dest.txt
```

**Flags**

| Flag | Meaning                 |
| ---- | ----------------------- |
| `-r` | Recursive (directories) |
| `-i` | Prompt before overwrite |
| `-v` | Verbose                 |
| `-p` | Preserve permissions    |

```bash
cp -rv src/ backup/
```

---

### 7️⃣ `mv` – Move / Rename Files

```bash
mv old.txt new.txt
```

**Flags**

| Flag | Meaning                 |
| ---- | ----------------------- |
| `-i` | Prompt before overwrite |
| `-v` | Verbose                 |

---

### 8️⃣ `rm` – Remove Files & Directories ⚠️

```bash
rm file.txt
```

**Flags**

| Flag | Meaning               |
| ---- | --------------------- |
| `-r` | Recursive             |
| `-f` | Force delete          |
| `-i` | Confirm before delete |

```bash
rm -rf temp/
```

⚠️ **No undo in Linux**

---

## 📄 Viewing & Searching Files

### 9️⃣ `cat` – View File Content

```bash
cat file.txt
```

**Flags**

| Flag | Meaning                |
| ---- | ---------------------- |
| `-n` | Show line numbers      |
| `-b` | Number non‑empty lines |

---

### 🔟 `head` – First Lines of File

```bash
head file.txt
```

**Flags**

| Flag | Meaning         |
| ---- | --------------- |
| `-n` | Number of lines |

```bash
head -n 5 file.txt
```

---

### 1️⃣1️⃣ `tail` – Last Lines of File

```bash
tail file.txt
```

**Flags**

| Flag | Meaning            |
| ---- | ------------------ |
| `-n` | Lines to show      |
| `-f` | Follow (live logs) |

```bash
tail -f /var/log/nginx/access.log
```

---

### 1️⃣2️⃣ `less` – Paginated File Viewer

```bash
less file.txt
```

**Keyboard Controls**

| Key     | Action      |
| ------- | ----------- |
| `q`     | Quit        |
| `/word` | Search      |
| `n`     | Next result |
| `G`     | End of file |

---

### 1️⃣3️⃣ `grep` – Search Text

```bash
grep "error" app.log
```

**Flags**

| Flag | Meaning       |
| ---- | ------------- |
| `-i` | Ignore case   |
| `-r` | Recursive     |
| `-n` | Line number   |
| `-v` | Exclude match |

```bash
grep -rin "failed" /var/log
```

---

## 🎯 Real‑World Combos (Very Important)

```bash
ls -lh | grep ".log"
```

```bash
tail -f app.log | grep error
```

---
