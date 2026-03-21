# 🧠 Writing **Readable & Maintainable Code**

> Code is read **10× more** than it is written.
> Your real audience is the **next developer** (often future you).

---

## 1️⃣ Readability vs Maintainability (They’re Not the Same)

### 📖 Readability

* Can I understand this code **in 30 seconds**?
* Can I explain it without running it?

### 🧰 Maintainability

* Can I safely change this code?
* Will a small change break unrelated logic?

Good code must have **both**.

---

## 2️⃣ The Senior Engineer’s Golden Rule

> **Make the code obvious, not clever.**

If someone needs to ask:

* “Why is this done like this?”
* “What does this flag mean?”

The code has failed.

---

## 3️⃣ Naming Is Design (THIS IS HUGE)

### ❌ Bad Names (Hide Intent)

```php
$data
$flag
$val
$process()
```

### ✅ Good Names (Reveal Intent)

```php
$orderItems
$isPaymentSuccessful
$discountAmount
$processPayment()
```

💡 **Rule**

> If you need a comment to explain a name, the name is wrong.

---

## 4️⃣ Functions That Read Like Sentences

### ❌ Bad

```php
if ($u && $u->a() && !$u->b()) {}
```

### ✅ Good

```php
if ($user->isActive() && $user->hasValidSubscription()) {}
```

Code should read like English.

---

## 5️⃣ One Function = One Responsibility

### ❌ Bad (Multiple Responsibilities)

```php
function placeOrder() {
    validate();
    pay();
    updateInventory();
    sendEmail();
}
```

### ✅ Better (Still readable, but structured)

```php
function placeOrder() {
    $this->validateOrder();
    $this->processPayment();
    $this->finalizeOrder();
}
```

Each function should operate at **one level of abstraction**.

---

## 6️⃣ Avoid Deep Nesting (Cognitive Load Killer)

### ❌ Bad

```php
if ($a) {
    if ($b) {
        if ($c) {
            doSomething();
        }
    }
}
```

### ✅ Good (Fail Fast)

```php
if (!$a || !$b || !$c) {
    return;
}

doSomething();
```

💡 Seniors prefer **guard clauses**.

---

## 7️⃣ Comments: When to Use and When NOT To

### ❌ Bad Comments

```php
// check if user is active
if ($user->isActive()) {}
```

### ✅ Good Comments (Explain WHY)

```php
// Payment gateway retries can cause duplicate charges
```

**Rule**

> Comment the *why*, not the *what*.

---

## 8️⃣ Magic Numbers & Strings (Silent Bugs)

### ❌ Bad

```php
if ($status === 3) {}
```

### ✅ Good

```php
if ($status === OrderStatus::CANCELLED) {}
```

Use:

* Constants
* Enums

---

## 9️⃣ Small Classes, Clear Boundaries

### ❌ Bad

```php
class OrderManager {
    // everything related to order
}
```

### ✅ Good

```php
class OrderService {}
class OrderValidator {}
class OrderRepository {}
```

Each class should fit in **one screen**.

---

## 🔟 Error Handling That Tells a Story

### ❌ Bad

```php
catch (Exception $e) {}
```

### ✅ Good

```php
catch (PaymentFailedException $e) {
    $logger->error($e->getMessage());
    throw $e;
}
```

Errors should be:

* Explicit
* Meaningful
* Actionable

---

## 1️⃣1️⃣ Readable Code Is Testable Code

If code is hard to test, it’s probably:

* Too coupled
* Too much responsibility
* Not readable

Readability and testability grow together.

---

## 1️⃣2️⃣ Real Refactoring Example (Before → After)

### ❌ Before

```php
function f($x, $y) {
    return $x > 100 ? $y * 0.2 : $y * 0.1;
}
```

### ✅ After

```php
function calculateDiscount(int $userOrderCount, float $amount): float {
    if ($this->isLoyalCustomer($userOrderCount)) {
        return $this->getLoyaltyDiscount($amount);
    }

    return $this->getStandardDiscount($amount);
}
```

Readable. Obvious. Safe.

---

## 1️⃣3️⃣ Senior Developer Checklist (Use Daily)

Before committing code, ask:

* Can a new dev understand this quickly?
* Are names self-explanatory?
* Are functions short and focused?
* Is error handling explicit?
* Can I change this safely?

If yes → good code.

---

## 1️⃣4️⃣ PRACTICE (THIS MAKES YOU LEVEL UP)

### 🧪 Exercise 1

Take any function you wrote recently:

* Rename variables
* Extract methods
* Remove nesting

### 🧪 Exercise 2

Rewrite this code to be readable:

```php
if ($a && !$b && ($c || $d)) {
    doIt();
}
```

---
