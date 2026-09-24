# 🔥 PHASE 1 — LLD BASICS

# COMPLETE QUICK REVISION (Principal Engineer Version)

This is your **high-speed revision sheet** for the entire `01_LLD_Basics` module.

Do NOT memorize definitions.

Your real goal is:

> Learn *what LLD is*, *where it sits vs HLD*, *which interview format you are in*, and *what interviewers actually score* — so you never design at the wrong depth again.

---

# 🧠 THE BIG PICTURE

This folder answers ONE question:

> “What does Low-Level Design actually mean in production and interviews — and how do I show that I can be trusted to design code on a team?”

Four skills, in order:

```text
What LLD is (and is not)
        ↓
HLD vs LLD (which depth am I at?)
        ↓
Interview formats (machine code / discussion / refactor)
        ↓
Hidden evaluation rubric (how they score you)
```

If you skip this, later SOLID and patterns become pattern-dumping.

---

# 🔥 THE CORE TRUTH (WRITE THIS DOWN)

| Junior belief | Senior truth |
| ------------- | ------------ |
| LLD = UML diagrams | LLD = classes, responsibilities, relationships, behavior |
| LLD = start coding | LLD = decide responsibilities **before** code |
| LLD = use many patterns | LLD = isolate change with the **simplest** design |
| HLD and LLD are the same “design” | HLD = boxes; LLD = classes **inside** a box |
| Interviews test typing speed | Interviews test **thinking under constraints** |
| Best design in the world wins | “Would I trust this person on my team?” wins |

> **LLD is not about writing code faster. It’s about changing code safely.**

---

# 1. WHAT IS LOW-LEVEL DESIGN?

---

# 🧠 Meaning

> **LLD is the art of converting requirements into clean, extensible classes and interactions.**

Not diagrams. Not patterns. Not frameworks.

```text
Classes. Responsibilities. Relationships. Behavior.
```

If you can answer these, you have done LLD:

* What classes exist?
* What does each class do?
* How do classes talk to each other?
* How is behavior distributed?
* Where will change happen?

---

# ❌ What LLD Is NOT

* UI design
* Database schema
* Infrastructure
* REST API design
* HLD

**LLD lives inside the codebase.**

---

# Where LLD Sits

```text
Business Problem
   ↓
High Level Design (HLD)     ← big boxes
   ↓
Low Level Design (LLD)      ← classes inside boxes
   ↓
Code
```

---

# LLD vs Coding (Critical)

| Coding | LLD |
| ------ | --- |
| “I’ll start writing and see.” | “Let me decide responsibilities first.” |

A senior can **delay coding** and still make progress by designing.

---

# What Interviewers Actually Look For

They are **not** checking syntax or framework knowledge.

They **are** checking:

* How you break a problem
* How you assign responsibilities
* How you handle change
* How clean your abstractions are

---

# Real Example — Notification System

**Problem:** support Email and SMS.

### ❌ No LLD (coding)

```php
function notify($type, $msg) {
    if ($type === 'email') {}
    elseif ($type === 'sms') {}
}
```

### ✅ LLD thinking (before code)

* What varies? → Notification type
* What stays same? → Sending a notification
* Who owns responsibility?

```php
interface NotificationChannel {
    public function send(string $message): void;
}

class EmailNotification implements NotificationChannel {}
class SmsNotification implements NotificationChannel {}

class NotificationService {
    public function notify(NotificationChannel $channel, string $message): void {
        $channel->send($message);
    }
}
```

This is **LLD**.

If they ask “Can we add WhatsApp?” and you say:

> “Yes — add a new class.”

You are winning.

---

# Golden Question of LLD

> **“Who should do this?”**

Bad LLD = one class does everything.  
Good LLD = responsibilities distributed logically.

---

# What Makes a GOOD LLD Answer

* Clear class responsibilities
* Low coupling
* High cohesion
* Easy to extend
* Simple to explain

---

# Typical LLD Interview Flow (NEVER SKIP)

1. Clarify requirements
2. Identify entities
3. Define responsibilities
4. Decide relationships
5. Apply patterns **(if needed)**
6. Write code / pseudocode

Skipping steps = bad impression.

---

# Senior Mental Model (before code)

* What are the core entities?
* What will change most often?
* How can I isolate that change?
* What is the **simplest** design that works?

---

# Practice flash

Alerts via Email + Push:

* Classes: `NotificationChannel`, `EmailChannel`, `PushChannel`, `AlertService`
* Change lives in **new channel classes**
* Open for extension: channel implementations, not `AlertService`

