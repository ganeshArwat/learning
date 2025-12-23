This is the **Master Standard Operating Procedure (SOP)** for a full server build on Ubuntu 22.04. This guide covers everything from the initial OS update to the specific manual configurations required to run **CodeIgniter 3** and **PHP 7.4** stably.

---

## 🛠️ Phase 1: Core Server Infrastructure (Apache & MySQL)

Before handling PHP, you must establish the web and database foundations.

1. **Update System Repositories**:
`sudo apt update && sudo apt upgrade -y`
2. **Install Apache Web Server**:
```bash
sudo apt install apache2 -y
sudo systemctl enable apache2
sudo systemctl start apache2

```


3. **Install MySQL Database Server**:
`sudo apt install mysql-server -y`
4. **Secure MySQL & Configure Authentication**:
Ubuntu 22.04 uses `auth_socket` by default. You must switch the root user to password-based authentication so phpMyAdmin can log in.
```bash
sudo mysql
# Inside the MySQL prompt:
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Your_Strong_Password';
FLUSH PRIVILEGES;
EXIT;

```



---

## 🧹 Phase 2: Total Removal of PHP 8.x & 7.4 Preparation

To prevent the `T_STATIC` parse errors (caused by newer Symfony libraries) and "Missing .ini" warnings, you must remove all traces of PHP 8.1/8.5.

1. **Purge PHP 8.x Packages**:
`sudo apt purge php8.* -y`
`sudo apt autoremove --purge -y`
2. **Delete Residual Config Folders**:
`sudo rm -rf /etc/php/8.*`
3. **Add Legacy PHP Repository**:
`sudo add-apt-repository ppa:ondrej/php -y`
`sudo apt update`

---

## ⚙️ Phase 3: PHP 7.4 "Clean" Installation

This phase installs the PHP 7.4 engine and the specific extensions required by CodeIgniter 3.

1. **Install PHP 7.4 Stack**:
`sudo apt install php7.4 libapache2-mod-php7.4 php7.4-mysql php7.4-mbstring php7.4-xml php7.4-gd php7.4-curl php7.4-zip php7.4-json php7.4-bcmath -y`
2. **Enable Modules & Fix Conflicts**:
```bash
# Disable modern modules if they exist
sudo a2dismod php8.1 php8.5 2>/dev/null
# Enable PHP 7.4 and Apache Rewrite
sudo a2enmod php7.4
sudo a2enmod rewrite
# Set CLI version to 7.4
sudo update-alternatives --set php /usr/bin/php7.4

```


3. **Restart Apache**:
`sudo systemctl restart apache2`

---

## 🗄️ Phase 4: Compatible phpMyAdmin Setup (Manual)

The `apt install phpmyadmin` version on Ubuntu 22.04 is too new for PHP 7.4. You must use the compatible **v5.0.4**.

1. **Download and Extract**:
```bash
cd /var/www/html
sudo wget https://files.phpmyadmin.net/phpMyAdmin/5.0.4/phpMyAdmin-5.0.4-all-languages.tar.gz
sudo tar xvf phpMyAdmin-5.0.4-all-languages.tar.gz
sudo mv phpMyAdmin-5.0.4-all-languages phpmyadmin

```


2. **Permissions and Temp Storage**:
```bash
sudo mkdir -p /var/www/html/phpmyadmin/tmp
sudo chown -R www-data:www-data /var/www/html/phpmyadmin
sudo chmod -R 755 /var/www/html/phpmyadmin

```



---

## 🚀 Phase 5: CodeIgniter 3 Project Deployment

1. **Ownership & Write Access**:
```bash
sudo chown -R www-data:www-data /var/www/html/your_project
sudo chmod -R 775 /var/www/html/your_project/application/logs
sudo chmod -R 775 /var/www/html/your_project/application/cache

```


2. **Database Driver Settings**:
Open `application/config/database.php` and set:
`$db['default']['dbdriver'] = 'mysqli';`
3. **Clean URLs**:
Create a `.htaccess` file in the project root:
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php/$1 [L]

```



---

## ✅ Phase 6: Final Verification

Delete troubleshooting files and check the status:

1. **Remove test files**: `sudo rm /var/www/html/info.php`
2. **Check PHP Version**: `php -v` (Must say 7.4.x)
3. **Monitor Errors**: `sudo tail -f /var/log/apache2/error.log`