# 🔥 PHASE 3 — CLASS RELATIONSHIPS

# COMPLETE QUICK REVISION (Principal Engineer Version)

This is your **high-speed revision sheet** for the entire `03_Class_Relationships` module.

Do NOT memorize UML diamonds.

Your real goal is:

> Learn how two objects are connected in **responsibility, lifecycle, ownership, cardinality, and coupling** — because that is what keeps production systems consistent.

This sheet = **module notes + Principal add-ons** (concurrency, aggregates, composition root, snapshots, service boundaries).

---

# 🧠 THE BIG PICTURE

Every relationship answers ONE question:

> “How are two entities connected in terms of **who knows whom, who owns whom, and who dies with whom**?”

```text
Dependency     USES-A      temporary capability, no ownership
Association    KNOWS-A     lasting reference, no ownership
Aggregation    HAS-A       whole–part, parts live independently
Composition    OWNS-A      whole–part, parts die with whole
Realization    CAN-DO      class fulfills an interface contract
Cardinality    HOW MANY    allowed counts (often state-dependent)
Ownership      WHO RULES   lifecycle authority (not “has a field”)
```

Strength (coupling / lifecycle tightness):

```text
Dependency  <  Association  <  Aggregation  <  Composition
   weakest                                      strongest
```

Realization is **orthogonal** — it is not “stronger composition.” It is **contract vs implementation**.

---

# 🔥 THE 3 QUESTIONS (LOCK THESE)

Before you name a relationship, ask only:

```text
1. Does it just KNOW?     → Association (or Dependency if temporary)
2. Does it HAVE (weak)?   → Aggregation
3. Does it OWN (strong)?  → Composition
```

Then add:

```text
4. How many, and when?    → Cardinality (maybe 1:1 ACTIVE, 1:N history)
5. Who is allowed to make it invalid?  → Ownership / aggregate root
```

If unsure → it is **probably NOT composition**.

---

# 🔥 THE CORE TRUTH

| Junior | Principal |
| ------ | --------- |
| “A has B” | Know vs have vs own — three different systems |
| DB FK = the relationship | FK is persistence. Objects may store **IDs**, not graphs |
| Bidirectional is complete | Bidirectional is usually a **bug factory** |
| `new` inside = convenience | `new` inside = **ownership claim** |
| Interface = extra file | Realization = **stabilize what changes** |
| Check in code | Constraints at **domain + DB + distributed** layers |
| Injected ⇒ owned | **DI is access, not ownership** |

> **Most LLD failures are wrong relationship choices, not missing patterns.**

---

# 1. DEPENDENCY (USES-A)

---

# 🧠 Meaning

> One class **temporarily uses** another to do a job. No ownership. No lifecycle control. Replaceable.

Mental model: **“I need a capability, not an implementation.”**

Not “I need MySQL.” → “I need something that can persist this.”

---

# How it shows up in code

| Type | When |
| ---- | ---- |
| Method / parameter | Temporary, scoped to one call |
| Constructor injection | Required collaborator for the object’s life |
| Setter injection | Optional / late — object can exist incomplete ⚠️ |

Stored field + long life starts looking like **association**. The difference is **intent**:

* Dependency = *behavior I use* (Logger, PaymentGateway, PricingService)
* Association = *a domain thing I know* (Order knows User)

---

# ❌ Tight coupling

```php
class PaymentService {
    public function pay() {
        $gateway = new Razorpay(); // HARD DEPENDENCY
        $gateway->process();
    }
}
```

Change provider → rewrite callers. Cannot mock. Cannot test.

# ✅ Depend on abstraction + inject

```php
class PaymentService {
    public function __construct(private PaymentGateway $gateway) {}
    public function pay(): void { $this->gateway->process(); }
}
```

---

# Golden principle

> **Depend on abstractions, not concretions.** (DIP)

Database, Logger, SMTP, Stripe — **dependencies**, never composition. The service does not *own* Stripe.

---

