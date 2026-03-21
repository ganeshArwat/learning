## **Code Smells** (How Pros *See* Bad Design Instantly)

> Senior engineers don’t read code line by line first.
> They **scan for smells**.

If they smell something bad, they *know* the system will be painful.

---

## 1️⃣ What Is a Code Smell (REAL MEANING)

A **code smell is NOT a bug**.

> It’s a **warning sign** that the design will fail under change.

Smelly code:

* Works today
* Breaks easily tomorrow
* Makes engineers afraid to touch it

---

## 2️⃣ The 5 Most Dangerous Code Smells (Industry Reality)

We’ll go **deep** into each, with:

* How it appears
* Why it happens
* How seniors fix it
* Practice

---

# 🚨 SMELL #1: GOD CLASS (The Silent Killer)

### What it looks like

```php
class OrderManager {
    public function createOrder() {}
    public function processPayment() {}
    public function updateInventory() {}
    public function sendNotification() {}
    public function generateInvoice() {}
    public function applyDiscount() {}
}
```

### Why this happens

* “Let’s keep everything in one place”
* Deadline pressure
* No clear responsibility boundaries

### Why seniors panic

* Any change risks breaking unrelated logic
* Impossible to test properly
* Merge conflicts everywhere

---

### Senior Fix (Step-by-Step Thinking)

**Question:**

> “What is changing for different reasons?”

Split by **reason to change**:

```php
class OrderService {}
class PaymentService {}
class InventoryService {}
class NotificationService {}
class InvoiceService {}
```

💡 **Rule**

> One class = one reason to change

---

### Practice (MANDATORY)

Take a large class from your project:

1. List its responsibilities
2. Create a class per responsibility
3. Move methods, don’t rewrite logic

---

# 🚨 SMELL #2: TIGHT COUPLING (Hidden Trap)

### What it looks like

```php
class OrderService {
    public function pay() {
        $gateway = new Razorpay();
        $gateway->pay();
    }
}
```

### Why this is dangerous

* Razorpay changes → your code breaks
* Cannot switch gateway
* Cannot mock for tests

---

### Senior Fix: Depend on Abstractions

```php
interface PaymentGateway {
    public function pay(): void;
}

class RazorpayGateway implements PaymentGateway {}

class OrderService {
    private PaymentGateway $gateway;

    public function __construct(PaymentGateway $gateway) {
        $this->gateway = $gateway;
    }
}
```

💡 **Senior Rule**

> High-level code should not care *which* implementation it uses.

---

### Practice

1. Find `new` keyword inside your business logic
2. Ask: “Should this be injected?”
3. Replace concrete dependency with interface

---

# 🚨 SMELL #3: DUPLICATION (THE COST MULTIPLIER)

### What it looks like

```php
if ($user->isPremium()) {
    $discount = $amount * 0.2;
}
```

Copied in:

* Order service
* Cart service
* Invoice service

### Why juniors ignore it

> “It’s just 2 lines”

### Why seniors eliminate it

> “One bug × N places”

---

### Senior Fix

Extract **concept**, not code:

```php
class DiscountCalculator {
    public function calculate(User $user, float $amount): float {
        return $user->isPremium() ? $amount * 0.2 : 0;
    }
}
```

---

### Practice

* Search your codebase for copy-paste
* Extract shared logic into a domain class

---

# 🚨 SMELL #4: LONG METHODS (COGNITIVE OVERLOAD)

### What it looks like

```php
function placeOrder() {
    // validation (30 lines)
    // payment (40 lines)
    // inventory (20 lines)
    // notification (10 lines)
}
```

### Why it’s bad

* Hard to read
* Impossible to test pieces
* Bugs hide easily

---

### Senior Fix: Extract Intent

```php
function placeOrder() {
    $this->validateOrder();
    $this->processPayment();
    $this->updateInventory();
    $this->notifyUser();
}
```

💡 **Rule**

> A method should do ONE thing at ONE level of abstraction.

---

### Practice

* Find a method >30 lines
* Extract meaningful private methods
* Keep names expressive

---

# 🚨 SMELL #5: PRIMITIVE OBSESSION (VERY COMMON)

### What it looks like

```php
function createUser(string $email, string $phone) {}
```

### Why this hurts

* Validation logic everywhere
* Business meaning lost

---

### Senior Fix: Introduce Value Objects

```php
class Email {
    public function __construct(private string $value) {
        // validate
    }
}
```

Now:

* Validation in one place
* Stronger domain modeling

---

## 3️⃣ How Seniors Detect Smells FAST

They ask:

* Why does this class exist?
* What will change first?
* Why is this method so long?
* Why do I need to read so much to understand this?

If answers feel uncomfortable → smell detected.

---

## 4️⃣ Refactoring Strategy (REAL-WORLD)

❌ Bad approach:

> “Let’s rewrite everything”

✅ Pro approach:

1. Small refactor
2. One smell at a time
3. Tests (or manual verification)
4. Commit
5. Repeat

---

## 5️⃣ PRACTICE ASSIGNMENT (DO THIS)

### Task 1

Pick ONE file from your codebase:

* Identify **minimum 3 smells**
* Write them down

### Task 2

Fix **only ONE smell**

* Commit or save separately
* Do not refactor everything

---

## 6️⃣ Interview Gold Statements

Say things like:

* “This class has multiple reasons to change”
* “This dependency is too tightly coupled”
* “There’s duplication that will increase bug risk”

Interviewers love **smell awareness**.

---
