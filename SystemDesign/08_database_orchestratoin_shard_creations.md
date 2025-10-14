# Data Base Orchestration and Shard Creation

### 🔹 **1. What “Orchestration” Means**

In general, **orchestration** means automating and managing multiple complex operations so that they work together smoothly — like conducting an orchestra.

In databases, this means managing **many database instances, replicas, and services** automatically, ensuring they:

* Run in sync
* Stay healthy
* Scale as needed
* Recover from failures
* Handle schema or version changes with minimal downtime

---

### 🔹 **2. Key Components of Database Orchestration**

| Component                    | Description                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| **Provisioning**             | Automatically creating and initializing new database instances.                    |
| **Configuration Management** | Applying consistent configuration (e.g., user roles, ports, replication settings). |
| **Scaling**                  | Increasing or decreasing database nodes depending on load.                         |
| **Replication & Sharding**   | Managing replicas and splitting data for horizontal scaling.                       |
| **Failover Handling**        | Automatically promoting replicas to primary if a failure occurs.                   |
| **Backups & Recovery**       | Scheduling backups and restoring them when needed.                                 |
| **Monitoring & Alerting**    | Tracking performance, latency, and resource usage.                                 |

---

### 🔹 **3. Examples of Database Orchestration Tools**

| Tool                           | Description                                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------------------- |
| **Kubernetes Operators**       | Automate DB lifecycle in Kubernetes (e.g., MySQL Operator, MongoDB Operator, PostgreSQL Operator). |
| **Vitess**                     | A database clustering system for scaling MySQL horizontally (used by YouTube).                     |
| **Crunchy Data Operator**      | PostgreSQL operator for automated deployment, scaling, and backup.                                 |
| **AWS RDS / Aurora**           | Cloud-managed services that perform orchestration under the hood.                                  |
| **Google Cloud SQL / AlloyDB** | Cloud-managed databases with orchestration features.                                               |

---

### 🔹 **4. Why It Matters**

Database orchestration helps achieve:

* ✅ **High availability**
* ⚡ **Auto-scaling**
* 🔄 **Self-healing clusters**
* 🧩 **Consistent deployments**
* 📦 **Infrastructure as Code (IaC) integration**

It’s especially important in **microservices** and **cloud-native** systems, where multiple apps and databases need to coordinate efficiently.

---

### 🔹 **5. Example Scenario**

Imagine you’re running a PostgreSQL cluster in Kubernetes:

* A **PostgreSQL Operator** automatically deploys 1 primary and 2 replicas.
* If the primary fails, the operator promotes a replica automatically.
* Backups are scheduled daily.
* Scaling rules add more replicas during peak load.
  👉 All of this happens automatically — that’s **database orchestration**.

---

# 🧭 Consistent Hashing and Database Orchestration

---

## ⚙️ Consistent Hashing (under different settings)

The routing algorithm (**consistent hashing**) determines the **sharding**.
Data is created on the go — if all of Swetha's requests go to **Server C**, then her data will automatically be in **Server C**.

---

### 🔹 Sharding (without Replication)

Each server gets **different data** – there’s **no overlap** of data across different servers.

In general:

| Term       | Meaning                                                       |
| ---------- | ------------------------------------------------------------- |
| **Shard**  | A piece or partition of the overall data.                     |
| **Server** | A physical or virtual machine that stores one or more shards. |

* Sometimes, **1 server contains multiple shards**.
* Sometimes, **1 server = 1 shard**.
* But **a single shard is never split** across multiple servers (it can only be *replicated*).

---

### ❓ Shard vs Server (in the case of Sharding without Replication)

* Every server contains a **different shard**.
* Therefore, **1 Server = 1 Shard**.
* Each server has a **unique set of data** (no duplication).

---

### ❓ What gets placed on the ring?

* **Servers (== shards)** get placed on the **consistent hashing ring**.

---

### ❓ Can a "shard" go down?

