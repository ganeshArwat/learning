## **Inheritance**

Let me say this upfront, like a principal engineer would in a design review:

> **Inheritance is the most dangerous tool in OOP.**

Powerful? Yes.
Necessary? Sometimes.
Default choice? **Absolutely not.**

---

## 1️⃣ What Inheritance REALLY is (beyond “is-a”)

Textbook says:

> “Inheritance represents an IS-A relationship.”

Senior engineer translation:

> **Inheritance permanently couples child behavior to parent decisions.**

Once you inherit:

* You inherit **all bugs**
* You inherit **future changes**
* You inherit **constraints you didn’t ask for**

This is why seniors fear inheritance.

---

## 2️⃣ The hidden cost of inheritance (most devs miss this)

When you write:

```php
class PremiumUser extends User {}
```

You are saying:

> “PremiumUser will always obey every rule User has — now and in the future.”

That’s a **huge promise**.

If tomorrow:

* User validation changes
* User lifecycle changes
* User constructor changes

👉 PremiumUser is affected **without touching its code**.

That’s tight coupling.

---

## 3️⃣ Classic real-world inheritance failure

### ❌ Example (very common)

```php
class Bird {
    public function fly() {}
}

class Penguin extends Bird {}
```

Penguins **cannot fly**.
Yet code allows:

```php
$penguin->fly();
```

This breaks **Liskov Substitution Principle** (we’ll go deep later).

This is inheritance lying to you.

---

## 4️⃣ Proper mental test before using inheritance

Ask **ALL** these questions:

1. Is the child a **true specialization**, not just reuse?
2. Can the child **safely replace** the parent everywhere?
3. Are parent behaviors **always valid** for child?
4. Will I regret this when requirements change?

If any answer is “not sure” → **don’t inherit**.

---

## 5️⃣ Real-life production example (payments)

### ❌ Bad inheritance

```php
class Payment {
    public function pay() {}
}

class RazorpayPayment extends Payment {}
class CashPayment extends Payment {}
```

Looks okay… until:

* Cash has no refund
* Razorpay has async callbacks
* Wallet has partial payments

Parent becomes bloated or wrong.

---

### ✅ Better: Composition + Abstraction

```php
interface PaymentMethod {
    public function pay(int $amount): bool;
}
```

```php
class RazorpayPayment implements PaymentMethod {}
class CashPayment implements PaymentMethod {}
```

Now:

* No shared wrong behavior
* Each class owns its rules
* No fragile parent

---

## 6️⃣ When inheritance IS actually good

Inheritance works well when:

* Parent defines **stable, invariant behavior**
* Child only **adds**, never removes
* Parent is abstract, not concrete

### Good example: Frameworks

```php
abstract class Controller {
    protected function json($data) {}
}
```

```php
class UserController extends Controller {}
```

Framework controls parent, you control child.

That’s a **safe direction of dependency**.

---

## 7️⃣ Abstract class vs Interface (inheritance flavor)

| Use case             | Interface | Abstract Class |
| -------------------- | --------- | -------------- |
| Multiple inheritance | ✅         | ❌              |
| Share code           | ❌         | ✅              |
| Contract only        | ✅         | ❌              |
| Framework base       | ❌         | ✅              |

Senior rule:

> Use **interfaces for behavior**,
> **abstract classes for shared implementation**.

---

## 8️⃣ JavaScript inheritance (same risk)

```js
class Vehicle {
  move() {}
}

class Car extends Vehicle {}
class Plane extends Vehicle {}
```

If later `move()` assumes wheels → Plane breaks.

JS inheritance is **not safer**, just more subtle.

---

## 9️⃣ Interview-level guidance (what to say)

If interviewer asks:

> “Why not use inheritance here?”

Strong answer:

> “Inheritance tightly couples child classes to parent behavior and makes change risky. Composition gives more flexibility and isolates change.”

That’s **senior maturity**.

---

## 🔟 Golden Rule (burn this into memory)

> **Inheritance is for behavior extension, not code reuse.**

If you want reuse → composition.
If you want polymorphism → interfaces.
If you want pain → inheritance everywhere.

---

## 🧠 Mini Practice

### Question:

Should `AdminUser` extend `User`?

Think:

* Does admin follow all user rules?
* Does admin have extra permissions or different lifecycle?

Most real systems:
👉 **NO inheritance**
👉 Use roles / composition

---

## 🧠 Final Principal-Engineer Take

> “If you reach for inheritance first,
> you haven’t thought hard enough.”

---
