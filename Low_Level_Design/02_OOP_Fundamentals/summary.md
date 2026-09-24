# 🔥 PHASE 2 — OOP FUNDAMENTALS

# COMPLETE QUICK REVISION (Principal Engineer Version)

This is your **high-speed revision sheet** for the entire `02_OOP_Fundamentals` module.

Do NOT memorize textbook definitions.

Your real goal is:

> Use OOP as a **risk-control system** — objects that protect rules, isolate change, and stay honest about identity, ownership, and lifetime.

This sheet = **module notes + Principal add-ons** (things production teams actually fight about, even if the lectures only hinted at them).

---

# 🧠 THE BIG PICTURE

Nine topics. One stack:

```text
Class = boundary around responsibility
   Object = runtime actor that enforces rules
      Encapsulation = nobody can put you in an invalid state
         Abstraction   = hide decisions that will change
            Inheritance  = dangerous coupling (use rarely)
            Polymorphism = same message, different behavior
            Interfaces   = contracts / team & module boundaries
               Enums        = illegal states cannot be represented
               Lifecycle    = who creates, who owns, how long it lives
               Immutability = small facts that never mutate
```

If you skip this, SOLID and patterns become copy-paste.

---

# 🔥 THE CORE TRUTH (WRITE THIS DOWN)

| Textbook | Principal Engineer |
| -------- | ------------------ |
| Class = blueprint | Class = **boundary around responsibility + invariants** |
| Object = instance | Object = **runtime actor** with identity, state, rules |
| Encapsulation = private fields | Encapsulation = **invalid state is impossible** |
| Abstraction = hide details | Abstraction = **hide change-prone decisions** |
| Inheritance = is-a / reuse | Inheritance = **permanent coupling to parent decisions** |
| Polymorphism = overriding | Polymorphism = **same message, different behavior** |
| Interface = method signatures | Interface = **a promise between collaborators** |
| Enum = named constants | Enum = **illegal values cannot exist** |
| Lifecycle = construct/destruct | Lifecycle = **creation, ownership, duration, cleanup** |
| Immutable = no setters | Immutable = **facts, not workflows** |

> **Classes protect business rules. Objects enforce them at runtime. Everything else is noise.**

---

# 0. FOUR PILLARS — ONE PICTURE (PE ADD-ON)

```text
ENCAPSULATION     hide HOW state changes     (correctness)
ABSTRACTION       hide WHAT will change      (sanity)
INHERITANCE       share IS-A structure       (coupling tax)
POLYMORPHISM      same call, many forms      (extensibility)
```

Principal order of preference:

```text
1. Encapsulate invariants first
2. Abstract only at the axis of change
3. Polymorph through interfaces / composition
4. Inherit last, and only when child can replace parent forever
```

---

# 1. CLASSES & OBJECTS

---

# 🧠 Meaning

Useless stop: “class = blueprint, object = instance.”

Useful start:

> **A class is a boundary around responsibility.**  
> **An object is a living thing with state + behavior + rules.**

If you don’t feel *responsibility* when you name a class, you are grouping functions — not doing OOP.

A class must answer **3 questions** or it should not exist:

1. What **data** does this thing own?
2. What **behavior** is it responsible for?
3. What **rules** must always be true? (invariants)

---

# ❌ Struct with a fake mustache

```php
class User {
    public $id;
    public $name;
    public $email;
}
```

Public bags of data are **not** classes.

# ✅ Ownership + rules + behavior

```php
class User {
    private int $id;
    private string $email;

    public function __construct(int $id, string $email) {
        $this->id = $id;
        $this->email = $this->normalizeEmail($email);
    }
}
```

**Rule:** if a class has only public properties → it is a **data leak**.

---

# Object ≠ DB row

An `Order` is a file on a desk: current status, rules like “cannot ship before pay.”

Business rules belong **inside objects**, not in controllers/services that poke fields.

```php
$order->pay();
$order->ship(); // throws if not PAID
```

---

# Class vs Object (interview table)

| | Class | Object |
| --- | --- | --- |
| Nature | Definition | Runtime instance |
| Exists | Compile / load time | Runtime |
| Memory | No (as an instance) | Yes |
| Job | Defines rules | Enforces rules |

**Why objects?**

