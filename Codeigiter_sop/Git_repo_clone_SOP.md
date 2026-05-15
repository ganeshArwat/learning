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

