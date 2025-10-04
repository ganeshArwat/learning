# 🎯 Design Interviews

### Example: *Google Typeahead / Autocomplete System*

---

### 💡 Nature of the Problem

* The **problem statement** in system design interviews is usually **extremely vague**.

  > e.g., “Design Typeahead” or “Design Twitter Feed”
* You might **not even know what the feature exactly is** — that’s expected.
* The interviewer wants to see **how you reason**, not just what you know.

---

### 🧭 Interview Dynamics

* **Open-ended discussion** — can go in *any direction*, depending on:

  * Your **expertise**
  * The **interviewer’s background**
* The **goal is not a perfect solution**, but a structured thought process.

---

### ⏱️ Time Constraints

* Typical duration: **45 minutes**

  * ~20–25 min → Requirements & estimation
  * ~20–25 min → System design & discussion

---

### ✅ What You Must Do

1. **Clarify the problem statement**

   * What exactly are you supposed to build?
   * What does the system do? Who uses it?
2. **Align with the interviewer**

   * Ask clarifying questions: “Are we focusing on scale or correctness?”
3. **Define the scope**

   * Choose what *not* to build (auth, payments, etc.)
4. **Design a solid solution**

   * Focus on tradeoffs, constraints, and real-world feasibility.
5. **Showcase your depth**

   * Pick **sufficiently complex components** to display your skill.
   * Don’t just make it simple — make it *thoughtful*.

---

### 🧩 Common Interviewer Expectations

* Can you handle **ambiguity**?
* Can you **break down** a big system into smaller pieces?
* Can you **estimate scale** realistically?
* Can you **justify** your design choices?
* Do you understand **tradeoffs** (consistency, latency, cost, complexity)?

---

# 🪜 The 5-Step Design Approach

---

### ⏱️ Recommended Timing

| Step | Description                 | Suggested Time |
| ---- | --------------------------- | -------------- |
| 1    | Problem Statement           | 3–5 mins       |
| 2    | Functional Requirements     | 5–7 mins       |
| 3    | Non-Functional Requirements | 3–4 mins       |
| 4    | Scale Estimation            | 5–7 mins       |
| 5    | System Design               | 20–25 mins     |

---

## 🧩 Step 1: Problem Statement

---

### 🎯 Objective

The first step in any system design interview is to **define the problem clearly** — because the question will almost always be vague.

Your goal is to:

* Understand **what exactly** you’re building
* Define **what’s in scope** and **what’s not**
* Align with the interviewer before you dive into design

---

### 🕵️ What to Do

* Identify **existing companies / systems / apps** that provide a **similar product or feature**

  > Example: “Design Typeahead” → Similar to Google Search Autocomplete or Twitter Search
* Ask clarifying questions like:

  * “Are we designing for web, mobile, or both?”
  * “Do we focus on user experience or scalability?”
  * “Should we assume the data already exists?”
* Clearly state **what not to build** — this saves you from wasting time on irrelevant areas.

  > Example: “We’ll assume authentication and payment systems already exist.”

---

### 💬 Example

> “We are designing a **Typeahead suggestion system** that provides **real-time search suggestions** as the user types.
> We will not design authentication, ranking algorithms, or ad systems — these are out of scope.”

---

## ⚙️ Step 2: Functional Requirements

---

### 🧠 Definition

**Functional requirements** describe *what functionality* the system must provide to its users (or “actors”).

They define **what the system does**, not how it does it.

---

### 🚫 Avoid Feature Frenzy

> Don’t try to list every possible feature — you’re designing an MVP, not a full product.

Focus on:

* Core functionalities that affect backend architecture
* Things that demonstrate your **design and reasoning skills**

> “If you can’t dazzle them with your brilliance, baffle them with your structured bullshit.”

---

### 👥 Actors

Identify who interacts with your system — e.g.:

* **User / Client App**
* **Backend Service**
* **Database / Cache**
* **External APIs** (if relevant)

This helps define boundaries and interactions early.

---

### ⚙️ Minimal Viable Product (MVP)

Keep the “minimal” in mind — an MVP is the **smallest useful version** of your system.

> ✅ Each feature should be written as a **complete sentence from the user’s perspective**.
> Example:
>
> * “As a user, I should see 5 most relevant suggestions as I type.”
> * “As a system, I should cache frequently used prefixes for faster response.”

---

### 🚫 What to Avoid

