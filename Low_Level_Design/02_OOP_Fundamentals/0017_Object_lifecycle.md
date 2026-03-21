## **Object Lifecycle**

If you want to think like a senior engineer, start asking:

> **Who creates this object?
> Who owns it?
> How long should it live?
> When should it die?**

That is object lifecycle thinking.

---

# 1️⃣ What is Object Lifecycle?

At a high level, an object goes through:

1. **Creation**
2. **Initialization**
3. **Usage**
4. **Destruction (cleanup)**

But senior engineers go deeper.

Lifecycle is about:

* Memory management
* Dependency boundaries
* Responsibility ownership
* Side effects
* Resource cleanup

---

# 2️⃣ Creation – The Most Important Phase

In PHP:

```php
$order = new Order();
```

But the real question is:

> Who should create this object?

### ❌ Bad design

```php
class OrderController {
    public function create() {
        $order = new Order();
    }
}
```

Now:

* Controller tightly couples to Order
* Hard to test
* Hard to inject dependencies

---

### ✅ Better design (Dependency Injection)

```php
class OrderController {
    public function __construct(private OrderService $service) {}
}
```

Now:

* Object creation responsibility is separated
* Lifecycle is controlled outside
* Easier to mock/test

Senior principle:

> The class that uses an object should not create it.

---

# 3️⃣ Initialization – Protect Invariants

Constructor exists for one reason:

> Ensure the object starts in a valid state.

Bad example:

```php
class User {
    public string $email;
}
```

User can exist with:

* null email
* invalid email
* empty string

That’s broken lifecycle.

---

### Proper initialization

```php
class User {
    private string $email;

    public function __construct(string $email) {
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException("Invalid email");
        }

        $this->email = $email;
    }
}
```

Now:

* Object cannot exist in invalid state
* Lifecycle begins safely

Senior rule:

> Constructor should enforce invariants.

---

# 4️⃣ Usage Phase – Ownership Matters

Ask:

> Who owns this object?

Example:

* Cart owns CartItems
* Order owns OrderLines
* User owns nothing directly (maybe just identity)

Ownership determines lifecycle.

---

### Composition = lifecycle binding

```php
class Cart {
    private array $items = [];

    public function addItem(Product $product) {
        $this->items[] = $product;
    }
}
```

When Cart dies → items die.

That’s lifecycle coupling.

---

# 5️⃣ Destruction – Often Ignored

In PHP, garbage collection handles memory.

But lifecycle matters when:

* DB connections
* File handles
* External API clients
* Locks
* Caches

Example:

```php
class FileLogger {
    private $handle;

    public function __construct() {
        $this->handle = fopen("log.txt", "a");
    }

    public function __destruct() {
        fclose($this->handle);
    }
}
```

Destructor cleans up resources.

In JS (Node):

You rely more on GC + explicit cleanup.

---

# 6️⃣ Object Lifecycle in Web Applications

Important insight:

In typical PHP apps:

* Request starts
* Objects created
* Request ends
* Objects destroyed

Lifecycle = per-request.

In long-running systems (Node, workers, microservices):

* Objects may live long
* Memory leaks matter
* Improper lifecycle = performance issues

Senior engineers think differently depending on environment.

---

# 7️⃣ Singleton & Lifecycle (preview)

Singleton = object lives entire app lifetime.

That’s powerful but dangerous.

Wrong singleton:

* Hard to test
* Global state
* Hidden coupling

We’ll cover this in patterns phase.

---

# 8️⃣ Common Lifecycle Mistakes 🚩

❌ Creating objects inside loops unnecessarily
❌ Creating DB connections repeatedly
❌ Storing state in static properties
❌ Long-lived objects holding too many dependencies
❌ Not cleaning external resources

Senior rule:

> Objects should live only as long as they are useful.

---

# 9️⃣ Lifecycle + Dependency Injection (Important)

DI containers (like in frameworks):

* Manage object creation
* Manage singleton vs transient lifecycle
* Prevent duplicate instances
* Handle cleanup

Laravel / Symfony do this automatically.

You need to understand the concept even if framework hides it.

---

# 🔟 Interview-Level Explanation

If asked:

> “What is object lifecycle?”

Strong answer:

> “Object lifecycle refers to the phases an object goes through — creation, initialization, usage, and destruction — and managing it correctly ensures resource safety, valid state, and proper dependency management.”

That shows architectural awareness.

---

# 🧠 Mini Practice

Question:

Should `Cart` create its own `TaxCalculator`?

No.

Why?

Because:

* Cart shouldn’t control lifecycle of tax logic.
* That’s dependency injection responsibility.

---

# 🧠 Principal Engineer Take

> “Design is not just about structure.
> It’s about how long things live and who owns them.”

---
