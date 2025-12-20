# 📘 SOP – SSL Installation on Website / Application Server

## Purpose

To securely install and manage SSL certificates using **Let’s Encrypt (Certbot)** on **Nginx** or **Apache** web servers.

---

## 🔐 Prerequisites

* SSH access to the server
* Domain name properly pointed to the server (A/AAAA record)
* Root or sudo privileges
* Web server installed (Nginx or Apache)
* Port **80 & 443** open in firewall/security group

---

## SECTION A: SSL INSTALLATION ON NGINX WEBSITE

### 1️⃣ Login to Server

```bash
ssh <user>@<server-ip>
```

---

### 2️⃣ Navigate to Nginx Config Directory

```bash
cd /etc/nginx/sites-available
```

---

### 3️⃣ Edit Website Configuration

```bash
sudo nano your_site.conf
```

**Single domain**

```nginx
server_name example.com;
```

**Multiple domains**

```nginx
server_name example.com www.example.com api.example.com;
```

---

### 4️⃣ Test Nginx Configuration

```bash
sudo nginx -t
```

---

### 5️⃣ Reload Nginx

```bash
sudo systemctl reload nginx
```

---

### 6️⃣ Install SSL Certificate

**Single domain**

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

**Multiple domains**

```bash
sudo certbot --nginx -d example.com -d www.example.com -d api.example.com
```

👉 When prompted, **choose option 2 (Redirect HTTP → HTTPS)**

---

### 7️⃣ Verify Installed Certificates

```bash
sudo certbot certificates
```

---

## SECTION B: SSL INSTALLATION ON APACHE APPLICATION

### 1️⃣ Login to Server

```bash
ssh <user>@<server-ip>
```

---

### 2️⃣ Install Certbot (If Not Installed)

```bash
sudo apt update
sudo apt install certbot python3-certbot-apache
```

---

### 3️⃣ Create or Edit Apache Virtual Host

```bash
sudo nano /etc/apache2/sites-available/your_domain.conf
```

**Example**

```apache
<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com

    DocumentRoot /var/www/html/app

    <Directory /var/www/html/app>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/app_error.log
    CustomLog ${APACHE_LOG_DIR}/app_access.log combined
</VirtualHost>
```

---

### 4️⃣ Enable Site (If New)

```bash
sudo a2ensite your_domain.conf
```

---

### 5️⃣ Test Apache Configuration

```bash
sudo apache2ctl configtest
```

---

### 6️⃣ Reload Apache

```bash
sudo systemctl reload apache2
```

---

### 7️⃣ Install SSL Certificate

```bash
sudo certbot --apache
```

OR (specific domain)

```bash
sudo certbot --apache -d example.com -d www.example.com
```

---

### 8️⃣ Check Auto-Renewal

```bash
sudo systemctl status certbot.timer
```

---

### 9️⃣ Test Renewal

```bash
sudo certbot renew --dry-run
```

---

## SECTION C: CERTBOT ROLLBACK & REINSTALL

### Rollback SSL Changes

```bash
sudo certbot rollback
```

### Reinstall SSL for a Domain

```bash
sudo certbot --apache -d example.com
```

---

## SECTION D: DELETE ALL SSL CERTIFICATES (⚠️ USE WITH CAUTION)

### Important Paths

```bash
/etc/letsencrypt/live
/etc/letsencrypt/archive
/etc/letsencrypt/renewal
/etc/apache2/sites-available
/etc/apache2/sites-enabled
```

> After deletion, reload web server:

```bash
sudo systemctl reload apache2
# OR
sudo systemctl reload nginx
```

---

## SECTION E: CREATE SEPARATE APACHE VHOST & INSTALL SSL

### 1️⃣ Create New VHost File

```bash
sudo nano /etc/apache2/sites-available/example.conf
```

### 2️⃣ Add Configuration

```apache
<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/html/app

    <Directory /var/www/html/app>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    # Disable redirects temporarily for certbot
    #RewriteEngine On
    #RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [L,NE,R=301]
</VirtualHost>
```

---

### 3️⃣ Enable Site

```bash
sudo a2ensite example.conf
```

---

### 4️⃣ Reload Apache

```bash
sudo systemctl reload apache2
```

---

### 5️⃣ Verify Virtual Host

```bash
sudo apache2ctl -S
```

Expected Output:

```
*:80 example.com (/etc/apache2/sites-enabled/example.conf:1)
```

---

### 6️⃣ Generate SSL Certificate

```bash
sudo certbot --apache -d example.com
```

---

### 7️⃣ Renewal Option

If prompted:

```
1: Attempt to reinstall existing certificate
```

✔️ Choose **Option 1**

---

## ✅ Best Practices

* Always test config before reload
* Avoid force HTTPS redirects before certbot validation
* Monitor certificate expiry
* Keep port 80 open for renewal
* Never store credentials in SOPs

---