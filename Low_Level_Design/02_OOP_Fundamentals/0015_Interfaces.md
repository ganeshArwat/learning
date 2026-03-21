## **Interfaces**

Let’s be clear from the start:

> **Interfaces are not about code.
> Interfaces are about collaboration.**

Between:

* Classes
* Teams
* Modules
* Even companies

---

## 1️⃣ What an Interface REALLY is

Textbook:

> “An interface defines method signatures.”

Senior engineer translation:

> **An interface is a promise.**

It says:

* “If you give me this behavior, I don’t care how you implement it.”

It is a **contract of trust**.

---

## 2️⃣ Why Interfaces exist (real-world reason)

Imagine you’re building a large e-commerce system.

You and I are working on different parts:

* You build `Order`
* I build `Payment`

How do we work independently?

👉 We agree on an interface.

```php
interface PaymentGateway {
    public function charge(int $amount): bool;
}
```

Now:

* I can build Razorpay
* You can build Stripe
* Order doesn’t break

That’s team-level abstraction.

---

## 3️⃣ Without interfaces (real production problem)

### ❌ Tight coupling

```php
class Order {
    private RazorpayGateway $gateway;
}
```

Now:

* Order depends on concrete class
* Testing becomes painful
* Switching providers = nightmare

---

## 4️⃣ With interface (loose coupling)

```php
class Order {
    private PaymentGateway $gateway;

    public function __construct(PaymentGateway $gateway) {
        $this->gateway = $gateway;
    }
}
```

Now:

* Order depends on **behavior**
* Not implementation
* Easy to test
* Easy to replace

This is Dependency Inversion in action (we’ll deep dive later).

---

## 5️⃣ When to use an Interface (senior checklist)

Ask:

1. Will there be multiple implementations?
2. Do I want to isolate change?
3. Is this a boundary between modules?
4. Will I mock this in tests?

If 2+ answers are “yes” → interface likely makes sense.

---

## 6️⃣ When NOT to use an Interface

Very important.

Avoid interfaces when:

* There will always be one implementation
* The behavior is tightly bound to one class
* You’re abstracting “just in case”

### 🚩 Smell:

```php
UserInterface
ProductInterface
CartInterface
```

If they only have one implementation, it’s ceremony.

Senior rule:

> Don’t create interfaces for entities.
> Create interfaces for behaviors.

---

## 7️⃣ Interface vs Abstract Class

This is a favorite interview question.

| Interface          | Abstract Class         |
| ------------------ | ---------------------- |
| Contract only      | Contract + shared code |
| Multiple allowed   | Single inheritance     |
| Behavior agreement | Partial implementation |
| Defines capability | Defines base structure |

### When to use interface:

* Payment method
* Logger
* Notifier
* Strategy

### When to use abstract class:

* Framework base classes
* Template Method pattern
* Shared algorithm skeleton

---

## 8️⃣ JavaScript Interfaces (JS reality)

JavaScript has no native interface keyword.

But polymorphism still works:

```js
class EmailNotifier {
  notify(msg) {}
}

class SMSNotifier {
  notify(msg) {}
}
```

JS relies on:

> “If it has the method, it works.”

That’s structural typing (duck typing).

In TypeScript, you get formal interfaces.

---

## 9️⃣ Real Production Example: Logging

### ❌ Bad

```php
class Order {
    private FileLogger $logger;
}
```

### ✅ Better

```php
interface Logger {
    public function log(string $message): void;
}
```

Now you can:

* FileLogger
* DatabaseLogger
* ElasticLogger

Zero Order changes.

That’s future-proofing.

---

## 🔟 Interface abuse warning ⚠️

If your project has:

* 300 interfaces
* Each with 1 implementation
* Everything named `SomethingInterface`

You’re overengineering.

Senior rule:

> **Abstraction should reduce complexity, not multiply files.**

---

## 🧠 Mini Practice

Question:

Should `Cart` implement `CartInterface`?

Probably NO.

Should `DiscountStrategy` have an interface?

Yes.

Why?

Because:

* Cart is an entity
* Discount behavior varies

---

## 🧠 Interview-grade explanation

If interviewer asks:

> “Why use interfaces?”

Strong answer:

> “Interfaces allow decoupling high-level business logic from low-level implementations, enabling easier testing, extensibility, and parallel development.”

That’s senior maturity.

---

## 🧠 Principal Engineer Take

> “Interfaces are boundaries.
> Boundaries are what keep large systems from collapsing.”

---
