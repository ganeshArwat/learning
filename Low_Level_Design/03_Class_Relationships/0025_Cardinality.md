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

- My Sample Answer

```php
class Payment{
    public $id;
    public $user_id;
    public $payment_method_id;
    public $amount;
    public $status;
    public $created_at;
    public $updated_at;

    public function makePayment($id, $user_id, $payment_method_id, $amount, $status, $created_at, $updated_at) {
        if ($amount > 0) {
            $this->amount = $amount;
            $this->status = $status;
            $this->created_at = $created_at;
            $this->updated_at = $updated_at;
        } else {
            throw new Exception("Amount must be greater than 0");
        }
        if($this->id > 0) {
            throw new Exception("Payment already exists");
        }
        return new Payment($id, $user_id, $payment_method_id, $amount, $status, $created_at, $updated_at);
    }

}

class PaymentAttempt {
    public $id;
    public $user_id;
    public $payment_id;
    public $payment_method_id;
    public $amount;
    public $status;
    public $created_at;
    public $updated_at;  

    public function makePaymentAttempt($id, $user_id, $payment_id, $payment_method_id, $amount, $status, $created_at, $updated_at) {
        if ($amount > 0) {
            $this->amount = $amount;
            $this->status = $status;
            $this->created_at = $created_at;
            $this->updated_at = $updated_at;
        } else {
            throw new Exception("Amount must be greater than 0");
        }
    }        
}
```
Good — you’ve started modeling entities, but right now this is still **CRUD-style thinking**, not **cardinality-driven design**.

I’m going to review this like I would in a real system design review.

---

# 🔍 First — What you did right

* You identified:

  * `Payment`
  * `PaymentAttempt`
* You separated attempts from payment → **this is correct direction**
* You added validation (`amount > 0`) → good instinct

But…

---

# ❌ Critical Design Issues (Principal-level review)

I’ll be blunt — because this is where engineers level up.

---

## ❌ 1. You are not modeling cardinality at all

Right now:

```php
public $payment_id;
```

This is **database thinking**, not **object relationship modeling**.

👉 You are saying:

> “There is a relation”

But NOT:

> “How many are allowed?”

---

### What’s missing?

From the problem:

> A Payment can have multiple attempts
> A Payment should have only ONE successful attempt

Your code:

* Does NOT enforce:

  * multiple attempts → ❌
  * single success → ❌

---

## ❌ 2. No ownership or relationship direction

Ask yourself:

> Who owns PaymentAttempt?

Right now:

* Payment doesn’t know attempts exist
* Attempts just store `payment_id`

👉 This is **weak modeling**

---

### Real design expectation:

```text
Payment → PaymentAttempts (1:N)
```

---

## ❌ 3. You are leaking persistence logic into domain

```php
public $user_id;
public $payment_method_id;
```

This is DB schema thinking.

👉 In LLD:

```php
User $user;
PaymentMethod $paymentMethod;
```

---

### Why this matters

* You lose:

  * encapsulation
  * navigation
  * behavior

---

## ❌ 4. Factory method is broken

```php
return new Payment(...)
```

But:

* No constructor defined
* You’re mixing:

  * state mutation (`$this->amount = ...`)
  * object creation

👉 This is inconsistent lifecycle design

---

## ❌ 5. No enforcement of “ONLY ONE SUCCESSFUL ATTEMPT”

This is the **most important requirement**.

Right now:

👉 System allows:

* 5 successful attempts ❌
* inconsistent state ❌

---

## ❌ 6. PaymentAttempt is too “dumb”

It’s just a data holder.

👉 Missing:

* behavior
* validation rules
* lifecycle

---

# ✅ Now — Let’s Refactor Like a Principal Engineer

We redesign with **cardinality as a first-class constraint**

---

## 🎯 Step 1: Define relationships properly

```text
User → PaymentMethods (1:N)
Payment → PaymentAttempts (1:N)
Payment → SuccessfulAttempt (1:1 constraint within attempts)
Payment → Refunds (1:N)
```

---

## 🎯 Step 2: Fix Domain Model (PHP)

---

### ✅ Payment (Aggregate Root)

