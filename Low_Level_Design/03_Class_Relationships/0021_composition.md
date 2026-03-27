# Phase 3 — Composition (Deep Dive)

Let’s forget textbook definitions.

A principal engineer understands composition like this:

> **Composition is about ownership + lifecycle control + meaning.**

---

# Core Idea of Composition

> **A whole object owns its parts completely.**

Meaning:

```text
Whole
 └── Parts (cannot exist independently)
```

If the whole dies → parts die.

If the whole is created → parts are created.

---

# Real World Example

### House → Rooms

```text
House
 ├── Bedroom
 ├── Kitchen
 ├── Bathroom
```

Now think carefully:

* Can a “room” exist without a house? ❌
* Does house control creation of rooms? ✅
* If house is destroyed, do rooms exist? ❌

So:

```text
House ◆── Room
```

This is **composition**.

---

# Key Properties of Composition

A relationship is composition if:

### 1️⃣ Strong ownership

Whole fully owns parts.

```text
Order owns OrderItems
```

---

### 2️⃣ Lifecycle dependency

Parts cannot exist without whole.

```text
Delete Order → OrderItems must be deleted
```

---

### 3️⃣ Parts are not shared

One part belongs to only one whole.

```text
OrderItem belongs to one Order only
```

---

### 4️⃣ Whole usually creates parts

```php
class Order
{
    private array $items = [];

    public function addItem(int $productId, int $qty, float $price)
    {
        $this->items[] = new OrderItem($productId, $qty, $price);
    }
}
```

Notice:

> Order creates OrderItem → strong signal of composition

---

# Example: Order System (Real Production Thinking)

Let’s model this properly.

### Entities

```text
Order
OrderItem
```

---

### Composition Relationship

```text
Order ◆── OrderItem
```

---

### PHP Design

```php
class Order
{
    private array $items = [];

    public function addItem(int $productId, int $quantity, float $price)
    {
        $this->items[] = new OrderItem($productId, $quantity, $price);
    }
}

class OrderItem
{
    private int $productId;
    private int $quantity;
    private float $price;

    public function __construct(int $productId, int $quantity, float $price)
    {
        $this->productId = $productId;
        $this->quantity = $quantity;
        $this->price = $price;
    }
}
```

---

# Why This Matters (Real System Impact)

### Data Integrity

If OrderItem existed independently:

```text
Orphan OrderItems → inconsistent system
```

Composition prevents this.

---

### Transaction Safety

In DB:

```sql
orders
order_items
```

We ensure:

```text
Order + OrderItems → single transaction
```

---

### Business Logic

Rules like:

```text
Total price = sum(OrderItems)
```

only make sense if items belong strictly to order.

---

# Composition vs Aggregation (Clear Mental Model)

This is where most people get confused.

| Feature   | Aggregation      | Composition        |
| --------- | ---------------- | ------------------ |
| Ownership | Weak             | Strong             |
| Lifecycle | Independent      | Dependent          |
| Sharing   | Allowed          | Not allowed        |
| Creation  | External         | Internal           |
| Example   | Playlist → Songs | Order → OrderItems |

---

### Simple Trick (Use in Interviews)

Ask:

> **If I delete the parent, should child exist?**

If YES → Aggregation
If NO → Composition

---

# Real Production Examples of Composition

Now think like a system designer.

---

## 1️⃣ E-commerce

```text
Order ◆── OrderItems
Cart ◆── CartItems
```

---

## 2️⃣ Payment System

```text
Payment ◆── PaymentDetails
```

Example:

```text
UPI details / card snapshot at time of payment
```

You do NOT want:

```text
PaymentDetails reused across payments
```

---

## 3️⃣ Logging System

```text
LogEntry ◆── Metadata
```

Metadata belongs only to that log.

---

## 4️⃣ File System

```text
Folder ◆── Files
```

(Depending on design, sometimes aggregation—but often composition in in-memory FS)

---

# Composition vs Inheritance (VERY IMPORTANT)

Now we touch something critical.

Most developers overuse inheritance:

```php
class Bird {}
class Sparrow extends Bird {}
class Penguin extends Bird {}
```

Then problems start:

```text
Penguin cannot fly ❌
```

Bad abstraction.

---

### Composition Fix

Instead of:

```text
Bird IS-A FlyingAnimal ❌
```

We do:

```text
Bird HAS-A FlyingBehavior ✅
```

---

### Example

```php
interface FlyBehavior
{
    public function fly();
}

class CanFly implements FlyBehavior
{
    public function fly() {}
}

class CannotFly implements FlyBehavior
{
    public function fly() {}
}

class Bird
{
    private FlyBehavior $flyBehavior;

    public function __construct(FlyBehavior $flyBehavior)
    {
        $this->flyBehavior = $flyBehavior;
    }
}
```

Now:

```text
Sparrow → CanFly
Penguin → CannotFly
```

This is **composition over inheritance**.

---

# Why Principal Engineers Prefer Composition

Because it gives:

### ✅ Flexibility

Change behavior at runtime

---

### ✅ Low coupling

Classes are not tightly bound

---

### ✅ Testability

Mock behaviors easily

---

### ✅ Extensibility

Add features without modifying existing code

---

This directly connects to:

```text
SOLID principles (coming next phase)
```

---

# Common Mistakes Developers Make

