## 🧰 **SOP: Install or Reinstall Imagick Extension for PHP**

### 🔹 Objective

To properly uninstall, clean, and reinstall the **Imagick** PHP extension to fix “`Class 'Imagick' not found`” errors.

---

### 🔹 Prerequisites

- Root or sudo access
- PHP and Apache already installed
- Internet connection for package installation

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

---

## :x: Error Meaning

```
attempt to perform an operation not allowed by the security policy `PDF'
@ error/constitute.c/IsCoderAuthorized/413
```

:arrow_right: **ImageMagick is blocking PDF processing** due to its **security policy**.
So when your code tries to **convert PDF → TIFF** (for those AWB numbers), ImageMagick refuses.
This is **NOT a code bug**. It’s a **server configuration restriction**.

---

## :white_check_mark: Solution: Allow PDF in ImageMagick policy

### :small_blue_diamond: Step 1: Locate `policy.xml`

Run:

```bash
locate policy.xml
```

Common paths:

- `/etc/ImageMagick-6/policy.xml`
- `/etc/ImageMagick-7/policy.xml`
- `/etc/ImageMagick/policy.xml`

---

### :small_blue_diamond: Step 2: Edit the policy file

```bash
sudo nano /etc/ImageMagick-6/policy.xml
```

## (or your actual path)

### :small_blue_diamond: Step 3: Find and **comment/remove** PDF restriction

You’ll see something like this:

```xml
<policy domain="coder" rights="none" pattern="PDF" />
```

Change it to:

```xml
<!-- <policy domain="coder" rights="none" pattern="PDF" /> -->
```

OR explicitly allow:

```xml
<policy domain="coder" rights="read|write" pattern="PDF" />
```

:warning: Do the same for:

- `PS`
- `EPS`
- `XPS`
  (if present)

---

### :small_blue_diamond: Step 4: Restart services

```bash
sudo systemctl restart apache2
sudo systemctl restart php-fpm
```

## (or `httpd` depending on server)

## :white_check_mark: Verify PDF is now allowed

Run:

```bash
convert -list policy | grep PDF
```

## You should **NOT** see `rights: None`.

## :white_check_mark: Test TIFF creation manually

```bash
convert test.pdf test.tiff
```

## If this works → your AWB TIFF generation will also work.

## :shield: Why this happens

- ImageMagick **disabled PDF by default** after security vulnerabilities
- PDF uses **Ghostscript**
- Servers block it unless explicitly enabled

---

## :fire: Important (Production Tip)

If this is a **public server**, also limit resource usage:

```xml
<policy domain="resource" name="memory" value="256MiB"/>
<policy domain="resource" name="disk" value="1GiB"/>
```

---
