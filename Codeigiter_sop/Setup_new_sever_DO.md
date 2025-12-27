# 📑 Master SOP  
## Ubuntu 25.04 (Plucky) Server Setup  
### PHP 7.4 + CodeIgniter 3 (Legacy Stack)

## 📌 Target Stack Summary

| Component | Version |
|---------|--------|
| OS | Ubuntu 25.04 (Plucky Puffin) |
| Web Server | Apache 2.4 |
| PHP | 7.4.x (Noble bridge) |
| Framework | CodeIgniter 3 |
| Database | MySQL 8.4 |
| phpMyAdmin | 4.9.11 (LTS) |
| Image Processing | ImageMagick (PECL) |

---

## 🛠️ Phase 1: Infrastructure & Legacy MySQL Fix

### ❗ Problem
MySQL 8.4 **disables `mysql_native_password`**, which PHP 7.4 **requires**.

### ✅ Solution
Force-enable legacy authentication and explicitly configure users.

---

### 1️⃣ Update System Packages
```bash
sudo apt update && sudo apt upgrade -y
````

---

### 2️⃣ Install Apache

```bash
sudo apt install apache2 -y
```

Verify:

```bash
apache2 -v
```

---

### 3️⃣ Install MySQL Server

```bash
sudo apt install mysql-server -y
```

Check status:

```bash
sudo systemctl status mysql
```

---

### 4️⃣ Force Enable Legacy Password Plugin

Edit MySQL configuration:

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Add **under `[mysqld]`**:

```ini
mysql-native-password=ON
bind-address = 0.0.0.0
```

> `bind-address = 0.0.0.0` is required for **HeidiSQL / remote DB tools**

Restart MySQL:

```bash
sudo systemctl restart mysql
```

---

### 5️⃣ Configure MySQL Users

Enter MySQL shell:

```sql
sudo mysql
```

Set root to legacy mode:

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'Your_Password';
```

Create project user:

```sql
CREATE USER 'select_user'@'%'
IDENTIFIED WITH mysql_native_password BY 'Your_Password';
```

Grant privileges:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'select_user'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;
```

---

## 🧹 Phase 2: PHP 7.4 “Noble” Bridge Setup

### ❗ Problem

Ubuntu 25.04 **does not ship PHP 7.4**

### ✅ Solution

Reuse **Ubuntu 24.04 (Noble)** packages via **Ondřej Surý PPA**
(using DEB822 source override)

---

### 1️⃣ Add Ondřej PHP PPA

```bash
sudo add-apt-repository ppa:ondrej/php -y
```

---

### 2️⃣ Modify DEB822 Source File

```bash
sudo nano /etc/apt/sources.list.d/ondrej-ubuntu-php-plucky.sources
```

Change:

```text
Suites: plucky
```

To:

```text
Suites: noble
```

> ⚠️ This is **mandatory** — without it PHP 7.4 will never install.

---

### 3️⃣ Install PHP 7.4 Stack

```bash
sudo apt update

# php7.4-json is built-in
# php7.4-zip is skipped due to libzip conflicts
sudo apt install \
php7.4 \
libapache2-mod-php7.4 \
php7.4-mysql \
php7.4-mbstring \
php7.4-xml \
php7.4-gd \
php7.4-curl \
php7.4-bcmath -y
```

Verify:

```bash
php -v
```

---

## ⚙️ Phase 3: Apache Module Synchronization

### ❗ Problem

Ubuntu 25.04 defaults to `mpm_event`
PHP 7.4 **requires `mpm_prefork`**

---

### Swap Apache Modules

```bash
sudo a2dismod php8.4 mpm_event 2>/dev/null
sudo a2enmod mpm_prefork php7.4 rewrite
sudo update-alternatives --set php /usr/bin/php7.4
sudo systemctl restart apache2
```

Verify:

```bash
apachectl -M | grep mpm
```

---

## 🗄️ Phase 4: phpMyAdmin (LTS Only)

### ❗ Problem

phpMyAdmin ≥ 5.x **breaks on PHP 7.4**

### ✅ Required Version

**phpMyAdmin 4.9.11**

---

### 1️⃣ Manual Installation

```bash
cd /var/www/html
sudo wget https://files.phpmyadmin.net/phpMyAdmin/4.9.11/phpMyAdmin-4.9.11-all-languages.tar.gz
sudo tar xvf phpMyAdmin-4.9.11-all-languages.tar.gz
sudo mv phpMyAdmin-4.9.11-all-languages phpmyadmin
sudo chown -R www-data:www-data phpmyadmin
```

---

### 2️⃣ Fix 404 Error (Apache Alias)

```bash
sudo nano /etc/apache2/conf-available/phpmyadmin.conf
```

Paste:

```apache
Alias /phpmyadmin /var/www/html/phpmyadmin

