# 1️⃣ Association

This is the **most basic relationship in object-oriented design**.

But understanding it deeply changes how you design systems.

---

# What is Association?

Association simply means:

> **One object knows about another object and can use it.**

That’s it.

No ownership.
No lifecycle dependency.
No strong binding.

Just **awareness and usage**.

In simple words:

> **Class A can talk to Class B**

---

# Real World Example

Think about this real world relationship.

**Customer → Order**

A customer places orders.

But:

* Customer does **not own** order objects in memory
* Order can exist in database independently
* Order may exist even if the customer object is not loaded

So we say:

> Customer is **associated** with Order.

Not composed.
Not aggregated.

Just **related**.

---

# Key Properties of Association

Association has **four main characteristics**.

### 1️⃣ Objects are independent

Neither object controls lifecycle of the other.

Example:

```php
class Customer {}
class Order {}
```

Customer object can exist without order.

Order object can exist without customer instance in memory.

---

### 2️⃣ One object references another

Example:

```php
class Order
{
    private Customer $customer;

    public function __construct(Customer $customer)
    {
        $this->customer = $customer;
    }
}
```

Here:

Order **knows about** customer.

But:

Customer does not necessarily manage Order.

---

### 3️⃣ Relationship can be bidirectional or unidirectional

Two types exist.

---

## Unidirectional Association

Only **one class knows about the other**.

Example:

```php
class Order
{
    private Customer $customer;
}
```

Order knows customer.

Customer does **not know orders**.

This is very common in backend systems.

---

## Bidirectional Association

Both objects know each other.

Example:

```php
class Customer
{
    private array $orders = [];

    public function addOrder(Order $order)
    {
        $this->orders[] = $order;
    }
}

class Order
{
    private Customer $customer;
}
```

Now:

Customer → Orders
Order → Customer

This is **bidirectional association**.

But beware:

> Principal engineers avoid bidirectional associations unless truly needed.

Because they create:

* circular dependencies
* complex testing
* memory issues
* confusing object graphs

---

# Association Cardinality (VERY IMPORTANT)

Association always defines **how many objects can relate**.

This is called **multiplicity / cardinality**.

Four common ones exist.

---

### 1️⃣ One to One

Example:

User → Profile

```php
class User
{
    private Profile $profile;
}
```

One user has one profile.

---

### 2️⃣ One to Many

Example:

Customer → Orders

```php
class Customer
{
    private array $orders;
}
```

One customer can have many orders.

---

### 3️⃣ Many to One

Example:

Many orders belong to one customer.

```php
class Order
{
    private Customer $customer;
}
```

---

### 4️⃣ Many to Many

Example:

Students → Courses

A student can enroll in many courses.
A course can have many students.

This usually requires **a join entity**.

Example:

```
StudentCourse
```

---

# Association in Real Systems (Important)

Let's see a **real e-commerce design**.

Entities:

```
User
Cart
Product
Order
Payment
```

Relationships:

```
User  → Cart
User  → Orders
Order → Payment
Order → Products
Cart  → Products
```

All of these are **associations**.

Because:

* objects don't own each other in memory
* they are connected logically

---

# Important Rule Principal Engineers Follow

When designing associations we ask:

> **Does this object really need to know that object?**

This question prevents **tight coupling**.

Example mistake.

Bad design:

```
Order
 ├── User
 ├── Product
 ├── Inventory
 ├── Payment
 ├── Notification
 ├── Shipping
```

Now Order knows everything.

This becomes **God Object**.

A principal engineer reduces association:

```
Order
 ├── User
 ├── OrderItems
 ├── Payment
```

Everything else handled by services.

---

# Association vs Database Relationships

Many developers confuse this.

Database relation:

```
orders.customer_id
```

But in code:

You might **not store full Customer object**.

Better design sometimes:

```php
class Order
{
    private int $customerId;
}
```

Then service fetches customer.

This reduces heavy object graphs.

Principal engineers constantly think about this.

---

# Hidden Problem with Association

Too many associations create:

### Object Graph Explosion

Example:

```
Order
 ├── Customer
 │    ├── Address
 │    ├── PaymentMethods
 │    ├── Orders
 │         ├── Items
 │              ├── Products
```

Now loading one object loads **50+ objects**.

This destroys performance.

ORM frameworks like:

* Doctrine
* Hibernate
* Eloquent

suffer heavily from this.

---

# Example: Real Production Association

Let's design **Order → Product association properly**.

Bad:

```php
class Order
{
    private array $products;
}
```

Better:

```php
class Order
{
    private array $items;
}

class OrderItem
{
    private int $productId;
    private int $quantity;
    private float $price;
}
```

Why?

Because order stores **snapshot of product**.

Not product object.

This prevents data inconsistency.

This is **real production thinking**.

---

# UML Representation

