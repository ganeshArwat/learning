# 🚀 New Server Setup Guide – Trackmate Lite

This document describes **step-by-step instructions** to set up a fresh Ubuntu server for the **Trackmate Lite** application.

---

## 1️⃣ Initial Server & User Setup

### Login as root (via PuTTY)

```bash
ssh root@<SERVER_IP>
```
- or 
- Open putty login with root

### Create deploy user

```bash
sudo adduser deploy
sudo passwd deploy
sudo usermod -aG sudo deploy
```

---

## 2️⃣ System Update & Apache Installation

```bash
sudo apt update
sudo apt install apache2
```

### Configure Firewall

```bash
sudo ufw app list
sudo ufw app info "Apache Full"
sudo ufw allow in "Apache Full"
```

---

## 3️⃣ MySQL Installation & Security

```bash
sudo apt install mysql-server
sudo mysql_secure_installation
```

**Selections during secure installation**

* Press **Y**
* Choose **1** for password validation
* Set MySQL root password : (ENTER YOUR DATABASE PASSWORD FOR ROOT DATABASE USER)
* Press **Y** for all remaining options

### Configure MySQL Root Authentication

```bash
sudo mysql
```

```sql
SELECT user,authentication_string,plugin,host FROM mysql.user;
```
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ROOT_USER_DATABASE_PASSWORD';
```
```sql
FLUSH PRIVILEGES;
```
```sql
SELECT user,authentication_string,plugin,host FROM mysql.user;
```
```sql
SELECT user,authentication_string,plugin,host FROM mysql.user;
EXIT;
```
---

## 4️⃣ PHP Installation

```bash
sudo apt install php libapache2-mod-php php-mysql
```

---

## 5️⃣ Apache Virtual Host Setup

```bash
cd /etc/apache2/sites-available
ls
sudo cp 000-default.conf trackmate_lite.conf
sudo nano trackmate_lite.conf
```

### Replace entire file content with:

- REMOVE ALL LINE by cntl+k and ADD THIS :

```apache
<VirtualHost *:80>
    #ServerAdmin loy@itdservices.in
    ServerName <SERVER_IP>
    DocumentRoot /var/www/html/trackmate_lite

    <Directory /var/www/html/trackmate_lite>
        Options -Indexes +FollowSymLinks
        AllowOverride All
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/trackmate_lite.log
    CustomLog ${APACHE_LOG_DIR}/trackmate_lite.log combined
</VirtualHost>
```

### Enable Site & Modules

```bash
sudo a2ensite trackmate_lite.conf
sudo a2dissite 000-default.conf
sudo apache2ctl configtest
sudo a2enmod rewrite
sudo systemctl restart apache2
```

---

## 6️⃣ phpMyAdmin Installation

- digitalocean
```
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-18-04
```

- Navigate to root directory
```bash
cd ../../../../
sudo apt update
```

```bash
sudo apt install phpmyadmin php-mbstring php-gettext

# or

