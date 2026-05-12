# DRY (Don’t Repeat Yourself)

# 1. Why DRY Exists — The Real Engineering Reason

Most developers misunderstand DRY.

They think:

> “If two lines look similar, create a helper function.”

That is not DRY.

Real DRY is:

> “Every piece of knowledge in a system must have one authoritative representation.”

This principle was born because large software systems became impossible to maintain.

---

# The Real Problem DRY Solves

Imagine a payment company.

Tax calculation logic exists in:

* Checkout service
* Invoice service
* Refund service
* Reporting service
* Mobile backend
* Admin panel

Initially everything works.

Then government changes GST rules.

Now engineering teams must update logic in 12 places.

One team forgets.

Production issues begin:

* wrong invoices
* incorrect refunds
* compliance violations
* customer support escalation
* financial reconciliation mismatch

This is not a “duplicate code” problem.

This is:

# Duplicate Knowledge

That distinction is critical.

---

# DRY is About Knowledge Duplication

Two identical-looking code blocks are NOT always duplication.

But if business rules are copied across systems:

* pricing logic
* validation rules
* authorization rules
* retry strategy
* shipping rules

then system consistency breaks.

---

# What Happens When Teams Ignore DRY

## 1. Logic Divergence

Different services behave differently.

Example:

* Mobile says shipping is free above ₹999
* Backend says above ₹1199

Now customers complain.

---

## 2. Change Amplification

One change requires modifying 20 files.

Engineering velocity collapses.

This is one of the biggest scalability killers in enterprise systems.

---

## 3. Bug Multiplication

One bug replicated everywhere.

Fixing becomes expensive because engineers don’t know all duplicate locations.

---

## 4. Cognitive Overload

Developers constantly ask:

* “Which version is correct?”
* “Where should I update this?”
* “Why are these implementations different?”

This destroys maintainability.

---

## 5. Architecture Rot

Over time systems become:

* inconsistent
* fragile
* impossible to refactor

Large legacy monoliths often fail because DRY was ignored for years.

---

# Why Principal Engineers Care Deeply About DRY

Junior engineers optimize for:

* “working code”

Senior engineers optimize for:

* maintainability

Principal engineers optimize for:

* system evolution over years

DRY is fundamentally about:

# Controlling change safely at scale

That is the real purpose.

---

# 2. Core Concept in Depth

# Formal Meaning

> Every piece of system knowledge should exist in exactly one place.

Notice:

* NOT “every line”
* NOT “every function”
* NOT “every syntax pattern”

But:

# every business rule

# Mental Model #1 — Source of Truth

For every rule ask:

> “Where is the single source of truth?”

Example:

## Wrong

Discount logic in:

* frontend
* backend
* invoice generator
* analytics

## Correct

Centralized discount policy engine.

---

# Mental Model #2 — Change Cost

Ask:

> “If requirement changes tomorrow, how many places break?”

This is one of the best architecture questions.

---

# Mental Model #3 — Knowledge Ownership

A rule should have:

* one owner
* one implementation
* one authority

---

# DRY Does NOT Mean:

## 1. Over-Abstraction

Huge mistake.

Developers see similarity too early.

Then they create:

* GenericManager
* BaseProcessor
* UniversalHandler

Now code becomes unreadable.

This is called:

# Accidental Abstraction

Bad DRY creates worse systems than duplication.

---

# 3. Real-World Engineering Examples

# Example 1 — E-Commerce Pricing Engine

Imagine:

```text
Amazon-like system
```

Pricing rules:

* festival discounts
* membership discounts
* coupon discounts
* seller discounts
* inventory-based pricing

If every service calculates pricing independently:

* checkout mismatch
* invoice mismatch
* cart mismatch

Instead:

```text
PricingEngine
   -> single pricing policy
```

All systems consume it.

That is DRY.

---

# Example 2 — Authentication Framework

Suppose JWT validation logic exists in:

* API gateway
* order service
* payment service
* notification service

One token rule changes.

Half services fail authentication.

Instead:

```text
Shared Authentication Middleware
```

Single authority.

---

# Example 3 — Distributed Retry Logic

Bad systems repeat retry logic everywhere:

```text
try {
   ...
} catch (...) {
   retry
}
```

Now retry behavior becomes inconsistent.

Some retry 2 times.
Some retry 5 times.
Some retry instantly.