Yes.
A shard (which equals one server in this setting) can go down.
In that case, the users who were originally routed to that shard will now be **routed automatically to the next server on the ring**.

However — note that while routing may continue, the **data that was stored on the failed shard** is **lost** (since there’s no replication).

---

### ❓ How does the data reach the next server in the ring?

When a server fails:

* The consistent hashing algorithm **re-maps the key range** that the failed shard was responsible for.
* The **next server clockwise on the ring** temporarily becomes responsible for that key range.
* **New data** for those users will now be written to this new server.
* **Old data** (if any) may be lost, since there’s no replication in this model.

---

## ⚙️ Sharding + Master-Slave Replication

### ❓ Shard vs Server

* **1 Shard = X Servers**, where **X = replication factor**.
* Each shard is made up of **multiple servers** in a **master-slave** (or leader-follower) configuration.
* All servers in the same shard contain **the same data** (due to replication).

---

### ❓ What gets placed on the ring?

* **Shards** (not individual servers) are placed on the **consistent hashing ring**.
* Each shard is a *logical unit* consisting of one master and multiple replicas.

---

### ❓ Can a "shard" go down?

* **No**, an entire shard going down is **highly unlikely**.
* Because a shard consists of multiple servers — for a shard to fail, **all servers** in that shard must fail simultaneously.

---

### ❓ What happens when a server crashes?

**No worries!**
The shard as a whole continues to function.

* If the **master** within a shard crashes → the **slaves elect a new master**.
* If a **slave** crashes → other slaves still hold replicas, so reads can continue.
* The system remains **available and consistent** (depending on replication policy).

---

## 🧩 Database Orchestration

Database orchestration is the process of **coordinating multiple database servers** (each with shards and replicas) to behave like **a single, self-managing system**.

It handles:

* Configuration management
* Replication
* Health checks
* Failover
* Recovery
* Scaling

---

### 🔹 Replication Factor (X)

The **replication factor (RF)** is the **minimum number of copies** maintained for any piece of data.

Example:
If **RF = 4**, then every shard’s data is replicated across **4 servers** (1 master + 3 slaves).

This ensures:

* **Fault tolerance**
* **High availability**
* **Data durability**

---

### 🔹 Configuration Management

When multiple servers work together as a distributed database, they must **share a common configuration** to remain in sync.

This configuration includes:

| Configuration Element   | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| **Server Availability** | Which servers are alive (via heartbeat or health checks). |
| **Shard Mapping**       | What shards exist, and which servers host each shard.     |
| **Replication Roles**   | Who is the master, who are the slaves.                    |
| **Replication Factor**  | How many replicas exist per shard.                        |
| **System Settings**     | SQL dialect, credentials, connection info, etc.           |

---

### 🔹 Distributed Configuration Management System

To ensure **consistency across servers**, a **distributed configuration management system** is used.
This ensures all nodes always **agree** on the state of the system.

#### Responsibilities:

1. Maintain the current configuration (server list, shard map, replication roles).
2. Detect failures and trigger recovery mechanisms (e.g., elect new master).
3. Propagate updates atomically across all nodes.
4. Enable coordination between shards.

#### Common Tools:

* 🐘 **Apache ZooKeeper**
* 🧩 **etcd**
* 🧭 **Consul**

---

### 🔹 Why ZooKeeper?

Apache ZooKeeper is a **centralized service for distributed coordination**.

In the context of databases:

* It stores **cluster metadata**.
* Maintains **heartbeats** to detect server failures.
* Manages **leader election**.
* Helps clients discover which server (or shard) to contact.

---

### 🔹 How It All Fits Together

Here’s what happens in a **sharded + replicated + orchestrated** database setup:

1. **Consistent Hashing** decides **which shard** stores each data key.
2. Each **shard** has **X servers** (replicas).
3. A **master** handles writes; **slaves** replicate from it.
4. **ZooKeeper (or etcd)** maintains cluster configuration:

   * Which shards exist
   * Which servers are in each shard
   * Who’s the current master