```php
class Payment {
    private $id;
    private $user;
    private $paymentMethod;
    private $amount;
    private $status;

    private $attempts = [];
    private $successfulAttempt = null;

    public function __construct($id, User $user, PaymentMethod $method, $amount) {
        if ($amount <= 0) {
            throw new Exception("Invalid amount");
        }

        $this->id = $id;
        $this->user = $user;
        $this->paymentMethod = $method;
        $this->amount = $amount;
        $this->status = "INITIATED";
    }

    public function addAttempt(PaymentAttempt $attempt) {
        // Enforce 1:N
        $this->attempts[] = $attempt;

        // Enforce ONLY ONE success
        if ($attempt->isSuccessful()) {
            if ($this->successfulAttempt !== null) {
                throw new Exception("Payment already has a successful attempt");
            }

            $this->successfulAttempt = $attempt;
            $this->status = "SUCCESS";
        }
    }

    public function getAttempts() {
        return $this->attempts;
    }
}
```

---

### 🔥 Key Improvements

* Payment **owns attempts**
* Enforces:

  * 1:N attempts
  * only 1 success
* Encapsulates rules

---

## ✅ PaymentAttempt

```php
class PaymentAttempt {
    private $id;
    private $payment;
    private $amount;
    private $status;

    public function __construct($id, Payment $payment, $amount, $status) {
        if ($amount <= 0) {
            throw new Exception("Invalid amount");
        }

        $this->id = $id;
        $this->payment = $payment;
        $this->amount = $amount;
        $this->status = $status;
    }

    public function isSuccessful() {
        return $this->status === "SUCCESS";
    }
}
```

---

### 🔥 Key Design Decisions

* No `payment_id` → replaced with object reference
* Behavior inside entity (`isSuccessful`)
* PaymentAttempt is NOT independent

---

# 🧠 Important Design Insight

> Payment is an **Aggregate Root**

Meaning:

* All rules must go through it
* No direct manipulation of PaymentAttempt

---

## ❌ What your design allowed

```php
$attempt1->status = "SUCCESS";
$attempt2->status = "SUCCESS";
```

👉 Broken system

---

## ✅ What correct design enforces

```php
$payment->addAttempt($attempt);
```

👉 Single entry point → controlled state

---

# 🔗 Cardinality Enforcement Layers (ADVANCED)

You should think in **3 layers**:

---

### 1. Application layer (what we did)

* `addAttempt()` logic

---

### 2. Database layer

```sql
UNIQUE(payment_id, status='SUCCESS')
```

---

### 3. Distributed systems layer

* Idempotency keys
* Retry handling

---

# ⚠️ Missing from your design (Important)

You didn’t model:

---

## ❗ User ↔ PaymentMethod (1:N)

```php
class User {
    private $paymentMethods = [];
}
```

---

## ❗ Refund (1:N from Payment)

You completely skipped it.

---

# 🧪 Final Evaluation (like interview feedback)

| Area                   | Verdict      |
| ---------------------- | ------------ |
| Entity identification  | ✅ Good start |
| Cardinality modeling   | ❌ Weak       |
| Constraint enforcement | ❌ Missing    |
| OOP modeling           | ❌ DB-driven  |
| Design maturity        | ⚠️ Mid-level |

---

Now we move from “clean OOP design” → **real-world system design pressure**.

This is where most engineers break.

---

# 🔥 Cardinality in Distributed Systems (Where Theory Fails)

So far, we enforced:

> Payment → Attempts (1:N)
> Payment → ONLY ONE successful attempt

Inside a single process, this is easy.

---

## 💣 Problem: In production, multiple services act at the same time

### Scenario

Two payment retries happen simultaneously:

```text
Request A → SUCCESS
Request B → SUCCESS
```

Both hit:

```php
$payment->addAttempt($attempt);
```

---

### ❌ What your current design does

* Both see `successfulAttempt == null`
* Both set success
* You now have **2 successful attempts**

👉 **Cardinality broken**

---

## 🧠 Key Insight

> In distributed systems, **object-level constraints are NOT enough**

---

# 🔒 Multi-Layer Cardinality Enforcement (Critical)

You must enforce cardinality at **3 levels simultaneously**

---

## 1️⃣ Application Layer (what we wrote)

```php
if ($this->successfulAttempt !== null) {
    throw new Exception("Already successful");
}
```

✅ Good
❌ Not sufficient

---

## 2️⃣ Database Layer (Hard Constraint)

