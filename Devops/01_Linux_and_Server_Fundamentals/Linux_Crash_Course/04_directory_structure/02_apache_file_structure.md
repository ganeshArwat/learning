# 🌐 Apache Directory Structure & Virtual Hosts (Production Guide)

> Understanding Apache’s directory layout and vhosts is **essential** for hosting multiple websites on one server.

---

## 1️⃣ `/etc/apache2/` – Apache Configuration Root

This directory contains **all Apache configuration files**.

```text
/etc/apache2/
 ├── apache2.conf        # Main Apache config
 ├── ports.conf          # Listening ports (80/443)
 ├── envvars              # Environment variables
 ├── sites-available/     # Virtual host configs (inactive)
 ├── sites-enabled/       # Active sites (symlinks)
 ├── mods-available/      # Available modules
 └── mods-enabled/        # Enabled modules
```

👉 **Rule**: Never put vhost configs directly in `apache2.conf`

---

## 2️⃣ `/etc/apache2/sites-available/site.conf`

### What it is

* Contains **VirtualHost (vhost) definitions**
* One file per website (best practice)

### Example vhost file

📄 `/etc/apache2/sites-available/example.com.conf`

```apache
<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    DocumentRoot /var/www/example.com/public

    <Directory /var/www/example.com/public>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/example-error.log
    CustomLog ${APACHE_LOG_DIR}/example-access.log combined
</VirtualHost>
```

---

## 3️⃣ `/var/www/html/` – Default Web Root

### What it is

* Default Apache website directory
* Used when **no vhost is configured**

```text
/var/www/html/
 └── index.html
```

### Best practice

❌ Don’t deploy production apps here

✅ Use:

```text
/var/www/example.com/
```

---

## 4️⃣ Enabling Virtual Hosts

### Enable a site

```bash
sudo a2ensite example.com.conf
sudo systemctl reload apache2
```

### Disable a site

```bash
sudo a2dissite example.com.conf
sudo systemctl reload apache2
```

### What actually happens

* `a2ensite` creates a **symlink**:

```text
sites-enabled/example.com.conf → sites-available/example.com.conf
```

---

## 5️⃣ Testing Apache Configuration (CRITICAL)

Before reload/restart:

```bash
sudo apachectl configtest
```

Expected output:

```text
Syntax OK
```

---

## 6️⃣ Common Apache Problems & Fixes

### Site not loading

```bash
systemctl status apache2
apachectl configtest
```

### Permission denied errors

```bash
chown -R www-data:www-data /var/www/example.com
chmod -R 755 /var/www/example.com
```

### Port conflict

Check:

```bash
cat /etc/apache2/ports.conf
```

---

## 🔥 Production Best Practices

✔ One site = one vhost file
✔ Always test config before reload
✔ Separate logs per site
✔ Never edit files in `sites-enabled` directly

---

## 🎯 Quick Summary

| Path                            | Purpose       |
| ------------------------------- | ------------- |
| `/etc/apache2/sites-available/` | Vhost configs |
| `/etc/apache2/sites-enabled/`   | Active sites  |
| `/var/www/html/`                | Default site  |
| `a2ensite`                      | Enable site   |
| `a2dissite`                     | Disable site  |

---
