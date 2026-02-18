## **Enums**

Let me start bluntly:

> **Enums exist to eliminate illegal states.**

That’s it.

If your system allows invalid values, your design is weak.

---

## 1️⃣ The Real Problem Enums Solve

Look at this:

```php
class Order {
    private string $status;
}
```

What values are allowed?

* "PAID"
* "paid"
* "Paid"
* "PAYD"
* "SHIPPED"
* "cancelled"

There is **no control**.

This is how production bugs happen.

---

## 2️⃣ What an Enum REALLY is

Textbook:

> “An enum is a fixed set of named constants.”

Senior engineer translation:

> **An enum restricts state to valid domain values only.**

It protects business rules at the type level.

---

## 3️⃣ PHP 8.1+ Enums (modern PHP)

```php
enum OrderStatus {
    case CREATED;
    case PAID;
    case SHIPPED;
    case CANCELLED;
}
```

Now use it:

```php
class Order {
    private OrderStatus $status;

    public function __construct() {
        $this->status = OrderStatus::CREATED;
    }
}
```

Now:

* You cannot assign invalid string
* No typos
* No inconsistent casing
* Compiler helps you

That’s design safety.

---

## 4️⃣ Why this matters in real systems

Imagine:

```php
if ($order->status === "Paid")
```

One typo:

```php
"PAID"
```

Now your payment flow breaks silently.

Enums eliminate that risk.

---

## 5️⃣ Enums + Behavior (advanced usage)

Enums can also contain logic.

```php
enum OrderStatus {
    case CREATED;
    case PAID;
    case SHIPPED;

    public function canShip(): bool {
        return $this === self::PAID;
    }
}
```

Now:

```php
if (!$order->getStatus()->canShip()) {
    throw new Exception("Cannot ship");
}
```

Now business logic is closer to the domain.

This is **domain-driven thinking**.

---

## 6️⃣ JavaScript Equivalent

JS doesn’t have true enums.

We simulate:

```js
const OrderStatus = Object.freeze({
  CREATED: "CREATED",
  PAID: "PAID",
  SHIPPED: "SHIPPED",
  CANCELLED: "CANCELLED"
});
```

Or in TypeScript:

```ts
enum OrderStatus {
  CREATED,
  PAID,
  SHIPPED,
  CANCELLED
}
```

But remember:
JS enums don’t enforce type safety like PHP 8.1 does.

---

## 7️⃣ When to Use Enums

Use enums for:

* OrderStatus
* PaymentStatus
* UserRole
* LogLevel
* NotificationType

Basically:

> Any closed set of known values.

---

## 8️⃣ When NOT to Use Enums

Avoid enums when:

* Values are dynamic
* Values come from DB and change frequently
* It’s user-generated data

Enums are for **fixed domain concepts**.

---

## 9️⃣ Common Enum Mistakes 🚩

❌ Using strings instead of enum type
❌ Comparing to raw string
❌ Using enums everywhere for no reason
❌ Not updating enum when business rules change

Senior rule:

> Enums should model domain language, not technical noise.

---

## 🔟 Real Production Design Insight

Combine:

* Encapsulation
* Enum
* Controlled state transition

```php
public function ship(): void {
    if ($this->status !== OrderStatus::PAID) {
        throw new Exception("Invalid transition");
    }

    $this->status = OrderStatus::SHIPPED;
}
```

Now:

* No invalid string
* No invalid transition
* Strong domain model

That’s mature LLD.

---

## 🧠 Interview-Grade Explanation

If interviewer asks:

> “Why use enums?”

Strong answer:

> “Enums restrict state to valid domain values, eliminating magic strings and preventing invalid states at compile-time.”

That shows **domain thinking**, not syntax knowledge.

---

## 🧠 Principal Engineer Take

> “Enums don’t add features.
> They remove bugs.”

---

