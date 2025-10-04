## ✅ **PHP Interview Questions and Answers**

---

### **1. What is the difference between `==` and `===` in PHP?**

* `==` compares **values** only (loose comparison).
* `===` compares **values and data types** (strict comparison).

```php
1 == "1"    // true
1 === "1"   // false
```

---

### **2. What are `include`, `require`, `include_once`, and `require_once`?**

| Function       | On Failure  | Multiple Inclusion |
| -------------- | ----------- | ------------------ |
| `include`      | Warning     | Yes                |
| `require`      | Fatal Error | Yes                |
| `include_once` | Warning     | No (once only)     |
| `require_once` | Fatal Error | No (once only)     |

Use `require_once` when a file **must be included only once**.

---

### **3. What are cookies and sessions in PHP?**

* **Cookies** store small amounts of data **on the client-side** (browser).
* **Sessions** store user data **on the server-side** and are more secure.

```php
// Set cookie
setcookie("user", "Ganesh", time()+3600);

// Start session
session_start();
$_SESSION['user'] = "Ganesh";
```

---

### **4. What are PHP Superglobals?**

Superglobals are built-in variables accessible anywhere:

* `$_GET`, `$_POST`, `$_REQUEST`
* `$_SESSION`, `$_COOKIE`, `$_FILES`, `$_SERVER`
* `$_ENV`, `$_GLOBALS`

---

### **5. What is the difference between GET and POST?**

| Feature    | GET                    | POST            |
| ---------- | ---------------------- | --------------- |
| Visibility | Parameters in URL      | Hidden          |
| Data Limit | Limited (\~2000 chars) | Large           |
| Use Case   | Fetching data          | Form submission |
| Security   | Less secure            | More secure     |

---

### **6. How does PHP handle error reporting?**

```php
error_reporting(E_ALL);
ini_set("display_errors", 1);
```

Types:

* `E_ERROR`, `E_WARNING`, `E_NOTICE`, `E_PARSE`, `E_ALL`

---

### **7. What is the difference between `unset()` and `unlink()`?**

* `unset()` removes a variable from memory.
* `unlink()` deletes a **file** from the filesystem.

```php
unset($var);         // remove variable
unlink("file.txt");  // delete file
```

---

### **8. What are traits in PHP?**

Traits allow you to reuse code **inside multiple classes** without inheritance.

```php
trait Logger {
    public function log($msg) {
        echo "Log: $msg";
    }
}

class App {
    use Logger;
}
```

---

### **9. What is the difference between abstract class and interface?**

| Feature     | Abstract Class | Interface           |
| ----------- | -------------- | ------------------- |
| Methods     | Can have both  | Only declarations   |
| Properties  | Yes            | No                  |
| Inheritance | One class only | Multiple interfaces |

---

### **10. What are access modifiers in PHP?**

* `public` – Accessible from anywhere.
* `private` – Accessible only within the class.
* `protected` – Accessible within the class and subclasses.

---

### **11. How to connect to MySQL using PDO in PHP?**

```php
try {
    $pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
    echo "Connected!";
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
```

---

### **12. How to prevent SQL injection in PHP?**

Use **prepared statements** with PDO or MySQLi.

```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$email]);
```

---

### **13. What is the use of `isset()` and `empty()`?**

* `isset()` checks if a variable is set and not null.
* `empty()` checks if a variable is **empty** (0, "", null, etc.)

```php
isset($x);   // true if defined and not null
empty($x);   // true if $x is "", 0, null, etc.
```

---

### **14. Difference between `explode()` and `implode()`**

* `explode()` splits a string into an array.
* `implode()` joins array elements into a string.

```php
explode(",", "a,b,c");       // ['a', 'b', 'c']
implode("-", ['a', 'b']);    // "a-b"
```

---

### **15. What is the difference between `for`, `foreach`, `while`, and `do-while` loops?**

* `for` – Known count iterations
* `foreach` – Iterate arrays
* `while` – Condition checked before loop
* `do-while` – Loop runs at least once

---

### **16. What is the difference between `echo`, `print`, and `print_r()`?**