Production chaos.

Correct approach:

```text
Central Retry Policy
```

---

# Example 4 — Validation Systems

Bad backend systems:

```text
if email invalid
if password invalid
if phone invalid
```

repeated across:

* controllers
* services
* APIs
* admin tools

Correct:

```text
Validation Layer
```

Reusable and centralized.

---

# Example 5 — Framework Design

Laravel, Spring, Express middleware.

Why middleware exists?

Because frameworks apply DRY to:

* auth
* logging
* validation
* rate limiting

instead of duplicating logic per controller.

---

# 4. Code Examples in Depth

# PHP Example

# BAD DESIGN

```php
class OrderService {

    public function calculateFinalPrice($price) {
        return $price - ($price * 0.10);
    }
}

class InvoiceService {

    public function calculateInvoicePrice($price) {
        return $price - ($price * 0.10);
    }
}
```

---

# Problem

Today discount is 10%.

Tomorrow it becomes:

* premium user specific
* festival based
* seller based

Now duplication explodes.

---

# GOOD DESIGN

```php
class DiscountPolicy {

    public function apply(float $price): float {
        return $price - ($price * 0.10);
    }
}

class OrderService {

    private DiscountPolicy $discountPolicy;

    public function __construct(DiscountPolicy $discountPolicy) {
        $this->discountPolicy = $discountPolicy;
    }

    public function calculateFinalPrice(float $price): float {
        return $this->discountPolicy->apply($price);
    }
}

class InvoiceService {

    private DiscountPolicy $discountPolicy;

    public function __construct(DiscountPolicy $discountPolicy) {
        $this->discountPolicy = $discountPolicy;
    }

    public function calculateInvoicePrice(float $price): float {
        return $this->discountPolicy->apply($price);
    }
}
```

---

# Design Decision

The important thing is NOT helper reuse.

The important thing is:

```text
Discount knowledge centralized
```

---

# C++ Example

# BAD

```cpp
class ShippingService {
public:
    double calculateTax(double amount) {
        return amount * 0.18;
    }
};

class InvoiceService {
public:
    double calculateTax(double amount) {
        return amount * 0.18;
    }
};
```

---

# GOOD

```cpp
class TaxCalculator {
public:
    double calculate(double amount) {
        return amount * 0.18;
    }
};

class ShippingService {
private:
    TaxCalculator& taxCalculator;

public:
    ShippingService(TaxCalculator& tc)
        : taxCalculator(tc) {}

    double getShippingCost(double amount) {
        return amount + taxCalculator.calculate(amount);
    }
};

class InvoiceService {
private:
    TaxCalculator& taxCalculator;

public:
    InvoiceService(TaxCalculator& tc)
        : taxCalculator(tc) {}

    double generateInvoice(double amount) {
        return amount + taxCalculator.calculate(amount);
    }
};
```

---

# Important Engineering Insight

DRY often leads to:

* shared policy objects
* shared domain services
* shared middleware
* shared utilities

NOT giant inheritance trees.

---

# JavaScript ES6 Example

# BAD

```javascript
class CartService {
    calculateDiscount(price) {
        return price * 0.9;
    }
}

class CheckoutService {
    calculateDiscount(price) {
        return price * 0.9;
    }
}
```

---

# GOOD

```javascript
class DiscountEngine {
    apply(price) {
        return price * 0.9;
    }
}

class CartService {
    constructor(discountEngine) {
        this.discountEngine = discountEngine;
    }

    calculate(price) {
        return this.discountEngine.apply(price);
    }
}

class CheckoutService {
    constructor(discountEngine) {
        this.discountEngine = discountEngine;
    }

    calculate(price) {
        return this.discountEngine.apply(price);
    }
}
```

---

# 5. Bad Design vs Good Design

# Real Production Failure Scenario

Suppose ride pricing logic exists in:

* rider app
* driver app
* backend
* invoice system

Now surge pricing changes.

One service deploys late.

Now:

* rider charged ₹450
* driver receives ₹380
* invoice says ₹410

Financial inconsistency.

This becomes a reconciliation nightmare.

---

# BAD DESIGN

```text
Every component owns pricing logic
```

This violates:

* DRY
* Single Source of Truth

---

# GOOD DESIGN

```text
PricingService
   -> authoritative fare calculation
```

All consumers depend on it.

---

# Why This Scales Better

