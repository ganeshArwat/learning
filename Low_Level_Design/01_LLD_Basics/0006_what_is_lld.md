
## **What Is Low-Level Design (LLD)?**

> **LLD is the art of converting requirements into clean, extensible classes and interactions.**

Not diagrams.
Not patterns.
Not frameworks.

**Classes. Responsibilities. Relationships. Behavior.**

---

## 1️⃣ What LLD Is (Real Meaning)

Low-Level Design answers **these exact questions**:

* What classes exist?
* What does each class do?
* How do classes talk to each other?
* How is behavior distributed?
* Where will change happen?

If you can answer those → you’ve done LLD.

---

## 2️⃣ What LLD Is NOT (Common Confusion)

### ❌ Not UI design

### ❌ Not database schema

### ❌ Not infrastructure

### ❌ Not REST API design

### ❌ Not HLD

LLD lives **inside the codebase**.

---

## 3️⃣ Where LLD Sits in Real Systems

Think in layers:

```
Business Problem
   ↓
High Level Design (HLD)
   ↓
Low Level Design (LLD)
   ↓
Code
```

* HLD = **big boxes**
* LLD = **classes inside boxes**

---

## 4️⃣ LLD vs Coding (Critical Distinction)

### ❌ Coding

> “I’ll start writing code and see what happens.”

### ✅ LLD

> “Let me decide responsibilities before writing code.”

A senior can **delay coding** and still make progress by designing.

---

## 5️⃣ What Interviewers ACTUALLY Look For

They are not checking:

* Syntax
* Framework knowledge

They are checking:

* How you break a problem
* How you assign responsibilities
* How you handle change
* How clean your abstractions are

---

## 6️⃣ A Real Example (No Theory)

### Problem

> “Design a notification system that supports Email and SMS.”

---

### ❌ No LLD (Bad Approach)

```php
function notify($type, $msg) {
    if ($type === 'email') {}
    elseif ($type === 'sms') {}
}
```

This is **coding**, not LLD.

---

### ✅ LLD Thinking (Before Code)

Ask:

* What varies? → Notification type
* What stays same? → Sending notification
* Who owns responsibility?

---

### LLD Output (Design First)

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

---

## 7️⃣ LLD Is About **Responsibility Assignment**

Golden question:

> “Who should do this?”

Bad LLD:

* One class does everything

Good LLD:

* Responsibilities are distributed logically

---

## 8️⃣ What Makes a GOOD LLD Answer in Interviews

### ✅ Clear class responsibilities

### ✅ Low coupling

### ✅ High cohesion

### ✅ Easy to extend

### ✅ Simple to explain

If interviewer says:

> “Can we add WhatsApp notifications?”

And you say:

> “Yes, by adding a new class”

You’re winning.

---

## 9️⃣ Typical LLD Interview Flow

1. Clarify requirements
2. Identify entities
3. Define responsibilities
4. Decide relationships
5. Apply patterns (if needed)
6. Write code / pseudocode

Skipping steps = bad impression.

---

## 🔟 The Senior Engineer’s LLD Mental Model

Before writing code, ask:

* What are the core entities?
* What will change most often?
* How can I isolate that change?
* What is the simplest design that works?

---

## 1️⃣1️⃣ PRACTICE (DO THIS)

### 🧪 Exercise 1

Design (on paper or text):

> A system to send alerts via Email and Push Notification.

Answer:

* Classes
* Responsibilities
* Relationships

(No code yet.)

---

### 🧪 Exercise 2

Given this requirement:

> “Support more notification channels in future”

Question:

* Where will change happen?
* Which class should be open for extension?

---

## 🔚 Key Takeaway (WRITE THIS)

> **LLD is not about writing code faster.
> It’s about changing code safely.**

---