Association is represented like this:

```
Customer -------- Order
```

With multiplicity:

```
Customer 1 -------- * Order
```

Meaning:

One customer can have many orders.

---

# Real Principal Engineer Mental Model

When designing association we ask:

1️⃣ Do these objects need to know each other?

2️⃣ Who should know whom?

3️⃣ Is bidirectional necessary?

4️⃣ What is multiplicity?

5️⃣ Will this create tight coupling?

6️⃣ Will this create heavy object graphs?

7️⃣ Should we store object reference or ID?

---

# Small Exercise (Do Not Skip)

Design this:

**Food Delivery System**

Entities:

```
User
Restaurant
MenuItem
Order
DeliveryAgent
```

Question:

Define associations.

Example format:

```
User → Orders (1 : many)
Order → Restaurant (many : 1)
Order → DeliveryAgent (1 : 1)
```

But go deeper:

Which relationships should **NOT be bidirectional**?

Think like a principal engineer.

---

---
My Answer:
```
User -> Order (1 : many)
Restaurant -> MenuItem (1 : many)
Restaurant -> Order (1 : many)
Restaurant -> DeliveryAgent (1 : many)
DeliveryAgent -> Order (1 : many)
```
---

# Review of Associations


# 1️⃣ User → Order (1 : many)

Correct.

One user can place many orders.

```
User 1 ------ * Order
```

But the **important design question** is:

Should this be **bidirectional**?

Meaning:

```
User -> Orders
Order -> User
```

Principal engineers usually design this as **unidirectional**.

Meaning:

```
Order → User
```

Why?

Because when we load a User object we **usually don't need all orders**.

Imagine:

User with **5000 orders**.

Loading all of them causes:

* memory overhead
* unnecessary queries
* large object graph

So better design is:

```php
class Order
{
    private int $userId;
}
```

Service layer fetches orders when required.

This is a **production-grade decision**.

---

# 2️⃣ Restaurant → MenuItem (1 : many)

Correct.

```
Restaurant 1 ----- * MenuItem
```

But here we must ask a deeper question.

Does MenuItem exist without Restaurant?

Example:

```
Pizza
Burger
Pasta
```

These items are meaningless without a restaurant.

This suggests something deeper than association.

This might actually be:

> **Composition**

Because MenuItem lifecycle depends on Restaurant.

If restaurant deletes menu → items disappear.

We will revisit this when we reach **Composition**.

For now we keep it as association.

---

# 3️⃣ Restaurant → Order (1 : many)

Conceptually correct.

But direction is **not ideal**.

Better design:

```
Order → Restaurant
```

Why?

Because when restaurant object loads, we **should not load thousands of orders**.

Orders are typically fetched through queries like:

```
SELECT * FROM orders WHERE restaurant_id = ?
```

So the object relationship should reflect **usage patterns**.

Better model:

```php
class Order
{
    private int $restaurantId;
}
```

Again:

Principal engineers avoid **large collections inside entities**.

---

# 4️⃣ Restaurant → DeliveryAgent (1 : many)

This is actually **not always true** in real systems.

In many food delivery platforms:

```
DeliveryAgent works with platform
NOT restaurant
```

Example:

Uber Eats / Swiggy / Zomato.

Relationship is actually:

```
DeliveryAgent → Order
Order → Restaurant
```

Delivery agent is assigned to order.

So the better design:

```
Order → DeliveryAgent
Order → Restaurant
```

Restaurant does not manage delivery agents.

---

# 5️⃣ DeliveryAgent → Order (1 : many)

Partially correct.

But timing matters.

During delivery:

```
DeliveryAgent 1 ---- 1 Order
```

But historically:

```
DeliveryAgent 1 ---- many Orders
```

So better representation:

```
Order → DeliveryAgent (many : 1)
```

Meaning:

Many orders over time belong to one delivery agent.

---

# The Correct Production Model

A principal engineer would likely model it like this:

```
User -----------< Order >----------- Restaurant
                     |
                     |
                     v
              DeliveryAgent

Restaurant --------< MenuItem
```

Meaning:

```
Order → User
Order → Restaurant
Order → DeliveryAgent
Restaurant → MenuItems
```

---

# Important Insight

Notice something.

Most relationships are:

```
Order → Something
```

Why?

Because **Order is the transactional entity**.

Transactional entities usually reference many other entities.

Examples:

```
Order
Invoice
Payment
Shipment
Booking
Ride
Ticket
```

These act as **central connectors in system design**.

Principal engineers identify these early.

---

# Now Let's Address The Developer Note

You quoted this line:

> Order object can exist without customer instance in memory.

This is **very important**.

It means:

Even though the database has:

```
orders.customer_id
```

In memory we do NOT need:

```php
$order->customer
```

We can just store:

```php
class Order
{
    private int $customerId;
}
```