Now pricing evolves safely:

* peak pricing
* traffic pricing
* weather pricing
* ML pricing

without duplication explosion.

---

# 6. Relationship with Other Concepts

# DRY + OOP

OOP helps DRY through:

* encapsulation
* abstraction
* composition

Example:

```text
TaxCalculator object
```

encapsulates tax knowledge.

---

# DRY + SOLID

## SRP (Single Responsibility)

A class owning one responsibility naturally reduces duplication.

---

## OCP

Centralized policies become extendable.

---

## DIP

Services depend on abstractions instead of duplicating implementations.

---

# DRY + Design Patterns

## Strategy Pattern

Centralizes interchangeable logic.

Example:

```text
PaymentStrategy
PricingStrategy
DiscountStrategy
```

---

## Factory Pattern

Avoids repeated object creation logic.

---

## Template Method

Avoids algorithm duplication.

---

## Decorator

Avoids feature duplication.

---

# 7. Common Mistakes Engineers Make

# Mistake 1 — Premature Abstraction

Seeing two similar functions and instantly merging them.

Bad example:

```text
BaseManager
UniversalProcessor
AbstractGenericHandler
```

Now everything becomes coupled.

---

# Mistake 2 — Confusing Coincidental Similarity

Two code blocks look same TODAY.

But business meaning differs.

Example:

```text
calculateEmployeeBonus()
calculateFestivalDiscount()
```

Same math.
Different domain meaning.

Do NOT merge them.

---

# Mistake 3 — Giant Utility Classes

```text
Utils.php
CommonHelper.cpp
GlobalFunctions.js
```

These become garbage containers.

No ownership.
No cohesion.

---

# Mistake 4 — DRY Across Wrong Boundaries

Distributed systems sometimes intentionally duplicate logic.

Example:

Frontend validation + backend validation.

This is acceptable because:

* security boundary
* latency optimization

Context matters.

---

# Mistake 5 — Shared Libraries Everywhere

Over-centralization creates:

* tight coupling
* deployment bottlenecks
* version conflicts

Sometimes duplication is cheaper.

Principal engineers know:

# DRY is about balancing change cost

not eliminating every duplicate.

---

# 8. Real System Case Study — Payment Gateway

# Problem

A payment gateway supports:

* cards
* UPI
* wallets
* net banking

Fraud detection logic duplicated across flows.

---

# What Happens

Each team adds fraud rules separately.

Eventually:

* UPI blocks transaction
* wallet allows same fraud
* card service behaves differently

This creates security holes.

---

# Correct Architecture

```text
FraudDetectionEngine
    -> centralized fraud rules
```

All payment methods call same engine.

---

# Benefits

## Consistency

All payment methods behave uniformly.

---

## Easier Evolution

Adding ML fraud scoring happens once.

---

## Better Observability

Single fraud engine logs everything centrally.

---

## Easier Compliance

Auditable rule management.

---

# Real Principal-Level Insight

At scale:

# DRY improves operational reliability

not just code cleanliness.

---

# 9. Practical Refactoring Exercise

# MESSY CODE

```php
class UserController {

    public function create($email) {

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email");
        }

        // create user
    }
}

class AdminController {

    public function createAdmin($email) {

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email");
        }

        // create admin
    }
}
```

---

# Problems

## Duplicate validation logic

---

## Validation rule change risk

---

## Inconsistent future behavior

---

# REFACTORED DESIGN

```php
class EmailValidator {

    public function validate(string $email): void {

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email");
        }
    }
}

class UserController {

    private EmailValidator $validator;

    public function __construct(EmailValidator $validator) {
        $this->validator = $validator;
    }

    public function create($email) {

        $this->validator->validate($email);

        // create user
    }
}

class AdminController {

    private EmailValidator $validator;

    public function __construct(EmailValidator $validator) {
        $this->validator = $validator;
    }

    public function createAdmin($email) {

        $this->validator->validate($email);

        // create admin
    }
}
```

---

# Important Insight

This is NOT about reducing lines.

This is about:

```text
centralizing validation knowledge
```

---

# 10. Principal Engineer Thinking About DRY

When reviewing systems ask:

# Question 1

> “What knowledge is duplicated?”

---

# Question 2

> “What changes frequently?”

Those are best DRY candidates.

---

# Question 3

> “Where is the source of truth?”

---

