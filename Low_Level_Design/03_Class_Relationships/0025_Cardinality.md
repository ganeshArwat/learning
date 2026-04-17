# 🔗 Cardinality — Think in Constraints, Not Just Relationships

## 1. Why this concept exists (deep engineering perspective)

When systems started growing beyond simple CRUD apps, teams realized something:

> “Defining relationships is not enough — we must define **how many objects can exist in that relationship**.”

### Real problem that led to Cardinality

Imagine early systems without cardinality thinking:

* A `User` could have **multiple active carts**
* An `Order` could accidentally have **multiple payments**
* A `Driver` could be assigned to **multiple rides at the same time**

These are not coding bugs — these are **design failures**.

### What goes wrong without cardinality?

#### ❌ Data corruption

* Multiple payments for one order → double charge
* Multiple active sessions → security issue

#### ❌ Business rule violations

* One seat → multiple bookings
* One driver → multiple concurrent trips

#### ❌ Race conditions in distributed systems

* Two services assume different constraints → inconsistent state

#### ❌ Complex validation logic everywhere

* Instead of designing constraints → developers add `if` conditions everywhere

---

### 💡 Key realization (Principal-level thinking)

> Cardinality is about **encoding business invariants into your design**, not leaving them to runtime checks.

---

## 2. Core Concept (deep understanding)

### What is Cardinality?

Cardinality defines:

> **How many instances of one entity can be associated with another**

---

### Types

| Type  | Meaning      |
| ----- | ------------ |
| 1 : 1 | One-to-one   |
| 1 : N | One-to-many  |
| N : 1 | Many-to-one  |
| N : M | Many-to-many |

---

### Mental Models (VERY IMPORTANT)

#### 🧠 Model 1: Ownership vs Reference

* If cardinality is **1:1**, ownership is usually strong
* If **1:N**, parent controls lifecycle
* If **N:M**, requires **mediator (join entity)**

---

#### 🧠 Model 2: Constraint First, Code Later

Before writing code, ask:

* Can this entity exist without the other?
* How many can exist at the same time?
* Is there a business rule limiting this?

---

#### 🧠 Model 3: Cardinality is a SYSTEM RULE, not just class design

It affects:

* Database schema (foreign keys, unique constraints)
* APIs
* Concurrency control
* Caching strategies

---

## 3. Real-world engineering examples

---

### 🛒 E-commerce

#### Case: User → Orders

* One user can have multiple orders → **1:N**

#### Case: Order → Payment

* Usually **1:1 (active payment)**
  But:
* Order → PaymentHistory → **1:N**

👉 Subtle difference → production impact

---

### 💳 Payment systems

#### Payment → Transaction Logs

* One payment → multiple logs → **1:N**

#### Payment → Refund

* One payment → multiple refunds → **1:N**

---

### 🚗 Ride-sharing system

#### Driver → Ride

* At a time: **1:1**
* Over time: **1:N**

👉 Cardinality can be **time-dependent**

---

### 💬 Chat system

#### User ↔ ChatRoom

* Many users in many rooms → **N:M**

👉 Requires **join entity (Membership)**

---

### 🧠 Key Insight

> Cardinality is not static — it can change based on **context, time, and business rules**

---

## 4. Code Examples (with design thinking)

---

### 🟢 PHP — 1:N (User → Orders)

```php
class User {
    private $orders = [];

    public function addOrder(Order $order) {
        $this->orders[] = $order;
    }

    public function getOrders() {
        return $this->orders;
    }
}

class Order {
    private $id;

    public function __construct($id) {
        $this->id = $id;
    }
}
```

### Design thinking

* User controls Orders → **aggregation**
* No limit enforced → business rule missing

---

### 🟢 C++ — 1:1 (Order → Payment)

```cpp
class Payment;

class Order {
private:
    Payment* payment;

public:
    void setPayment(Payment* p) {
        if (payment != nullptr) {
            throw runtime_error("Payment already exists");
        }
        payment = p;
    }
};
```

### Design thinking

* Enforcing **only one payment**
* Constraint at object level

---

### 🟢 JavaScript — N:M (User ↔ ChatRoom)

