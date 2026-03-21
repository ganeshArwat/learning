## **Encapsulation**

If you truly understand **encapsulation**,
you’ll immediately write **cleaner, safer, interview-winning code**.

Most devs *think* they know this.
Very few actually **practice** it.

---

## 1️⃣ What Encapsulation REALLY means (not textbook)

Textbook says:

> “Encapsulation is binding data and methods together and hiding internal details.”

Senior engineer translation:

> **Encapsulation is about controlling damage.**

It answers:

* Who is allowed to **change state**?
* How can state be **changed safely**?
* What must NEVER be violated?

Encapsulation is **risk management**, not syntax.

---

## 2️⃣ The core idea (one sentence you should remember)

> **Outside code should not be able to put your object into an invalid state.**

If it can — your design is broken.

---

## 3️⃣ The #1 mistake developers make

### ❌ Fake Encapsulation (very common in PHP)

```php
class Order {
    public $status;
}
```

Then elsewhere:

```php
$order->status = 'SHIPPED';
$order->status = 'CREATED';
$order->status = 'CANCELLED';
```

🚨 **This is chaos**
🚨 No rules
🚨 No control
🚨 Bugs waiting to happen

This is **not encapsulation**, even though it’s inside a class.

---

## 4️⃣ Real Encapsulation (production-grade)

```php
class Order {
    private string $status;

    public function __construct() {
        $this->status = 'CREATED';
    }

    public function pay(): void {
        if ($this->status !== 'CREATED') {
            throw new Exception("Only created orders can be paid");
        }
        $this->status = 'PAID';
    }

    public function ship(): void {
        if ($this->status !== 'PAID') {
            throw new Exception("Order must be paid before shipping");
        }
        $this->status = 'SHIPPED';
    }

    public function getStatus(): string {
        return $this->status;
    }
}
```

Now:

* State is **private**
* Changes go through **controlled paths**
* Rules are **enforced automatically**

This is **real encapsulation**.

---

## 5️⃣ Visibility keywords (but with meaning)

| Keyword     | Meaning in real life                        |
| ----------- | ------------------------------------------- |
| `public`    | Anyone can touch this (dangerous)           |
| `private`   | Only this class can touch it                |
| `protected` | Only subclasses can touch it (often abused) |

### Senior rule:

> Start with **private by default**.
> Make it public **only if you are forced to**.

---

## 6️⃣ Encapsulation is NOT “getters & setters”

This is a hard truth.

### ❌ Classic bad code

```php
class User {
    private string $email;

    public function setEmail(string $email): void {
        $this->email = $email;
    }

    public function getEmail(): string {
        return $this->email;
    }
}
```

This is just **public access with extra steps**.

---

### ✅ Better encapsulation

```php
class User {
    private string $email;

    public function __construct(string $email) {
        $this->email = $this->normalizeEmail($email);
    }

    public function changeEmail(string $newEmail): void {
        $this->email = $this->normalizeEmail($newEmail);
    }

    private function normalizeEmail(string $email): string {
        return strtolower(trim($email));
    }
}
```

Notice:

* No generic setter
* Method expresses **intent**: `changeEmail`
* Rules are centralized

💡 **Intent-based methods > setters**

---

## 7️⃣ JavaScript version (same concept)

```js
class Order {
  #status;

  constructor() {
    this.#status = "CREATED";
  }

  pay() {
    if (this.#status !== "CREATED") {
      throw new Error("Invalid state transition");
    }
    this.#status = "PAID";
  }

  ship() {
    if (this.#status !== "PAID") {
      throw new Error("Order must be paid");
    }
    this.#status = "SHIPPED";
  }

  getStatus() {
    return this.#status;
  }
}
```

Private fields (`#`) enforce encapsulation at **language level**.

---

## 8️⃣ Real-life analogy (used by senior architects)

Think of a **bank account**.

Would you allow:

```php
$account->balance = -100000;
```

Of course not.

Instead:

* `deposit(amount)`
* `withdraw(amount)`
* Rules: no overdraft

That’s encapsulation.

---

## 9️⃣ Encapsulation vs Validation (important distinction)

❌ Validation:

```php
if ($order->status !== 'PAID') { ... }
```

✅ Encapsulation:

```php
$order->ship();
```

Senior rule:

> **Validation checks state.
> Encapsulation prevents invalid state.**

---

## 🔟 Interview-winning line (memorize this)

> “Encapsulation ensures objects can never be in an invalid state by restricting direct access to internal data and forcing all mutations through well-defined behaviors.”

This line alone separates **mid-level** from **senior**.

---

## 🧠 Mini Practice (think before coding)

### Question:

Should `Cart` expose its items array publicly?

❌ `getItems(): array` → dangerous
✅ `addItem()`, `removeItem()`, `getTotalPrice()`

Why?
Because cart owns **rules** like quantity, duplicates, pricing.

---

## 🧠 Golden Rule (from production scars)

> **If outside code needs to “fix” your object,
> your object is badly encapsulated.**

---