---

# 2. HLD vs LLD

---

# 🧠 One-Line Difference (Senior-Level)

> **HLD = system architecture**  
> **LLD = class-level design**

Interviewers don’t want a dictionary. They want to see **which depth you think at**.

---

# What Each Answers

### HLD (big picture)

* Major components?
* How they communicate?
* Where data flows?
* How the system scales?

**Food delivery HLD:** User Service, Order Service, Payment Service, Delivery Service, Notification Service, DBs, caches, queues.

📦 **Boxes and arrows**

### LLD (inside the box)

* What classes exist inside Order Service?
* How is Order created, validated, paid?
* How do objects collaborate?
* Where do we apply patterns?

**Order Service LLD:** `Order`, `OrderItem`, `OrderValidator`, `PaymentProcessor`, `OrderRepository`

🧩 **Classes and interactions**

---

# Interview-Ready Comparison

| Aspect    | HLD                 | LLD                 |
| --------- | ------------------- | ------------------- |
| Focus     | Architecture        | Code structure      |
| Level     | System              | Class / method      |
| Artifacts | Services, APIs      | Classes, interfaces |
| Patterns  | Microservices, CQRS | Strategy, Factory   |
| Output    | System diagram      | UML / code          |
| Audience  | Architects          | Developers          |

---

# 🔥 THE PARKING LOT TRICK

> “Design a parking lot system.”

### ❌ Weak (jumped to HLD)

Microservices, APIs, DB sharding.

### ✅ Strong (stayed in LLD)

`Vehicle`, `ParkingSlot`, `ParkingFloor`, `Ticket`, `Payment`

**If they asked LLD, start with classes — not Kafka.**

---

# How Interviewers Shift Levels (SENIOR SIGNAL)

| They say | You do |
| -------- | ------ |
| “Now zoom in on Order Service.” | Stop architecture. Start class design. |
| “How would this scale?” | Step back to HLD. |

**Knowing when to switch = senior signal.**

---

# Practical Mental Model

```text
Databases, APIs, scaling     → HLD
Classes, methods, interfaces → LLD
```

If you’re unsure → you are probably mixing levels.

---

# ⚠️ Why Candidates Fail

1. Mixing HLD into LLD (Kafka, Redis, load balancers when they asked for classes)
2. Writing code without design (no responsibilities explained)
3. Over-engineering LLD (5 patterns where 1 is enough)

---

# 🔥 Perfect Interview Sentence

> “HLD focuses on system-level components and interactions, while LLD focuses on class-level design, responsibilities, and object interactions inside a component.”

---

# Practice flash

**Online bookstore**

* HLD: Catalog Service, Cart Service, Order Service, Payment Service, Search/Inventory
* LLD inside Order: `Order`, `OrderItem`, `OrderValidator`, `PricingEngine`, `OrderRepository`

**Payment Service**

* HLD: service boundaries, gateway, queues, DB
* LLD: `PaymentProcessor`, `PaymentMethod` interface, `CardPayment`, `RefundService`

---

# Key Takeaway

> **Good engineers know both. Great engineers know when to use which.**

---

# 3. TYPES OF LLD INTERVIEWS

---

# 🧠 Meaning

Companies don’t test LLD one way.

They test **how you think under different constraints**.

Most people fail because they **prepared the wrong format**.

---

# The 3 Types

```text
1. Machine Coding Round
2. LLD Design Discussion
3. Code Review / Refactoring Round
```

You may face **one or all**.

---

## TYPE 1 — MACHINE CODING

* Time: **60–120 min**
* You write **actual code**
* Scored on: design + readability + extensibility

**Expect:** clean classes, SOLID, working code (not perfect UI)

**Typical:** Parking Lot, Snake & Ladder, LRU Cache, Tic Tac Toe, Vending Machine

### ❌ Mistakes

Jump straight to code · no class list · god classes · no extensibility

### ✅ Senior time-box (GOLD)

| Time | Do |
| ---- | -- |
| First 10–15 min | Clarify requirements. Write **class names** on paper |
| Next 20 min | Responsibilities + relationships |
| Last ~60 min | Code cleanly. Refactor if time |

Say out loud:

> “I’ll start with a basic version and evolve it.”

---

## TYPE 2 — LLD DESIGN DISCUSSION

* Whiteboard / shared editor
* Mostly **design**, minimal code
* Heavy on thinking

**Look for:** breakdown, change handling, justifying decisions

**Typical:** Splitwise, Elevator, Chat App, URL Shortener (LLD view)