sudo apt install phpmyadmin php-mbstring php7.4-gettext
```

⚠️ **Important**: When prompted, select **Apache2** using **SPACE**, then TAB → ENTER
- If you do not hit SPACE to select Apache, the installer will not move the necessary files during installation.
- Select Yes- enter password - select ok

```bash
sudo phpenmod mbstring
sudo systemctl restart apache2
```

---

## 7️⃣ PHP Configuration (php.ini)

```bash
cd /etc/php/7.4/apache2
sudo nano php.ini
```

Update values:

```ini
post_max_size = 512M
upload_max_filesize = 512M
memory_limit = 1024M
max_file_uploads = 200
```

```bash
sudo systemctl restart apache2
```

---

## 8️⃣ Database Setup

1. Login to **phpMyAdmin**
2. Create database: `trackmate_lite` (type = utfmb4_genral_ci)
3. Import databse file for `trackmate_lite`
4. Execute truncate queries
- sql query
```sql
TRUNCATE `address_book`;
TRUNCATE `address_book_email`;
TRUNCATE `admin_user`;
TRUNCATE `app_settings`;
TRUNCATE `attendance`;
TRUNCATE `auth_token`;
TRUNCATE `bank_ledger_item`;
TRUNCATE `billing_history`;
TRUNCATE `brand`;
TRUNCATE `business_type_master`;
TRUNCATE `cft_contracts`;
TRUNCATE `charge_master`;
TRUNCATE `city`;
TRUNCATE `city_master_history`;
TRUNCATE `ci_sessions`;
TRUNCATE `company`;
TRUNCATE `company_bank`;
TRUNCATE `company_invoice_range`;
TRUNCATE `company_master`;
TRUNCATE `consignee`;
TRUNCATE `consignee_master_history`;
TRUNCATE `country`;
TRUNCATE `country_master_history`;
TRUNCATE `co_vendor`;
TRUNCATE `co_vendor_master_history`;
TRUNCATE `credit_debit_note`;
TRUNCATE `credit_debit_note_history`;
TRUNCATE `credit_debit_note_item`;
TRUNCATE `currency_master`;
TRUNCATE `currency_master_rate`;
TRUNCATE `customer`;
TRUNCATE `customer_contract`;
TRUNCATE `customer_contract_head`;
TRUNCATE `customer_contract_history`;
TRUNCATE `customer_contract_rate`;
TRUNCATE `customer_estimate`;
TRUNCATE `customer_estimate_data`;
TRUNCATE `customer_estimate_other_charge`;
TRUNCATE `customer_master_history`;
TRUNCATE `customer_users`;
TRUNCATE `customer_users_permission_map`;
TRUNCATE `custom_invoice`;
TRUNCATE `custom_invoice_history`;
TRUNCATE `custom_invoice_setting`;
TRUNCATE `custom_report`;
TRUNCATE `custom_report_column_adjustment`;
TRUNCATE `custom_report_field`;
TRUNCATE `custom_report_history`;
TRUNCATE `custom_validation_field`;
TRUNCATE `dashboard_data`;
TRUNCATE `description`;
TRUNCATE `district`;
TRUNCATE `district_master_history`;
TRUNCATE `docket`;
TRUNCATE `docket_charges`;
TRUNCATE `docket_comment`;
TRUNCATE `docket_consignee`;
TRUNCATE `docket_delivery`;
TRUNCATE `docket_entry_invoice`;
TRUNCATE `docket_extra_field`;
TRUNCATE `docket_free_form_invoice`;
TRUNCATE `docket_history`;
TRUNCATE `docket_include_data`;
TRUNCATE `docket_inventory_map`;
TRUNCATE `docket_invoice`;
TRUNCATE `docket_invoice_map`;
TRUNCATE `docket_items`;
TRUNCATE `docket_less_invoice`;
TRUNCATE `docket_less_invoice_item`;
TRUNCATE `docket_less_item`;
TRUNCATE `docket_material`;
TRUNCATE `docket_purchase_billing`;
TRUNCATE `docket_receipt`;
TRUNCATE `docket_sales_billing`;
TRUNCATE `docket_service_field`;
TRUNCATE `docket_shipper`;
TRUNCATE `docket_state`;
TRUNCATE `docket_state_description`;
TRUNCATE `docket_state_master`;
TRUNCATE `docket_tracking`;
TRUNCATE `docket_weight_change_history`;
TRUNCATE `document_mapping`;
TRUNCATE `edit_bag_no`;
TRUNCATE `email_configuration`;
TRUNCATE `email_cron_setting`;
TRUNCATE `email_queue`;
TRUNCATE `expense_sub_type`;
TRUNCATE `expense_type`;
TRUNCATE `flight`;
TRUNCATE `flight_masters_history`;
TRUNCATE `follow_up`;
TRUNCATE `forwarder`;
TRUNCATE `free_form_item`;
TRUNCATE `free_form_note`;
TRUNCATE `fsc_masters`;
TRUNCATE `fsc_masters_history`;
TRUNCATE `holiday`;
TRUNCATE `hub`;
TRUNCATE `hub_mapping`;
TRUNCATE `hub_master_history`;
TRUNCATE `incoterm`;
TRUNCATE `inquiries`;
TRUNCATE `inquiry_follow_up`;
TRUNCATE `inventory`;
TRUNCATE `inventory_history`;
TRUNCATE `inventory_multiple_field`;
TRUNCATE `inventory_vendor`;
TRUNCATE `invoice_history`;
TRUNCATE `invoice_range`;
TRUNCATE `invoice_range_history`;
TRUNCATE `invoice_type`;
TRUNCATE `irn_cancel`;
TRUNCATE `irn_data`;
TRUNCATE `itd_admin_email`;
TRUNCATE `leads`;
TRUNCATE `lead_status_master`;
TRUNCATE `lead_type_master`;
TRUNCATE `leave_application`;
TRUNCATE `leave_type`;
TRUNCATE `ledger_item`;
TRUNCATE `ledger_outstanding_item`;
TRUNCATE `license`;
TRUNCATE `license_location`;
TRUNCATE `location`;
TRUNCATE `location_history`;
TRUNCATE `location_zone_map`;
TRUNCATE `manifest`;
TRUNCATE `manifest_charge`;
TRUNCATE `manifest_charge_amt`;
TRUNCATE `manifest_docket`;
TRUNCATE `manifest_edi_excel_data`;
TRUNCATE `manifest_history`;
TRUNCATE `material`;
TRUNCATE `media_attachment`;
TRUNCATE `migration_log`;
TRUNCATE `mode`;
TRUNCATE `module_setting`;
TRUNCATE `notification`;
TRUNCATE `offer`;
TRUNCATE `opening_balance`;
TRUNCATE `opening_balance_history`;
TRUNCATE `other_address`;
TRUNCATE `otp_log`;
TRUNCATE `payment_receipt`;
TRUNCATE `payment_receipt_history`;
TRUNCATE `pickup_address`;
TRUNCATE `pickup_request`;
TRUNCATE `pickup_request_detail`;
TRUNCATE `pick_up_sheets`;
TRUNCATE `pincode`;
TRUNCATE `pincode_zone_map`;
TRUNCATE `postorderdata`;
TRUNCATE `preorderdata`;
TRUNCATE `product`;
TRUNCATE `product_master_history`;
TRUNCATE `project`;
TRUNCATE `purchase_credit_debit_note`;
TRUNCATE `purchase_credit_debit_note_item`;
TRUNCATE `purchase_include_data`;
TRUNCATE `purchase_invoice`;
TRUNCATE `purchase_invoice_history`;
TRUNCATE `purchase_invoice_item`;
TRUNCATE `purchase_ledger_item`;
TRUNCATE `purchase_ledger_outstanding_item`;
TRUNCATE `purchase_opening_balance`;
TRUNCATE `purchase_opening_balance_history`;
TRUNCATE `purchase_payment_receipt`;
TRUNCATE `purchase_payment_receipt_history`;
TRUNCATE `purchase_vendor`;
TRUNCATE `purchase_vendor_credit_debit_history`;
TRUNCATE `rack_number`;
TRUNCATE `rate_modifier`;
TRUNCATE `rate_modifier_data`;
TRUNCATE `rate_modifier_history`;
TRUNCATE `refresh_log`;
TRUNCATE `route`;
TRUNCATE `route_master_history`;
TRUNCATE `run_sheet`;
TRUNCATE `run_sheet_docket`;
TRUNCATE `run_sheet_history`;
TRUNCATE `send_address_book_email`;
TRUNCATE `service_type`;
TRUNCATE `setting_data`;
TRUNCATE `shipper`;
TRUNCATE `slider`;
TRUNCATE `sms_master`;
TRUNCATE `sms_master_variable`;
TRUNCATE `state`;
TRUNCATE `state_master_history`;
TRUNCATE `state_zone_map`;
TRUNCATE `sub_rack_number`;
TRUNCATE `task`;
TRUNCATE `task_assignee`;
TRUNCATE `task_comment`;
TRUNCATE `tqs_department`;
TRUNCATE `tqs_role`;
TRUNCATE `transfer_manifest`;
TRUNCATE `transfer_manifest_docket`;
TRUNCATE `trigger_email_setting`;
TRUNCATE `user_permission_map`;
TRUNCATE `vehicle`;
TRUNCATE `vendor`;
TRUNCATE `vendor_contract`;
TRUNCATE `vendor_contract_history`;
TRUNCATE `vendor_contract_rate`;
TRUNCATE `vendor_docket_item`;
TRUNCATE `vendor_estimate`;
TRUNCATE `vendor_estimate_contract`;
TRUNCATE `vendor_estimate_data`;
TRUNCATE `vendor_estimate_other_charge`;
TRUNCATE `vendor_invoice`;
TRUNCATE `vendor_invoice_docket`;
TRUNCATE `vendor_mapping`;
TRUNCATE `vendor_master_history`;
TRUNCATE `vendor_type`;
TRUNCATE `vendor_type_master_history`;
TRUNCATE `voucher`;
TRUNCATE `voucher_data`;
TRUNCATE `voucher_history`;
TRUNCATE `weight_bag`;
TRUNCATE `whatsapp_master`;
TRUNCATE `whatsapp_master_variable`;
TRUNCATE `zone`;
TRUNCATE `zone_master_history`;
``` 

```sql
set global sql_mode='ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```
```sql
INSERT INTO `admin_user` (`id`, `status`, `name`, `user_name`, `user_code`, `password`, `email`, `role`, `company_id`, `contactno`, `address`, `valid_till`, `created_date`, `created_by`, `modified_date`, `modified_by`, `auth_token`, `migration_id`) VALUES
(1, 1, 'ITD ADMIN', 'admin@itdservices.in', 'ITD12', 'fcea920f7412b5da7be0cf42b8c93759', 'admin@itdservices.in', 4, 1, '23323', '', '2021-07-31', '2021-07-22 13:06:38', 0, '2021-07-31 15:10:02', 2, '', 0);
```
```sql
INSERT INTO `company` (`id`, `status`, `company_code`, `company_name`, `company_domain`, `sef_url`, `login_count`, `description`, `is_restrict`, `onboard_date`, `expiry_date`, `payment_days`, `logo`, `portal_login_count`, `created_date`, `created_by`, `modified_date`, `modified_by`, `old_domain`,`powered_by_desc`,`portal_domain`) VALUES (1, 1, 'ITD12', 'ITD Services', '', '', 0, '', 1, NULL, '2021-07-29', 0, '', 0, '2021-07-22 13:06:01', 0, '2021-07-22 13:06:01', 0, '','','');
```