* `echo` – Faster, can output multiple strings, no return value.
* `print` – Returns 1, so it can be used in expressions.
* `print_r()` – Used to print arrays and objects in human-readable format.

```php
echo "Hello", " World";
print "Hello"; // returns 1
print_r($array); // shows array structure
```

---

### **17. What are magic methods in PHP?**

Magic methods start with double underscores (`__`) and are triggered automatically.

Common ones:

* `__construct()` – Constructor
* `__destruct()` – Destructor
* `__get()`, `__set()` – Property overloading
* `__call()` – Method overloading
* `__toString()` – When object is treated as a string

---

### **18. What is the difference between `require_once` and autoloading classes?**

* `require_once` manually loads files.
* Autoloading dynamically loads classes when they’re needed using `spl_autoload_register`.

```php
spl_autoload_register(function ($class) {
    include $class . '.php';
});
```

---

### **19. How do you handle file uploads in PHP?**

```php
if (isset($_FILES['file'])) {
    move_uploaded_file($_FILES['file']['tmp_name'], "uploads/" . $_FILES['file']['name']);
}
```

Important: Check file type and size to prevent attacks.

---

### **20. What is CSRF and how do you prevent it in PHP?**

**CSRF** (Cross-Site Request Forgery) is when unauthorized commands are transmitted from a trusted user.

**Prevention:**

* Use **CSRF tokens** in forms.
* Validate tokens on form submission.

---

### **21. What is XSS and how do you prevent it?**

**XSS** (Cross-Site Scripting) is when malicious scripts are injected into websites.

**Prevention:**

* Use `htmlspecialchars()` or `htmlentities()` to sanitize output.

```php
echo htmlspecialchars($userInput);
```

---

### **22. How do you send email using PHP?**

Using the `mail()` function:

```php
mail("to@example.com", "Subject", "Message", "From: you@example.com");
```

For better reliability, use libraries like **PHPMailer** or **SwiftMailer**.

---

### **23. What is output buffering in PHP?**

It temporarily holds output data before sending it to the browser.

```php
ob_start();
echo "Hello";
$output = ob_get_clean(); // stores "Hello"
```

Useful for manipulating headers or compression.

---

### **24. What is the use of `final` keyword in PHP?**

* `final class` – Cannot be extended.
* `final function` – Cannot be overridden.

```php
final class A {}
final function myFunc() {}
```

---

### **25. How does PHP handle form submission and validation?**

* Use `$_POST` to retrieve data.
* Validate using `filter_var()`, `preg_match()`, or custom logic.
* Sanitize input before saving or using.

```php
$name = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
```

---

### **26. What is the difference between `array_merge()` and `+` operator with arrays?**

* `array_merge()` merges values (overwrites keys).
* `+` operator merges arrays but keeps the first array’s keys if duplicated.

```php
$a = ['a' => 1];
$b = ['a' => 2, 'b' => 3];

print_r(array_merge($a, $b)); // a=2, b=3
print_r($a + $b);             // a=1, b=3
```

---

### **27. What is a namespace in PHP and why is it used?**

Namespace allows grouping of related classes, functions, and constants to avoid naming conflicts.

```php
namespace App\Controllers;
class User {}
```

Used in larger apps, especially with autoloaders.

---

### **28. How do you destroy a session in PHP?**

```php
session_start();
session_unset();
session_destroy();
```

Also, clear the session cookie for complete removal.

---

### **29. How do you handle exceptions in PHP?**

```php
try {
    // risky code
} catch (Exception $e) {
    echo $e->getMessage();
}
```

You can create **custom exception classes** by extending `Exception`.

---

### **30. What are static methods and when should you use them?**

Static methods can be called without creating an object.

```php
class Math {
    public static function add($a, $b) {
        return $a + $b;
    }
}
echo Math::add(2, 3);
```

Used when logic doesn’t depend on object state (e.g., utility functions).

---

### **31. How do you secure a PHP application?**

* **Validate and sanitize** all user inputs.
* Use **prepared statements** to prevent SQL Injection.
* Escape output using `htmlspecialchars()` to prevent XSS.
* Use **HTTPS** for all data transfer.
* Implement **CSRF tokens** in forms.
* Avoid displaying sensitive error messages in production.
* Keep PHP and libraries up-to-date.