# 🔥 PRINCIPAL ADD-ONS — DI / IoC / COMPOSITION ROOT

### Dependency vs Dependency Injection

Knowing you *use* PaymentGateway is dependency.  
If you still `new Razorpay()` in the constructor, you are **still coupled**.

> **DI = receive what you need; do not create it.**  
> **IoC = creation control lives outside the class.**  
> **DI is how you achieve IoC.**

### Composition Root

The **one place** that wires the graph (`main`, `bootstrap`, Laravel provider, Nest module).

> Classes receive. The root creates.

Scattered `new Stripe()` in controllers = no architecture.

### Injection preference

1. **Constructor** — mandatory, object always complete (default)
2. **Method** — truly temporary
3. **Setter** — optional only; risk of half-built objects

### Anti-patterns

* **Service Locator** (`Container::get('db')`) — *hidden* dependency, untestable
* **Constructor explosion** (8 collaborators) — class is doing too much; split
* **Interface for technology** (`Database`) vs **behavior** (`UserRepository`)
* **DI for value objects** — `new Money(100)` is correct; don’t inject Money
* **God composition root** — 5000 lines of bindings; split by module

### When NOT to DI

Simple scripts · value objects · no variation · cargo-cult `FooInterface` + `FooImpl`

### Maturity

Beginner uses classes → Advanced uses DI → **Principal designs dependency flow across the system.**

---

# Interview traps

**Is Database composition?** No. Independent, not owned → **dependency**.  
**Is Logger composition?** No. **Dependency.**  
**Microservices between each other?** **Dependency** (network), never composition.

---

# 2. ASSOCIATION (KNOWS-A)

---

# 🧠 Meaning

> One object **knows about** another and can use it. Independent lifecycles. No ownership.

```text
Class A can talk to Class B.
```

Customer ↔ Order in the *business* sense is associated. Customer does **not** own Order objects in memory.

---

# Direction

| | |
| --- | --- |
| **Unidirectional** | Only one side knows. Default in backends. |
| **Bidirectional** | Both know. Avoid unless you *must*. |

Bidirectional costs: circular deps, testing pain, memory, confusing graphs, ORM explosions, JSON recursion.

**PE default:** `Order → User`, not `User → all Orders`.

Why? Loading User with 5000 orders is a production incident, not a UML win.

---

# Cardinality lives on association

`1:1` User–Profile · `1:N` Customer–Orders · `N:1` Order–Customer · `N:M` Student–Course (needs **join entity**)

---

# God-object smell

Order knowing User + Product + Inventory + Payment + Notification + Shipping = **too many associations**.

Cut to what Order needs: User (or `userId`), OrderItems, maybe Payment. Rest = **services (dependencies)**.

---

# 🔥 PRINCIPAL ADD-ONS

### Object graph ≠ database graph

```php
// DB: orders.customer_id
// Memory: often this, not Customer object
private int $customerId; // or UserId value object
```

Service fetches Customer when needed. Prevents **N+1** (100 orders → 100 customer queries).

### Snapshot vs live reference

❌ `Order` holds `Product[]` (price changes later → historical invoices lie)  
✅ `Order ◆── OrderItem` with `productId`, `quantity`, **price snapshot**

Association to Product is **logical**. Composition of the line item is **physical**.

### Transactional hubs

Order, Invoice, Payment, Ride, Booking, Ticket — **central connectors**. Most arrows **from** the hub **out**:

```text
Order → User
Order → Restaurant
Order → DeliveryAgent
```

Not Restaurant → thousands of Orders in the object model.

### Association vs dependency (fine line)

* `Order` knows `User` → **association** (domain identity)
* `OrderService` uses `Mailer` → **dependency** (capability)

If you would never persist the link, it is probably a dependency.

### Historical integrity

Payments store `userId`, not a live User graph. User can change/delete; **the financial record must remain valid**.

---

# Mental checklist (association)

