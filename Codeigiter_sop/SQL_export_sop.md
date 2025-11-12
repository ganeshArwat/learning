# 🧰 **SOP: Export Live Database Using mysqldump Command**

---

## 🔹 **Objective**

To export (take a backup of) a **live MySQL database** from a Linux server into a `.sql` file using the `mysqldump` command.

---

## 🔹 **Scope**

This procedure applies to all system administrators or developers who need to take a **manual or scheduled backup** of MySQL/MariaDB databases hosted on a live server.

---

## 🔹 **Prerequisites**

✅ SSH access to the server (root or user with database dump privileges)
✅ Database credentials (username, password, database name)
✅ Sufficient disk space to store the backup file

---

## 🔹 **Details**

* **Database Name:** `trackmate_company_16`
* **Backup File Name:** `trackmate_company_16_12_11_2025.sql`
* **Command Tool:** `mysqldump`
* **User:** `root`

---

## 🔹 **Procedure**

### **Step 1: Connect to the Server**

Use **SSH** to access your server:

```bash
ssh root@your-server-ip
```

Enter your **server password** if prompted.

---

### **Step 2: Navigate to Backup Directory**

(Optional but recommended — store backups in a specific folder)

```bash
cd /var/backups/
```

or

```bash
cd /home/backup/
```

If the folder doesn’t exist:

```bash
mkdir -p /var/backups
```

---

### **Step 3: Execute the mysqldump Command**

Run the following command to export the live database:

```bash
mysqldump -u root -p trackmate_company_16 > trackmate_company_16_12_11_2025.sql
```

**Explanation of Parameters:**

| Parameter                             | Description                            |
| ------------------------------------- | -------------------------------------- |
| `mysqldump`                           | Utility used to export MySQL databases |
| `-u root`                             | Username (here, `root`)                |
| `-p`                                  | Prompts for the password               |
| `trackmate_company_16`                | Name of the database to export         |
| `>`                                   | Redirects output to a file             |
| `trackmate_company_16_12_11_2025.sql` | Name of the exported backup file       |

---

### **Step 4: Enter the MySQL Password**

After running the command, you’ll be prompted:

```
Enter password:
```

Type your **MySQL root password**, then press **Enter**.

---

### **Step 5: Verify the Backup File**

Once the command finishes successfully, check if the `.sql` file was created:

```bash
ls -lh trackmate_company_16_12_11_2025.sql
```

✅ Example Output:

```
-rw-r--r-- 1 root root 25M Nov 12 12:45 trackmate_company_16_12_11_2025.sql
```

---

### **Step 6 (Optional): Compress the Backup File**

To save disk space, you can compress it using gzip:

```bash
gzip trackmate_company_16_12_11_2025.sql
```

Resulting file:

```
trackmate_company_16_12_11_2025.sql.gz
```

---

### **Step 7 (Optional): Move Backup to Safe Location**

You can move or copy the backup file to another directory or remote storage:

```bash
mv trackmate_company_16_12_11_2025.sql.gz /backup/mysql/
```

or transfer it via SCP:

```bash
scp trackmate_company_16_12_11_2025.sql.gz user@remote-server:/remote/backup/path/
```

---

## 🔹 **Verification Checklist**

| Check                                       | Status |
| ------------------------------------------- | ------ |
| SSH access working                          | ✅      |
| Backup file created                         | ✅      |
| File contains SQL data (`CREATE`, `INSERT`) | ✅      |
| File size reasonable                        | ✅      |
| Optional compression done                   | ⬜      |

---

## 🔹 **Sample Command Summary**

```bash
mysqldump -u root -p trackmate_company_16 > trackmate_company_16_12_11_2025.sql
```

---

## ✅ **Result**

A backup file named
`trackmate_company_16_12_11_2025.sql`
is successfully generated in the current directory containing the **entire live database dump**.