1. **Anything that doesn’t affect backend infrastructure**

   * Example: UI color themes, button animations
2. **Frontend-only features**

   * Purely cosmetic, not system-level
3. **Common dependencies** (not the core system)

   * Example: In *Design Uber*

     * Authentication exists, but you’re not designing auth.
     * Payments exist, but you’re not designing payment infra.
     * Focus on *ride-matching*, not login or billing.
4. **Incomplete features**

   * Always describe features as a **clear sentence** that implies both intent and function.

---

### 🕵️ Hidden (Implicit) Functionalities

Some features are not user-facing but are crucial for backend design.

#### Example: APIs

When discussing APIs:

* You don’t need to specify protocols (HTTP, RPC, WebSocket)
* But you **must specify input and output**

  * What goes *in*
  * What comes *out*

> Example:
> `typeahead(partialQuery)` → Returns top N suggestions

---

✅ **Summary**

| Concept                 | Key Idea                                       |
| ----------------------- | ---------------------------------------------- |
| Problem Statement       | Define what & what not to build                |
| MVP Focus               | Keep it minimal and core                       |
| Functional Requirements | Describe system behavior in complete sentences |
| Hidden Features         | Always specify API I/O, not protocol           |
| Avoid                   | Cosmetic, dependent, or non-core features      |

---

## ⚙️ Non-Functional Requirements (NFRs)

Non-functional requirements define the **“quality attributes”** of a system — how it behaves rather than what it does.
They ensure **reliability, scalability, performance, and consistency** of your design.

---

### 🧭 Key Non-Functional Concerns

| Concern          | Description                                               | Example                         |
| ---------------- | --------------------------------------------------------- | ------------------------------- |
| **Availability** | System remains operational even when some components fail | 99.9% uptime SLA                |
| **Consistency**  | All users see the same data at the same time              | Banking systems, transactions   |
| **Latency**      | Time taken to respond to a user’s request                 | <200 ms for search autocomplete |
| **Scalability**  | Ability to handle increased load (users, data, traffic)   | Horizontal scaling, sharding    |
| **Reliability**  | System continues to function correctly over time          | Fault-tolerant design           |
| **Durability**   | Data persists even after failures                         | Write-ahead logs, replication   |
| **Throughput**   | Number of requests handled per second                     | 10 K req/s                      |

---

### ⚖️ PACELC Theorem

The **PACELC theorem** extends the **CAP theorem** — it adds latency trade-offs that occur *even without network partitions*.

| Scenario                        | Trade-off                                                   | Explanation                                             |
| ------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| **When a Partition occurs (P)** | Choose between **Availability (A)** and **Consistency (C)** | CAP theorem — you can’t have both                       |
| **Else (no Partition)**         | Choose between **Latency (L)** and **Consistency (C)**      | Even in normal operation, strong consistency adds delay |

#### 🧠 Summary

> **PACELC = “If Partition (P), choose A or C; Else, choose L or C.”**

Examples:

* **Cassandra:** PA/EL — prioritizes *Availability* and *Low Latency* (eventual consistency)
* **Spanner:** PC/EC — prioritizes *Consistency* even if it increases latency

---

## 📏 Scale Estimation

Before designing your system, **estimate the scale** — so your architecture decisions are realistic.

These are **derived** numbers, not guesses.

---

### 🔹 Step 1: Understand Large Number Units (Short Scale)

| Name             | Numerical Value   | Power of 10 | Indian Equivalent |
| ---------------- | ----------------- | ----------- | ----------------- |
| **Thousand (K)** | 1,000             | 10³         | 1 Thousand        |
| **Million (M)**  | 1,000,000         | 10⁶         | 10 Lakh           |
| **Billion (B)**  | 1,000,000,000     | 10⁹         | 100 Crore         |
| **Trillion (T)** | 1,000,000,000,000 | 10¹²        | 1 Lakh Crore      |

> 💡 1 B = 100 Crore
> 💡 1 M = 10 Lakh

---

### 🔹 Step 2: Define Basic Population / Usage Assumptions

| Metric                       | Approx. Value                       | Notes                |
| ---------------------------- | ----------------------------------- | -------------------- |
| **World population**         | ~8 B                                | 2025 estimate        |
| **Internet users**           | ~5 B                                | 60% of world         |
| **India’s population**       | ~1.4 B                              | 700 M internet users |
| **USA’s population**         | ~350 M                              | 300 M internet users |
| **Daily Active Users (DAU)** | ≈ 20% of Monthly Active Users (MAU) | Standard ratio       |