# Question 4

> “Will abstraction reduce or increase complexity?”

Critical question.

---

# Question 5

> “What is the blast radius of change?”

This is advanced engineering thinking.

---

# 11. Problem for You to Solve

# SYSTEM DESIGN PROBLEM

You are building an E-Commerce platform.

Currently:

* CartService calculates discounts
* CheckoutService calculates discounts
* InvoiceService calculates discounts
* RefundService calculates discounts

Each has copied logic.

Now business introduces:

* festival discounts
* membership discounts
* seller-specific discounts
* coupon stacking rules

---

# Your Task

Design a DRY architecture for this system.

Answer these:

1. What classes/services will you create?
2. Where will discount knowledge live?
3. How will future discount rules be added?
4. How will you avoid tight coupling?
5. Which SOLID principles will help?
6. Would you use inheritance or composition?
7. How would this work in distributed systems?

---

# IMPORTANT

Do NOT give a shallow answer.

Think like:

* scalability
* maintainability
* extensibility
* ownership
* deployment evolution

Reply with your design.

I will review it like a Principal Engineer reviewing a real production architecture.

---

#### My Sample Answer

```php
interface DiscountService {
    public function calculateDiscount($amount);
}

class FestivalDiscountService implements DiscountService {
    public function calculateDiscount($amount) {
        return $amount * 0.1;
    }
}

class MembershipDiscountService implements DiscountService {
    public function calculateDiscount($amount) {
        return $amount * 0.2;
    }
}

class SellerSpecificDiscountService implements DiscountService {
    public function calculateDiscount($amount) {
        return $amount * 0.3;
    }
}

class CouponStackingDiscountService implements DiscountService {
    public function calculateDiscount($amount) {
        return $amount * 0.4;
    }
}

Class DiscountCalculator {

    private $discountServices = [];

    public function addDiscountService(DiscountService $discountService) {
        $this->discountServices[] = $discountService;
    }

    public function calculateTotalDiscount($amount) {
        $totalDiscount = 0;
        foreach($this->discountServices as $discountService) {
            $totalDiscount += $discountService->calculateDiscount($amount);
        }
        return $totalDiscount;
    }
}


class CartService {
    private $discountCalculator;
    public function __construct(DiscountCalculator $discountCalculator) {
        $this->discountCalculator = $discountCalculator;
    }
    public function calculateTotalDiscount($amount) {
        return $this->discountCalculator->calculateTotalDiscount($amount);
    }
}

class CheckoutService {
    private $discountCalculator;
    public function __construct(DiscountCalculator $discountCalculator) {
        $this->discountCalculator = $discountCalculator;
    }
    public function calculateTotalDiscount($amount) {
        return $this->discountCalculator->calculateTotalDiscount($amount);
    }
}

class InvoiceService {
    private $discountCalculator;
    public function __construct(DiscountCalculator $discountCalculator) {
        $this->discountCalculator = $discountCalculator;
    }
    public function calculateTotalDiscount($amount) {
        return $this->discountCalculator->calculateTotalDiscount($amount);
    }
}

class RefundService {
    private $discountCalculator;
    public function __construct(DiscountCalculator $discountCalculator) {
        $this->discountCalculator = $discountCalculator;
    }
    public function calculateTotalDiscount($amount) {
        return $this->discountCalculator->calculateTotalDiscount($amount);
    }
}


DiscountCalculator $discountCalculator = new DiscountCalculator();
$discountCalculator->addDiscountService(new FestivalDiscountService());
$discountCalculator->addDiscountService(new MembershipDiscountService());
$discountCalculator->addDiscountService(new SellerSpecificDiscountService());
$discountCalculator->addDiscountService(new CouponStackingDiscountService());

$cartService = new CartService($discountCalculator);
$checkoutService = new CheckoutService($discountCalculator);
$invoiceService = new InvoiceService($discountCalculator);
$refundService = new RefundService($discountCalculator);

$cartService->calculateTotalDiscount(100);
$checkoutService->calculateTotalDiscount(100);
$invoiceService->calculateTotalDiscount(100);
$refundService->calculateTotalDiscount(100);
```

--- 

Your direction is correct.

You understood the most important DRY idea:

> discount logic should not live independently inside Cart, Checkout, Invoice, Refund.

That is the correct architectural instinct.

Now I’ll review this like a Principal Engineer reviewing production-grade architecture.