---

### **32. What are design patterns you have used in PHP?**

Common ones:

* **Singleton** – Only one instance of a class.
* **Factory** – Creates objects without exposing creation logic.
* **MVC** – Used in frameworks like CodeIgniter.

Example – Singleton:

```php
class DB {
    private static $instance;
    private function __construct() {}
    public static function getInstance() {
        if (!self::$instance) {
            self::$instance = new DB();
        }
        return self::$instance;
    }
}
```

---

### **33. What are differences between POST and PUT methods in REST API (PHP)?**

| Method | Purpose | Idempotent? |
| ------ | ------- | ----------- |
| POST   | Create  | ❌ No        |
| PUT    | Update  | ✅ Yes       |

* `POST`: Creates a new resource.
* `PUT`: Updates/replaces existing resource.

---

### **34. What are magic constants in PHP?**

They change depending on their usage. Examples:

* `__FILE__` – Full path of the file.
* `__DIR__` – Directory of the file.
* `__LINE__` – Current line number.
* `__FUNCTION__`, `__CLASS__` – Current function or class name.

---

### **35. How do you implement pagination in PHP?**

Use `LIMIT` and `OFFSET` in MySQL query.

```php
$page = $_GET['page'] ?? 1;
$limit = 10;
$offset = ($page - 1) * $limit;

$sql = "SELECT * FROM users LIMIT $limit OFFSET $offset";
```

---

### **36. What’s the difference between `isset()` and `array_key_exists()`?**

* `isset()` checks if a variable exists and is not null.
* `array_key_exists()` checks if a key exists in an array **even if the value is null**.

```php
$arr = ['a' => null];
isset($arr['a']); // false
array_key_exists('a', $arr); // true
```

---

### **37. How can you redirect a user in PHP?**

```php
header("Location: dashboard.php");
exit;
```

> Always call `exit;` after a `Location` header to prevent further script execution.

---

### **38. How do you handle JSON data in PHP?**

* `json_encode()` – Converts PHP array/object to JSON string.
* `json_decode()` – Converts JSON string to PHP data.

```php
$data = ['name' => 'Ganesh'];
$json = json_encode($data);

$parsed = json_decode($json, true); // decode as associative array
```

---

### **39. Difference between `strcmp()` and `===`?**

* `strcmp()` compares two strings **case-sensitively**, returns:

  * 0 if equal
  * < 0 if str1 < str2
  * > 0 if str1 > str2
* `===` checks if values and types are strictly equal.

---

### **40. What are some performance tips for PHP?**

* Use caching (`OPcache`, Redis, etc.)
* Avoid unnecessary loops and database queries.
* Use string functions efficiently (e.g., avoid `.` in loops).
* Minify assets (JS/CSS) and combine HTTP requests.
* Optimize SQL queries and use indexes.

---

### **41. What are the lifecycle stages of a PHP script?**

1. **Server receives request**
2. PHP script is interpreted
3. Output is generated (HTML/JSON/etc.)
4. Server sends response to browser
5. Memory is cleaned up

---

### **42. What is the difference between `count()` and `sizeof()`?**

There is no difference; both return the number of elements in an array.

---

### **43. How do you sort arrays in PHP?**

* `sort()` – Sorts array values (re-indexed)
* `asort()` – Sorts values, keeps keys
* `ksort()` – Sorts by keys
* `usort()` – Custom sort using callback

```php
usort($arr, function($a, $b) {
    return $a['score'] <=> $b['score'];
});
```

---

### **44. How to handle multi-dimensional arrays?**

Use `foreach` for nesting:

```php
$data = [['name' => 'A'], ['name' => 'B']];
foreach ($data as $user) {
    echo $user['name'];
}
```

---

### **45. What’s the difference between `require` and `autoload` in large apps?**

* `require` needs manual inclusion of every file.
* `autoload` uses a dynamic approach, automatically loading classes when needed – efficient for large apps with many classes.

---