---

### 🔹 Step 3: Load Estimation

#### 1️⃣ Amount of Load

To estimate:

* **Monthly Active Users (MAU):** From target market
* **Daily Active Users (DAU):** = 20 % × MAU
* **Requests per second (RPS):**
  [
  RPS = \frac{\text{DAU} \times \text{Avg Requests per User per Day}}{86400}
  ]

✅ Example:
If DAU = 10 M and each user makes 20 requests/day
→ RPS = (10 M × 20)/86400 ≈ 2314 req/s

---

#### 2️⃣ Peak Load

* **Peak ≈ 2–5 × average**
* Always design for **peak traffic** (e.g. promotions, new-year events)

---

#### 3️⃣ Amount of Data

Estimate using:
[
\text{Total Data} = \text{Number of Records} \times \text{Average Record Size}
]

* Include metadata, indexes, replication factor.
* Helps decide if **sharding** or **compression** is needed.

---

#### 4️⃣ Read-Heavy vs Write-Heavy Workloads

| Type                        | Description                  | Typical Strategy                                                                                                                                |
| --------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Read-Heavy**              | e.g. Feed, Search, Analytics | Add **Cache** (Redis, CDN), pre-compute                                                                                                         |
| **Write-Heavy**             | e.g. Logging, IoT, Chat      | Use **Batching**, **Queueing**, **Eventual Consistency**                                                                                        |
| **Both Read & Write Heavy** | Complex workloads            | Options: <br>① Cache reads (convert to write-heavy) <br>② Reduce writes (batching, sampling) <br>③ Shard massively (but beware fan-out latency) |

---

✅ **Final Rule of Thumb**

| Component               | Typical Range | Notes                     |
| ----------------------- | ------------- | ------------------------- |
| **Latency (good UX)**   | < 200 ms      | < 100 ms for autocomplete |
| **Cache hit ratio**     | > 80 %        | Higher = fewer DB reads   |
| **Replication factor**  | 3             | Standard for HA           |
| **Peak/Avg Load Ratio** | 3–5×          | Design buffer             |

---

## 🧱 Typical Components in System Design

When designing any scalable system, you’ll typically deal with these core components.
Each component should be **introduced, justified, and configured** based on the **functional + non-functional requirements**.

---

### ⚙️ 1. Microservices Architecture

* Break the application into **independent services**, each responsible for a **specific domain**.
* Enables **scalability, maintainability, and fault isolation**.

| Pros                       | Cons                                |
| -------------------------- | ----------------------------------- |
| Easier scaling per service | Complex deployment & orchestration  |
| Clear service boundaries   | Requires service discovery          |
| Tech stack flexibility     | More network overhead               |
| Fault isolation            | Harder debugging (distributed logs) |

> 💡 Usually, start with a monolith → refactor into microservices once scaling demands justify it.

---

### 🌐 2. Load Balancer

Distributes incoming traffic across multiple servers to:

* Prevent overload on a single node
* Improve availability and response time

| Type                 | Description                                               |
| -------------------- | --------------------------------------------------------- |
| **L4 Load Balancer** | Works at TCP/UDP level — faster, less control             |
| **L7 Load Balancer** | Works at HTTP level — can route by path, cookies, headers |

> Examples: **Nginx**, **HAProxy**, **AWS ELB**, **Cloudflare Load Balancer**

---

### 🗄️ 3. Database Choice

#### **SQL (Relational)**

* Follows **ACID** principles
* Enforces **schema and relationships**
* Suitable for **strong consistency** and **structured data**

> Examples: **PostgreSQL**, **MySQL**, **Aurora**

#### **NoSQL (Non-relational)**

* Follows **BASE** principles (Basically Available, Soft state, Eventually consistent)
* Schema-less, horizontally scalable
* Best for **high volume / flexible data models**

| Type            | Example            | Use Case                         |
| --------------- | ------------------ | -------------------------------- |
| **Key-Value**   | Redis, DynamoDB    | Caching, session stores          |
| **Document**    | MongoDB, Couchbase | User profiles, catalogs          |
| **Wide-Column** | Cassandra, HBase   | Logging, IoT, analytics          |
| **Graph**       | Neo4j              | Social networks, recommendations |