5. If a master dies → **ZooKeeper triggers leader election**.
6. If a new server is added → **ZooKeeper updates mappings** and rebalances shards.

---

### 🔹 Real-World Examples

| System               | Coordination Tool | Notes                                          |
| -------------------- | ----------------- | ---------------------------------------------- |
| **HBase**            | Apache ZooKeeper  | Tracks region servers and masters.             |
| **Kafka**            | ZooKeeper / KRaft | Tracks brokers, topics, and leader partitions. |
| **Cassandra**        | Gossip protocol   | Peer-to-peer coordination without ZooKeeper.   |
| **Vitess (YouTube)** | etcd              | Orchestrates MySQL clusters at scale.          |
| **MongoDB**          | Config servers    | Manage shard metadata and replica sets.        |

---

### 🧩 Visualization

```
        ┌────────────────────────────────────────────┐
        │   Distributed Config Store (ZooKeeper)     │
        │ Maintains shard map, roles, health, etc.   │
        └───────────────────┬────────────────────────┘
                            │
     ┌──────────────────────┼──────────────────────┐
     │                      │                      │
┌────────────┐        ┌────────────┐        ┌────────────┐
│  Shard A   │        │  Shard B   │        │  Shard C   │
│ (1 master  │        │ (1 master  │        │ (1 master  │
│ + replicas)│        │ + replicas)│        │ + replicas)│
└────────────┘        └────────────┘        └────────────┘
```

All shards work independently, but ZooKeeper (or etcd) ensures they stay in sync and self-heal when something fails.

---

### 🔹 Benefits of Database Orchestration

✅ **High Availability** – Automatic failover via replication
⚡ **Scalability** – New shards/servers can join dynamically
🧠 **Consistency** – Shared configuration across the cluster
🔁 **Self-Healing** – Auto recovery from crashes
📦 **Automation** – Less manual database management

---

# 🧠 Database Orchestration (Detailed View)

---

## ⚙️ Orchestrator — *The Brain of the Distributed Database*

The **Orchestrator** is the **control plane** or **brain** behind a distributed database system.
It continuously monitors the state of the cluster — all shards, servers, replication factors, and load distribution — and takes decisions to keep the system **balanced, consistent, and fault-tolerant**.

Think of it as the **air traffic controller** for your database cluster.

---

### 🧩 The Orchestrator is responsible for:

#### 1. Maintaining the **Replication Factor**

* Each shard must always have *X copies* of its data (as per the replication factor).
* If a server within a shard crashes, the number of available replicas drops.
* The Orchestrator must **add a new server** to that shard to restore the replication factor.

> 🧠 Example:
> If RF = 4 and one slave in a shard fails → replication factor temporarily becomes 3.
> The Orchestrator immediately assigns a *spare server* to that shard and triggers **data replication** from the master until the new server catches up.

---

#### 2. Deciding **Server-to-Shard Assignments**

* The Orchestrator maintains a **mapping** of which servers belong to which shard.
* When new servers are added, it determines whether to:

  * Attach them to **existing shards**, or
  * Create **new shards** (for scaling out).

---

#### 3. **Scaling Out / Scaling In**

* **Scale Out (Add Shards):**
  When system utilization is high (e.g., >90%), the Orchestrator adds *new shards* to reduce load.
* **Scale In (Remove Shards):**
  When traffic decreases or resources must be reclaimed, it can merge or remove shards safely.

---

#### 4. **Load Balancing**

* Ensures that load (both read and write) is distributed **evenly** across shards and servers.
* Works in coordination with the **Load Balancer (LB)**, which handles real-time routing.
* If certain shards are overloaded, the Orchestrator can **rearrange data distribution** or move users/data ranges to new shards.

---

## ⚙️ Adding New Servers

Let’s break this down as a sequence of events:

---

### 🧩 Step 1: Detect Need for Expansion