You MUST enforce:

```sql
UNIQUE(payment_id, status = 'SUCCESS')
```

---

### Why?

* DB is the **source of truth**
* Prevents race condition corruption

---

## 3️⃣ Concurrency Control Layer

You need one of:

---

### Option A: Pessimistic Lock

```sql
SELECT * FROM payments WHERE id = ? FOR UPDATE;
```

* Locks row
* Only one request proceeds

---

### Option B: Optimistic Lock

```text
version = 1 → update → version = 2
```

If version mismatch → retry

---

### Option C: Idempotency Key (VERY IMPORTANT in payments)

```text
Request-ID: txn_123
```

* Same request → same result
* Prevents duplicate execution

---

# 🔥 Real Failure Case (Production Reality)

---

## 💳 Double Charge Bug

---

### What happened in real systems:

1. Payment API called twice (network retry)
2. Both succeed
3. Customer charged twice

---

### Root cause:

* No cardinality enforcement at system level
* Only application-level checks

---

### Fix:

* Idempotency keys
* DB unique constraint
* Payment gateway reconciliation

---

# 🔄 Time-Based Cardinality (Advanced)

---

## Driver → Ride example

---

### At time T:

```text
Driver → Ride (1:1)
```

---

### Over lifetime:

```text
Driver → Ride (1:N)
```

---

### How to model?

You don’t store:

```php
$driver->rides = [];
```

Instead:

```php
class Ride {
    private $driver;
    private $status; // ACTIVE, COMPLETED
}
```

---

### Constraint:

```text
Driver can have ONLY ONE ACTIVE ride
```

---

### Enforced via:

```sql
UNIQUE(driver_id, status = 'ACTIVE')
```

---

## 💡 Insight

> Cardinality is often **state-dependent**

---

# 🔗 Strong vs Weak Cardinality

---

## Strong Cardinality (must NEVER break)

* Payment → only one success
* Driver → only one active ride

👉 Enforce at DB + system level

---

## Weak Cardinality (can tolerate inconsistency)

* User → notifications
* Post → likes

👉 Eventually consistent is OK

---

# 🧠 Principal Engineer Thinking

---

When you see a relationship, ask:

---

### 1. Is this constraint CRITICAL?

If yes:

* Enforce at:

  * Domain
  * DB
  * Distributed layer

---

### 2. What happens if it breaks?

* Money loss?
* Data inconsistency?
* User trust impact?

---

### 3. Is this time-dependent?

* Active vs historical

---

# ⚠️ Interview Trap (Very Common)

---

## Interviewer asks:

> “Design Payment System”

Candidate says:

* Payment → Attempts (1:N)
* Only one success

---

Interviewer asks:

> “What if two requests come at the same time?”

---

### ❌ Weak answer

> “We check in code”

---

### ✅ Strong answer

> “We enforce it at 3 layers:
>
> * Domain logic
> * DB unique constraint
> * Idempotency key + locking”

---

👉 That’s Principal-level thinking

---

# 🔥 Let’s Fix Your Original Design (Production-Ready)

---

## Add Idempotency

```php
class PaymentService {
    public function processPayment($paymentId, $idempotencyKey) {
        if ($this->isDuplicate($idempotencyKey)) {
            return $this->getPreviousResult($idempotencyKey);
        }

        // process payment safely
    }
}
```

---

## Add DB Constraint (conceptual)

```sql
ALTER TABLE payment_attempts
ADD CONSTRAINT unique_success UNIQUE(payment_id, status)
WHERE status = 'SUCCESS';
```

---

## Add Locking

```php
$this->lockPayment($paymentId);
```

---

# 🧪 Final Challenge (Principal-Level)

---

## Design this scenario:

---

### 🚨 Problem

You are building **Ride Sharing System**

---

### Requirements:

1. Driver can have many rides over time
2. Driver can have only ONE ACTIVE ride
3. Ride must have exactly ONE driver
4. Ride can exist without driver initially (matching phase)

---

### Your task:

1. Define classes
2. Define cardinality
3. Identify:

   * Mandatory vs optional
4. Enforce:

   * ONLY ONE ACTIVE ride per driver
5. Handle:

   * Race condition when assigning driver

---

- MY ANSWER

