
## ✅ **SQL Interview Questions & Answers for PHP Developers**

---

### **1. What is the difference between `WHERE` and `HAVING`?**

* `WHERE` filters **rows before** grouping.
* `HAVING` filters **groups after** `GROUP BY`.

```sql
SELECT department, COUNT(*) 
FROM employees 
WHERE status = 'active' 
GROUP BY department 
HAVING COUNT(*) > 5;
```

---

### **2. What is the difference between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`?**

| Join Type    | Returns                                                                     |
| ------------ | --------------------------------------------------------------------------- |
| `INNER JOIN` | Matching rows in both tables                                                |
| `LEFT JOIN`  | All rows from left + matching from right                                    |
| `RIGHT JOIN` | All rows from right + matching from left                                    |
| `FULL JOIN`  | All rows from both sides (MySQL doesn't support it natively; needs `UNION`) |

---

### **3. How do you find the second highest salary in a table?**

```sql
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

Or using `LIMIT`:

```sql
SELECT DISTINCT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1;
```

---

### **4. What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?**

| Operation  | Removes Data | Can Rollback            | Resets Auto-Increment | Affects Structure |
| ---------- | ------------ | ----------------------- | --------------------- | ----------------- |
| `DELETE`   | Yes          | Yes (with transactions) | No                    | No                |
| `TRUNCATE` | Yes (all)    | No                      | Yes                   | No                |
| `DROP`     | Entire table | No                      | -                     | Yes (table gone)  |

---

### **5. What are indexes in MySQL?**

Indexes improve **read/query performance** by allowing fast lookup.

```sql
CREATE INDEX idx_name ON employees(name);
```

Types:

* **Primary Key** (unique, not null)
* **Unique Index**
* **Composite Index** (multi-column)
* **Fulltext Index** (for searching text)

---

### **6. What is a primary key and foreign key?**

* **Primary Key**: Uniquely identifies a record in a table.
* **Foreign Key**: Links one table to another.

```sql
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

### **7. What is normalization? What are 1NF, 2NF, and 3NF?**

**Normalization** is the process of organizing data to remove redundancy.

* **1NF**: Atomic values (no repeating groups)
* **2NF**: No partial dependency on a composite primary key
* **3NF**: No transitive dependency (non-key depending on non-key)

---

### **8. What’s the difference between `GROUP BY` and `ORDER BY`?**

* `GROUP BY` is used to aggregate (SUM, COUNT, etc.)
* `ORDER BY` is used to sort the result

```sql
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department 
ORDER BY COUNT(*) DESC;
```

---

### **9. How do you update data from another table?**

```sql
UPDATE orders 
JOIN users ON orders.user_id = users.id 
SET orders.status = 'verified' 
WHERE users.verified = 1;
```

---

### **10. How do you find duplicate values in a column?**

```sql
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;
```

---

### **11. What is the use of `IFNULL()` or `COALESCE()` in SQL?**

* `IFNULL(expr, value)` – returns `value` if `expr` is null
* `COALESCE(expr1, expr2, ...)` – returns first non-null

```sql
SELECT name, IFNULL(phone, 'Not Provided') FROM users;
```

---

### **12. How do you select only the top N records in MySQL?**

```sql
SELECT * FROM products 
ORDER BY created_at DESC 
LIMIT 5;
```

---

### **13. What is a subquery? Provide an example.**

A **subquery** is a query nested inside another query.

```sql
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE status = 'pending');
```

---

### **14. What is a self join?**

A table joins with itself.

```sql
SELECT a.name AS emp, b.name AS manager 
FROM employees a 
JOIN employees b ON a.manager_id = b.id;
```

---

### **15. Difference between `UNION` and `UNION ALL`?**

* `UNION` removes duplicates.
* `UNION ALL` includes all rows (faster).

```sql
SELECT name FROM students
UNION
SELECT name FROM alumni;
```

---

### **16. How do you count rows with conditions?**

```sql
SELECT COUNT(*) FROM users WHERE status = 'active';
```

---

### **17. How do you get the current date and time in MySQL?**

```sql
SELECT NOW(); -- current datetime
SELECT CURDATE(); -- only date
SELECT CURTIME(); -- only time
```

---

### **18. How do you rename a table or column?**

```sql
RENAME TABLE old_name TO new_name;

ALTER TABLE users RENAME COLUMN old_col TO new_col;
```

---

### **19. How to add a new column to an existing table?**

```sql
ALTER TABLE users ADD COLUMN bio TEXT;
```

---

### **20. What are transactions in MySQL?**

They ensure **ACID** properties (Atomicity, Consistency, Isolation, Durability).

```sql
START TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE id = 1;
UPDATE account SET balance = balance + 100 WHERE id = 2;
COMMIT; -- or ROLLBACK;
```

---

