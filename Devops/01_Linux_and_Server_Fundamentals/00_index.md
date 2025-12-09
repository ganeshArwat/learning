
# ✅ **WEEK 1 – Linux & Server Fundamentals (Full Detailed Index)**

---

## **📌 DAY 1 — Linux Basics & Server Navigation**

### **1. Introduction to Linux**

* What is Linux
* Distributions (Ubuntu, Debian, CentOS)
* CLI vs GUI

### **2. Essential Linux Commands**

* Navigation: `ls`, `cd`, `pwd`
* File operations: `cp`, `mv`, `rm`, `mkdir`, `touch`
* Viewing files: `cat`, `head`, `tail`, `less`, `grep`

### **3. Permissions & Ownership**

* Understanding `rwx` permissions
* Users, groups, others
* Commands:

  * `chmod`
  * `chown`
  * `chgrp`
  * `umask`

### **4. System Info Commands**

* `top`, `htop`
* `df -h`, `du -sh`
* `free -m`
* `hostnamectl`

### **🎯 Hands-on Tasks**

* Create 5 folders and manipulate permissions
* Create a new user and switch using `su` and `sudo`
* Monitor system usage using `top` and `free -m`

---

## **📌 DAY 2 — SSH, Keys, and Server Access**

### **1. SSH Basics**

* What is SSH
* Default port (22)
* Config files (`/etc/ssh/sshd_config`)

### **2. SSH Key-Based Login**

* Generate keys: `ssh-keygen -t ed25519`
* Copy key:

  * `ssh-copy-id user@server`
    OR manually paste in `~/.ssh/authorized_keys`
* Disable password login (optional hardening)

### **3. SSH Config File**

* Creating custom entries in `~/.ssh/config`
* Adding identity name (`ganeshpc` example)
* Custom ports, HostAliases

### **🎯 Hands-on Tasks**

* Create an Ubuntu server (Local VM or Cloud)
* Setup SSH keys
* Disable root login
* Change SSH port (optional)

---

## **📌 DAY 3 — Linux Services (systemctl) & Cron Jobs**

### **1. Understanding systemd**

* Service: start/stop/restart
* Daemon
* Unit files in `/etc/systemd/system/`

### **2. systemctl Commands**

* `systemctl status apache2`
* `systemctl restart nginx`
* `systemctl enable --now redis`

### **3. Cron Jobs**

* Intro to cron
* `crontab -e`
* Cron timing syntax
* Checking cron logs

### **4. Timers (advanced alternative to cron)**

### **🎯 Hands-on Tasks**

* Create a cron job that writes date to a file every minute
* Check output using `tail -f`
* Start/stop Apache/Nginx using systemctl

---

## **📌 DAY 4 — Directory Structure for Web Apps**

### **1. Linux Directory Tree**

* `/var/www/` → web apps
* `/etc/nginx/` → Nginx configs
* `/etc/apache2/` → Apache configs
* `/var/log/` → logs
* `/home/` → user data

### **2. Apache Directory Structure**

* `/etc/apache2/sites-available/site.conf`
* `/var/www/html/`
* Enabling vhosts: `a2ensite`, `a2dissite`

### **3. Nginx Directory Structure**

* `/etc/nginx/sites-available/`
* `/etc/nginx/sites-enabled/`
* `nginx -t` test config

### **🎯 Hands-on Tasks**

* Create a folder for PHP app `/var/www/myapp`
* Create a custom virtual host for Apache or Nginx
* Test with `curl localhost`

---

## **📌 DAY 5 — Logs & Log Reading**

### **1. Apache Logs**

* `/var/log/apache2/access.log`
* `/var/log/apache2/error.log`

### **2. Nginx Logs**

* `/var/log/nginx/access.log`
* `/var/log/nginx/error.log`

### **3. System Logs**

* `journalctl -u apache2`
* `journalctl -xe`
* `dmesg` (kernel logs)

### **4. Useful Log Commands**

* `tail -f`
* `grep`
* `awk` basics

### **🎯 Hands-on Tasks**

* Trigger 404 & check logs
* Tail logs in real time using:
  `tail -f /var/log/nginx/access.log`

---

## **📌 DAY 6 — Firewall & Networking (UFW / iptables)**

### **1. Networking Basics**

* What is a port
* Listening services: `ss -tulpn`

### **2. UFW Firewall**

* Enable UFW
* Allow ports:

  * `ufw allow 80`
  * `ufw allow 443`
  * `ufw allow 22`
* Deny ports
* View status

### **3. iptables (for advanced)**

* Chains: INPUT, OUTPUT, FORWARD
* Basic allow/deny rules

### **🎯 Hands-on Tasks**

* Enable firewall on your server
* Allow SSH, HTTP, HTTPS
* Block a test port and verify with `nc`

---

## **📌 DAY 7 — Basic Server Hardening**

### **1. Hardening SSH**

* Disable root login
* Change port (optional)
* Allow only your user

### **2. System Hardening**

* Install Fail2ban
* Disable unused services
* Secure file permissions
* Auto security updates

### **3. Basics of Intrusion Prevention**

* Detect strange processes: `ps aux | grep`
* Check listening ports: `ss -tulpn`
* Check auth logs:

  * `/var/log/auth.log`

### **🎯 Hands-on Tasks**

* Install and configure Fail2ban
* Harden SSH
* Remove unused packages
* Verify logs for intrusion attempts

---

# ⭐ BONUS PRACTICALS (Highly Recommended)

### **Deploy Simple PHP App**

* Install Apache
* Install PHP 8.x
* Create `index.php`
* Test in browser

### **Deploy Simple Node.js App**

* Install Node + PM2
* Run app on port 3000
* Reverse proxy using Nginx

---
