# Phase 3 — Aggregation

Most developers misunderstand aggregation because many tutorials explain it poorly.

A principal engineer does not memorize definitions like:

> “Aggregation is a weak has-a relationship.”

That explanation is useless.

Instead we understand **the lifecycle and ownership rules of objects**.

---

# The Core Idea of Aggregation

Aggregation describes this relationship:

> **A whole object contains other objects, but those objects can exist independently.**

Meaning:

```
Whole
  └── Parts
```

But the parts are **not owned by the whole**.

If the whole disappears, the parts **still exist**.

---

# Real World Example

### Team and Player

```
Team
 ├── Player
 ├── Player
 ├── Player
```

But players exist even if the team is deleted.

Example:

```
Cristiano Ronaldo
```

He can move from:

```
Manchester United → Juventus → Al Nassr
```

The **player exists independently** of any team.

This is **Aggregation**.

```
Team ◇── Player
```

(The hollow diamond in UML represents aggregation.)

---

# Key Properties of Aggregation

A relationship is aggregation when **all these conditions hold**.

### 1️⃣ Whole–Part relationship exists

Example:

```
Team → Players
Department → Employees
Playlist → Songs
Library → Books
```

---

### 2️⃣ Parts can exist independently

If the whole object disappears, the parts still exist.

Example:

Delete playlist → songs still exist.

---

### 3️⃣ Parts may belong to multiple wholes

Example:

```
Song
 ├── Playlist A
 ├── Playlist B
 ├── Playlist C
```

This is common in aggregation.

---

# Example: Playlist System

Let’s design a **music playlist**.

Entities:

```
Playlist
Song
```

Relationship:

```
Playlist ◇── Song
```

Why aggregation?

Because:

```
Song exists in database independently
Song can appear in many playlists
Song exists even if playlist deleted
```

---

# PHP Example of Aggregation

```php
class Song
{
    private int $id;
    private string $title;

    public function __construct(int $id, string $title)
    {
        $this->id = $id;
        $this->title = $title;
    }
}
```

Playlist:

```php
class Playlist
{
    private array $songs = [];

    public function addSong(Song $song)
    {
        $this->songs[] = $song;
    }
}
```

Notice something important.

Playlist **does not create songs**.

Songs already exist.

This is a strong signal of **aggregation**.

---

# Aggregation vs Association

Many developers ask:

> “Isn’t this just association?”

Good question.

Technically aggregation **is a specialized form of association**.

But aggregation explicitly expresses **whole–part meaning**.

Compare these two:

### Association

```
Teacher → Student
```

Teacher uses student data.

But student is not a **part** of teacher.

---

### Aggregation

```
Department → Employees
```

Employees are **part of department structure**, but they exist independently.

---

# Aggregation vs Composition (VERY IMPORTANT)

This is where most developers fail interviews.

Aggregation:

```
Whole → Part
Part lives independently
```

Composition:

```
Whole → Part
Part cannot live independently
```

Example:

### Aggregation

```
Team → Player
```

Players survive team deletion.

---

### Composition

```
House → Room
```

If the house is destroyed, the rooms **cannot exist independently**.

Rooms depend on house.

---

# UML Representation

Aggregation uses **hollow diamond**.

```
Team ◇──── Player
```

Meaning:

```
Team has Players
Players exist independently
```

Composition uses **filled diamond**.

```
House ◆──── Room
```

Meaning:

```
Rooms belong exclusively to house
Rooms die with house
```

We will study composition in the next topic.

---

# Real Production Example

Let’s analyze a **company structure**.

Entities:

```
Company
Department
Employee
```

Relationships:

```
Company ◇── Department
Department ◇── Employee
```

Why aggregation?

Because:

Employees exist even if department changes.

Example:

```
Engineering → Product → Platform
```

Employee moves between departments.

They do not die with the department.

---

# Important Engineering Insight

Aggregation is mostly used when objects are:

```
Reusable
Shared
Independent
```

Examples:

```
Playlist → Song
Course → Student
Team → Player
Department → Employee
Library → Book
```

---

# Common Mistake Developers Make

Bad design:

```php
class Team
{
    private array $players;

    public function __construct()
    {
        $this->players[] = new Player();
    }
}
```

This looks innocent.

But now **team is creating players**.

This starts to look like **composition**, not aggregation.

Aggregation means:

> The whole does not control creation or destruction of parts.

Parts come from outside.

Correct design:

```php
$team = new Team();

$player1 = new Player("Ronaldo");
$player2 = new Player("Messi");

$team->addPlayer($player1);
$team->addPlayer($player2);
```

Now the relationship is **aggregation**.

---

# Aggregation in Backend Systems

You will see aggregation often in systems like:

### E-commerce

```
Category ◇── Products
Cart ◇── Products
```

Products exist independently.

---

### Education platforms

