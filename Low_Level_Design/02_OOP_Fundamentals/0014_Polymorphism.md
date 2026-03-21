## **Polymorphism**

Most devs think:

> “Polymorphism = method overriding”

That’s… incomplete.

---

## 1️⃣ What Polymorphism REALLY means

Senior engineer definition:

> **Polymorphism lets different objects respond to the same message in their own way — without the caller knowing the difference.**

Key phrase:
👉 **“Same message, different behavior”**

Not `if/else`
Not `switch`
Not `instanceof`

---

## 2️⃣ Why seniors love polymorphism

Because it:

* Kills `if-else` chains
* Removes conditional complexity
* Makes systems **open for extension**
* Makes code **read like business language**

---

## 3️⃣ Bad code (no polymorphism)

### ❌ Conditional hell

```php
function pay(string $method, int $amount) {
    if ($method === 'RAZORPAY') {
        // razorpay logic
    } elseif ($method === 'CASH') {
        // cash logic
    } elseif ($method === 'WALLET') {
        // wallet logic
    }
}
```

Problems:

* Every new method = modify function
* Violates Open/Closed
* Hard to test
* Grows endlessly

---

## 4️⃣ Good code (polymorphism in action)

### Step 1: Define behavior contract

```php
interface PaymentMethod {
    public function pay(int $amount): bool;
}
```

### Step 2: Implement variations

```php
class RazorpayPayment implements PaymentMethod {
    public function pay(int $amount): bool {
        return true;
    }
}
```

```php
class CashPayment implements PaymentMethod {
    public function pay(int $amount): bool {
        return true;
    }
}
```

### Step 3: Use polymorphism

```php
class Order {
    public function pay(PaymentMethod $method, int $amount): void {
        if (!$method->pay($amount)) {
            throw new Exception("Payment failed");
        }
    }
}
```

Now:

* Order doesn’t care *which* payment
* Just sends the **same message**: `pay()`
* Behavior changes automatically

That’s polymorphism.

---

## 5️⃣ The mental model (used in design reviews)

Think:

> “What is the **verb** here?”

* Pay
* Notify
* Ship
* Calculate

Then let **objects decide HOW**, not the caller.

---

## 6️⃣ Polymorphism WITHOUT inheritance (important)

This is critical.

Polymorphism does **NOT** require inheritance.

### JavaScript example

```js
class EmailNotifier {
  notify(message) {}
}

class SMSNotifier {
  notify(message) {}
}

function sendNotification(notifier) {
  notifier.notify("Order placed");
}
```

No interface.
No extends.
Still polymorphism.

Senior rule:

> **If it walks like a duck and quacks like a duck, treat it like a duck.**

---

## 7️⃣ Real-world system example: Notifications

### ❌ Bad

```php
if ($type === 'EMAIL') {}
if ($type === 'SMS') {}
if ($type === 'PUSH') {}
```

### ✅ Good

```php
interface Notifier {
    public function notify(string $message): void;
}
```

Now:

* EmailNotifier
* SMSNotifier
* PushNotifier

Zero conditionals.

---

## 8️⃣ Interview trap (very common)

**Question:**

> “Difference between inheritance and polymorphism?”

❌ Bad answer:

> “Polymorphism is method overriding”

✅ Strong answer:

> “Inheritance is one way to achieve polymorphism, but polymorphism itself is about substituting objects through a common contract.”

This answer = **experience**.

---

## 9️⃣ When polymorphism is OVERKILL

Avoid polymorphism when:

* Only one behavior exists
* Logic will never vary
* Adds more files than value

Senior rule:

> **Polymorphism is earned, not assumed.**

---

## 🔟 Golden Rule (write this)

> **Replace conditionals with polymorphism only when behavior varies.**

---

## 🧠 Mini Practice

### Question:

Should `Discount` be polymorphic?

Think:

* Percentage discount
* Flat discount
* Coupon-based discount

Answer:
👉 Yes. Different rules, same action: `apply()`

---

## 🧠 Principal Engineer Take

> “Polymorphism lets me add features without touching stable code — and that’s how systems survive for years.”

---