<Directory /var/www/html/phpmyadmin>
    Options FollowSymLinks
    DirectoryIndex index.php
    AllowOverride All
</Directory>
```

Enable:

```bash
sudo a2enconf phpmyadmin
sudo systemctl reload apache2
```

Test:

```
http://YOUR_IP/phpmyadmin
```

---

## 🚀 Phase 5: Project Deployment

### 1️⃣ Clone Repository

```bash
cd /var/www/html
git clone https://github.com/ashish27aghera/TRACKMATE-PHP.git
```

---

### 2️⃣ Permissions

```bash
sudo chown -R www-data:www-data /var/www/html/trackmate_lite
# 1. Change ownership of the entire project to the web user
sudo chown -R www-data:www-data /var/www/html/trackmate_lite

# 2. Set directory permissions so the web server can write/create folders
sudo find /var/www/html/trackmate_lite -type d -exec chmod 775 {} +

# 3. Set file permissions
sudo find /var/www/html/trackmate_lite -type f -exec chmod 664 {} +
```

---

### 3️⃣ Database Setup

* Create `trackmate_lite`
* Create `trackmate_company_10`

---

## 🚀 Phase 6: PHP Configuration

```bash
cd /etc/php/7.4/apache2
sudo nano php.ini
```

Tune:

```ini
post_max_size
upload_max_filesize
memory_limit
max_file_upload
```

Restart:

```bash
sudo systemctl restart apache2
```

---

## 🚀 Phase 7: Apache Virtual Host

```bash
cd /etc/apache2/sites-available
sudo cp 000-default.conf trackmate_lite.conf
sudo nano trackmate_lite.conf
```

**Remove everything and paste:**

```apache
<VirtualHost *:80>
    ServerName http://165.22.218.189/
    DocumentRoot /var/www/html/trackmate_lite

    <Directory /var/www/html/trackmate_lite>
        Options -Indexes +FollowSymLinks
        AllowOverride All
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/trackmate_lite.log
    CustomLog ${APACHE_LOG_DIR}/trackmate_lite.log combined
</VirtualHost>
```

Enable:

```bash
sudo a2ensite trackmate_lite.conf
sudo a2dissite 000-default.conf
sudo apache2ctl configtest
sudo a2enmod rewrite
sudo systemctl restart apache2
```

---

## 🚀 Phase 8: SOAP Extension

```bash
sudo apt install php7.4-soap -y
sudo systemctl restart apache2
```

---

## 🚀 Phase 9: wkhtmltopdf

```bash
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt install ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb -y
sudo apt install -f
wkhtmltopdf --version
```

---

## 🚀 Phase 10: AutoMySQLBackup

```bash
sudo apt install automysqlbackup
```

Edit config:

```bash
sudo nano /etc/default/automysqlbackup
```

Change:

```ini
BACKUPDIR="/var/www/html/trackmate_lite/db_backup_daily"
DOWEEKLY=0
```

Permissions fixes:

```bash
sudo nano /usr/sbin/automysqlbackup
```

* Line 384:

```bash
chmod 777 ${BACKUPDIR}
```

* Line 426:

```bash
chmod 777 $2
```

---

## 🚀 Phase 11: ImageMagick (PECL – Mandatory)

### ❗ Why PECL?

* Ubuntu 25.04 → ImageMagick 7
* PHP 7.4 → expects ImageMagick 6
* `apt` **cannot resolve this**

---

### Step 1️⃣ Install Build Tools

```bash
sudo apt install build-essential php7.4-dev libmagickwand-dev imagemagick -y
```

---

### Step 2️⃣ Compile Imagick

```bash
sudo pecl -d php_suffix=7.4 install imagick
```

Press **Enter** when prompted.

---

### Step 3️⃣ Enable Extension

```bash
echo "extension=imagick.so" | sudo tee /etc/php/7.4/mods-available/imagick.ini
sudo phpenmod imagick
sudo systemctl restart apache2
```

---

### Step 4️⃣ Verify

```bash
php -m | grep imagick
```

---

## ✅ Final Notes

* `php7.4-imagick` **will never work** on Ubuntu 25.04
* PECL is **mandatory**
* This SOP is **legacy-safe & production-tested**

---

## 🏁 END OF SOP