```
Course ◇── Students
Course ◇── Lessons
```

Lessons may exist independently in CMS.

---

### Project management

```
Project ◇── Developers
Project ◇── Tasks
```

Developers can move to other projects.

---

# Hidden Complexity in Aggregation

Aggregation can introduce **shared mutable state problems**.

Example:

```
Song used in 100 playlists
```

If one playlist modifies the song:

```
Title changed
```

All playlists see the change.

Sometimes this is desired.

Sometimes it's dangerous.

Principal engineers are careful with **shared objects**.

---

# Quick Mental Test

If you are unsure whether something is aggregation, ask:

### Question 1

Can the part exist without the whole?

### Question 2

Can the part belong to multiple wholes?

### Question 3

Does the whole NOT control lifecycle?

If yes → **Aggregation**

---

# Small Exercise (Important)

Identify which of these are **Aggregation**.

1️⃣ **University → Professors**

2️⃣ **Car → Engine**

3️⃣ **Order → OrderItem**

4️⃣ **BlogPost → Comments**

5️⃣ **Library → Books**

For each, answer:

```
Aggregation
Composition
Association
```

---

---
Your Sample Answer:
```
1️⃣ **University → Professors**
aggrigation

2️⃣ **Car → Engine**
composition

3️⃣ **Order → OrderItem**
association

4️⃣ **BlogPost → Comments**
composition

5️⃣ **Library → Books**
aggrigation
```
---

Good attempt. You’re thinking in terms of lifecycle—that’s exactly what matters.
Now let’s refine this to **principal engineer level precision**.

I’ll review each one, but more importantly I’ll show you **how to reason**, not just the answer.

---

# 1️⃣ University → Professors

You said: **Aggregation ✅**

Correct.

### Why?

* Professors exist independently of a university
* They can move:

```
MIT → Stanford → IIT
```

* University does NOT control their lifecycle

So:

```
University ◇── Professor
```

✔️ This is clean aggregation.

---

# 2️⃣ Car → Engine

You said: **Composition ✅**

Correct.

### Why?

* Engine is tightly bound to the car
* If car is destroyed, engine typically loses meaning (in system design terms)
* Engine is not shared across multiple cars in normal modeling

```
Car ◆── Engine
```

✔️ Strong lifecycle dependency → Composition

---

# 3️⃣ Order → OrderItem

You said: **Association ❌ (This is wrong, and very important)**

Correct answer: **Composition**

This is a **classic interview trap**.

---

### Think deeply:

Does `OrderItem` exist without `Order`?

Example:

```
OrderItem:
- productId
- quantity
- price
```

Without order, this data is meaningless.

You never have:

```
"OrderItem floating independently in system"
```

Also:

* Order creates OrderItems
* Order deletes OrderItems
* Order fully owns them

So:

```
Order ◆── OrderItem
```

✔️ This is **Composition**, not association

---

### Why this matters in real systems

Bad design (association mindset):

```php
class OrderItem
{
    private int $orderId;
}
```

Good design (composition mindset):

```php
class Order
{
    private array $items;
}
```

Order controls lifecycle.

This impacts:

* data integrity
* business rules
* transaction boundaries

---

# 4️⃣ BlogPost → Comments

You said: **Composition ✅ (Mostly correct, but let's refine)**

This one is **context-dependent**, and this is where engineers level up.

---

### Case A: Simple system

* Comments belong to blog post
* Delete post → delete comments

```
BlogPost ◆── Comments
```

✔️ Composition

---

### Case B: Advanced system (like Reddit, Facebook)

Comments may:

* have independent moderation
* be stored separately
* survive post deletion (soft delete)

Then:

```
BlogPost ◇── Comments
```

✔️ Aggregation

---

### Principal Engineer Insight

> **There is no single correct answer without context.**

In interviews:

👉 Always clarify:

> “Should comments exist independently if the post is deleted?”

That’s how seniors stand out.

---

# 5️⃣ Library → Books

You said: **Aggregation ✅**

Correct.

### Why?

* Books exist independently of library
* Same book can exist in multiple libraries
* Library does not create books

```
Library ◇── Book
```

✔️ Aggregation

---

# Final Correct Answers

```
1. University → Professors   → Aggregation ✅
2. Car → Engine             → Composition ✅
3. Order → OrderItem        → Composition ❗
4. BlogPost → Comments      → Depends (Composition / Aggregation)
5. Library → Books          → Aggregation ✅
```

---

# What You Just Learned (Very Important)

You just crossed an important level.

You now understand:

### 1️⃣ Lifecycle defines relationship

Not just “has-a”

---

### 2️⃣ Context matters

Same relationship can change:

```
Blog → Comments
```

based on system requirements.

---

### 3️⃣ Composition is stronger than aggregation

```
Association < Aggregation < Composition
```

Increasing strength of relationship.

---
