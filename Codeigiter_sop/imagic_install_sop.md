
## 🧰 **SOP: Install or Reinstall Imagick Extension for PHP**

### 🔹 Objective

To properly uninstall, clean, and reinstall the **Imagick** PHP extension to fix “`Class 'Imagick' not found`” errors.

---

### 🔹 Prerequisites

* Root or sudo access
* PHP and Apache already installed
* Internet connection for package installation

---

### 🔹 Steps to Install Imagick

#### **Step 1: Check if Imagick is Currently Installed**

```bash
php -m | grep imagick
```

✅ **If output shows:** `imagick` → Imagick is installed
❌ **If output is empty:** Imagick is not installed

---

#### **Step 2: Uninstall Existing Imagick**

```bash
sudo apt-get remove --purge php-imagick -y
sudo apt-get autoremove -y
sudo systemctl restart apache2
```

---

#### **Step 3: Confirm Uninstallation**

```bash
php -m | grep imagick
```

✅ **If no output:** Imagick has been fully removed

---

#### **Step 4: Clean PHP Configuration**

Open the Imagick configuration file:

```bash
sudo nano /etc/php/7.4/mods-available/imagick.ini
```

👉 Comment out or delete this line (if present):

```
extension=imagick.so
```

Save and exit (`CTRL + O`, `ENTER`, `CTRL + X`)

---

#### **Step 5: Check Your PHP Version**

```bash
php -v
```

Example output:

```
PHP 7.4.33 (cli) (built: ...)
```

📌 **Note your PHP version** (e.g., `7.4`) — you’ll need it for the next step.

---

#### **Step 6: Install New Imagick**

```bash
sudo apt-get install imagemagick php7.4-imagick -y
sudo systemctl restart apache2
```

---

#### **Step 7: Verify PHP Imagick Configuration File**

Open the file again:

```bash
sudo nano /etc/php/7.4/mods-available/imagick.ini
```

---

#### **Step 8: Add or Replace Extension Line**

Replace existing line (if any) with:

```
extension=php_imagick.dll
```

💾 Save and exit (`CTRL + O`, `ENTER`, `CTRL + X`)

---

#### **Step 9: Restart Apache**

```bash
sudo systemctl restart apache2
```

---

#### **Step 10: Verify Installation**

```bash
php -m | grep imagick
```

✅ Expected output:

```
imagick
```

🎉 **Installation Successful!**