> 💬 **Justify your DB choice**:
>
> * SQL → strong consistency, joins, transactions
> * NoSQL → scalability, flexible schema, denormalized queries

---

### ⚡ 4. Cache Choice

#### **Why Caching?**

* Reduces **latency** by storing precomputed or frequently accessed data.
* Reduces **DB load** and **improves throughput**.

#### **Types of Cache**

| Type             | Scope                | Description             | Example                          |
| ---------------- | -------------------- | ----------------------- | -------------------------------- |
| **Local Cache**  | Single server        | Fast, but not shared    | In-memory (e.g. LRU, in-process) |
| **Global Cache** | Shared among servers | Centralized, consistent | Redis, Memcached                 |

#### **If Global → Single vs Distributed**

| Type            | Description                           | Example                         |
| --------------- | ------------------------------------- | ------------------------------- |
| **Single Node** | Simple setup, but not fault-tolerant  | One Redis node                  |
| **Distributed** | Scalable, fault-tolerant, partitioned | Redis Cluster, Memcached shards |

---

#### **Cache Invalidation**

“How do you know when to remove or update stale data?”

| Strategy             | Description                     |
| -------------------- | ------------------------------- |
| **Time-based (TTL)** | Auto-expire after N seconds     |
| **Write-through**    | Update cache on write           |
| **Write-behind**     | Update DB asynchronously        |
| **Delete-on-write**  | Remove cache entry on DB update |

---

#### **Cache Eviction Policies**

When cache is full, remove entries based on:

| Policy                          | Description                      |
| ------------------------------- | -------------------------------- |
| **LRU (Least Recently Used)**   | Remove least recently accessed   |
| **LFU (Least Frequently Used)** | Remove least frequently accessed |
| **FIFO (First In, First Out)**  | Remove oldest                    |
| **Random**                      | Remove random entries (simpler)  |

> 💡 Default choice: **LRU** — widely supported and balanced for general workloads.

---

### 🔄 5. Communication

#### **User ↔ Backend**

* Usually over **HTTP/HTTPS** using **REST** or **GraphQL**
* Real-time systems may use **WebSockets**, **SSE**, or **gRPC**

| Method               | Use Case                                |
| -------------------- | --------------------------------------- |
| **HTTP REST**        | Standard APIs, CRUD ops                 |
| **WebSockets / SSE** | Real-time updates, chat, notifications  |
| **gRPC**             | High-performance internal communication |

#### **Backend ↔ Backend**

* **Synchronous:** RPC, REST, gRPC
* **Asynchronous:** Message queues (Kafka, RabbitMQ, SQS)

> 💡 Prefer **async messaging** for decoupled, resilient microservice communication.

---

### 🌎 6. CDN (Content Delivery Network)

* Distributes **static assets** (images, JS, CSS, videos) across edge locations globally.
* Reduces **latency** and **bandwidth costs**.

| Benefit                   | Example                            |
| ------------------------- | ---------------------------------- |
| Reduces latency           | Cloudflare, Akamai, AWS CloudFront |
| Handles spikes in traffic | Popular media / e-commerce         |
| Improves availability     | Caches at edge servers             |

> 💡 Rule of thumb: Always put **images, videos, scripts, CSS** behind a CDN.

---

### 🔍 7. Observability

Monitor, debug, and understand your system’s internal state through:

| Category     | Tool / Concept                              | Purpose                            |
| ------------ | ------------------------------------------- | ---------------------------------- |
| **Logging**  | ELK Stack (Elasticsearch, Logstash, Kibana) | Collect & visualize logs           |
| **Metrics**  | Prometheus, Grafana                         | Monitor CPU, memory, latency       |
| **Tracing**  | Jaeger, OpenTelemetry                       | Track request flow across services |
| **Alerting** | PagerDuty, Grafana Alerts                   | Detect anomalies, downtime         |

> 💡 Observability = **Logging + Metrics + Tracing**

---

✅ **Tip:**
In interviews, you don’t have to name every component — mention the ones **relevant to your design** and **justify** why you’re using them.

---


# Optimizing the System

Short, practical playbook for tuning systems depending on workload shape and constraints. Use this during interviews to show you can move from high-level trade-offs to concrete techniques.

---

## 1) If the system is **read-heavy**