1. Do they need to know each other at all?
2. Who should know whom? (follow **usage**, not the ER diagram)
3. Bidirectional necessary?
4. Multiplicity?
5. Tight coupling?
6. Heavy graph?
7. **Object or ID?**

---

# Food-delivery production model (from the lectures)

```text
Order → User
Order → Restaurant
Order → DeliveryAgent
Restaurant ◆/◇ MenuItem   (often composition — item dies with restaurant)
```

Restaurant does **not** own Swiggy drivers. Driver assigned to **Order**.

---

# Payment-system directions (information flow)

```text
Payment → User            (many : 1)   store userId
Payment → Invoice         (many : 1)   invoice 1 — * payments (partials)
Payment → PaymentMethod   (many : 1)   entity if saved card; else enum/VO
Refund  → Payment         (many : 1)   keeps Payment immutable
```

Direction follows **who needs the fact**. Reverse collections explode graphs.

---

# 3. AGGREGATION (HAS-A, WEAK)

---

# 🧠 Meaning

> Whole **contains** parts, but **does not own** their lifecycle. Parts survive the whole. Parts may be **shared**.

UML: **hollow diamond** `Team ◇── Player`

Ronaldo exists if the club is deleted. Song exists if the playlist is deleted.

---

# All of these must hold

1. Whole–part meaning (not just “uses”)
2. Part exists independently
3. Part may belong to multiple wholes
4. Whole does **not** create/destroy the part

```php
$team->addPlayer($existingPlayer); // NOT new Player() inside Team
```

If the whole `new`s the part and deletes it → you drifted to **composition**.

---

# vs Association

Aggregation **is** a special association with **whole–part language**.

Teacher → Student = association (student is not *part of* teacher).  
Department ◇── Employee = aggregation (structural grouping, independent people).

---

# Shared mutable state (PE)

One Song in 100 playlists. Mutate title → all playlists see it. Sometimes desired, often a bug. Prefer **immutable songs** / copy-on-write titles if playlists need isolation.

---

# Backend examples

Category ◇── Products · Cart ◇── Products (careful: cart *lines* are often composition) · Course ◇── Students · Project ◇── Developers

---

# Quick test

Part exist without whole? Shared? Whole doesn’t control lifecycle? → **Aggregation**

---

# 4. COMPOSITION (OWNS-A, STRONG)

---

# 🧠 Meaning

> Whole **fully owns** parts. Create together, die together, **not shared**.

UML: **filled diamond** `House ◆── Room` · `Order ◆── OrderItem`

---

# Properties

| | |
| --- | --- |
| Strong ownership | Whole owns parts |
| Lifecycle | Delete Order → delete items |
| No sharing | Item belongs to **one** Order |
| Creation | Whole usually `new`s the part |

```php
class Order {
    public function addItem(int $productId, int $qty, float $price): void {
        $this->items[] = new OrderItem($productId, $qty, $price);
    }
}
```

`new` inside is a **composition signal**.

---

# Why it matters in production

* **Integrity** — no orphan line items
* **Transactions** — `orders` + `order_items` in one commit
* **Rules** — total = sum(items) only makes sense if items belong strictly to the order

Do **not** expose `$order->items = ...` — encapsulation + ownership together.

---

# Interview trap

`Order → OrderItem` is **composition**, not association.  
`Car → Engine` typical composition (not shared in the model).  
`BlogPost → Comments` → **ask**: delete post → delete comments? Simple blog = composition. Reddit-like independent threads = aggregation. **Context decides.**

---

# Golden rule

> If you are unsure, it is probably **not** composition.

Need: strong ownership + lifecycle + **no sharing**.

**Composition is rare.** Most of a real system is association + aggregation + dependency.

---

# Composition over inheritance (same module, different meaning)

Here “composition” also means the **design philosophy**: assemble behaviors (`Bird HAS-A FlyBehavior`) instead of `Penguin extends FlyingBird`.

That is **HAS-A for behavior**, often via **realization** of `FlyBehavior`. Do not confuse:

* UML composition (Order owns items)
* “Prefer composition over inheritance” (plug behaviors)

Both are “combine small parts.” Different diagrams.

---

# Ride-sharing (lecture-corrected)

```text
Ride ◇── Driver          aggregation (or association + driverId)
Ride ◇── Vehicle         aggregation
Ride  →  Rider           association
Ride ◆── RideLocation    composition (pickup/drop/route points)
Payment → Ride           association (payment service is separate)
```

❌ `Driver ◆── Rider` — they only meet through Ride.  
❌ `Payment ◆── Ride` — payments have refunds, disputes, own service.

---

# 5. ASSOCIATION vs AGGREGATION vs COMPOSITION (ONE TABLE)

| | Association | Aggregation | Composition |
| --- | --- | --- | --- |
| Meaning | Knows | Has (weak) | Owns (strong) |
| Lifecycle | Independent | Independent | Dependent |
| Ownership | ❌ | Weak | ✅ |
| Sharing | ✅ | ✅ | ❌ |
| Creation | External | External | Internal |
| Example | Order → User | Team ◇ Player | Order ◆ Item |

**Traps:** everything-as-association (weak domain) · everything-as-composition (rigid) · **FK ≠ composition** · bidirectional spaghetti.

**Interview sentence:**

> “I’ll decide the relationship from lifecycle and ownership: can the child exist alone, is it shared, who creates and deletes it?”

---

# 6. REALIZATION (IMPLEMENTS / CAN-DO)

---

# 🧠 Meaning

> A class **fulfills a contract**. Interface = WHAT. Class = HOW.

UML: dashed line, hollow triangle, class → interface.

| | Realization | Inheritance |
| --- | --- | --- |
| Relationship | Implements | Extends |
| Focus | Contract | Behavior reuse |
| Coupling | Loose | Tight |
| Mental model | “I **can-do** this” | “I **am** this” |

❌ `EmailNotification extends NotificationService`  
✅ `EmailNotificationChannel implements NotificationChannel`

> Use inheritance for **is-a**. Use realization for **can-do**.

---

# Combined picture

```text
NotificationService
    ↓ association / dependency
NotificationChannel  (interface)
    ↑ realization
EmailChannel / SmsChannel / PushChannel
```

Realization = what is **possible**.  
Dependency = what is **used**.  
Composition/association = how the **system is assembled**.

Without realization, composition is rigid (`new EmailChannel()` baked in).  
Without composition/DI, realization is a unused interface.

---

# Production stack (PE)

```text
Controller
  → Service
    → Strategy (interface)          realization
      → Decorator (Retry, Log, Safe)  also realization of SAME interface
        → Concrete EmailChannel
```

Same contract → stack retry + logging + failover **without changing** EmailChannel. That is Strategy + Decorator on realization.

**Factory** decides *which* realization. **DI** injects it. Together: *what to do* vs *how to create*.

**Adapter:** wrap legacy `sendEmail()` as `NotificationChannel`. Realization fits old systems into new contracts.

---

# Smells that kill realization

* `if ($channel instanceof EmailChannel)` — you just deleted polymorphism
* Fat interface (`pay, refund, invoice, email`) — ISP fail; Cash must stub lies
* `payWithRazorpayAPI()` on the interface — leaked vendor
* `UserServiceInterface` + one impl — ceremony
* Interface without DI — still `new Razorpay()` inside

---

# When to use / skip

**Use:** behavior varies, multiple impls, tests, expected change (payments, notify, pricing).  
**Skip:** one impl forever, no variation — introduce when pain appears (Rule of Three).

Stabilize **high-change** pieces (gateway). Keep **low-change** entities concrete (User).

---

# Interview answers

**Why an interface?**  
> Behavior varies; I decouple policy from providers so we can select at runtime, test with fakes, and extend without editing stable code.

**Only one impl — why interface?**  
> I wouldn’t. I’d add it when implementations diverge.

**30-second definition:**  
> Realization is class-implements-interface: contract separate from how, enabling polymorphism, DIP, and extension.