Imagine the distributed database is running at **90% capacity** — nearing its limits.

Either:

* A **human operator**, or
* An **auto-scaling service**

decides to **add more servers** to handle increasing traffic.

---

### 🧩 Step 2: Provision New Servers

These new servers are provisioned with the following setup:

1. **Provision hardware / VMs**
2. **Install database software**
3. **Configure database networking, URLs, ports, credentials**
4. **Register servers** with the **Orchestrator**

Once registered, these servers become **visible** to the Orchestrator as available capacity.

---

### 🧩 Step 3: Orchestrator’s Decision — What to Do With the New Servers?

#### ❓ Should we assign these servers to an existing shard?

**No.**
Each existing shard already has the desired **replication factor (X)**.

If we add more servers to an existing shard, it would **increase the replication factor unnecessarily**, leading to resource waste and imbalance.

Instead, we use these servers to **create new shards**, allowing **horizontal scaling**.

---

### 🧩 Step 4: Create New Shards

If replication factor = X and number of new servers = N,
then we can create up to:

[
\text{New Shards} = \text{floor}(N / X)
]

> Example:
> If RF = 4 and 8 new servers are added → we can create `floor(8 / 4) = 2` new shards.

Each new shard will have:

* 1 master
* (X – 1) slave replicas

---

### 🧩 Step 5: Keep Some Servers in Reserve

It’s important **not** to use *all* new servers immediately.

Why?

* If all servers are used for new shards, and later one server crashes,
  there will be **no free servers** available to maintain the replication factor.
* Reserved (idle) servers act as **standby nodes** for **failover recovery**.

---

### 🧩 Step 6: Distributing Data to New Shards

When new shards are added, we must **rebalance data** from existing shards.

This must happen **seamlessly**, with **minimal downtime**.

#### Process:

1. **Simulation Phase**

   * The Orchestrator simulates how data redistribution will occur.
   * It calculates the data ranges (e.g., consistent hash key ranges) to migrate.
2. **Real Phase**

   * Actual data movement begins.
   * Background replication ensures that users experience **zero downtime**.
   * Once migration completes, routing tables are updated to direct future requests to new shards.

---

## 💥 Failure Recovery

### ❓ When a Server Crashes Within a Shard

* The Orchestrator detects failure (via heartbeat timeout).
* It immediately **assigns a reserved (standby) server** to the affected shard.
* The new server:

  * Has no data initially.
  * Syncs up with the shard’s master to **replicate all data**.
  * Once fully caught up, it joins the shard as a functional slave.

---

### ❓ When a Crashed Server Recovers

When a previously crashed server comes back online:

* It is **treated as a new server**.
* Any old data is **wiped out** to avoid inconsistencies.
* It is moved into the **reserved pool**, ready for future assignments.

---

## 🧩 How All This Works Together

| Step | Component                                    | Function                                                             |
| ---- | -------------------------------------------- | -------------------------------------------------------------------- |
| 1    | **Auto-Scaling Service**                     | Adds or removes physical servers.                                    |
| 2    | **Orchestrator**                             | Assigns servers to shards, maintains replication, manages balancing. |
| 3    | **Load Balancer (LB)**                       | Routes requests to the right shard/server.                           |
| 4    | **Configuration Manager (ZooKeeper / etcd)** | Keeps metadata and shard-server mapping consistent.                  |

---

### 🧭 Example Real-World Analogues

| System        | Orchestrator Role                                                       | Configuration Management |
| ------------- | ----------------------------------------------------------------------- | ------------------------ |
| **Vitess**    | Handles shard splitting, rebalancing, and topology management for MySQL | Uses **etcd**            |
| **Cassandra** | Internal orchestration via gossip protocol                              | No central orchestrator  |
| **MongoDB**   | Config servers + mongos router manage shards and replication            | Internal config service  |
| **HBase**     | HMaster acts as orchestrator                                            | Uses **ZooKeeper**       |

---

### 🧩 Visualization

