## **Abstraction**

If encapsulation is about **protecting state**,
**abstraction is about protecting your brain** 🧠.

---

## 1️⃣ What Abstraction REALLY means (no textbook fluff)

Textbook says:

> “Abstraction hides implementation details.”

Senior engineer translation:

> **Abstraction hides decisions that are likely to change.**

That’s it. That’s the whole point.

If something is **unlikely to change**, don’t abstract it.
If something **will change**, abstraction saves your future self.

---

## 2️⃣ The mental model seniors use

When I design abstraction, I ask:

1. **What problem am I solving?**
2. **What variations might exist tomorrow?**
3. **What should the caller NOT care about?**

Abstraction is a **contract**, not a trick.

---

## 3️⃣ BAD abstraction (very common mistake)

### ❌ Abstracting too early

```php
interface OrderServiceInterface {
    public function createOrder();
}
```

And there is **only one implementation** forever.

This is **cargo-cult abstraction**.
You added:

* Extra files
* Extra complexity
* Zero benefit

Senior rule:

> **Don’t abstract until you feel pain.**

---

## 4️⃣ GOOD abstraction (real-world case)

### Scenario: Payment processing

Today:

* Razorpay

Tomorrow:

* Stripe
* Cash on Delivery
* Wallet

### ❌ Bad design

```php
class Order {
    public function payWithRazorpay() {}
}
```

Now `Order` changes **every time payment changes**.
This violates **Open/Closed Principle** (we’ll cover later).

---

### ✅ Proper abstraction

```php
interface PaymentGateway {
    public function charge(int $amount): bool;
}
```

```php
class RazorpayGateway implements PaymentGateway {
    public function charge(int $amount): bool {
        // Razorpay logic
        return true;
    }
}
```

```php
class Order {
    private PaymentGateway $paymentGateway;

    public function __construct(PaymentGateway $paymentGateway) {
        $this->paymentGateway = $paymentGateway;
    }

    public function pay(int $amount): void {
        if (!$this->paymentGateway->charge($amount)) {
            throw new Exception("Payment failed");
        }
    }
}
```

Now:

* Order doesn’t know *how* payment works
* Only knows *what* it needs: `charge()`
* Payment method can change without touching Order

That’s abstraction **done right**.

---

## 5️⃣ Abstraction is NOT Interfaces only

This is important.

### Abstraction can be:

* Interface
* Abstract class
* Method contract
* Even a simple class boundary

Example:

```php
class TaxCalculator {
    public function calculate(Order $order): int {
        // tax logic
    }
}
```

Here:

* `Order` doesn’t know tax logic
* That’s abstraction **without interfaces**

Interfaces are a **tool**, not the goal.

---

## 6️⃣ PHP vs JavaScript abstraction

### PHP (interface)

```php
interface Logger {
    public function log(string $message): void;
}
```

### JavaScript (duck typing)

```js
class FileLogger {
  log(message) {}
}
```

JS doesn’t need interfaces — **behavior matters**, not type.

Senior insight:

> Abstraction is about **expectations**, not syntax.

---

## 7️⃣ How seniors decide “Should I abstract this?”

Ask these questions **in order**:

1. Will there be **multiple implementations**?
2. Will this logic **change independently**?
3. Will abstraction reduce **cognitive load**?
4. Is this a **core business rule** or infra detail?

If most answers are “no” → **don’t abstract**.

---

## 8️⃣ Real-life analogy (very practical)

Think of a **remote control**:

* You press “Power”
* You don’t care if TV is Sony or Samsung

Remote = abstraction
TV internals = implementation

If remote exposed:

* Voltage
* Circuit details

You’d lose your mind.

---

## 9️⃣ Common Abstraction Smells (RED FLAGS 🚩)

Avoid abstraction when you see:

* Interfaces with 1 implementation
* Interfaces named `SomethingInterface`
* Abstract classes with no shared logic
* Methods like `doSomething()`

Senior rule:

> **If you struggle to name it, abstraction is wrong.**

---

## 🔟 Interview-grade explanation (memorize this)

> “Abstraction helps manage complexity by exposing only what the caller needs, while hiding change-prone implementation details behind a stable contract.”

That’s a **principal-level answer**.

---

## 🧠 Mini Practice (think, don’t code)

### Question:

Should `Cart` know **how discounts are calculated**?

Answer:

* ❌ If discounts change often → abstract
* ✅ Cart should just say: `applyDiscount()`

Why?
Because **pricing strategies evolve**, cart ownership doesn’t.

---

## 🧠 Golden Rule (experience-based)

> **Encapsulation protects correctness.
> Abstraction protects sanity.**

---