---

# 🔥 PRINCIPAL ADD-ON — domain message, not string

Weak: `notify(string $message)`  
Strong: `send(Notification $notification)` with recipient, metadata, priority.

Name the service `NotificationService`, not `PaymentService`. Composite channel for email+SMS. `SafeNotificationChannel` for catch/log/retry. **Don’t break the interface** when adding retry — decorate it.

---

# 7. CARDINALITY (HOW MANY — A CONSTRAINT)

---

# 🧠 Meaning

> Not “they are related.” **How many may exist, at the same time, in which state.**

Without it: two active carts, two payments, two drivers on one live ride. Those are **design failures**, not typos.

> Cardinality **encodes business invariants**. Don’t leave them as scattered `if`s.

| | |
| --- | --- |
| 1 : 1 | User–Profile; Order–**active** Payment |
| 1 : N | User–Orders; Payment–Attempts; Payment–Refunds |
| N : 1 | Order–User |
| N : M | User–ChatRoom → **join entity** (Membership + role, joinedAt) |

---

# Cardinality is not static

```text
Driver → Ride
  at time T, ACTIVE:     0..1
  over lifetime:         1:N
```

Model:

```text
Ride has driver + status
Constraint: UNIQUE(driver_id) WHERE status = 'ACTIVE'
```

Do **not** dump `$driver->rides = [every ride ever]` as the way you enforce “one active.”

Same idea: Order → **one successful payment**, many **attempts**. Payment history ≠ active payment.

---

# Enforce in the type, not a public array

❌ `public $payments = []`  
✅ `assignPayment()` throws if already set — **illegal state unrepresentable**

N:M without a join class = nowhere for metadata (role, enrollment date).

---

# 🔥 PRINCIPAL ADD-ONS — THREE LAYERS

Object-level `if` is **not enough** under concurrency.

Two retries both see `successfulAttempt == null` → **double charge**.

| Layer | Example |
| ----- | ------- |
| 1. Domain | `Payment::addAttempt()` — only one success |
| 2. Database | partial unique index: one SUCCESS per `payment_id` |
| 3. Distributed | idempotency key + row lock (`FOR UPDATE`) / optimistic version |

**Interview:** “What if two requests at once?”  
❌ “We check in code.”  
✅ “Domain + unique constraint + idempotency/locking.”

### Strong vs weak cardinality

* **Strong** (money, active ride, unique seat) — all three layers  
* **Weak** (likes, notification fanout) — eventual consistency OK

### Aggregate root

`Payment` owns attempts. Nobody sets `$attempt->status = SUCCESS` from outside. **Single entry point** = constraint lives in one place.

### Optional vs mandatory

Ride → Driver is **0..1** during matching, **1** when ACTIVE. Null is a cardinality (`0..1`), not sloppiness — **name the states**.

### Price as state-dependent cardinality (ride surge)

Before assign: many estimates (mutable). After assign: **exactly one** `finalPrice` (immutable). Pricing **service** calculates; Ride **locks**. Don’t put surge math inside Ride (god object).

---

# 8. OWNERSHIP RULES (ARCHITECTURE, NOT A FIELD)

---

# 🧠 Meaning

Ownership is **lifecycle authority**:

1. Who creates?
2. Who holds?
3. Who destroys?
4. Can it exist independently?
5. What happens on failure?

> Ownership is **not** “I have a property.”  
> **DI is not ownership.** Injection = access.

Signals:

```text
$this->route = new Route(...)     → strong ownership (creation)
$this->driver = $driver           → usually shared, not owned
```

| Relationship | Ownership |
| ------------ | --------- |
| Composition | Strong |
| Aggregation | Weak |
| Association | None |
| Dependency | None |

---

# Types

* **Strong** — Car ◆ Engine  
* **Weak** — Team ◇ Players  
* **None** — OrderService → PaymentGateway  
* **Transfer** — Cart items → Order item **snapshots** (atomic, then clear cart)