```php

Class Driver {
    public $id;
    public $name;
    public $activeRide;
    public $rides;
    public function __construct($id, $name)
    {
        $this->id = $id;
        $this->name = $name;
        $this->activeRide = null;
        $this->rides = [];
    }
}

Class Ride {
    public $id;
    public $driver;
    public $status;

    public function __construct($id, $status)
    {
        $this->id = $id;
        $this->status = $status;
        $this->driver = null;
    }
}

Class RideService{

    public function assignDriverToRide($ride, $driver){
        if($ride->driver){
            throw new Exception("Ride already has a driver");
        }
        if($driver->activeRide){
            throw new Exception("Driver already has an active ride");
        }
        $ride->driver = $driver;
        $driver->activeRide = $ride;
    }

    public function completeRide($ride){
        if($ride->status !== "completed"){
            throw new Exception("Ride is not completed");
        }
        $ride->driver->activeRide = null;
        $ride->status = "completed";
        $ride->driver->rides[] = $ride;
    }

}
```
---

Good — this is a solid attempt. You’re now **thinking in relationships**, not just tables.

But I’m going to review this like a **Principal Engineer in a design review**, so expect precision.

---

# 🔍 High-Level Evaluation

| Area                   | Verdict             |
| ---------------------- | ------------------- |
| Entity modeling        | ✅ Good              |
| Cardinality awareness  | ✅ Partially correct |
| Constraint enforcement | ⚠️ Incomplete       |
| Encapsulation          | ❌ Weak              |
| Distributed safety     | ❌ Missing           |

You’re moving in the right direction — but this still won’t survive production.

---

# ❌ Critical Issues (Deep Review)

---

## ❌ 1. You violated your own requirement

### Requirement:

> Ride can exist without driver initially

But:

```php
public function assignDriverToRide($ride, $driver){
    if($ride->driver){
        throw new Exception("Ride already has a driver");
    }
```

This part is fine.

But you didn’t explicitly model:

```text
Ride → Driver (0..1)
```

👉 You’re relying on `null`, not **explicit cardinality thinking**

---

## ❌ 2. You are exposing internal state directly

```php
public $activeRide;
public $rides;
```

👉 This is dangerous.

---

### Why this breaks systems

Anyone can do:

```php
$driver->activeRide = $ride1;
$driver->activeRide = $ride2; // silently overrides
```

👉 Your constraint is gone.

---

### 💣 Production impact

* Multiple active rides
* Inconsistent system state
* Hard-to-debug bugs

---

## ❌ 3. Bidirectional relationship is inconsistent

You set:

```php
$ride->driver = $driver;
$driver->activeRide = $ride;
```

But nothing ensures consistency later.

---

### Example bug:

```php
$ride->driver = null;
```

👉 Driver still thinks it has an active ride

---

## ❌ 4. No enforcement of "ONLY ONE ACTIVE RIDE" at system level

Your check:

```php
if($driver->activeRide){
```

👉 Works only in single-threaded environment

---

### ❌ Race condition:

Two requests:

```text
Request A → assign ride1
Request B → assign ride2
```

Both pass check → both assign

👉 Driver now has 2 active rides

---

## ❌ 5. Status logic is broken

```php
if($ride->status !== "completed"){
    throw new Exception("Ride is not completed");
}
```

This makes no sense.

👉 You’re saying:

> “If not completed → throw”

But then you set:

```php
$ride->status = "completed";
```

---

### This is logically inconsistent

---

## ❌ 6. Ride lifecycle is not controlled

Anyone can do:

```php
$ride->status = "ACTIVE";
```

👉 No validation

---

# ✅ Now — Let’s Refactor Like a Principal Engineer

---

# 🎯 Step 1: Make state private (encapsulation first)

---

### ✅ Driver

```php
class Driver {
    private $id;
    private $name;
    private $activeRide = null;
    private $rideHistory = [];

    public function __construct($id, $name) {
        $this->id = $id;
        $this->name = $name;
    }

    public function assignRide(Ride $ride) {
        if ($this->activeRide !== null) {
            throw new Exception("Driver already has an active ride");
        }
        $this->activeRide = $ride;
    }

    public function completeRide() {
        if ($this->activeRide === null) {
            throw new Exception("No active ride");
        }

        $this->rideHistory[] = $this->activeRide;
        $this->activeRide = null;
    }

    public function hasActiveRide() {
        return $this->activeRide !== null;
    }
}
```