```
        ┌──────────────────────────────────────────────┐
        │                 ORCHESTRATOR                 │
        │----------------------------------------------│
        │ 1. Maintain replication factor               │
        │ 2. Assign servers to shards                  │
        │ 3. Add/remove shards (scaling)               │
        │ 4. Balance load across cluster               │
        └─────────────┬──────────────┬────────────────┘
                      │              │
          ┌───────────┘              └───────────┐
          ▼                                      ▼
┌────────────────────┐                 ┌────────────────────┐
│   Existing Shards  │                 │    New Shards      │
│  (Master + Slaves) │                 │ (Created via new   │
│                    │                 │   servers)         │
└────────────────────┘                 └────────────────────┘
```

---

### ⚡ Key Takeaways

| Concept                | Summary                                                                   |
| ---------------------- | ------------------------------------------------------------------------- |
| **Orchestrator**       | The brain that maintains replication, shard assignment, and load balance. |
| **Replication Factor** | Ensures each shard has enough data copies.                                |
| **Scaling Out/In**     | Adds or removes shards based on cluster capacity.                         |
| **Reserved Servers**   | Standby nodes for handling failures.                                      |
| **Recovery**           | Crashed servers are replaced and re-synced automatically.                 |

---


Perfect 👍 — this “Reserved Servers” section fits beautifully as the next module after **Orchestrator** in a distributed database architecture document.

Here’s your content slightly refined for **clarity, flow, and completeness**, while keeping *all* your points intact and adding just a few enhancements for depth and readability:

---

## 🧠 Reserved Servers

Even the most well-designed systems face failures — hardware crashes, network outages, or maintenance downtimes. To handle such failures gracefully without downtime or data loss, **the orchestrator maintains a pool of reserved servers**.

Reserved servers act as **standby nodes** — always ready to be swapped in when any active database server fails within a shard.

---

### 💡 Why Reserved Servers?

If any server within a shard crashes, the **replication factor** (number of copies per shard) temporarily drops. To restore it immediately, the orchestrator replaces the failed server with one of the reserved servers.

Thus, having reserved servers ensures:

* No service interruption during server failure.
* Immediate restoration of replication factor.
* High availability and resilience of the database cluster.

---

### 📊 Estimating the Number of Reserved Servers

The **optimal number** of reserved servers depends on:

1. **Total number of servers** (N) in the system.
2. **Failure probability** of each server [P(Crash) : Probability of Crash].

If we know:

* A typical server fails once per year.
* Recovery/repair takes **2 days**.

Then:

```
P(Crash) = 2/365 = aprox 0.5%

```

Expected number of crashed servers on any given day [E(Down Server) : Expected no of servers can down]:

```
E(Down Server) = N * P(Crash)
```

Example:

* N = 1000 servers
* E = 1000 × 0.005 = **5 servers (expected)**

So on average, ~5 servers will be down on any given day.

---

### ⚠️ But Expectation Isn’t Enough!

If we maintain exactly 5 reserved servers:

* Half the days, that’s enough.
* But half the days, more than 5 servers might be down → **insufficient reserves**.

Hence, the orchestrator should maintain **enough reserved servers to cover failures with 99% probability**:

```
P(number of crashed servers ≤ R) > 99%
```

Where **R** = minimum number of reserved servers to maintain.

This ensures the system almost never runs out of spare servers, even under rare failure spikes.

---

### ⚠️ Why “Expectation Isn’t Enough”

---

#### 🧮 1. What does “Expectation” mean?

When we say the *expected number* of crashed servers is **5**, it means:

> “On average, we expect around 5 servers to be down on any given day.”

It’s a **statistical average**, not a guarantee.

Some days:

* Maybe only **2** servers crash.
  Other days:
* Maybe **8 or 10** servers crash.

The *expectation* (mean) just tells you what happens **on average**, over a long period — not what happens **every day**.

---

#### 🎯 2. Why that’s not enough for reliability