> Objects encapsulate state and behavior together so business rules cannot be violated accidentally.

---

# When to create a class

Create if it has **state + rules + invariants**.

Do **not** create classes just to:

* Group functions
* Host static helpers
* Wrap one method with no identity

That’s a util, not a domain object.

---

# 🔥 PRINCIPAL ADD-ONS

### Anemic vs Rich domain

| Anemic | Rich |
| ------ | ---- |
| `Order` is getters/setters | `Order` has `pay()`, `ship()`, `cancel()` |
| All logic in services | Services orchestrate; objects protect rules |
| Easy to map to DB | Harder to violate business rules |

Services are fine for **workflows**. They should not be the only place rules live.

### Identity vs equality (Entity vs Value)

| Entity (`Order`, `User`) | Value (`Money`, `Email`, `OrderId`) |
| ------------------------ | ----------------------------------- |
| Has identity (`id`) | Equal if values equal |
| Lifecycle, mutates over time | Usually immutable |
| “This order” vs “that order” | “₹100” is “₹100” |

If two objects with the same `id` are “the same thing” → **entity**.  
If only the numbers/strings matter → **value object**.

### Tell, Don’t Ask (PE)

❌ Ask for state, decide outside:

```php
if ($order->getStatus() === 'PAID') { $order->setStatus('SHIPPED'); }
```

✅ Tell the object to do the work:

```php
$order->ship();
```

### Law of Demeter (don’t talk to strangers)

❌ `$order->getCustomer()->getAddress()->getCity()`  
✅ `$order->deliveryCity()` or pass `Address` as a value

Train wrecks = leaked encapsulation across objects.

### DTO vs Domain class

* **DTO / request object** — data across a boundary (HTTP, queue). Can be “flat.”
* **Domain class** — invariants. Never treat them as the same thing.

### Mini trade-off (from the lecture)

Should `Cart` calculate total?

* **YES** if cart owns items and pricing is stable.
* **NO** if pricing rules churn → `PricingService` / `DiscountStrategy`.

---

# ⚠️ Common mistakes

* God class (`OrderManager` creates + tax + email + DB) = procedural code in OOP clothes
* Split by **who owns the rule**: `TaxCalculator`, `NotificationService`, `Order`

---

# 2. ENCAPSULATION

---

# 🧠 Meaning

Textbook: bind data + methods, hide internals.

Principal:

> **Encapsulation is controlling damage.**  
> Outside code must not be able to put your object into an invalid state.

If it can — the design is broken.

---

# Fake vs real

### ❌ Fake (public state)

```php
$order->status = 'SHIPPED'; // no rules
```

Still “inside a class.” Still **not** encapsulation.

### ✅ Real (private + controlled paths)

```php
class Order {
    private string $status;

    public function pay(): void { /* CREATED → PAID only */ }
    public function ship(): void { /* PAID → SHIPPED only */ }
    public function getStatus(): string { return $this->status; }
}
```

---

# Visibility (with meaning)

| Keyword | Real meaning |
| ------- | ------------ |
| `public` | Anyone can touch (dangerous) |
| `private` | Only this class |
| `protected` | Subclasses (often a leak) |

**Start private. Promote only when forced.**

`protected` is not “safer public.” It is **encapsulation broken for the inheritance tree**.

---

# Encapsulation ≠ getters/setters

`setEmail()` is **public access with extra steps**.

Prefer **intent methods**: `changeEmail()`, `deposit()`, `withdraw()`.

---

# Encapsulation vs validation

| Validation | Encapsulation |
| ---------- | ------------- |
| Outside checks state | Object **prevents** invalid state |
| `if ($order->status !== 'PAID')` | `$order->ship()` |

> Validation checks. Encapsulation prevents.

---

# 🔥 PRINCIPAL ADD-ONS

### Invariants

An invariant is a rule that must **always** be true:

* Order cannot be SHIPPED if not PAID
* Balance cannot go negative
* Email must be normalized

Constructors + mutating methods must preserve invariants. Period.

### Never leak mutable internals

```php
// ❌ caller can mutate your guts
public function getItems(): array { return $this->items; }

// ✅ copy, or expose operations
public function getItems(): array { return [...$this->items]; }
public function addItem(CartItem $item): void { /* rules */ }
```