Transfer without cloning live Product refs = duplicate/stale/double-pay bugs.

---

# Ride ownership (lecture-grade)

| Entity | Owner | Why |
| ------ | ----- | --- |
| Route / RideLocation | Ride | derived, not reusable |
| Payment | often Ride *or* Payment service | lifecycle after complete; don’t force in constructor |
| Driver / Rider | Independent | shared |

Flow: create Ride (rider + route) → assign driver later → complete → create Payment. Constructor that demands driver+payment **violates lifecycle**.

Ownership without a **state machine** is fake: CREATED → DRIVER_ASSIGNED → IN_PROGRESS → COMPLETED → PAID. Cancelled ride must not still charge — that is ownership + state mismatch.

---

# 🔥 PRINCIPAL ADD-ONS

### Microservices: owner of **data**

| Data | Owner |
| ---- | ----- |
| Order | Order Service |
| Payment | Payment Service |
| Inventory | Inventory Service |

Order Service must **request** payment, not UPDATE payment rows. **The owner enforces invariants** (amount never negative).

### Immutability makes ownership thinkable

`$order->address->city = "Delhi"` after ship/invoice = shared mutable disaster. New address value object. Events/DTOs/Money immutable.

### C++ mental model (even in PHP)

`unique_ptr` = exclusive owner. `shared_ptr` = shared lifetime (cycles, mystery deaths). Prefer **one owner**. PHP GC hides this; **bugs remain** (two services mutating one Payment).

### Frameworks own some lifecycles

Container singleton = **container** owns the instance. You chose that lifetime; don’t also “own” it in a random service.

### Factory transfers ownership to **caller**. Observer is usually **not** owned (else leak).

### Anti-patterns

God owner (`ApplicationManager` holds users+orders+payments) · Circular ownership (Order owns Payment owns Order) · Shared mutable ownership · Passing owned internals everywhere.

### DDD

Ownership boundary ≈ **aggregate boundary**. Outside may not mutate `OrderItem` except through `Order`.

### Prefer ID across aggregates

`Order` holds `UserId`, not `User` nested graph. Clearer scaling, no serialization loops.

---

# Ownership checklist (every LLD)

Who creates / destroys · Independent? · Shared state? · Inconsistent lifecycle possible? · Exclusive or shared? · Failure path?

Junior: “classes connected.”  
Senior: “relationships affect lifecycle.”  
**Principal: “ownership boundaries define architecture.”**

---

# 9. UNIFIED DECISION TREE

```text
Is this a behavior/capability (pay, log, notify)?
  YES → Dependency (+ interface if it varies) = Realization of that capability
  NO  → domain entity link...

Do I only need identity / a lookup?
  YES → Association (prefer ID)

Is it whole–part AND independent AND shareable?
  YES → Aggregation

Must it die with parent, unshared, parent creates it?
  YES → Composition

How many, in which state, under two concurrent requests?
  → Cardinality + 3-layer enforcement

Who is allowed to make this invalid?
  → Ownership / aggregate root / service boundary
```

---

# 10. REAL SYSTEM CHEAT SHEET

### E-commerce

```text
Order ◆── OrderItems          composition + snapshots
Order  → User                 association (userId)
Cart ◇── Product              aggregation of catalog; CartItem often composition
Cart → Order                  ownership TRANSFER via snapshots
OrderService → PaymentGateway dependency + realization
```

### Ride sharing

```text
Ride ◆── Route/Locations
Ride ◇── Driver / Vehicle
Ride  → Rider
Payment → Ride                association
RideService → PricingService  dependency (price not owned by Ride)
Driver active ride            0..1 cardinality, unique + lock
```

### Payments

```text
Payment ◆── Attempts / Details snapshot
Refund → Payment
LedgerEntry owned by Ledger service (not PaymentService mutating ledger rows)
ONE successful attempt        domain + unique + idempotency
```

### Chat

```text
ChatRoom ◇── User via Membership (N:M join)
Message → Sender
Message ◆── Attachments
```

