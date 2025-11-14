# Database Alteration SOP

## Roles & responsibilities

* **Author / Developer** — prepares SQL / migration code and tests locally.
* **Reviewer** — reviews SQL/migration, approves, confirms no breaking changes.
* **DB Admin / Ops** — runs migrations on staging/production (or author with ops approval).
* **Release Coordinator** — schedules change window and notifies stakeholders.

---

# A. PREPARATION (always do these first)

1. **Back up the database** (full dump) for every environment you will touch:

   * Staging: `mysqldump ... > staging_backup_YYYYMMDD.sql`
   * Production: `mysqldump ... > prod_backup_YYYYMMDD.sql`
2. **Open a change ticket** with:

   * Purpose, affected tables, SQL, rollback plan, downtime window, contact person.
3. **Confirm environment variables** (DB host, DB name, credentials) and ensure you have permissions.
4. **Publish change window** to the team/stakeholders (time, duration, expected impact).
5. **Version control**: add migration / helper code to git branch and create PR.

---

# B. ADD NEW COLUMN — Standard flow

### 1. Add to `create_table_helper.php`

Add the column to the table creation function so new installs get the correct schema.

```php
if (!function_exists('address_book_email_table_qry')) {
    function address_book_email_table_qry()
    {
        $qry = "CREATE TABLE IF NOT EXISTS `address_book_email` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `status` tinyint(1) NOT NULL DEFAULT 1,
            `address_book_id` int(11) NOT NULL,
            `email_id` varchar(255) NOT NULL,
            `customer_id` int(11) NOT NULL,
            `customer_code` varchar(255) NOT NULL,
            `customer_name` varchar(255) NOT NULL,
            `created_date` datetime NOT NULL,
            `created_by` int(11) NOT NULL,
            `modified_date` datetime NOT NULL,
            `modified_by` int(11) NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";
        return $qry;
    }
}
```

> If adding a column (e.g. `address_book_id`) ensure it's present in this function.

### 2. Update `database_migration/<table_file_name>.php`

Add the new column entry to `column_list()` so migrations/tools that read column metadata know the column exists.

```php
class Address_book_email_table extends MX_Controller
{
    public function column_list()
    {
        $column_structure = array(
            0 => 'Field:id, Type:int(11), Null:NO, Key:PRI, Default:, Extra:auto_increment',
            1 => 'Field:status, Type:tinyint(1), Null:NO, Key:, Default:1, Extra:',
            2 => 'Field:address_book_id, Type:int(11), Null:NO, Key:, Default:, Extra:',
            3 => 'Field:email_id, Type:varchar(255), Null:NO, Key:, Default:, Extra:',
            // ...
        );
        return $column_structure;
    }
}
```

### 3. Add ALTER query to `script.php` (add_new_column function)

Add the query you will run on servers. Example:

```php
$column_qury = "ALTER TABLE `address_book_email`
    ADD COLUMN `address_book_id` INT(11) NOT NULL AFTER `status`;";
```

Place the query in the `add_new_column` logic so the script executes it in each environment.

### 4. Run the script on each server

Open the migration script URL (or run via CLI) on each environment:

```
http://localhost/trackmate_lite/script/add_new_column
```

Or run equivalent CLI/script that your deployment uses.

### 5. Verify

* Confirm column exists: `SHOW COLUMNS FROM address_book_email;`
* Confirm app behavior: run the application features that read/write the column.
* Check logs / error monitoring.

### 6. Rollback (if needed)

* DROP the column:

```sql
ALTER TABLE `address_book_email` DROP COLUMN `address_book_id`;
```

* Restore DB from backup if data was corrupted.

---

# C. ADD NEW TABLE — Standard flow

### 1. Add table query in `create_table_helper.php`

Add a new function that returns `CREATE TABLE IF NOT EXISTS` SQL.

```php
if (!function_exists('address_book_email_table_qry')) {
    function address_book_email_table_qry()
    {
        $qry = "CREATE TABLE IF NOT EXISTS `address_book_email` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `status` tinyint(1) NOT NULL DEFAULT 1,
            `address_book_id` int(11) NOT NULL,
            `email_id` varchar(255) NOT NULL,
            `customer_id` int(11) NOT NULL,
            `customer_code` varchar(255) NOT NULL,
            `customer_name` varchar(255) NOT NULL,
            `created_date` datetime NOT NULL,
            `created_by` int(11) NOT NULL,
            `modified_date` datetime NOT NULL,
            `modified_by` int(11) NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";
        return $qry;
    }
}
```

### 2. Add table name to `create_all_table` in `database_manage_helper.php`

Add the function name to the `$table_list` so it will be processed:

```php
$table_list = array(
    'customer',
    'shipper',
    'address_book_email_table_qry'
);
```

### 3. Create migration file via Docket_table create_file flow

Update any controller logic that expects the new table name variable, e.g. in `Docket_table.php` adjust:

```php
if ($tvalue == 'address_book_email_table_qry') {
    // handle creation
}
```

Then run:

```
http://localhost/trackmate_lite/database_migration/docket_table/create_file
```

This should generate the migration file in `database_migration`.

### 4. Add create-table query to `script.php` (add_new_table function)

Include the exact `CREATE TABLE IF NOT EXISTS` SQL for the script to run across servers. Example:

```php
$table_exist_query1 = "CREATE TABLE IF NOT EXISTS `address_book_email` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `status` tinyint(1) NOT NULL DEFAULT 1,
    `manifest_id` int(11) NOT NULL,
    `actual_arrival_time` time NULL DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8";
```

### 5. Run script on all servers

```
http://localhost/trackmate_lite/script/add_new_table
```






