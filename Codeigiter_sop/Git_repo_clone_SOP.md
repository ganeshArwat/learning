#  A:- Standard Operating Procedure (SOP): Total Repository Reset via Git Bash

## Purpose

To completely remove all local files, wipe the existing Git commit history, and overwrite the remote GitHub repository with a clean, empty state.

---

## Prerequisites

- Git Bash installed on Windows
- Network connectivity to GitHub
- Write permissions to the target repository (`ashish27aghera/SKYNET_PHP`)

---

# Step-by-Step Execution Plan

## Step 1: Navigate to Your Project Directory

```bash
cd /c/xampp_new/htdocs/SKYNET_PHP
```

---

## Step 2: Delete Existing Files and Git Tracking

```bash
rm -rf .git
rm -rf *
```

> ⚠️ Warning:  
> These commands permanently delete all repository files from your local project folder.

---

## Step 3: Initialize a Fresh Repository

```bash
git init
git branch -M main
```

---

## Step 4: Create a Baseline Empty Commit

```bash
git commit --allow-empty -m "Total wipe - Initial empty commit"
```

---

## Step 5: Link the Correct GitHub Remote URL

```bash
git remote add origin https://github.com/ashish27aghera/SKYNET_PHP.git
```

> **Note:**  
> If you ever need to change or fix this URL later, use:

```bash
git remote set-url origin https://github.com/ashish27aghera/SKYNET_PHP.git
```

---

## Step 6: Verify Remote Configuration

```bash
git remote -v
```

### Expected Output

```bash
origin  https://github.com/ashish27aghera/SKYNET_PHP.git (fetch)
origin  https://github.com/ashish27aghera/SKYNET_PHP.git (push)
```

---

## Step 7: Overwrite Remote Repository History

```bash
git push -f origin main
```


## B:- SOP: Git Repository Mirroring & Environment Alignment

### 1. Repository Mirroring (The "Bridge" Method)

Use this whenever you need to move a full project with all branch history to a new destination.

* **Step A:** Navigate to a clean directory (e.g., `/c/xampp/htdocs/`).
* **Step B:** Create a bare clone of the source.
```bash
git clone --bare https://github.com/ashish27aghera/TRACKMATE-PHP.git

```


* **Step C:** Push to the new destination.
```bash
cd TRACKMATE-PHP.git
git push --mirror https://github.com/ashish27aghera/SKYNET_PHP.git