Same for objects: return copies / immutable views, not the live reference.

### Bank-account test

If this is legal, you failed:

```php
$account->balance = -100000;
```

Must be `deposit()` / `withdraw()` with rules.

### Cart test (from lecture)

Do **not** expose the items array. Own quantity, duplicates, pricing via `addItem()`, `removeItem()`, `getTotalPrice()`.

### Information hiding ≠ just `private`

Hiding a field but exposing a 20-method “god API” still leaks **decisions**. Small, intention-revealing API = real hiding.

---

# Interview line

> “Encapsulation ensures objects can never be in an invalid state by restricting direct access to internal data and forcing all mutations through well-defined behaviors.”

# Golden rule

> If outside code needs to “fix” your object, your object is badly encapsulated.

---

# 3. ABSTRACTION

---

# 🧠 Meaning

Textbook: hide implementation.

Principal:

> **Abstraction hides decisions that are likely to change.**

Unlikely to change → don’t abstract.  
Will change → a contract saves your future self.

Ask:

1. What problem am I solving?
2. What variations might exist tomorrow?
3. What should the **caller NOT care about**?

Abstraction is a **contract**, not a trick.

---

# Cargo-cult vs earned

### ❌ Too early

`OrderServiceInterface` with **one** implementation forever = extra files, zero benefit.

> Don’t abstract until you feel pain. (Pairs with Phase 0 **Rule of Three**.)

### ✅ Axis of change: payments

`Order` must not have `payWithRazorpay()`. Depend on:

```php
interface PaymentGateway {
    public function charge(int $amount): bool;
}
```

Order knows **what** (`charge`), not **how**. New gateway = new class. Open/Closed.

---

# Abstraction is NOT “interfaces only”

Can be:

* Interface
* Abstract class
* A method contract
* A simple class boundary (`TaxCalculator` so `Order` doesn’t know tax math)

**Interfaces are a tool, not the goal.**

JS: duck typing. Abstraction is **expectations**, not syntax.

---

# Should I abstract? (in order)

1. Multiple implementations?
2. Logic changes independently?
3. Reduces cognitive load?
4. Core business vs infra detail?

Mostly no → **don’t**.

---

# Smells 🚩

* Interface with 1 implementation
* Named `SomethingInterface` by ritual
* Abstract class with no shared logic
* Methods named `doSomething()`
* **If you struggle to name it, the abstraction is wrong**

---

# 🔥 PRINCIPAL ADD-ONS

### Wrong abstraction is worse than none

A leaky or premature interface forces every caller through a lie. Delete it. Concrete is honest.

### Don’t mix abstraction levels in one method

```php
function placeOrder() {
    $this->validate();           // domain
    curl_exec($ch);              // HTTP guts  ← wrong level
    $this->notify();
}
```

Orchestrate at one level; push I/O behind a port.

### Remote-control test

You press Power. You must not see voltage. If the API exposes circuits, abstraction leaked.

### Cart / discount (lecture)

Cart should **not** know how discounts are calculated if they churn. Cart says `applyDiscount()` / uses a strategy. Pricing evolves; cart ownership does not.

---

# Interview line

> “Abstraction helps manage complexity by exposing only what the caller needs, while hiding change-prone implementation details behind a stable contract.”

# Golden pair

> Encapsulation protects **correctness**. Abstraction protects **sanity**.

---

# 4. INHERITANCE

---

# 🧠 Meaning (read this twice)

> **Inheritance is the most dangerous tool in OOP.**  
> Default choice? **Absolutely not.**

Textbook: IS-A.

Principal:

> **Inheritance permanently couples child behavior to parent decisions.**

You inherit bugs, future changes, and constraints you didn’t ask for.

`PremiumUser extends User` means: *this child will obey every User rule — now and forever.* Tomorrow’s constructor/validation change hits the child **without touching its file**. That is tight coupling.

---

# Classic lie: Penguin extends Bird with `fly()`

Breaks **Liskov Substitution** (child cannot safely replace parent). Inheritance that lies is worse than duplication.

---

# Mental test — ALL must be yes

1. True **specialization**, not “I needed a method”?
2. Child can **replace parent everywhere**?
3. All parent behaviors **always valid** for child?
4. Will I still be happy when requirements change?