---

# What You Did Correctly

# 1. Centralized Discount Knowledge ✅

This is the biggest success in your design.

You moved discount calculation responsibility into:

```php
DiscountCalculator
```

instead of:

```text
CartService
CheckoutService
InvoiceService
RefundService
```

This is true DRY.

You avoided:

* logic divergence
* duplicate business rules
* inconsistent pricing

Excellent.

---

# 2. Used Polymorphism Correctly ✅

This is very important.

```php
interface DiscountService
```

allows extensibility.

Now new discounts can be added without modifying existing services.

This follows:

# Open Closed Principle (OCP)

Good engineering direction.

---

# 3. Composition Over Inheritance ✅

Very important architectural decision.

You used:

```php
DiscountCalculator HAS discount services
```

instead of:

```text
BaseDiscount
AdvancedDiscount
MegaDiscount
```

This is much better.

Inheritance would become rigid very quickly.

---

# 4. Service Isolation ✅

Each discount type has its own responsibility.

Good cohesion.

---

# But Now Let's Go Deep

Your design is good for:

```text
LLD beginner/intermediate level
```

Now let’s evolve it toward:

# production-grade architecture

because real systems become much harder.

---

# Critical Production Problems in Your Current Design

# Problem 1 — Discounts Are Blind

Your interface:

```php
calculateDiscount($amount)
```

is too weak.

Real discounts depend on:

* user type
* seller
* product category
* geography
* coupon
* cart items
* time
* inventory
* campaign
* payment method

Your current design cannot support this.

---

# Principal-Level Insight

In real systems:

# discounts are contextual policies

NOT simple arithmetic functions.

---

# Better Design

Create:

```php
DiscountContext
```

Example:

```php
class DiscountContext {
    public User $user;
    public Cart $cart;
    public Seller $seller;
    public ?Coupon $coupon;
    public DateTime $purchaseTime;
}
```

Now:

```php
interface DiscountPolicy {
    public function apply(DiscountContext $context): DiscountResult;
}
```

This is much more scalable.

---

# Problem 2 — Your Discounts Stack Incorrectly

Currently:

```php
$totalDiscount += ...
```

This is dangerous.

Real systems have rules like:

* coupons cannot combine
* max discount ₹500
* seller discount applies before coupon
* membership applies after tax
* some discounts mutually exclusive

Your architecture currently cannot model:

# discount orchestration rules

This is a massive real-world problem.

---

# Real Production Example

Amazon/Uber/Zomato pricing engines are extremely complicated because:

# order of rule execution matters

---

# Better Design

Instead of:

```php
DiscountCalculator
```

Think:

# DiscountEngine

which contains:

* rule evaluation
* prioritization
* stacking policy
* eligibility validation
* conflict resolution

---

# Example

```php
interface DiscountPolicy {
    public function isApplicable(DiscountContext $context): bool;

    public function apply(DiscountContext $context): DiscountResult;

    public function priority(): int;
}
```

Now engine can:

```php
sort by priority
validate conflicts
apply sequentially
```

That is production-level design.

---

# Problem 3 — Missing Domain Modeling

Your services:

```php
FestivalDiscountService
MembershipDiscountService
```

are still too implementation-oriented.

Real systems model:

# business capabilities

not calculation functions.

Better naming:

```text
FestivalCampaignPolicy
MembershipPricingPolicy
SellerPromotionPolicy
CouponPolicy
```

This matters at scale because naming shapes architecture thinking.

---

# Problem 4 — No Ownership Boundary

Right now:

```php
DiscountCalculator
```

directly manages policy registration.

In large systems this becomes problematic.

Because:

* marketing team adds rules
* campaigns change dynamically
* A/B testing exists
* feature flags exist

Hardcoded registration becomes impossible.

---

# Real Architecture

Usually:

```text
DiscountPolicyRepository
CampaignService
RuleEngine
FeatureFlagService
```

provide rules dynamically.

---

# Problem 5 — No Auditability

In real payment/e-commerce systems:

you MUST explain:

```text
Why user got this discount?
```

Your current design returns:

```php
float
```

Not enough.

---

# Better

```php
class DiscountResult {
    public float $amount;
    public string $reason;
    public string $discountCode;
}
```

Now invoices and analytics become possible.

---

# Problem 6 — Shared Logic vs Shared State