---

# 11. CODE SIGNALS (READ A CLASS IN 10 SECONDS)

| You see | Likely |
| ------- | ------ |
| `new Part()` inside Whole | Composition |
| `add(Part $p)` from outside | Aggregation |
| `private int $userId` | Association by ID |
| `function foo(Logger $l)` | Dependency |
| `implements PaymentGateway` | Realization |
| `public array $payments` | Missing cardinality |
| `Container::get()` | Hidden dependency |
| `$a instanceof Concrete` | Broken realization |
| Bidirectional fields both public | Graph / consistency bug |

---

# 🔥 60-SECOND FLASH CARD

| Topic | One-liner |
| ----- | --------- |
| Dependency | Uses capability; no ownership; inject abstraction |
| DI / IoC | Receive, don’t create; control outside the class |
| Composition root | One wiring place |
| Association | Knows; prefer unidirectional + IDs |
| Aggregation | Has; parts live and may be shared |
| Composition | Owns; parts die; not shared |
| If unsure | Not composition |
| Realization | Can-do contract; not is-a |
| instanceof | You failed realization |
| Cardinality | How many, **when**, under races |
| 3 layers | Domain + DB unique + idempotency/lock |
| Ownership | Who may keep it valid |
| DI ≠ own | Injection is access |
| `new` inside | Ownership claim |
| FK ≠ UML | Persistence ≠ object graph |
| Hub entity | Arrows out from Order/Ride/Payment |
| Snapshot | Historical truth vs live Product |
| Transfer | Cart → Order clone items atomically |

---

# 🔥 INTERVIEW ANSWER BANK

**Difference association / aggregation / composition?**  
Know vs weak has-a vs strong owns-a. Decide by independent existence, sharing, who creates/deletes.

**Why not User.orders collection?**  
Usage and graphs. Loading a user must not load 5000 orders. Query by `user_id`. Unidirectional `Order → userId`.

**Order–OrderItem?**  
Composition. Orphans forbidden. Same transaction. Order creates items.

**Why interface for payments?**  
Variation + DIP + tests + add provider without touching checkout.

**Two successful payment attempts?**  
Illegal cardinality. Enforce in aggregate, unique constraint, idempotency key.

**Does injecting Engine mean Car owns it?**  
Usually **no** — that’s shared/aggregation. `new Engine()` in Car is the ownership signal.

**Microservices ownership?**  
Each service owns its data and invariants. Don’t update another service’s tables.

---

# 🧪 SELF-CHECK (NO NOTES)

1. Strength order of the four structural relationships?
2. Three questions: know / have / own?
3. When is `new` inside a class correct vs a smell?
4. Why store `customerId` instead of `Customer`?
5. OrderItem vs Product — which relationship each?
6. Playlist–Song vs Order–OrderItem?
7. Why is Order→OrderItem an interview trap?
8. Ride–Payment — why not composition?
9. Realization vs inheritance in one sentence?
10. What does `instanceof` on a strategy do?
11. Constructor vs setter vs method injection?
12. What is a composition root? Service locator?
13. Driver–Ride cardinality **now** vs **historically**?
14. Three layers against double charge?
15. DI vs ownership?
16. Cart → Order ownership transfer — what must you clone?
17. FK in DB vs composition in objects?
18. Who owns payment status in a microservice world?

If you can answer all 18 out loud, this module is in muscle memory.

---

# 🔚 MODULE TAKEAWAY

> Class relationships are not decorations on a diagram.
> They are **decisions about lifecycle, consistency, and what is allowed to break**.

Phase 0 = judgment (simple vs extensible).  
Phase 1 = arena (what LLD is).  
Phase 2 = what an object **is**.  
Phase 3 = how objects are **wired** — know, have, own, fulfill a contract, and **how many**, under **who is responsible**.

Next: **design principles** (coupling, cohesion, LoD, YAGNI) — they are the *rules of thumb* for when these relationships went too far.