Any “not sure” → **do not inherit**.

---

# Payments: inheritance vs composition

Cash has no refund. Razorpay has async callbacks. Wallet has partial pay. A shared `Payment` parent **bloats or lies**.

```php
interface PaymentMethod {
    public function pay(int $amount): bool;
}
class RazorpayPayment implements PaymentMethod {}
class CashPayment implements PaymentMethod {}
```

No fragile parent. Each owns its rules.

---

# When inheritance IS good

* Parent defines **stable, invariant** behavior
* Child **adds**, never removes / never disables
* Parent is **abstract**, not a concrete “god”
* **Frameworks**: `UserController extends Controller` — framework owns parent, you own child (safe dependency direction)

---

# Interface vs abstract class (inheritance flavor)

| | Interface | Abstract class |
| --- | --- | --- |
| Multiple | ✅ | ❌ (single inheritance) |
| Share code | ❌ (mostly) | ✅ |
| Contract only | ✅ | ❌ |
| Framework base | ❌ | ✅ |

> Interfaces for **behavior**. Abstract classes for **shared implementation** (Template Method).

---

# 🔥 PRINCIPAL ADD-ONS

### Fragile base class problem (name it)

Any change to a parent can break children you never recompiled in your head. That’s why seniors fear deep trees.

### Inheritance is not reuse

Want reuse → **composition**.  
Want polymorphism → **interfaces**.  
Want pain → `extends` everywhere.

### `AdminUser extends User`? Usually NO

Admins often have different lifecycle/permissions. Prefer **roles / composition** (`User` + `Role`), not a subclass that violates user rules.

### Diamond / multiple inheritance

PHP/Java: one parent. That’s a feature. Multiple *behavior* → interfaces + composition (or traits **carefully** — traits are copy-paste with extra steps).

### Prefer composition (the actual default)

```php
class Car {
    public function __construct(private Engine $engine) {}
}
```

Has-a engine. Can swap. No “Car is-a Engine” lie.

---

# Interview line

> “Inheritance tightly couples children to parent behavior and makes change risky. Composition gives more flexibility and isolates change.”

# Golden rule

> Inheritance is for **behavior extension**, not code reuse.

> If you reach for inheritance first, you haven’t thought hard enough.

---

# 5. POLYMORPHISM

---

# 🧠 Meaning

Not “method overriding.”

> **Different objects respond to the same message in their own way — caller doesn’t know the difference.**

**Same message, different behavior.**  
Not `if/else`. Not `switch`. Not `instanceof`.

Why seniors love it: kills conditionals, Open/Closed, reads like business language.

---

# Conditional hell vs polymorphic pay

```php
// ❌ every new method edits this function
if ($method === 'RAZORPAY') {}

// ✅
class Order {
    public function pay(PaymentMethod $method, int $amount): void {
        $method->pay($amount);
    }
}
```

Mental model: find the **verb** (pay, notify, ship, calculate). Objects decide **HOW**. Caller only sends the message.

---

# Polymorphism does NOT require inheritance

JS duck typing: `notifier.notify()` works with no `extends`. PHP uses interfaces for the same idea.

> If it walks like a duck and quacks like a duck, treat it like a duck.

---

# When it’s overkill

Only one behavior, will never vary, more files than value.

> **Polymorphism is earned, not assumed.**  
> Replace conditionals with polymorphism **only when behavior varies.** (Rule of Three.)

Discounts: percentage / flat / coupon → same verb `apply()` → **yes**.

---

# 🔥 PRINCIPAL ADD-ONS

### Three meanings people mix (know the names)

| Kind | Meaning | Typical |
| ---- | ------- | ------- |
| Subtype | Child/interface stand-in | `PaymentMethod` |
| Ad-hoc | Overloading / different types | limited in PHP |
| Parametric | Generics | `Repository<T>` |

Interview “polymorphism” almost always means **subtype**.

### Runtime vs compile-time

* Overriding / interface dispatch = **runtime** (the useful one in LLD)
* Overloading = compile-time (PHP barely has it)

### `instanceof` is a smell

A big `if ($x instanceof Foo)` switch is **polymorphism you refused to do**. Fix the contract.