---

### ❌ Mistake 1: Using aggregation instead of composition

```text
Order → OrderItems (aggregation)
```

Leads to:

* orphan data
* weak consistency

---

### ❌ Mistake 2: Overusing inheritance

```text
Payment → UPI → Card → Wallet
```

Becomes rigid and hard to extend.

---

### ❌ Mistake 3: Exposing internal parts

```php
$order->items = [...]
```

Breaks encapsulation.

---

# Deep Insight (Principal Engineer Thinking)

Composition is not just a relationship.

It is a **design philosophy**:

> Build systems by combining small, well-defined components.

Instead of:

```text
One big class doing everything
```

We do:

```text
Small objects collaborating
```

---

# Final Mental Model

```text
Association  → "knows about"
Aggregation  → "has-a (weak)"
Composition  → "owns-a (strong)"
```

---

# Final Exercise (Important)

Design relationships for:

### Ride Sharing System

Entities:

```text
Ride
Driver
Rider
Vehicle
RideLocation
Payment
```

Your task:

Define:

```text
Ride → ? (which are composition)
Ride → ? (which are aggregation)
Ride → ? (which are association)
```

Think deeply:

* Which objects **cannot exist without Ride**?
* Which are shared?
* Which are just referenced?

---

Your Sample Answer:

```
Ride -> Vehicle (Aggregation)
Ride -> Driver (Aggregation)


Ride -> RideLocation (Composition)
Driver -> Rider (Composition)
Payment -> Ride  (Composition)
```

Good — you’re thinking in terms of **lifecycle**, which is exactly what I want.

But now I’m going to push you harder, because this is where most developers plateau.
We’ll refine your thinking to **production-grade system design clarity**.

---

# Your Answer (Reviewed)

```
Ride -> Vehicle (Aggregation) ✅
Ride -> Driver (Aggregation) ✅

Ride -> RideLocation (Composition) ✅
Driver -> Rider (Composition) ❌
Payment -> Ride (Composition) ❌
```

Let’s break this down like a real design review.

---

# 1️⃣ Ride → Vehicle (Aggregation) ✅

Correct.

### Why?

* Vehicle exists independently of Ride
* Same vehicle serves multiple rides over time

```text
Ride ◇── Vehicle
```

Better modeled as:

```php
class Ride {
    private int $vehicleId;
}
```

We don’t load full Vehicle object inside Ride.

✔️ Good thinking.

---

# 2️⃣ Ride → Driver (Aggregation) ✅

Correct.

### Why?

* Driver exists independently
* Driver handles many rides over time

```text
Ride ◇── Driver
```

Again, in real systems:

```php
class Ride {
    private int $driverId;
}
```

✔️ This is clean.

---

# 3️⃣ Ride → RideLocation (Composition) ✅

Correct — and important.

But let’s go deeper.

What is `RideLocation`?

It could be:

```text
pickup location
drop location
route points
```

Now think:

* Does this exist without Ride? ❌
* Is it created specifically for Ride? ✅
* Is it shared? ❌

So:

```text
Ride ◆── RideLocation
```

✔️ Strong composition

---

# 4️⃣ Driver → Rider (Composition) ❌

This is **incorrect**, and very important to fix.

---

### Think:

Does a Rider belong to a Driver?

```text
NO
```

Reality:

```text
Rider requests ride
Driver gets assigned
```

They are connected only via **Ride**.

Correct model:

```text
Ride → Rider (many : 1)
Ride → Driver (many : 1)
```

There is **NO direct relationship** between Driver and Rider.

---

### Why your design is dangerous

If you write:

```text
Driver ◆── Rider
```

You are saying:

* Rider lifecycle depends on Driver ❌
* Rider belongs to Driver ❌

This is completely wrong in domain modeling.

---

# 5️⃣ Payment → Ride (Composition) ❌

This is subtle. Many developers get this wrong.

---

### Think:

Does Payment belong to Ride?

Or

Does Ride belong to Payment?

---

### Reality:

* Ride happens
* Payment is created **after ride**

So:

```text
Payment → Ride (Association)
```

NOT composition.

---

### Now deeper question:

Is it composition in reverse?

```text
Ride ◆── Payment ?
```

Even that is usually **NOT composition**.

Why?

Because:

* Payment may exist independently (refunds, disputes)
* Payment systems are often separate services
* Payment lifecycle is not strictly tied to Ride object

---

### Correct Design

```text
Payment → Ride (many : 1)
```

Association.

---

# Final Correct Model (Principal Engineer Version)

```text
Ride ◇── Driver
Ride ◇── Vehicle
Ride → Rider (association)

Ride ◆── RideLocation   (composition)

Payment → Ride (association)
```

---

# Important Insight (VERY IMPORTANT)

Notice something:

### Composition is rare

Most relationships in real systems are:

```text
Association
Aggregation
```

Composition is used only when:

```text
STRICT ownership exists
```

---

# Golden Rule (Remember Forever)

> **If you are unsure, it is probably NOT composition.**

Composition requires:

```text
Strong ownership + lifecycle dependency + no sharing
```

---

# What You Just Learned

You now understand:

### ✅ How to identify wrong composition

### ✅ Why direct relationships can be misleading

### ✅ Why domain modeling matters more than class diagrams

This is a **big jump toward senior-level thinking**.

---