If we only keep **5 reserved servers**, we’re planning for the *average* case.
But distributed systems need to survive **worst-case** days too — when more servers crash than expected.

Think of it like this:

| Day | Servers Crashed | Reserved Servers Available        | Result         |
| --- | --------------- | --------------------------------- | -------------- |
| Mon | 3               | ✅ 5 available                     | OK             |
| Tue | 5               | ✅ 5 available                     | OK             |
| Wed | 8               | ❌ Only 5 reserved → insufficient! | Failures start |

So even though **5 is the expected number**, it’s **not safe enough** — because 8 crashes in one day isn’t impossible.
And when it happens, your system won’t have enough backup servers to maintain replication — leading to reduced availability or even data risk.

---

#### 📊 3. How to make it reliable

To make sure your system almost *always* has enough reserves, we plan for the **99th percentile**, not just the mean.

That means we choose **R (reserved servers)** such that:

> There’s only a 1% chance that more than R servers crash in a day.

```
P(number of crashed servers ≤ R) > 99%
```

So even on bad days, we’re still covered.

---


#### To ensure 99% reliability, if each server has a 0.5% daily crash chance and you have 1000 servers (expected 5 crashes/day), you should keep about 10–11 reserved servers instead of just 5.


### Step-by-step reasoning

#### 1️⃣ Given

* Total servers (N = 1000)
* Probability a server crashes on any day (p = 0.005)
* Expected crashes per day E[X] = N × p = 5

---

#### 2️⃣ Model

Each server can either **crash (1)** or **not crash (0)** independently.
So total crashes per day follow a **Binomial distribution**:

```
X∼Binomial(N=1000,p=0.005)
```

For large N, small p, we can approximate this by a **Poisson(λ = 5)** distribution.

---

#### 3️⃣ Find R for 99% reliability

We want the smallest (R) such that:

```
P(X≤R) ≥ 0.9
```

Using the Poisson cumulative distribution with λ = 5:

| R      | P(X ≤ R)    |
| ------ | ----------- |
| 5      | 0.616       |
| 6      | 0.762       |
| 7      | 0.866       |
| 8      | 0.938       |
| 9      | 0.972       |
| **10** | **0.989** ✅ |
| 11     | 0.995 ✅     |

---

#### ✅ Therefore

To cover **99% of days**, you need **R ≈ 10 or 11 reserved servers**,
even though the *average* expected crashes per day is only 5.

---

### 💤 Should Reserved Servers Stay Idle?

**No — servers are expensive!**

We want every server to be useful, even if it’s reserved. So, we keep them **active as extra read replicas**.

#### ✅ Reserved Server Utilization Strategy:

1. Reserved servers are added as **read replicas** in existing shards.
2. They are marked as **“reserved”** — available for replacement if any server fails.
3. They **do not become master nodes**.
4. They can handle part of the read traffic — improving read scalability.

---

### 📘 Important Notes

* The **replication factor (X)** is a *minimum requirement*, not a hard cap.
  You can have more replicas than X, but never fewer.

* Reserved servers acting as read replicas *exceed* the replication factor temporarily, which is fine as long as resources aren’t wasted.

---

### 🔁 Failure & Recovery Workflow

**Case 1: Server crash within a shard**

* If the shard has extra read replicas (reserved servers):
  → Mark one as *active* (no longer reserved).
* Otherwise:
  → The orchestrator reassigns a reserved server from another shard.
  → Wipes its data and syncs it with the crashed shard’s data.

**Case 2: Crashed server recovers**

* The recovered server is **re-initialized** and moved to the **reserved pool**.
* Any old data on it is discarded to maintain consistency.

Throughout all this, **no downtime** occurs for users — other replicas in the shard continue handling reads/writes.

---

### 🧩 Summary