---

# 🎯 Step 2: Control Ride lifecycle

---

### ✅ Ride

```php
class Ride {
    private $id;
    private $driver = null;
    private $status;

    public function __construct($id) {
        $this->id = $id;
        $this->status = "REQUESTED";
    }

    public function assignDriver(Driver $driver) {
        if ($this->driver !== null) {
            throw new Exception("Ride already has a driver");
        }

        $this->driver = $driver;
        $this->status = "ACTIVE";
    }

    public function complete() {
        if ($this->status !== "ACTIVE") {
            throw new Exception("Ride is not active");
        }

        $this->status = "COMPLETED";
    }

    public function hasDriver() {
        return $this->driver !== null;
    }
}
```

---

# 🎯 Step 3: Service coordinates (NOT owns logic)

---

### ✅ RideService

```php
class RideService {

    public function assignDriverToRide(Ride $ride, Driver $driver) {

        if ($ride->hasDriver()) {
            throw new Exception("Ride already has driver");
        }

        if ($driver->hasActiveRide()) {
            throw new Exception("Driver already busy");
        }

        // Maintain consistency
        $ride->assignDriver($driver);
        $driver->assignRide($ride);
    }

    public function completeRide(Ride $ride, Driver $driver) {

        $ride->complete();
        $driver->completeRide();
    }
}
```

---

# 🔥 What improved

---

## ✅ Cardinality is now enforced properly

| Relationship                | Enforcement          |
| --------------------------- | -------------------- |
| Driver → Active Ride (0..1) | `assignRide()`       |
| Driver → Ride History (1:N) | array but controlled |
| Ride → Driver (0..1)        | `assignDriver()`     |

---

## ✅ Encapsulation fixed

* No public mutation
* Controlled transitions

---

## ✅ Lifecycle modeled

```text
REQUESTED → ACTIVE → COMPLETED
```

---

# 🚨 Still Missing (Production-Level Thinking)

---

## 🔒 1. Race condition protection

You still need:

---

### DB Constraint

```sql
UNIQUE(driver_id, status = 'ACTIVE')
```

---

### Locking

```sql
SELECT * FROM drivers WHERE id = ? FOR UPDATE;
```

---

## 🔁 2. Idempotency

If API retries:

* Same ride assignment shouldn’t duplicate

---

## ⚠️ 3. Event-driven consistency (advanced)

In real systems:

* Driver service
* Ride service

👉 Different services → eventual consistency issues

---

# 🧠 Principal-Level Insight

---

## Your biggest improvement needed:

You are still thinking:

> “Check → then assign”

You must think:

> “System must be impossible to break — even under concurrency”

---

# 🔥 Final Feedback

---

### What you did well

* Identified key entities
* Attempted constraint checks
* Used service layer

---

### What you must improve

* Stop exposing state
* Model lifecycle explicitly
* Think in **failure scenarios**
* Design for **concurrency, not just logic**

---

# 🚀 Next Step (Advanced Challenge)

---

## Modify your design:

Add:

### 🚨 Surge pricing scenario

1. Ride price changes dynamically
2. Price locked when driver assigned
3. Cannot change after assignment

---

### Questions:

* Where will you store price?
* How will you enforce immutability after assignment?
* How does cardinality affect this?

### My Answer
```
Before Desinging I need info about When and how the price will changes for a perticular ride
```
---

Good question — this is exactly how a system designer should think:

> “Don’t answer blindly — first define **when and why state changes happen**.”

Let’s design this properly.

---

# 🔥 When does ride price change?

In a real ride-sharing system, price is **not static**.

It changes based on **system state, demand, and timing**.

---

## 🧭 Phase-based Pricing Model (Real Systems)

Think of ride lifecycle:

```text
REQUESTED → MATCHING → DRIVER_ASSIGNED → ACTIVE → COMPLETED
```

---

## 🎯 Phase 1: Before driver assignment (PRICE CAN CHANGE)

---

### When does price change?

#### 1. 📈 Surge pricing (Demand vs Supply)

* Too many users, fewer drivers
* System increases price

```text
High demand → Surge multiplier applied
```

---

#### 2. 📍 Location-based pricing

* Airport / peak zones
* Different base fare

---

