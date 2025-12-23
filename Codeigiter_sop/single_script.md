Below is the complete, automated **Bash script** and the **Manual SOP** for setting up a full production environment on Ubuntu 22.04 with Apache, MySQL, PHP 7.4, and CodeIgniter 3.

### 📜 The "One-Command" Setup Script

You can save this as `setup.sh`, give it execution permissions, and run it. It automates every fix we implemented, from purging PHP 8.x to installing the compatible version of phpMyAdmin.

```bash
#!/bin/bash

# 1. System Cleanup & Repository Setup
sudo apt update && sudo apt upgrade -y
sudo apt purge php8.* -y
sudo apt autoremove --purge -y
sudo rm -rf /etc/php/8.*
sudo add-apt-repository ppa:ondrej/php -y
sudo apt update

# 2. Install Core Infrastructure (Apache & MySQL)
sudo apt install apache2 mysql-server -y

# 3. Install PHP 7.4 & Critical Extensions
sudo apt install php7.4 libapache2-mod-php7.4 php7.4-mysql php7.4-mbstring \
php7.4-xml php7.4-gd php7.4-curl php7.4-zip php7.4-json php7.4-bcmath -y

# 4. Configure Apache Modules & PHP CLI
sudo a2dismod php8.1 php8.5 2>/dev/null
sudo a2enmod php7.4
sudo a2enmod rewrite
sudo update-alternatives --set php /usr/bin/php7.4

# 5. Manual phpMyAdmin 5.0.4 Installation (PHP 7.4 Compatible)
cd /var/www/html
sudo wget https://files.phpmyadmin.net/phpMyAdmin/5.0.4/phpMyAdmin-5.0.4-all-languages.tar.gz
sudo tar xvf phpMyAdmin-5.0.4-all-languages.tar.gz
sudo mv phpMyAdmin-5.0.4-all-languages phpmyadmin
sudo mkdir -p /var/www/html/phpmyadmin/tmp
sudo chown -R www-data:www-data /var/www/html/phpmyadmin
sudo rm phpMyAdmin-5.0.4-all-languages.tar.gz

# 6. Restart Services
sudo systemctl restart apache2
sudo systemctl restart mysql

echo "Setup Complete. Please configure your MySQL root password manually."

```

---

## 📘 Master SOP: Full Server Setup (Manual Reference)

### Phase 1: OS & Foundation

* **Step 1:** Update the system to ensure all security patches are current.
* **Step 2:** Install **Apache2**. Use `sudo systemctl status apache2` to confirm it is active.
* **Step 3:** Install **MySQL Server**.
* **Step 4:** **Crucial Step:** Switch MySQL to password authentication.
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'YourPassword';
FLUSH PRIVILEGES;

```



### Phase 2: PHP 7.4 Isolation

* **Step 1:** Purge all PHP 8.x packages to prevent "unexpected 'static'" errors in libraries.
* **Step 2:** Install PHP 7.4 and its "bridge" for Apache (`libapache2-mod-php7.4`).
* **Step 3:** Install extensions required by **CodeIgniter 3**: `mysqli`, `mbstring`, `curl`, and `gd`.
* **Step 4:** Ensure the terminal uses the correct version: `php -v`.

### Phase 3: Application & phpMyAdmin

* **Step 1:** Download phpMyAdmin **v5.0.4**. Do not use `apt` as it will pull version 5.1+, which crashes on PHP 7.4.
* **Step 2:** Set the correct directory ownership. Apache runs as the `www-data` user; it must own your project files.
* `sudo chown -R www-data:www-data /var/www/html/project_name`


* **Step 3:** Configure CodeIgniter's Writable folders:
* `application/logs` and `application/cache` must be **775** permissions.



---

### Phase 4: Clean URLs (CI3 Optimization)

To make your site look like `site.com/welcome` instead of `site.com/index.php/welcome`:

1. Enable Apache Rewrite: `sudo a2enmod rewrite`.
2. Modify the Apache config (`/etc/apache2/apache2.conf`) to set `AllowOverride All` for the `/var/www/` directory.
3. Add a `.htaccess` file to the CodeIgniter root.

### Final Verification Checklist

1. Visit `http://IP/phpmyadmin` (Login should work with `root`).
2. Visit `http://IP/info.php` (Should show PHP 7.4.33).
3. Check Error Logs: `sudo tail -f /var/log/apache2/error.log` (Should be empty).

**Would you like me to explain how to secure this server with an SSL certificate using Let's Encrypt?**