* **If eventual consistency is acceptable**

  * **Absorb reads in cache** (Redis / Memcached / CDN).

    * Use TTLs and cache warming for hot keys.
  * **Optimize DB for writes**: denormalize data, use append-only stores, and avoid heavy read-side indexes.
  * **Patterns**: read-through cache, cache-aside, materialized views for expensive joins/aggregations.
* **If immediate (strong) consistency is required**

  * **Serve reads from DB** (or read-replicas with synchronous replication if needed).
  * **Optimize DB for reads**: add appropriate indexes, use columnar stores for analytics.
  * Expect **higher latency** than cache-first designs — call this out and justify.

**Quick examples**

* Autocomplete → read-heavy, eventual OK → cache prefixes + precomputed suggestion lists.
* Bank balance lookup → strong consistency → read from primary or strongly consistent store.

---

## 2) If the system is **write-heavy**

* Absorb reads in a **cache** to avoid read amplification.
* **Buffer / batch writes** via queues (Kafka, SQS) and apply to DB asynchronously when possible.
* Use **log-structured or append-optimized stores** (e.g., Cassandra, Kafka + materialized view) to handle high write throughput.
* Use **compaction** and background processing for index maintenance.
* Apply **rate limiting** and backpressure to protect downstream systems.

**Patterns**

* Write-behind cache (careful with durability)
* Batching + bulk inserts
* Idempotent writes (safe retries)

---

## 3) If the system is **both read & write heavy**

* This is difficult — pick trade-offs:

  1. **Reduce writes**

     * Batch writes → forces eventual consistency.
     * Sample or aggregate (lose some fidelity) where acceptable.
  2. **Absorb reads heavily in caches / materialized views**

     * Precompute commonly read results.
  3. **Scale horizontally (sharding)**

     * Partition data so reads/writes are localized.
     * Beware fan-out queries: they can become slow across many shards.
* **Consider CQRS (Command Query Responsibility Segregation)**:

  * Writes go to write model; reads served from optimized read model (eventually consistent).
* **Consider multi-tier caching + read-replicas**.

---

## 4) Sharding / Partitioning trade-offs

* **Horizontal sharding** reduces per-shard load but:

  * Makes cross-shard joins expensive.
  * Requires careful shard key selection (even distribution).
* Techniques:

  * Hash-based partitioning (uniform distribution)
  * Range-based partitioning (good for range scans)
  * Directory-based / lookup sharding (flexible but needs central mapping)
* **Rule of thumb:** avoid fan-out writes and fan-in reads across all shards.

---

## 5) Indexing & Denormalization

* **Denormalize** read-heavy data to reduce joins and latency (store pre-joined views).
* **Selective indexing**: indexes speed reads but slow writes and consume space.
* **Materialized views**: precompute expensive queries — refresh asynchronously or incrementally (CDC).

---

## 6) Caching best practices (quick)

* Cache the **right layer** (edge/CDN for static, Redis for fast hot keys).
* Use **consistent hashing** for distributed caches to reduce re-sharding cost.
* Choose proper **eviction** (LRU/LFU) and **invalidation** strategy (TTL, delete-on-write, write-through).
* Monitor **cache hit ratio** — >80% target for effective caches.

---

## 7) Asynchrony, Queues & Event-Driven Design

* Use message brokers to **decouple** producers from consumers.
* Benefits: smoothing spikes, retry/backoff, parallel processing.
* Downsides: complexity, eventual consistency, failure modes.
* Use **dead-letter queues**, idempotency tokens, and monitoring.

---

## 8) Observability & Feedback loops

* Instrument latency, error rates, queue depths, cache hits, and DB metrics.
* Use tracing (OpenTelemetry/Jaeger) to find hotspots (fan-outs, long tails).
* Tune based on real telemetry — don’t guess.

---

## 9) Safety & Resilience

* Add **circuit breakers**, **rate limiters**, **bulkheads** to protect services.
* Auto-scale cautiously — ensure warm-up, avoid cascading scaling storms.
* Plan for graceful degradation: if under heavy load, return stale but available data.

---

## 10) Quick interview checklist (say this out loud)

1. Identify workload: read-heavy / write-heavy / both.
2. State consistency requirement (eventual vs strong).
3. Pick 2–3 main optimizations (cache, batching, sharding, CQRS).
4. Mention trade-offs (latency vs consistency, complexity vs throughput).
5. Describe monitoring and rollback / safety controls.

---