#### 3. ⏱ Time-based pricing

* Peak hours (office time, rain, events)
* Night charges

---

#### 4. 🔄 Dynamic recalculation

User opens app:

```text
Price at 10:00 → ₹200  
Price at 10:02 → ₹260 (surge started)
```

👉 Price is **NOT stable yet**

---

## 🧠 Key Insight

> Before driver assignment → price is **volatile (dynamic)**

---

## 🎯 Phase 2: Driver Assigned (PRICE MUST FREEZE)

---

### Critical Business Rule:

> Once driver is assigned → price must NOT change

---

### Why?

#### ❌ If price changes after assignment:

* User sees ₹200 → charged ₹300 → trust broken
* Driver expects ₹200 → gets ₹150 → dispute

---

### ✅ Real systems do:

```text
Lock price at assignment time
```

---

## 🎯 Phase 3: After ride starts

* Price may include:

  * waiting charges
  * tolls
  * distance variation

👉 BUT base fare is already locked

---

# 🔥 Now — Design Implication (This is what I want from you)

---

## You must model TWO prices:

---

### 1. Dynamic Price (before assignment)

```php
$ride->estimatedPrice
```

* Changes frequently
* Calculated externally (pricing engine)

---

### 2. Locked Price (after assignment)

```php
$ride->finalPrice
```

* Immutable
* Set once

---

# 🧠 Cardinality + State Insight

---

This is NOT just a field change.

This is:

> **State-dependent cardinality constraint**

---

## Before assignment:

```text
Ride → Price (many recalculations)
```

---

## After assignment:

```text
Ride → Price (exactly ONE locked value)
```

---

👉 Same entity, different cardinality over time

---

# ❌ Common Wrong Design

---

```php
public $price;
```

---

### Why this fails

* Price keeps changing
* No history
* No guarantee of locking

---

# ✅ Better Design (Hint for you)

---

```php
class Ride {
    private $estimatedPrice;
    private $finalPrice;
}
```

---

And rule:

```text
IF driver assigned → set finalPrice ONCE → never change
```

---

# 🔥 Edge Cases (Real Production Thinking)

---

## Case 1: Driver cancels

* Do we unlock price again?
  👉 Depends on business

---

## Case 2: Retry matching

* Recalculate price?
  👉 Usually YES

---

## Case 3: Network delay

* Price shown ≠ price at assignment
  👉 Need timestamp/versioning

---

# 🧠 Principal-Level Thinking

---

You should now think:

---

### 1. What triggers price change?

* External system (pricing engine)
* Not Ride itself

---

### 2. When does price become immutable?

* At **driver assignment**

---

### 3. Where is rule enforced?

* Ride entity (domain)
* Not UI, not service

---

# 🚀 Now Your Turn (Answer Properly)

---

### Extend your previous design:

---

### Requirements:

1. Add:

   * `estimatedPrice`
   * `finalPrice`

2. Enforce:

   * Price can change before assignment
   * Price must lock after assignment

3. Prevent:

   * Changing price after driver assigned

4. Decide:

   * Where pricing logic lives

---

### Your answer must include:

* Updated `Ride` class
* Where price is calculated
* How immutability is enforced

---

Good — now we push this into **real system design territory**.

You asked *“when and how price changes”* — now we go one level deeper:

> **Who controls price, and how does it safely interact with Ride without breaking cardinality?**

---

# 🔥 Core Problem You Must Solve

You now have two truths:

1. Price is **dynamic before assignment**
2. Price is **immutable after assignment**

But here’s the real challenge:

> Pricing logic **does NOT belong inside Ride**

---

# ❌ Why NOT put pricing inside Ride?

If you do this:

```php
$ride->calculatePrice();
```

You are coupling:

* Ride lifecycle
* Pricing logic
* External signals (traffic, demand, surge)

👉 This becomes a **God Object**

---

# ✅ Correct Architecture (Real Systems)

---

## 🎯 Separation of Concerns

```text
Ride Service        → owns lifecycle
Pricing Service     → calculates price
Matching Service    → assigns driver
```

---

## 🔁 Flow (Production Level)

```text
User requests ride
    ↓
Pricing Service → returns estimated price
    ↓
Ride created with estimatedPrice
    ↓
Matching Service finds driver
    ↓
Ride locks price (finalPrice = estimatedPrice)
    ↓
Ride becomes ACTIVE
```