### ❌ Mistakes

Over-detailing · patterns too early · ignoring edge cases

### ✅ Structure (always)

1. Clarify requirements  
2. Identify core entities  
3. Define responsibilities  
4. Discuss relationships  
5. Handle extensions  

Say:

> “Let’s first agree on the core objects.”

---

## TYPE 3 — CODE REVIEW / REFACTORING

* Given messy code
* Identify issues → improve design → refactor

**They test:** smell detection, refactoring skill, communication

**Typical:** break god class, kill duplication, naming, introduce interfaces

### ❌ Mistakes

Rewrite everything · change behavior · stay silent

### ✅ First sentence (calms them instantly)

> “I’ll start by extracting responsibilities without changing behavior.”

That is Phase 0 (engineering mindset) applied live.

---

# How Companies Map Experience

| Level   | Expectation            |
| ------- | ---------------------- |
| 0–2 yrs | Working code           |
| 2–4 yrs | Clean structure        |
| 4–6 yrs | Extensible design      |
| 6+ yrs  | Trade-offs & evolution |

**Aim your answers at 4–6 year level:** extensible, but honest about trade-offs.

---

# Prep by Format

| Format | Practice |
| ------ | -------- |
| Machine coding | 90-min sessions; class design **first** |
| Design discussion | Explain **aloud**; draw class diagrams |
| Refactoring | Take messy code weekly; improve one smell at a time |

---

# Practice flash

* Parking Lot is usually **machine coding** → 15 min classes, then code a basic version
* God class round → first sentence: extract responsibilities, **don’t change behavior**

---

# Key Takeaway

> **LLD interviews test thinking, not typing speed.**

---

# 4. HOW INTERVIEWERS EVALUATE LLD (HIDDEN RUBRIC)

---

# 🧠 The Real Bar

They are **not** asking: “Is this the best design in the world?”

They **are** asking:

```text
"Would I trust this person to design code in my team?"
```

---

# The 6 Dimensions (MEMORIZE)

1. Problem Understanding  
2. Requirement Clarification  
3. Responsibility Assignment  
4. Design Quality  
5. Extensibility & Change Handling  
6. Communication & Trade-offs  

---

## D1 — Problem Understanding (first 5 minutes)

| Weak | Strong |
| ---- | ------ |
| “Okay, I’ll start coding.” | “Let me confirm the core requirements first.” |

**Rule:** if you misunderstand the problem, **nothing else matters**.

Signals: do you rush? restate? clarify scope?

---

## D2 — Requirement Clarification

They want: functional + non-functional + **explicit assumptions**.

* Weak: assumes too much, builds imaginary features  
* Strong: **3–5 smart questions**, states assumptions

Example:

> “Should we support multiple payment methods now, or design for future extension?”

---

## D3 — Responsibility Assignment (CORE LLD SKILL)

* Each class one job? Responsibilities in the right place?

| Red flag | Green flag |
| -------- | ---------- |
| God class | Cohesive classes |
| Utility classes everywhere | Meaningful names |

They love:

> “This responsibility belongs here because…”

---

## D4 — Design Quality

Signals: low coupling, high cohesion, clean abstractions, **minimal but sufficient** patterns.

| Bad | Good |
| --- | ---- |
| Deep inheritance | Interfaces **where change happens** |
| Pattern overuse | Composition over inheritance |
| Tight coupling | Simple flows |

---

## D5 — Extensibility & Change Handling

Favorite question:

> “What if we add X tomorrow?”

| Weak | Strong |
| ---- | ------ |
| “We’ll rewrite this part.” | “Add a new implementation without touching existing code.” |

This is where SOLID actually scores.

---

## D6 — Communication & Trade-offs

Seniors explain **why**, not just what.

| Weak | Strong |
| ---- | ------ |
| “This is better.” | “This adds one extra class, but it reduces change risk.” |

They score **how you think aloud**.

---

# Unofficial Scoring Table (PATTERNS MATTER LEAST)

| Skill              | Weight |
| ------------------ | ------ |
| Thinking clarity   | ⭐⭐⭐⭐   |
| Design cleanliness | ⭐⭐⭐⭐   |
| Extensibility      | ⭐⭐⭐    |
| Code correctness   | ⭐⭐     |
| Pattern knowledge  | ⭐      |

A **correct design badly explained still fails**.

---

# Why “Correct” Answers Fail

* Over-engineering
* No explanation
* Poor naming
* Ignoring change scenarios
* Silent coding

---

# Extra-Point Sentences (SAY THESE)

