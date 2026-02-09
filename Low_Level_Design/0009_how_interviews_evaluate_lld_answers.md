## **How Interviewers Evaluate LLD Answers (The Hidden Rubric)**

> Interviewers rarely tell you how they score.
> But they all use **almost the same mental checklist**.

Let’s open it up.

---

## 1️⃣ The Truth About LLD Evaluation

Interviewers are NOT asking:

* “Is this the best design in the world?”

They ARE asking:

* “Would I trust this person to design code in my team?”

That’s the bar.

---

## 2️⃣ The 6 Core Evaluation Dimensions

Every LLD interview is scored roughly on these:

1. Problem Understanding
2. Requirement Clarification
3. Responsibility Assignment
4. Design Quality
5. Extensibility & Change Handling
6. Communication & Trade-offs

Let’s break each **like a senior reviewer**.

---

## 3️⃣ Dimension 1: Problem Understanding (First 5 Minutes)

### What They Observe

* Do you rush to code?
* Do you restate the problem?
* Do you clarify scope?

### ❌ Weak Signal

> “Okay, I’ll start coding.”

### ✅ Strong Signal

> “Let me confirm the core requirements first.”

💡 **Rule**

> If you misunderstand the problem, nothing else matters.

---

## 4️⃣ Dimension 2: Requirement Clarification

### What They Want

* Functional requirements
* Non-functional expectations
* Explicit assumptions

### ❌ Weak Candidate

* Assumes too much
* Builds imaginary features

### ✅ Strong Candidate

* Asks 3–5 smart questions
* States assumptions clearly

Example:

> “Should we support multiple payment methods now, or design for future extension?”

---

## 5️⃣ Dimension 3: Responsibility Assignment (CORE LLD SKILL)

### What They Check

* Does each class have one job?
* Are responsibilities logically placed?

### ❌ Red Flag

* One God class
* Utility classes everywhere

### ✅ Green Flag

* Clear, cohesive classes
* Meaningful names

Interviewers love hearing:

> “This responsibility belongs here because…”

---

## 6️⃣ Dimension 4: Design Quality

### Key Signals

* Low coupling
* High cohesion
* Clean abstractions
* Minimal but sufficient patterns

### ❌ Bad Design Signals

* Deep inheritance
* Overuse of patterns
* Tight coupling

### ✅ Good Design Signals

* Interfaces where change happens
* Composition over inheritance
* Simple flows

---

## 7️⃣ Dimension 5: Extensibility & Change Handling

### The Favorite Interview Question

> “What if we add X tomorrow?”

They want to see:

* Can you evolve the design?
* Do you panic or adapt?

### ❌ Weak Answer

> “We’ll rewrite this part.”

### ✅ Strong Answer

> “We can add a new implementation without touching existing code.”

This is where SOLID shines.

---

## 8️⃣ Dimension 6: Communication & Trade-offs

### What Separates Seniors

They **explain why**, not just what.

### Weak Candidate

> “This is better.”

### Strong Candidate

> “This adds one extra class, but it reduces change risk.”

💡 Interviewers score **how you think aloud**.

---

## 9️⃣ The Unofficial Scoring Table

| Skill              | Weight |
| ------------------ | ------ |
| Thinking clarity   | ⭐⭐⭐⭐   |
| Design cleanliness | ⭐⭐⭐⭐   |
| Extensibility      | ⭐⭐⭐    |
| Code correctness   | ⭐⭐     |
| Pattern knowledge  | ⭐      |

Patterns matter **least**.

---

## 🔟 Why Many “Correct” Answers Fail

Common failure reasons:

* Over-engineering
* No explanation
* Poor naming
* Ignoring change scenarios
* Silent coding

A correct design **badly explained** still fails.

---

## 1️⃣1️⃣ How to Score Extra Points (Insider Tips)

Say things like:

* “I’ll keep this simple for now.”
* “If requirements grow, we can refactor here.”
* “This abstraction isolates the change.”

These sentences signal experience.

---

## 1️⃣2️⃣ PRACTICE (DO THIS)

### 🧪 Exercise 1

Given:

> “Design a logging system.”

Answer verbally:

1. What clarifying questions will you ask?
2. What’s the first class you’ll design?
3. What change do you anticipate?

---

### 🧪 Exercise 2

You finish your design. Interviewer asks:

> “Why not use inheritance here?”

Write your answer.

---

## 🔚 PHASE 1 COMPLETE 🎯

You now know:

* What LLD is
* How it differs from HLD
* Interview formats
* How answers are evaluated

You are **ahead of 70% candidates already**.

---