---

## 9️⃣ SOAP Extension Installation

- Navigate to root directory
```bash
cd ../../../../
```

```bash
sudo apt-get install php7.4-soap
sudo systemctl restart apache2
```

---

## 🔟 Application Code Setup

```bash
cd /var/www/html
git clone https://github.com/ashish27aghera/TRACKMATE-PHP.git
```

- Rename TRACKMATE-PHP to trackmate_lite

```
mv TRACKMATE-PHP trackmate_lite
```
- add config files
- `config.php`
- `constants.php` 
- `database.php` 

### Configure Database Credentials

Update **Constants.php** (1 place):

```php
define('DB_HOSTNAME', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', 'DB_Password');
```

Update **database.php** (2 places):

### Permissions

- create following folder with permission (777) using filezilla
    -  `trackmate_lite/application/logs` 
    -  `trackmate_lite/application/log1` 
- create following folder with permission (777) using filezilla
    - `trackmate_lite/client_media`

```bash
cd application
mkdir logs log1
chmod -R 777 logs log1

cd ..
mkdir client_media log1
chmod -R 777 client_media
```


---

## 1️⃣1️⃣ Install wkhtmltopdf

- Navigate to root directory
```bash
cd ../../../../

# or

cd /
```

```bash
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo apt install ./wkhtmltox_0.12.6-1.bionic_amd64.deb
```