Right now you share:

```php
DiscountCalculator
```

object.

Fine.

But in distributed systems:

* cart service
* checkout service
* invoice service

may be separate microservices.

Now sharing PHP objects is impossible.

---

# Real Distributed Architecture

You need:

# Central Pricing Service

Example:

```text
Pricing Service
   -> calculates authoritative pricing
```

All services call it.

This avoids:

* pricing mismatch
* invoice mismatch
* refund mismatch

This is where DRY becomes architectural.

---

# HUGE Principal Engineer Insight

At scale:

# DRY evolves from code-level reuse to domain-level consistency.

This is the evolution many engineers never understand.

---

# What You Did Well With SOLID

# SRP ✅

Each policy has one responsibility.

---

# OCP ✅

New policies added without modifying existing ones.

---

# DIP ✅

Services depend on abstraction.

Good.

---

# What Still Needs Improvement

# ISP

Your interface is too narrow.

---

# LSP

Potential future issue.

Suppose:

```php
CouponStackingDiscountService
```

needs cart-level data.

Now interface breaks.

This means abstraction is not yet stable.

---

# Better Interface

```php
interface DiscountPolicy {
    public function apply(
        DiscountContext $context
    ): DiscountResult;
}
```

Now abstraction survives growth.

---

# Important Distributed System Discussion

You answered only LLD-level DRY.

But Principal Engineers think about:

# organizational scalability

Imagine:

* Cart team
* Checkout team
* Payments team
* Marketing promotions team

all independently deploying.

Now duplicated pricing logic becomes catastrophic.

---

# Real Production Failure

Suppose:

```text
Cart total = ₹900
Checkout total = ₹940
Invoice total = ₹920
Refund total = ₹870
```

This creates:

* finance reconciliation failure
* customer distrust
* support escalation
* accounting mismatch

---

# Therefore:

Real systems establish:

# authoritative pricing ownership

Usually:

```text
Pricing Domain Team
```

This is DRY at organization scale.

---

# Final Evaluation

# Your Current Level

You already understand:

✅ DRY basics
✅ Polymorphic extensibility
✅ Composition
✅ Shared business logic

That is good.

---

# To Reach Senior/Principal Level

You now need to think about:

* rule orchestration
* policy conflicts
* contextual business rules
* distributed consistency
* auditability
* ownership boundaries
* runtime extensibility
* domain-driven design

That is the next evolution.

---

# Your Next Challenge (Much Harder)

Design a production-grade:

# Pricing Engine

Requirements:

* multiple discount types
* discount priority
* mutually exclusive discounts
* max discount cap
* dynamic campaigns from DB
* coupon eligibility
* region-specific pricing
* A/B testing support
* audit logs
* explainable pricing
* distributed microservice support
* idempotent recalculation

---

# Your Task

Design:

1. Core classes/interfaces
2. Policy execution flow
3. Conflict resolution
4. How pricing becomes source of truth
5. How other services consume pricing
6. How audit history works
7. How extensibility works
8. What patterns you would use
9. How caching would work
10. How versioning of pricing rules would work

---

# DRY — Interview Thinking, Architecture Thinking, and Senior Engineer Maturity

You now understand:

* code-level DRY
* business-level DRY
* distributed-system DRY
* organizational DRY

Now we move into:

# Engineering maturity with DRY

This is where engineers separate into:

* coders
* software engineers
* system designers
* architects
* principal engineers

---

# 15. DRY in LLD Interviews

Most candidates fail DRY discussions because they give:

```text
“I created a utility class.”
```

That is weak.

Interviewers actually evaluate:

* system evolution thinking
* ownership clarity
* change management
* extensibility
* abstraction maturity

---

# Weak Candidate Thinking

```text
“I reduced duplicate code.”
```

---

# Strong Candidate Thinking

```text
“I centralized pricing policy because
pricing consistency is business critical
and multiple services depend on it.”
```

That sounds like a system designer.

---

# Interviewers Secretly Check

# 1. Can you identify volatile logic?

Volatile = changes frequently.

Examples:

* pricing
* discounts
* fraud rules
* tax rules
* permissions

These are DRY-sensitive areas.

---

# 2. Can you distinguish:

```text
shared behavior
vs
coincidental similarity
```

This is a huge signal.

---

# 3. Can you avoid over-engineering?

Senior engineers know:

# over-DRY can destroy maintainability.

---

# 4. Can you think about change safely?

This is the real purpose of DRY.

---

# 16. Advanced DRY Refactoring Strategy

Real systems are messy.

You rarely design clean systems from scratch.

Most work is:

# refactoring legacy systems

---

# The Wrong Refactoring Approach

Junior engineers often:

* create giant abstractions
* aggressively merge classes
* centralize everything

Result:

* impossible debugging
* tight coupling
* abstraction leaks

---

# Better Refactoring Process

# Step 1 — Identify Knowledge Duplication

Ask:

> “What business rule exists in multiple places?”

---

# Step 2 — Analyze Change Frequency

Does this logic evolve frequently?

If yes → high DRY value.

---

# Step 3 — Analyze Ownership

Who owns this rule?

* finance?
* pricing?
* authentication?
* compliance?

---

# Step 4 — Extract Stable Abstraction

Stable abstractions survive future changes.

Unstable abstractions create technical debt.

---

# Step 5 — Introduce Contract

Usually:

* interface
* policy
* service
* middleware
* domain object

---

# Step 6 — Migrate Incrementally

Never refactor entire enterprise systems at once.

Principal engineers avoid:

# big-bang rewrites

---

# 17. DRY vs Reusability

Massive misunderstanding.

People think:

```text
DRY == reusable
```

Not always.

---

# Example

Suppose:

```php
calculateEmployeeBonus()
calculateFestivalOffer()
```

Both use:

```php
amount * 0.2
```

Should they share implementation?

NO.

Because:

# business meaning differs.

---

# Important Principle

# Shared math ≠ shared knowledge

This distinction is extremely advanced.

---

# 18. DRY vs Generic Programming

Another dangerous trap.

Developers try making everything generic.

---

# BAD

```php
class GenericManager<T> {}
```

or

```php
class UniversalServiceHandler {}
```

These become:

* unreadable
* fragile
* tightly coupled

---

# Why This Happens

Engineers optimize for:

```text
minimum code
```

instead of:

```text
minimum complexity
```

---

# Principal Engineer Rule

# Complexity is more expensive than duplication.

Very important.

---

# 19. DRY and Domain Driven Design (DDD)

Now we connect DRY with architecture.

DDD teaches:

# domain boundaries matter.

---

# Example

Pricing domain owns:

* fare calculation
* surge rules
* discounts
* taxes

Order domain owns:

* order lifecycle

Inventory domain owns:

* stock consistency

---

# DRY Within Bounded Contexts

Inside a bounded context:

centralize aggressively.

Across contexts:

be careful.

---

# Example

User Service may define:

```text
ACTIVE
BLOCKED
```

Fraud Service may define:

```text
RISKY
TRUSTED
```

Do NOT force same abstraction.

Different domains.

---

# This is why:

# DRY must respect domain boundaries.

---

# 20. DRY and Event Sourcing

Advanced architecture topic.

In event sourcing systems:

state is reconstructed from events.

---

# DRY Problem

Business rules duplicated between:

* command handlers
* projections
* read models

---

# Better Design

Central domain policies generate authoritative events.

Example:

```text
FareCalculated
DiscountApplied
TripCompleted
```

All downstream systems consume same truth.

Again DRY.

---

# 21. DRY and Caching

Very important real-world issue.

---

# BAD

Each service caches pricing differently.

Now:

```text
Cart -> ₹500
Checkout -> ₹520
Invoice -> ₹490
```

because cache invalidation differs.

---

# Proper DRY Thinking

Centralize:

* pricing computation
* cache invalidation policy
* cache ownership

---

# Important Insight

# Cache policy is business knowledge too.

---

# 22. DRY and Feature Flags

Modern systems rely heavily on:

* A/B testing
* rollout controls
* feature flags

---

# BAD

Feature logic duplicated across services.

Now rollout behaves inconsistently.

---

# GOOD

Centralized feature evaluation system.

Example:

```text
LaunchDarkly
Internal Flag Service
```

Again:

# authoritative business decision source.

---

# 23. DRY and Observability

Even logging can violate DRY.

---

# BAD

Every service logs differently.

Different formats.
Different fields.

Impossible debugging.

---

# GOOD

Shared logging standards.

NOT necessarily shared logging code.

This distinction matters.

---

# Example

Standardize:

```json
{
  "traceId": "",
  "requestId": "",
  "userId": ""
}
```

This is DRY at operational level.

---

# 24. DRY and Error Handling

Real enterprise nightmare.

Different services handling same errors differently.

Example:

```text
timeout
rate limit
payment failure
```

Now system behavior becomes inconsistent.

---

# Better

Shared retry policies.
Shared error taxonomy.
Shared resilience standards.

---

# 25. DRY and Security Architecture

One of the most important areas.

---

# BAD

Authorization checks duplicated.

One service forgets:

```text
ADMIN_ONLY
```

Security breach.

---

# GOOD

Central authorization middleware/policy engine.

Examples:

* OAuth middleware
* API Gateway
* OPA (Open Policy Agent)

---

# DRY Here Is Critical

Because inconsistency becomes vulnerability.

---

# 26. DRY and Data Pipelines

Analytics systems suffer heavily from DRY violations.

---

# Example

Revenue calculation differs between:

* dashboard
* finance reports
* invoices
* analytics warehouse

Now executives see different numbers.

This is extremely common.

---

# Solution

Central business metric definitions.

Example:

```text
RevenueDefinitionService
Metric Registry
Semantic Layer
```

---

# 27. DRY and AI/ML Systems

Modern architecture issue.

Feature engineering duplicated across:

* training
* inference
* analytics

Now models behave differently in production.

---

# Solution

Central Feature Store.

Again:

# authoritative feature knowledge.

---

# 28. DRY and Team Topology

Huge principal-level topic.

---

# BAD Organization

Every team owns its own pricing logic.

Result:

* inconsistent pricing
* deployment chaos
* duplicated effort

---

# GOOD Organization

Dedicated pricing platform/domain team.

Clear ownership.

---

# Architecture Mirrors Teams

This is Conway’s Law.

---

# 29. DRY vs Performance Tradeoffs

Sometimes duplication improves performance.

---

# Example

Denormalized database tables.

Technically duplicate data.

But improve:

* query speed
* scalability
* read performance

---

# Therefore:

# DRY must balance performance realities.

---

# 30. DRY vs Reliability Tradeoffs

Centralization increases consistency.

But may create:

* single point of failure
* deployment bottleneck

---

# Example

Central Pricing Service down.

Entire checkout flow breaks.

---

# Real Solution

* fallback pricing snapshot
* cached fare
* versioned policy
* resilience strategy

---

# Mature Engineering Thinking

# DRY without resilience is dangerous.

---

# 31. The Principal Engineer DRY Checklist

When reviewing architecture:

---

# A. What knowledge changes often?

High DRY candidate.

---

# B. What inconsistency is catastrophic?

Centralize aggressively.

Examples:

* money
* security
* compliance

---

# C. What duplication improves autonomy?

Allow it.

---

# D. Is abstraction stable?

If unstable → avoid over-DRY.

---

# E. Does centralization increase coupling?

Critical tradeoff.

---

# F. Who owns this business rule?

Ownership clarity matters enormously.

---

# G. Can services evolve independently?

Avoid shared-code hell.

---

# H. Can this abstraction survive 5 years?

Principal-level thinking.

---

# 32. Final DRY Philosophy

Junior Engineers Think:

```text
“How can I reduce duplicate code?”
```

---

# Senior Engineers Think:

```text
“How can I reduce change amplification?”
```

---

# Principal Engineers Think:

```text
“How can this system evolve safely
for years across teams and services?”
```

That is the true evolution.

---

# Ultimate DRY Definition

# DRY is the discipline of managing system knowledge safely, consistently, and evolvably.

Not merely removing repeated code.

---

# Complete Mental Model of DRY

| Level        | DRY Meaning                     |
| ------------ | ------------------------------- |
| Beginner     | avoid repeated code             |
| Intermediate | reuse logic                     |
| Senior       | centralize business rules       |
| Staff        | manage ownership boundaries     |
| Principal    | control system evolution safely |

---

# Final Deep Insight

Sometimes the best architecture is:

* small duplication
* clear ownership
* independent services
* lower coupling

NOT maximum reuse.

---

# THIS is the engineering maturity most developers never reach.

---

# PHASE 4 — DRY COMPLETE

You now understand DRY at:

* code level
* OOP level
* architecture level
* distributed system level
* organizational level
* operational level
* principal engineer level

---