### Null Object

`NullNotifier` that no-ops is polymorphism that deletes null checks. Use at edges.

### Visitor / double dispatch

When *two* types vary (shape × renderer), single polymorphism isn’t enough. Rare in CRUD; know it exists. Don’t lead with it.

---

# Interview trap

❌ “Polymorphism is method overriding.”  
✅ “Inheritance is **one way** to get polymorphism. Polymorphism is substituting objects through a **common contract**.”

# Principal take

> Polymorphism lets me add features without touching stable code — that’s how systems survive for years.

---

# 6. INTERFACES

---

# 🧠 Meaning

> **Interfaces are not about code. They are about collaboration.**  
> Classes, teams, modules, even companies.

Textbook: method signatures.  
Principal: **a promise.**

“If you give me this behavior, I don’t care how you implement it.”

`Order` team and `Payment` team agree on `PaymentGateway::charge()`. Parallel work. Order doesn’t break.

---

# Tight vs loose

```php
// ❌
private RazorpayGateway $gateway;

// ✅
private PaymentGateway $gateway; // inject
```

Depend on **behavior**, not vendor. Testable. Swappable. That’s DIP in one slide.

---

# When to use (2+ yes → likely)

1. Multiple implementations?
2. Isolate change?
3. Boundary between modules?
4. Will I mock this in tests?

---

# When NOT to

Always one implementation · tightly bound to one class · “just in case.”

🚩 `UserInterface`, `ProductInterface`, `CartInterface` with one impl = ceremony.

> Don’t create interfaces for **entities**.  
> Create interfaces for **behaviors**.

`Cart` → no `CartInterface`.  
`DiscountStrategy` → yes (behavior varies).

---

# Interface vs abstract class (favorite question)

| Interface | Abstract class |
| --------- | -------------- |
| Contract only | Contract + shared code |
| Many | Single inheritance |
| Capability (`can pay`) | Base structure |
| Strategy, Logger, Notifier | Framework base, Template Method |

---

# Abuse warning

300 interfaces × 1 impl × `FooInterface` naming = over-engineering.

> Abstraction should **reduce** complexity, not multiply files.

JS: no `interface` keyword; duck typing. TypeScript: formal contracts.

---

# 🔥 PRINCIPAL ADD-ONS

### Role interfaces, not header interfaces

Header = dump every method of a class onto an interface (ISP violation).  
Role = `CanCharge`, `CanRefund` — clients depend only on what they need.

Fat `PaymentGateway` with `charge`, `refund`, `tokenize`, `subscribe` forces Cash to stub lies. Split by role.

### Program to an interface, not an implementation

Callers type-hint the contract. `new` lives at the **composition root** (container / factory), not inside domain.

### Adapters at the boundary

Your domain talks `PaymentGateway`. Stripe SDK stays in `StripePaymentAdapter`. Vendor types never leak inward.

### Naming

Prefer `PaymentGateway`, `Notifier`, `Clock` — capability names. `IPaymentGateway` / `PaymentGatewayInterface` is noise unless house style demands it.

---

# Interview line

> “Interfaces decouple high-level business logic from low-level implementations — testing, extensibility, and parallel development.”

# Principal take

> Interfaces are **boundaries**. Boundaries keep large systems from collapsing.

---

# 7. ENUMS

---

# 🧠 Meaning

> **Enums exist to eliminate illegal states.**

Textbook: named constants.  
Principal: **restrict state to valid domain values at the type level.**

Strings allow `"PAID"`, `"paid"`, `"PAYD"` — silent production bugs.

```php
enum OrderStatus { case CREATED; case PAID; case SHIPPED; case CANCELLED; }

class Order {
    private OrderStatus $status;
}
```

No invalid string. No casing bugs. Compiler helps.

---

# Enums + behavior (domain)

```php
public function canShip(): bool {
    return $this === self::PAID;
}
```

Logic next to the domain concept. Still: **Order** should own *transitions*; enum can own *questions about a value*.

Combine: encapsulation + enum + controlled transition = mature LLD.

```php
public function ship(): void {
    if ($this->status !== OrderStatus::PAID) {
        throw new Exception("Invalid transition");
    }
    $this->status = OrderStatus::SHIPPED;
}
```

---

