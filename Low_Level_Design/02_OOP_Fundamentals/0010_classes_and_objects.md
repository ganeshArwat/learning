## **Classes & Objects**

Before we touch code, let me set the **mental model**.

---

## 0️⃣ First: Forget “OOP definitions” for a minute

Most juniors think:

> “Class = blueprint, Object = instance”

That’s **true**, but it’s also **useless** if you stop there.

As a senior engineer, I think of **classes and objects** like this:

> **A class is a boundary around responsibility.**
> **An object is a living thing with state + behavior + rules.**

If you don’t feel *responsibility* when you design a class, you’re not doing OOP — you’re just grouping functions.

---

## 1️⃣ What is a Class (REAL meaning)

A **class** answers 3 questions:

1. **What data does this thing own?**
2. **What behavior is it responsible for?**
3. **What rules must always be true?**

If you can’t answer these, the class shouldn’t exist yet.

### ❌ Bad mindset

```php
class User {
    public $id;
    public $name;
    public $email;
}
```

This is **not** OOP.
This is a **struct with a fake mustache**.

---

### ✅ Good mindset

```php
class User {
    private int $id;
    private string $email;

    public function __construct(int $id, string $email) {
        $this->id = $id;
        $this->email = $this->normalizeEmail($email);
    }

    public function getEmail(): string {
        return $this->email;
    }

    private function normalizeEmail(string $email): string {
        return strtolower(trim($email));
    }
}
```

Now we have:

* **Ownership** of data
* **Rules** (email normalization)
* **Behavior** tied to data

💡 **Rule from experience:**

> If a class has only public properties → it’s not a class, it’s a data leak.

---

## 2️⃣ What is an Object (REAL meaning)

An **object** is a **runtime actor**.

Think of it as:

* It has **memory**
* It has **identity**
* It reacts to messages (method calls)

### Real-life analogy (used in system design meetings)

Think of an **Order object** as:

* A file on a desk
* With current status
* With rules like “you can’t ship before payment”

That’s an **object**, not a row in DB.

---

### Example: Order as an object (not DB row)

```php
class Order {
    private string $status;

    public function __construct() {
        $this->status = 'CREATED';
    }

    public function pay(): void {
        if ($this->status !== 'CREATED') {
            throw new Exception("Order cannot be paid");
        }
        $this->status = 'PAID';
    }

    public function ship(): void {
        if ($this->status !== 'PAID') {
            throw new Exception("Order must be paid before shipping");
        }
        $this->status = 'SHIPPED';
    }
}
```

💡 **Senior insight:**

> Business rules belong inside objects, not in controllers or services.

---

## 3️⃣ Classes vs Objects (Interview-grade explanation)

| Concept        | Class         | Object           |
| -------------- | ------------- | ---------------- |
| Nature         | Definition    | Runtime instance |
| Exists when    | Compile time  | Runtime          |
| Memory         | No            | Yes              |
| Responsibility | Defines rules | Enforces rules   |

If an interviewer asks:

> “Why do we need objects?”

Your answer:

> “Objects encapsulate state and behavior together so business rules cannot be violated accidentally.”

That’s a **strong** answer.

---

## 4️⃣ Common Real-World Mistakes (3+ years devs still do this)

### ❌ God Class

```php
class OrderManager {
    public function createOrder() {}
    public function calculateTax() {}
    public function sendEmail() {}
    public function saveToDB() {}
}
```

This is **procedural code wearing OOP clothes**.

---

### ✅ Correct thinking

Ask:

* Who **owns** tax calculation? → `TaxCalculator`
* Who **owns** email sending? → `NotificationService`
* Who **owns** order rules? → `Order`

---

## 5️⃣ When should you create a class?

Create a class **only if**:

* It has **state**
* It has **rules**
* It protects invariants

### ❌ Don’t create classes for:

* Just grouping functions
* Utility helpers
* Static-only behavior

That’s a rookie mistake.

---

## 6️⃣ PHP vs JavaScript (same idea, different syntax)

### PHP

```php
$user = new User(1, "TEST@Email.com");
```

### JavaScript (ES6)

```js
const user = new User(1, "TEST@Email.com");
```

**Concept is identical.**
Language doesn’t matter — **design does**.

---

## 7️⃣ Mini Practice (DO THIS NOW)

Think, don’t code immediately.

### Question:

> Should `Cart` know how to calculate total price?

Answer:

* YES — because **cart owns items**
* NO — if pricing rules change frequently → delegate to a service

This is **design trade-off thinking**.

---

## 8️⃣ Senior Engineer Golden Rule (Write this down)

> **Classes protect business rules.
> Objects enforce them at runtime.
> Everything else is noise.**

---