---

# 🔥 Design the Pricing System Properly

---

## 🎯 Pricing Service (External)

```php
class PricingService {

    public function calculateEstimate(Location $from, Location $to) {
        $base = 100;

        $surge = $this->getSurgeMultiplier($from);
        $distance = $this->calculateDistance($from, $to);

        return $base + ($distance * 10 * $surge);
    }

    private function getSurgeMultiplier(Location $location) {
        // external signal: demand/supply
        return rand(1, 3); // simplified
    }
}
```

---

### 🔥 Key Insight

> Pricing depends on **external system state**, not Ride state

---

# 🎯 Updated Ride Design (with Cardinality + State Control)

---

```php
class Ride {
    private $id;
    private $driver = null;
    private $status;

    private $estimatedPrice;
    private $finalPrice = null;

    public function __construct($id, $estimatedPrice) {
        $this->id = $id;
        $this->estimatedPrice = $estimatedPrice;
        $this->status = "REQUESTED";
    }

    // 🔄 Price can change BEFORE assignment
    public function updateEstimatedPrice($price) {
        if ($this->driver !== null) {
            throw new Exception("Cannot update price after driver assignment");
        }

        $this->estimatedPrice = $price;
    }

    // 🔒 Lock price ONCE
    public function assignDriver(Driver $driver) {
        if ($this->driver !== null) {
            throw new Exception("Driver already assigned");
        }

        $this->driver = $driver;
        $this->finalPrice = $this->estimatedPrice; // lock here
        $this->status = "ACTIVE";
    }

    public function getFinalPrice() {
        return $this->finalPrice;
    }
}
```

---

# 🔥 What You Just Achieved

---

## ✅ State-driven cardinality

| State     | Price Behavior           |
| --------- | ------------------------ |
| REQUESTED | estimatedPrice → mutable |
| ACTIVE    | finalPrice → immutable   |

---

## ✅ Constraint enforced at domain level

* No price change after assignment
* Exactly ONE final price

---

## ✅ Clean separation

* Ride does NOT calculate price
* PricingService does

---

# ⚠️ Real Production Problems (Where Most Fail)

---

## 💣 Problem 1: Stale price

---

### Scenario:

```text
User sees ₹200
→ waits 10 seconds
→ surge increases
→ actual price should be ₹300
```

---

### Solution:

Add **price versioning**

```php
class PriceQuote {
    public $amount;
    public $timestamp;
}
```

---

## 💣 Problem 2: Race condition at assignment

---

Two flows:

```text
Thread A → assigns driver (price = 200)
Thread B → updates price (price = 300)
```

---

👉 Which wins?

---

### ✅ Solution:

Lock order:

```text
1. Lock Ride
2. Assign driver
3. Freeze price
4. Reject further updates
```

---

# 🔒 DB-Level Protection (VERY IMPORTANT)

---

You must enforce:

```sql
CHECK (final_price IS NOT NULL ⇒ driver_id IS NOT NULL)
```

---

And:

```sql
final_price cannot be updated once set
```

---

# 🔥 Advanced Insight (Principal Level)

---

## You are not just designing objects

You are designing:

> **State machines with constraints**

---

### Ride is actually:

```text
Finite State Machine (FSM)
```

---

```text
REQUESTED → MATCHING → ACTIVE → COMPLETED
```

---

Each transition:

* changes cardinality
* changes mutability rules

---

# 🧠 Mental Model Upgrade

---

Instead of thinking:

> “Ride has price”

Think:

> “Ride transitions between states, and each state defines allowed relationships”

---

# 🔥 Final Challenge (Real Interview Level)

---

## Extend system:

---

### 🚨 Add Cancellation

---

Requirements:

1. User can cancel BEFORE driver assigned
2. Driver can cancel AFTER assignment
3. If driver cancels:

   * Ride goes back to MATCHING
   * Price may change again
4. If user cancels:

   * Ride is TERMINATED
   * No further changes allowed

---

### Your task:

1. Define:

   * New states
2. Update:

   * Ride class
3. Handle:

   * Price unlocking logic
4. Ensure:

   * Cardinality still holds

---

👉 This will test if you truly understand:

* Cardinality
* State transitions
* Real-world constraints

---