Why?

Because loading full objects causes:

### ORM N+1 Query Problem

Example:

Load 100 orders.

Each order loads customer.

Now database performs:

```
1 query for orders
100 queries for customers
```

Total = **101 queries**

This is called **N + 1 problem**.

Principal engineers avoid this by **careful association design**.

---

# Mental Model You Should Remember

Association answers this question:

> **Which object needs to know about which other object to perform its job?**

Not:

> Which entities are related in database.

Those are **different concerns**.

---

# Small Real-World Exercise (Very Important)

Design associations for a **Payment System**.

Entities:

```
User
Payment
PaymentMethod
Invoice
Refund
```

Think like a principal engineer.

Write associations like this:

```
Payment -> User (many : 1)
Payment -> PaymentMethod (many : 1)
```

But think deeply:

* Should User know Payments?
* Should Payment know Invoice?
* Should Refund know Payment?

Do **not rush**.

---
---

My Answer:
```
Payment -> User
Payment -> PaymentMethod
Payment -> Invoice
Payment -> Refund

```

Conceptually good, but it needs **refinement, cardinality, and responsibility clarity**.

Design is never just **A → B**.
A real design always asks:

```
Direction
Multiplicity
Ownership
Lifecycle
```

Let's go deeper.

---

# 1️⃣ Payment → User

This is correct.

```
Payment → User (many : 1)
```

Meaning:

```
Many payments belong to one user.
```

Example:

```
User
 ├── Payment #1
 ├── Payment #2
 ├── Payment #3
```

But here is an **important design decision**.

Should we store a full `User` object?

Usually **no**.

Better:

```php
class Payment
{
    private int $userId;
}
```

Why?

Payments are **immutable financial records**.

If a user account changes or is deleted, the payment record **must remain valid**.

This is called **historical integrity**.

Large payment systems (Stripe, PayPal, Razorpay) almost always store **IDs rather than object graphs**.

---

# 2️⃣ Payment → PaymentMethod

Correct relationship.

```
Payment → PaymentMethod (many : 1)
```

Example:

```
UPI
Credit Card
Debit Card
Wallet
Net Banking
```

Many payments can use the same method.

Example:

```
Payment #1 → UPI
Payment #2 → UPI
Payment #3 → Credit Card
```

But there is another important modeling question:

Is `PaymentMethod`:

```
a value
or
an entity
```

Two designs exist.

### Design A (Entity)

```
PaymentMethod
 ├── id
 ├── type
 ├── details
```

Used when users **save cards**.

### Design B (Enum / Value Object)

```
enum PaymentMethod {
    UPI,
    CARD,
    NETBANKING
}
```

Principal engineers prefer **value objects when possible**.

Less complexity.

---

# 3️⃣ Payment → Invoice

This one needs clarification.

The real relationship is usually:

```
Invoice → Payment
```

Because invoice **requests money**, payment **fulfills it**.

Example:

```
Invoice $100
Payment $100
```

But real systems allow:

```
Partial payments
Multiple payments
```

Example:

```
Invoice $100
Payment $40
Payment $60
```

So the relationship is:

```
Invoice 1 -------- * Payment
```

Meaning:

```
Payment → Invoice (many : 1)
```

Your design was conceptually right, but the **business meaning matters**.

---

# 4️⃣ Payment → Refund

This one is interesting.

Real systems design it like this:

```
Refund → Payment
```

Because refund **refers to a previous payment**.

Example:

```
Payment $100
Refund $30
```

Or even:

```
Payment $100
Refund $30
Refund $20
```

So relationship becomes:

```
Payment 1 -------- * Refund
```

Meaning:

```
Refund → Payment (many : 1)
```

Not the other way around.

This keeps `Payment` immutable.

---

# The Final Production-Grade Model

A principal engineer would probably design it like this:

```
User
  |
  |
  v
Payment -----> PaymentMethod
  |
  |
  v
Invoice

Refund -----> Payment
```

Or written clearly:

```
Payment → User (many : 1)
Payment → Invoice (many : 1)
Payment → PaymentMethod (many : 1)

Refund → Payment (many : 1)
```

---

# Important Design Insight

Notice something interesting.

The **direction of association always follows information flow**.

Example:

```
Payment knows User
Refund knows Payment
Payment knows Invoice
```

But reverse is often avoided.

Why?

Because reverse relationships create **huge object graphs**.

Example bad design:

```
User
 ├── Payments
 │     ├── Refunds
 │     ├── Invoice
 │     ├── PaymentMethod
```

Now loading one user loads the entire payment history.

This is terrible for performance.

---

# A Key Principle Used By Principal Engineers

> **Entities should not know more than they need to perform their responsibility.**

This is directly connected to:

```
Low coupling
High cohesion
Law of Demeter
```

Which you will master in later phases.

---