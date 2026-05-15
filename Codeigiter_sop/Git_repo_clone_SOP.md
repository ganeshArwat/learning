Here is the Standard Operating Procedure (SOP) to totally wipe a repository and reset it to a clean state using Git Bash.
------------------------------
## Standard Operating Procedure (SOP): Total Repository Reset via Git Bash## Purpose
To completely remove all local files, wipe the existing Git commit history, and overwrite the remote GitHub repository with a clean, empty state.
## Prerequisites

* Git Bash installed on Windows.
* Network connectivity to GitHub.
* Write permissions to the target repository (ashish27aghera/SKYNET_PHP).

------------------------------
## Step-by-Step Execution Plan## Step 1: Navigate to your Project Directory
Open Git Bash and change your directory to your project folder using UNIX-style forward slashes (/).

cd /c/xampp_new/htdocs/SKYNET_PHP

## Step 2: Delete Existing Files and Git Tracking
Force-delete the hidden configuration directory and all project files to ensure a total wipe.

rm -rf .git
rm -rf *

## Step 3: Initialize a Fresh Repository
Create a brand new, empty local Git database and rename the default branch to match modern naming conventions.

git init
git branch -M main

## Step 4: Create a Baseline Empty Commit
Git cannot push a branch without a commit history. Because the folder is physically empty, you must tell Git to allow an empty commit.

git commit --allow-empty -m "Total wipe - Initial empty commit"

## Step 5: Link the Correct GitHub Remote URL
Add the full URL path to point exactly to your personal repository destination. Ensure you type the word git at the beginning.

git remote add origin https://github.com

(Note: If you ever need to change or fix this URL later, use git remote set-url origin <URL> instead).
## Step 6: Verify Remote Configuration
Ensure your repository tracking points directly to the project instead of just a generic website homepage.

git remote -v

Expected Output:

origin https://github.com (fetch)
origin https://github.com (push)

## Step 7: Overwrite Remote Repository History
Force-push the empty baseline commit to GitHub. This permanently replaces any files or code previously visible on the website.

git push -f origin main

## SOP: Git Repository Mirroring & Environment Alignment

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