| Concept              | Purpose                                          |
| -------------------- | ------------------------------------------------ |
| **Reserved Servers** | Standby servers for handling crashes             |
| **Optimal Count**    | Determined statistically using crash probability |
| **Utilization**      | Act as read replicas when idle                   |
| **Failover Action**  | Immediately replace crashed nodes                |
| **Recovery**         | Repaired nodes rejoin reserved pool              |

---

Perfect! We can now enhance your content by keeping **all your original points**, adding clarity, additional notes, and a **visual diagram** to make seamless shard creation easier to understand. Here’s the enriched version:

---

# Seamless Shard Creation

When the orchestrator decides to create a new shard from new servers, the **data movement** happens as follows:

1. The new shard must take some data from **every existing shard**.

   * Reduce the load of each existing shard **equally**.
2. There should be **minimal downtime** for the users being migrated to this new shard.

---

### ⚠️ Why the simplest approach doesn’t work (single-phase operation)

1. Orchestrator creates a new shard.
2. Initially, this shard is **empty**.

   * Data copy starts (can take hours, e.g., 2 hours).
3. LB immediately starts sending users to the new shard.
4. Problem: the shard **doesn’t have data yet** → users may see missing data.

**Naive solutions:**

* Wait until all data is copied (2-hour downtime) → high disruption.
* Allow users to access the shard (eventual consistency) → data temporarily inconsistent, bad user experience.

**Conclusion:** Single-phase approach is unacceptable; we need **two-step migration**.

---

## 1️⃣ Simulation Phase

Orchestrator creates the shard **silently**:

1. **Simulation without LB awareness:**

   * Knows all metadata via config management:

     * Users, servers, consistent-hash info.
   * Determines **which users** will move to the new shard.
2. **Bulk copy of historical data**:

   * For each source shard:

     ```sql
     SELECT * FROM table1, table2, ...
     WHERE user_id IN (4, 9, 12, ...)
     ```

     → Insert into new shard.
   * Let’s assume this runs from `t0 → t1` (2 hours).

**Delta problem:**

* New data created during bulk copy is **not captured** (cursor isolation).
* `Delta` = new writes during t0 → t1.
* Usually small (e.g., 2 hours of transactions → 30 seconds copy).

---

### Visualization — Simulation Phase

```
t0: start bulk copy
 ┌───────────────┐
 │ Old Shards    │ <--- LB continues routing requests here
 └─────┬─────────┘
       │ bulk copy selected users → New Shard
       ▼
┌───────────────┐
│ New Shard     │  empty initially, receiving bulk data
└───────────────┘
t0 → t1: delta writes captured in background
```

---

## 2️⃣ Real Phase

Starts at `t1` after bulk copy:

1. Orchestrator informs LB about new shard.
2. LB begins routing requests to the new shard.
3. **Delta copy** (WAL/binlog based):

   ```sql
   SELECT * FROM table1, table2, ...
   WHERE user_id IN (4, 9, 12, ...)
   AND modified_at >= t0
   ```

   * Applies missing transactions to the new shard.
4. Delta typically small → fast copy (seconds).

---

### Consistency Options

| Option                                  | Pros                  | Cons                                                          |
| --------------------------------------- | --------------------- | ------------------------------------------------------------- |
| Serve requests while delta copies       | No downtime           | Users may see missing data temporarily (eventual consistency) |
| Deny requests until delta copy finishes | Immediate consistency | Minimal downtime (seconds)                                    |

> Goal: reduce downtime from **2 hours → few seconds** for immediate consistency.

---

### Why two-step works

1. **Single-step**:

   * Copying 1 TB → wait for 1–2 hours for consistency → long downtime.
2. **Two-step**:

   * Bulk copy large historical data **without affecting users**.
   * Delta (small) copied while LB routes traffic.
   * Immediate consistency downtime reduced from **2 hours → a few seconds**.

---

### Visualization — Real Phase