```bash
sudo ln -s /usr/local/bin/wkhtmltopdf /usr/bin
sudo ln -s /usr/local/bin/wkhtmltoimage /usr/bin
cd /var/www/html
sudo cp /usr/local/bin/wkhtmltopdf trackmate_lite/
```
- give 755 permission to wkhtmltopdf in /var/www/html/trackmate_lite

---

## 1️⃣2️⃣ Deploy User Sudo Access

```bash
sudo nano /etc/sudoers
```

Add at end:

```text
deploy ALL=(ALL:ALL) ALL
```

---

## 1️⃣3️⃣ Email Configuration

Add emails in **ITD ADMIN EMAIL**:

* [admin@itdservices.in](mailto:admin@itdservices.in)
* [virag@itdservices.in](mailto:virag@itdservices.in)

---

## 1️⃣4️⃣ Automated MySQL Backup

- Navigate to root directory
```bash
cd ../../../../

# or

cd /
```

```bash
sudo apt-get install automysqlbackup
```
- type Y
- pop will open
    - press tab to select no configuraton
    - perss tab to select Ok
    
### Configure Backup Path

```bash
sudo nano /etc/default/automysqlbackup
```

```bash
BACKUPDIR="/var/www/html/trackmate_lite/db_backup_daily"
```

- create db_backup_daily directory in trackmate_lite

```bash
mkdir -p /var/www/html/trackmate_lite/db_backup_daily
```

### Modify Permissions

```bash
sudo nano /usr/sbin/automysqlbackup
```

Change:

```bash
chmod o-r ${BACKUPDIR}   → chmod 777 ${BACKUPDIR}
chmod 600 $2             → chmod 777 $2
```

### Disable Weekly Backup

```bash
DOWEEKLY=0
```

---

## ✅ Setup Completed

Your **Trackmate Lite server** is now fully configured with:

* Apache + PHP 7.4
* MySQL secured
* phpMyAdmin
* Application deployed
* Automated database backups

---

📌 **Recommended Next Steps**

* Install Imagick
