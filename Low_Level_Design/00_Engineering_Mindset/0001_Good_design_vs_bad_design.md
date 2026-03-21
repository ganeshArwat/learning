## Topic 1: **Good Design vs Bad Design** (DEEP DIVE)

> A pro developer doesn’t write “working code”.
> A pro developer writes **change-friendly code**.

---

## 1️⃣ What “Design” Really Means (From Real Experience)

When seniors say *design*, they **do NOT** mean:

* UML diagrams
* Fancy patterns
* Over-engineering

They mean:

> “How painful will it be to change this code 6 months later?”

That’s it. That’s the whole game.

---

## 2️⃣ The Real Definition of Good Design

### ✅ Good Design

Code that:

* Accepts **change without fear**
* Localizes impact (change in one place)
* Can be understood **without explanation**
* Can be tested in isolation

### ❌ Bad Design

Code that:

* Works today, scares everyone tomorrow
* One change → many files touched
* Only the original author understands
* Nobody wants to refactor

💡 **Industry truth**
Most production bugs happen **while changing existing code**, not while writing new code.

---

## 3️⃣ The “Change Test” (Senior Engineer’s Mental Model)

Whenever you look at code, ask:

> “If I add ONE new requirement, how many places do I change?”

| Places to change | Design Quality |
| ---------------- | -------------- |
| 1 place          | Excellent      |
| 2–3 places       | Acceptable     |
| 5+ places        | Bad            |
| “Not sure”       | Very bad       |

This test never lies.

---

## 4️⃣ Real Example from Production (Payment System)

### ❌ Version 1 – Bad Design (Looks Simple)

```php
function processPayment($type, $amount) {
    if ($type === 'card') {
        // card logic
    } elseif ($type === 'upi') {
        // upi logic
    } elseif ($type === 'netbanking') {
        // netbanking logic
    }
}
```

### Why juniors think this is OK

* Easy to read
* Less files
* Works fine

### Why seniors hate it

* Every new payment method → modify this function
* Risk of breaking existing logic
* Violates Open/Closed Principle

---

## 5️⃣ The First Trade-off Lesson (VERY IMPORTANT)

Let’s be honest:

| Version         | Pros       | Cons           |
| --------------- | ---------- | -------------- |
| If-else         | Simple     | Hard to extend |
| OOP + Interface | Extensible | More code      |

### Senior Decision

> “Do we expect new payment methods?”

* **No** → keep it simple
* **Yes** → design for extension

💡 **Interview GOLD**

> “I’ll start simple and refactor when new requirements appear.”

---

## 6️⃣ Refactor Like a Professional (Step by Step)

### Step 1: Identify the **Axis of Change**

Ask:

> “What is changing here?”

Answer:
➡️ Payment type

---

### Step 2: Create an Abstraction

```php
interface PaymentMethod {
    public function pay(float $amount): void;
}
```

This is NOT theory.
This is isolating change.

---

### Step 3: Concrete Implementations

```php
class CardPayment implements PaymentMethod {
    public function pay(float $amount): void {
        // card logic
    }
}

class UpiPayment implements PaymentMethod {
    public function pay(float $amount): void {
        // upi logic
    }
}
```

---

### Step 4: High-Level Class Depends on Abstraction

```php
class PaymentProcessor {
    private PaymentMethod $method;

    public function __construct(PaymentMethod $method) {
        $this->method = $method;
    }

    public function process(float $amount): void {
        $this->method->pay($amount);
    }
}
```

### Why this is **professional-grade**

* Adding payment = new class only
* No existing code touched
* Easy to test
* Easy to explain

---

## 7️⃣ Common Junior Mistakes (Learn from Pain)

### 🚫 Mistake 1: Over-engineering too early

Creating 10 interfaces for a small script.

### 🚫 Mistake 2: Pattern obsession

Using Strategy/Factory where simple code is enough.

### 🚫 Mistake 3: Fear of refactoring

Good developers refactor often.

---

## 8️⃣ How Seniors Actually Decide Design

They ask 3 questions:

1. **What will change?**
2. **How often will it change?**
3. **What happens if I’m wrong?**

Design is **risk management**, not perfection.

---

## 9️⃣ PRACTICE (REAL, NOT TOY)

### 🧪 Exercise 1 – Thought Exercise

Given this code:

```php
function calculateDiscount($userType, $amount) {
    if ($userType === 'premium') {
        return $amount * 0.2;
    } elseif ($userType === 'regular') {
        return $amount * 0.1;
    }
    return 0;
}
```

Answer:

1. What is the axis of change?
2. When does this design break?
3. Should we refactor now or later? Why?

---

### 🧪 Exercise 2 – Refactor

Refactor it using:

* Interface
* Separate classes
* Clean naming

---

## 10️⃣ Homework (MANDATORY)

### Task A

Pick **one real PHP file** from your project:

* Identify **3 places** where change would be painful
* Write down why

### Task B

Refactor **only one** of those places.

---