```
t1: bulk copy complete, delta remaining
 ┌───────────────┐
 │ New Shard     │  delta copy starts
 └─────┬─────────┘
       │ LB starts routing requests here
       ▼
┌───────────────┐
│ Users         │  Some requests may wait (if enforcing consistency)
└───────────────┘
t2: delta copy complete
 ┌───────────────┐
 │ New Shard     │  fully consistent, serving all requests
 └───────────────┘
```

---

Here’s a polished, enriched version of your **Sharding + Multi-Master Replication** notes, keeping all your points and adding clarity, structure, and some visualization ideas:

---

# Sharding + Multi-Master Replication

Multi-master replication **removes the strict master-slave distinction**.

* Every server handles both **reads and writes**.
* Every server acts as **master (write)** and **slave (read & replicate)**.
* All servers are **homogeneous** and communicate via **Gossip Protocol**.

---

## 🧩 Server vs Shard

* In **Master-Slave**, we have heterogeneous servers:

  * Load balancer, orchestrator, master, slave, reserved slave, etc.
* In **Multi-Master**, all servers are the same:

  * Each server handles LB, orchestration, reads, and writes.
  * Sharding & replication are merged.

**Implication:**

* Shards exist conceptually, but every server contains **multiple partitions**.
* Each server can contain **some primary partitions and some replica partitions**.

---

## Ring Placement

* Servers (not shards) are placed on the **consistent hashing ring**.
* No concept of a separate “shard crash”: if a server crashes, consistent hashing redirects traffic automatically.

---

## Data Replication & Partitioning

* Each piece of data is **written in multiple places**:

  * Some writes are **synchronous** (to meet consistency requirements).
  * Others may be **asynchronous**.
* Uses **tunable consistency** (parameters X, R, W).

**Example:**

* N = 4 Servers: `{A, B, C, D}`
* K = 5 virtual spots per server on the ring
* Replication factor X = 3
* Users `{u1 .. u20}`

**Partitions per server:**

| Server | Primary                | Replica 2              | Replica 3              |
| ------ | ---------------------- | ---------------------- | ---------------------- |
| A      | u1, u7, u11, u14, u16  | u6, u10, u13, u15, u20 | u19, u5, u9, u12, u14  |
| B      | u5, u8, u10, u13, u19  | u4, u7, u9, u12, u18   | u3, u6, u8, u11, u17   |
| C      | u3, u12, u15, u17, u20 | u2, u11, u14, u16, u19 | u1, u10, u13, u15, u18 |
| D      | u2, u4, u6, u9, u18    | u1, u3, u5, u8, u17    | u20, u2, u4, u7, u16   |

> Each user’s data is replicated across **3 servers**.
> **Important:** Do **not** store multiple replicas of the same data on the same server — defeats replication purpose.

---

## 🔄 Load Balancing & Routing

* **Master-Slave:** All requests go to LB first, then routed to master/slave.
* **Multi-Master:** Any server can receive requests.

  * Server uses **consistent hashing** to locate which servers contain the data.
  * Forward requests as needed.
  * Higher availability, no central LB required.

**Homogeneous Servers:**

* Each server acts as:

  * LB
  * Orchestrator
  * Master
  * Slave

**Communication:**

* Continuous peer-to-peer via **Gossip Protocol**
* Ensures metadata consistency and fault tolerance.

---

## 🔹 Key Advantages of Multi-Master

1. **No single point of failure** (no master dependency).
2. **Higher availability**: any server can handle requests.
3. **Simplified architecture**: homogeneous servers.
4. **Elastic scaling**: new servers join the ring and sync via gossip.
5. **Tunable consistency**: control trade-off between latency & data durability.

---

### 💡 Visualization Idea

```
Consistent Hash Ring:

       A
      / \
     D---B
      \ /
       C

Server partitions (example, replication factor = 3):

u1 → Primary: A | Replica: C, D
u2 → Primary: D | Replica: C, B
u3 → Primary: C | Replica: B, D
...
```

* Each server contains **primary and replica partitions**.
* Requests hitting any server are routed internally to the correct replicas.

---