# When to use vs not

**Use (closed sets):** OrderStatus, PaymentStatus, UserRole, LogLevel, NotificationType.

**Don’t:** dynamic DB-driven lists, user-generated tags, values that change weekly.

> Enums = **fixed domain language**, not technical noise.

---

# JS

`Object.freeze({ CREATED: "CREATED", ... })` or TS `enum`. Weaker than PHP 8.1 backed/unit enums.

---

# 🔥 PRINCIPAL ADD-ONS

### Make illegal states unrepresentable

Not just enums: `PaidOrder` vs a boolean `$isPaid` plus `$shippedAt` plus `$cancelled`. Booleans combine into nonsense. Enums / small types collapse the matrix.

### Backed enums (PHP)

`enum OrderStatus: string { case PAID = 'paid'; }` for DB/API mapping. Compare **enum to enum**, not to raw `=== 'paid'` in domain code.

### Exhaustive `match`

```php
return match ($status) {
    OrderStatus::CREATED => ...,
    OrderStatus::PAID => ...,
    // missing case = error  ← good
};
```

### When enums are not enough → State pattern

If each status has **different behavior** (allowed operations, side effects), an enum + 40 `if`s is a smell. Then each state is a type. Enum is the **closed set**; State is **behavior per set member**.

### Don’t enum technical flags

`enum TrueFalse { YES, NO }` is a boolean with extra steps.

---

# Interview line

> “Enums restrict state to valid domain values, eliminating magic strings and preventing invalid states at compile time.”

# Principal take

> Enums don’t add features. They **remove bugs**.

---

# 8. OBJECT LIFECYCLE

---

# 🧠 Meaning

Senior questions:

> Who **creates** this? Who **owns** it? How long should it **live**? When should it **die**?

Phases: **create → initialize → use → destroy/cleanup**.

Deeper: memory, dependency boundaries, ownership, side effects, resource cleanup.

---

# Creation — most important

❌ `new Order()` inside controller/domain = tight coupling, hard tests.

✅ Inject what you **use**. Composition root / container **creates**.

> **The class that uses an object should not create it.**  
> (Except value objects / true children you own.)

---

# Initialization — protect invariants

Constructor exists to **start valid**. `User` with empty email is a broken lifecycle.

> Constructor should enforce invariants.  
> Two-phase init (`new` then `init()` / `setX` required) is a smell — object exists invalid.

---

# Usage — ownership

* Cart owns CartItems  
* Order owns OrderLines  
* User often owns identity, not the whole world  

**Composition binds lifecycle:** Cart dies → items die.

---

# Destruction

PHP GC handles memory. You still care about: DB connections, files, HTTP clients, locks, caches.

`__destruct` for **resource** cleanup (fclose), **not** for business logic (“send email on destroy” is a landmine).

---

# Environment matters

| PHP request | Node / workers / daemons |
| ----------- | ------------------------ |
| Create → use → request ends → die | Objects may live for hours |
| Per-request lifecycle | Leaks and “accidental singletons” hurt |

---

# Singleton preview

Lives for app lifetime. Powerful, dangerous: global state, hard tests, hidden coupling.

---

# Lifecycle mistakes 🚩

* `new` inside hot loops
* New DB connection per call
* State in **static** properties
* Long-lived objects holding the world
* Forgetting to close external resources
* Objects living longer than they are useful

---

# DI containers

Frameworks manage: create, singleton vs transient vs scoped, duplicates, sometimes cleanup. You must still **choose** the lifetime.

---

# Lecture practice

Should `Cart` `new TaxCalculator()`? **No.** Cart shouldn’t own tax-logic lifetime. Inject it.

---

# 🔥 PRINCIPAL ADD-ONS

### DI lifetimes (name them)

| Lifetime | Lives | Use for |
| -------- | ----- | ------- |
| Transient | New every resolve | Stateless calculators, commands |
| Scoped | Once per request / unit of work | DbContext, current user |
| Singleton | Process | Config, clocks, connection pools (careful) |

Wrong lifetime = leaked state across users. That’s a **security** bug, not a style issue.

### Factory vs constructor

Constructor: “this object is valid.”  
Factory / `Order::place(...)`: “this is how the **domain** starts a workflow” (extra validation, events).  
`new` in domain for **values** you own is OK (`new Money(100)`).