* “I’ll keep this simple for now.”
* “If requirements grow, we can refactor here.”
* “This abstraction isolates the change.”

These signal experience (Phase 0 + Phase 1 together).

---

# Practice flash

**Design a logging system (verbal):**

1. Questions: destinations now vs later? sync/async? levels? format?
2. First class: `Logger` or `LogSink` interface — not a god `LogManager`
3. Anticipated change: new sink (file / stdout / cloud)

**“Why not inheritance?”**

> Composition keeps coupling lower and lets us mix behaviors. Inheritance is for a true is-a, not for plugging new channels.

---

# 🔗 HOW THE 4 TOPICS CONNECT (ONE SYSTEM)

```text
LLD = classes + responsibilities + change isolation
        ↓
HLD vs LLD = never answer at the wrong depth
        ↓
Interview type = pick the right strategy (time-box / talk / refactor)
        ↓
Rubric = they hire trust: clarify → assign → extend → explain trade-offs
```

Same notification / payment / parking-lot problem is reused on purpose:

```text
if/else coding  →  channel interface  →  new class for WhatsApp
HLD boxes       →  LLD classes inside one box
Machine code    →  15 min design then implement
“Add X?”        →  “new class, existing code closed”
```

That is Phase 1 in one move.

---

# 🔥 60-SECOND FLASH CARD

| Topic | One-liner |
| ----- | --------- |
| LLD | Convert requirements → classes, responsibilities, relationships, behavior |
| LLD is not | UI, DB schema, infra, REST, HLD |
| LLD vs coding | Decide responsibilities **before** writing |
| Good LLD | Low coupling, high cohesion, easy to extend, easy to explain |
| Golden question | “Who should do this?” |
| HLD | System architecture — boxes and arrows |
| LLD | Class-level design — inside one box |
| Switch cue | “Zoom in” = LLD; “How does it scale?” = HLD |
| Machine coding | 10–15 min classes, then code; evolve a basic version |
| Design discussion | Core objects first; patterns last |
| Refactor round | Extract responsibilities; **don’t change behavior** |
| Career bar | Aim 4–6 yr answers: extensible + trade-offs |
| Real interview question | “Would I trust this person on my team?” |
| 6 dimensions | Understand → clarify → assign → quality → extend → communicate |
| Scoring | Clarity + cleanliness >> patterns |
| Kill sentence | “Add a new class / implementation, don’t touch existing code.” |

---

# 🔥 INTERVIEW ANSWER BANK (SAY THESE)

**What is LLD?**

> Converting requirements into classes, responsibilities, and interactions so change stays isolated. Not diagrams, not infrastructure.

**LLD vs HLD?**

> HLD is system-level components and how they talk. LLD is class-level design inside one component.

**How do you start a machine-coding round?**

> First 10–15 minutes I clarify and list classes. Then responsibilities and relationships. Then I code a basic version and evolve it.

**How do you start a design discussion?**

> Let’s first agree on the core objects.

**Messy code round — first sentence?**

> I’ll extract responsibilities without changing behavior.

**Can we add WhatsApp / a new payment method?**

> Yes — a new class implementing the same interface. Existing code stays closed.

**Why this extra interface?**

> It isolates the axis of change. One extra class now, much lower change risk later.

---

# 🧪 SELF-CHECK (CAN YOU ANSWER WITHOUT NOTES?)

1. What 5 questions does LLD answer?
2. Name 4 things LLD is **not**.
3. LLD vs coding — one sentence.
4. Notification system: what varies, what stays, which classes?
5. One-line HLD vs LLD?
6. Parking lot asked as LLD — first 5 classes, not first 5 services.
7. Interviewer says “zoom in on Order Service” — what do you stop/start?
8. Three LLD interview types + strategy for each?
9. Machine-coding time-box?
10. First sentence in a refactor round?
11. What are the 6 evaluation dimensions?
12. Unofficial scoring — what matters most / least?
13. Why do correct designs still fail?
14. The trust question interviewers are really asking?

If you can answer all 14 out loud, this module is in your muscle memory.

---

# 🔚 MODULE TAKEAWAY

> A professional does not start typing.
> A professional **clarifies**, **assigns responsibilities**, **isolates change**, and **explains trade-offs** — at the **right depth** (HLD or LLD), for the **right interview format**.

Phase 0 was **judgment** (when to stay simple).  
Phase 1 is **arena** (what LLD is, and how interviews score it).

Next modules are the tools: class relationships, SOLID, patterns.
You now know **what game you are playing**.