```javascript
class Membership {
    constructor(user, room) {
        this.user = user;
        this.room = room;
    }
}

class User {
    constructor(name) {
        this.name = name;
        this.memberships = [];
    }
}

class ChatRoom {
    constructor(name) {
        this.name = name;
        this.memberships = [];
    }
}
```

### Design thinking

* Explicit join entity → scalable
* Can store metadata (role, join time)

---

## 5. Bad Design vs Good Design

---

### ❌ BAD: Ignoring cardinality

```php
class Order {
    public $payments = [];
}
```

#### Why this fails

* Allows unlimited payments
* Business logic leaks everywhere
* Hard to enforce correctness

---

### ✅ GOOD: Explicit constraint

```php
class Order {
    private $payment;

    public function assignPayment(Payment $payment) {
        if ($this->payment !== null) {
            throw new Exception("Payment already assigned");
        }
        $this->payment = $payment;
    }
}
```

---

### 🔥 Production Insight

> If your class allows invalid states → your system will eventually reach them.

---

## 6. Relationship with other concepts

---

### 🔗 With OOP

* Cardinality defines **object graph structure**
* Impacts encapsulation boundaries

---

### 🔗 With SOLID

#### SRP

* Entities should manage their own constraints

#### OCP

* Cardinality changes should not break design

#### DIP

* Relationships should depend on abstractions, not counts

---

### 🔗 With Design Patterns

* **Many-to-many → Mediator / Association class**
* **1:N → Composite pattern**
* **1:1 → Decorator / Wrapper sometimes**

---

## 7. Common mistakes engineers make

---

### ❌ Mistake 1: Thinking only in database terms

> “Foreign key laga diya, done”

No.

* DB constraint ≠ System design

---

### ❌ Mistake 2: Ignoring time dimension

* Driver → Ride is not always 1:N
* It’s **1:1 at runtime**

---

### ❌ Mistake 3: Overusing arrays/lists

```php
$payments = [];
```

👉 Lazy design → no constraints

---

### ❌ Mistake 4: Not modeling N:M properly

* Direct references instead of join entity
* No place for metadata

---

## 9. Real System Case Study (Deep)

### 🛒 E-commerce Order System

---

### Entities

* User
* Order
* Payment
* OrderItem
* Product

---

### Cardinality decisions

| Relationship        | Cardinality | Why                     |
| ------------------- | ----------- | ----------------------- |
| User → Order        | 1:N         | User places many orders |
| Order → OrderItem   | 1:N         | Multiple products       |
| Order → Payment     | 1:1         | One active payment      |
| Order → Refund      | 1:N         | Partial refunds         |
| Product ↔ OrderItem | 1:N         | Product reused          |

---

### Critical decision

👉 Order → Payment is NOT array

Why?

* Prevent double payment
* Simplify reconciliation
* Avoid race conditions

---

### Production-level thinking

* Use DB constraint: UNIQUE(order_id)
* Use service-level lock
* Use idempotency keys

---

## 10. Practical Refactoring Exercise

---

### ❌ Messy Code

```php
class Ride {
    public $drivers = [];
}
```

---

### Problems

* Multiple drivers assigned
* No active ride constraint
* Impossible to scale

---

### ✅ Refactored

```php
class Ride {
    private $driver;

    public function assignDriver(Driver $driver) {
        if ($this->driver !== null) {
            throw new Exception("Driver already assigned");
        }
        $this->driver = $driver;
    }
}
```

---

### Improvement

* Encodes **1:1 constraint**
* Prevents invalid states

---

## 11. Problem for You (VERY IMPORTANT)

---

### 🔥 Design Problem

Design a **Payment Gateway System**

#### Requirements:

1. A User can have multiple PaymentMethods
2. A PaymentMethod belongs to exactly one User
3. A Payment can have multiple attempts (retry logic)
4. Each PaymentAttempt belongs to one Payment
5. A Payment should have only ONE successful attempt
6. A Refund belongs to one Payment
7. A Payment can have multiple Refunds

---

### 👉 Your Task

1. Define classes
2. Define relationships
3. Define cardinality
4. Write sample code (any language)

---