### Don’t put domain in `__destruct` / shutdown functions

Unreliable in PHP-FPM / fatal errors. Cleanup I/O explicitly (`try/finally`).

### Temporal coupling

If callers must call `open()` before `read()` or the object explodes, lifecycle is leaking. Make illegal sequences unrepresentable (`OpenedFile` type) or open in constructor.

### ORM entities vs request lifecycle

An `Order` loaded from DB is **rehydrated**, not “newborn.” Invariants still apply. Don’t treat ORM models as DTOs you mutate from HTTP without going through domain methods.

---

# Interview line

> “Lifecycle is creation, initialization, usage, and destruction — done well it means valid state, owned resources, and explicit dependency management.”

# Principal take

> Design is not just structure. It’s **how long things live and who owns them**.

---

# 9. IMMUTABILITY

---

# 🧠 Meaning

> An immutable object **cannot change after creation**.  
> New value → new object.

> **Mutable state is the root of most complex bugs.**

Benefits: no accidental change, predictable, easier debug, thread-safe, less defensive code.

---

# Mutable vs immutable

```php
// mutable — who changed email? when?
$user->changeEmail($email);

// immutable
$user2 = $user1->withEmail("new@email.com"); // $user1 untouched
```

---

# Value objects = home of immutability

**Always immutable:** Money, Email, DateTime, Coordinates, OrderId, Price.

```php
$newMoney = $money->add(100); // never $money->amount += 100
```

Fintech lives on this. **Entities change; values are facts.**

---

# When NOT to freeze everything

Avoid full immutability for:

* Large aggregates with many steps
* Tight loops / alloc-sensitive code
* Complex state machines
* High-mutation workflows (`Order` CREATED → PAID → SHIPPED)

> **Small domain objects immutable. Large aggregates controlled but mutable.**

`OrderStatus` enum: immutable.  
`Order` entity: mutable **through** `pay()` / `ship()`, not through field writes.

---

# JS / React

`Object.freeze`, spread `{ ...user, email }`. React assumes immutability for change detection.

---

# Concurrency

Immutable objects don’t need locks. Huge in workers, threads, distributed copies of a value.

---

# Mistakes 🚩

* Returning internal mutable arrays
* Exposing live references
* Immutability everywhere blindly
* Confusing `readonly` property with **behavioral** immutability (object can still mutate nested arrays)

> Immutability is **behavior**, not syntax.

---

# 🔥 PRINCIPAL ADD-ONS

### `withX()` convention

`withEmail`, `withAmount` = copy-with-change. Signals “returns new instance.”

### PHP `readonly` / readonly classes (8.1/8.2)

Great for values. Not a substitute for not leaking `$this->items` as a mutable array.

### DateTimeImmutable

`DateTime` mutating in place is a classic PHP footgun. Prefer immutable time types. Same idea as Money.

### Defensive copy on the way in and out

If you store an array/object the caller still holds, they can mutate you **after** construct. Copy or freeze on ingest.

### Shared mutable state is the real enemy

One `User` instance cached as singleton, then mutated per request = cross-request bugs. Immutability **or** correct lifetime — pick at least one.

### Event / audit friendliness

Immutable values + new instances make “what changed” obvious (`$old` vs `$new`). Mutable in-place writes erase history unless you log by hand.

---

# Interview line

> “Immutability reduces side effects, increases predictability, simplifies concurrency, and makes debugging easier because state cannot change unexpectedly.”

# Principal take

> Immutability is not fancy. It **reduces the number of things that can go wrong**.

---

# 🔗 HOW THE 9 TOPICS CONNECT (ONE SYSTEM)

```text
Class/object     →  there is a place for the rule
Encapsulation    →  the rule cannot be bypassed
Enum             →  illegal values cannot be typed
Immutability     →  facts don’t drift
Lifecycle        →  valid from birth; owned resources; correct duration
Abstraction      →  hide the decision that will change
Interface        →  the promise at the boundary
Polymorphism     →  new behavior = new class, same message
Inheritance      →  last resort, true is-a only
```

Same **Order / Payment / Notify** example on purpose:

```text
Order owns status (class + encapsulation + enum + lifecycle)
pay() / ship() are intent methods (not setters)
PaymentGateway interface + Razorpay/Cash (abstraction + polymorphism)
Do NOT inherit Payment for Cash (inheritance trap)
Money / Email immutable; Order mutable via transitions
Controller does not new the gateway (lifecycle / DI)
```

That is this whole module in one design.

---

# 🔥 60-SECOND FLASH CARD

| Topic | One-liner |
| ----- | --------- |
| Class | Boundary around responsibility + invariants |
| Object | Runtime actor; not a DB row |
| Entity vs Value | Identity vs “equal by data” |
| Tell Don’t Ask | `$order->ship()` not get/set status |
| Encapsulation | Invalid state impossible |
| Setter | Usually fake encapsulation |
| Abstraction | Hide **change**, not “details for sport” |
| Rule of Three | Don’t abstract until it hurts |
| Inheritance | Couples you to parent’s future; last resort |
| LSP sniff | Penguin must not `fly()` |
| Polymorphism | Same message, different behavior |
| instanceof chains | Polymorphism you refused |
| Interface | Promise / boundary; for **behaviors** not entities |
| Role interface | Small; ISP |
| Enum | Illegal values unrepresentable |
| State pattern | When each enum case has heavy behavior |
| Lifecycle | Create / own / live / die |
| DI rule | Users shouldn’t `new` their dependencies |
| Transient/Scoped/Singleton | Pick lifetime or leak state |
| Immutability | New object, not mutation — for **values** |
| Money | Always immutable |

---

# 🔥 INTERVIEW ANSWER BANK

**Class vs object?**  
Class defines rules; object enforces them at runtime with identity and memory.

**Why encapsulate?**  
So nothing outside can create an invalid state. Mutations go through intent methods.

**Why not public setters?**  
That’s public fields with extra steps. `changeEmail()` carries rules.

**Abstraction vs encapsulation?**  
Encapsulation protects correctness of *this* object. Abstraction hides decisions that will *change* from callers.

**Why not inherit here?**  
Inheritance couples children to every future parent change. Composition + interfaces isolate change. Inheritance only if the child can replace the parent everywhere.

**Inheritance vs polymorphism?**  
Inheritance is one implementation technique. Polymorphism is substitution via a common contract.

**Why interfaces?**  
Decouple policy from mechanism; test with fakes; teams agree on a promise.

**Why enums?**  
Domain values only; no magic strings; invalid states can’t be assigned.

**Object lifecycle?**  
Who creates, who owns, how long it lives, what must be cleaned up — plus invariants from the first constructor call.

**Why immutability?**  
Predictable facts, no surprise writes, safer concurrency. Use on value objects, not necessarily on whole aggregates.

**Should Admin extend User?**  
Usually no — roles/composition. Admin lifecycle/permissions often break User rules.

---

# 🧪 SELF-CHECK (NO NOTES)

1. Three questions a class must answer?
2. Why is a public-property class not OOP?
3. Entity vs value object?
4. Tell Don’t Ask — rewrite a get/set status pair.
5. Encapsulation vs validation?
6. Why are getters+setters not encapsulation?
7. When is an interface cargo-cult?
8. Four questions before inheriting?
9. Fragile base class — in one sentence?
10. Polymorphism without inheritance — example?
11. Interface for `Cart` vs `DiscountStrategy` — which and why?
12. Role interface vs header interface?
13. Enum vs State pattern?
14. “Users shouldn’t create their dependencies” — exception?
15. Transient vs scoped vs singleton — one example each?
16. Why Money immutable but Order not fully?
17. How do you leak encapsulation with `getItems()`?
18. Penguin/Bird — which principle?

If you can answer all 18 out loud, this module is in muscle memory.

---

# 🔚 MODULE TAKEAWAY

> OOP is not “I used a class.”
> OOP is **invariants that cannot be violated**, **change that has a home**, **contracts at boundaries**, and **honest lifetimes**.

Phase 0 = judgment (simple vs extensible).  
Phase 1 = arena (what LLD is, how interviews score).  
Phase 2 = **the material of design**: objects that mean something.

Next: **class relationships** (dependency → association → aggregation → composition) — those are how these objects are **wired**, now that you know what an object is allowed to be.
