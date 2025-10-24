# ⚖️ **Load Balancing**

Load balancing determines **which server should handle a particular request**.
It ensures even distribution of traffic, optimal resource utilization, and high availability.

In **data-aware systems** (like sharded databases, distributed caches, etc.), load balancing is tightly coupled with **data distribution** — because if a request goes to the wrong server, the data won’t be found.

> Example:
> If Sanjana’s user profile is stored on **Server B**, but the load balancer routes her request to **Server A**, the request fails (or returns “User not found”).

---

## 🧩 **1️⃣ Data Sharding**

**Sharding** is the process of **splitting large datasets into smaller, more manageable pieces (shards)** and distributing them across multiple servers.
It improves **scalability**, **parallelism**, and **fault isolation**.

---

### **Types of Sharding**

#### 1. Vertical Partitioning (Normalization)

* Data is divided by **columns (attributes)**.
* Each table or microservice handles a subset of attributes.

**Example:**

```
User(id, name, age, address)
→ UserBasic(id, name, age)
→ UserAddress(id, address)
```

✅ Efficient queries for specific attributes
❌ Requires joins or multiple calls to rebuild full entity

---

#### 2. Horizontal Partitioning (Row-wise)

* Data is divided by **rows (records)**.
* Each shard stores a **subset of users or objects**.

**Example:**

```
Server1 → user_id 1–1000  
Server2 → user_id 1001–2000
```

✅ Most common approach in large systems
✅ Each shard is independent
❌ Choosing the right sharding key is critical (to avoid hotspots)

---

#### 3. Vertical Partitioning Across Servers

* Different **columns** live on different **physical servers**.
* Used when tables are very wide or have heavy column access patterns.

---

#### 4. Horizontal Partitioning Across Servers

* Each server holds **different rows** of a single logical table.
* Typically used with **routing algorithms** (hashing, consistent hashing, etc.) for distributing queries.

---

## 🔑 **2️⃣ Sharding Key**

A **sharding key** is the attribute that decides **where a record lives**.

**Example:**

* `user_id` for user-related data
* `region_id` for geo-distributed systems
* `order_id` for e-commerce orders

### **Good Sharding Key Characteristics**

* **Uniformly distributed** (avoids hotspots)
* **Immutable** (should not change over time)
* **Present in most queries** (to simplify routing)

---

## 🧭 **3️⃣ Sharding & Routing**

Routing logic must **exactly match** the sharding logic.
Otherwise, a query might hit the wrong shard.

Example:

* Sharding Logic: `hash(user_id) % N`
* Routing Logic: must use the same `hash(user_id) % N`

Mismatch → data inconsistencies or failed lookups.

---

## ⚙️ **Routing Algorithm: Key Characteristics**

A good routing algorithm must be:

| Property                  | Description                                                |
| ------------------------- | ---------------------------------------------------------- |
| **Fast**                  | Must quickly decide which node to use                      |
| **Equal Distribution**    | Should spread requests evenly                              |
| **Elastic**               | Adding/removing servers should not cause major reshuffling |
| **Minimal Data Movement** | Data migration should be small                             |
| **Deterministic**         | Same input → same server without coordination              |

---

# 🔁 **Round Robin Load Balancing**

Round Robin is the **simplest** and most widely used load balancing strategy.

---

### **1️⃣ How It Works**

* Requests are distributed **sequentially** across all servers.
* Each new request goes to the **next server in the list**, looping back after the last.

**Flow:**
`A → B → C → A → B → C → ...`

---

### **2️⃣ Example**

| Request | Server |
| ------- | ------ |
| R1      | A      |
| R2      | B      |
| R3      | C      |
| R4      | A      |
| R5      | B      |
| R6      | C      |

---

### **3️⃣ Variants**

* **Simple Round Robin:** Equal turn for all servers.
* **Weighted Round Robin:** Assigns different weights based on server capacity.
  Example: A(2x), B(1x) → sequence: A, A, B, A, A, B…

---

### **4️⃣ Adding & Removing Servers**

* When adding/removing servers, rotation order changes.
* Does **not** preserve session affinity.
* Existing clients may lose session continuity.

---

### **5️⃣ Pros**

✅ Simple, stateless, no metadata needed
✅ Good for **homogeneous** servers
✅ Works well for **stateless applications**

---

### **6️⃣ Cons**

❌ Ignores server load or response time
❌ No data-awareness
❌ Not ideal for **session persistence** or **stateful workloads**

---

### **7️⃣ When to Use**

* All servers have **similar capacity**
* Applications are **stateless**
* Need quick, simple balancing
* Example: REST APIs, static content servers

---

# 🪣 **Bucketing (Modulo) Load Balancing**

Bucketing (or Modulo-based hashing) uses a **hash function** to deterministically map each user/request to a specific server.

---

### **1️⃣ How It Works**

Each request is hashed → hash result is divided by total servers → server index chosen.

```
server_index = hash(key) % N
```

* All requests with same key go to same server.
* Predictable and data-aware.

---

### **2️⃣ Example**

| Server | Range |
| ------ | ----- |
| A      | 0–3   |
| B      | 4–6   |
| C      | 7–9   |

User `u1` → hash(u1)=2 → A
User `u2` → hash(u2)=8 → C

---

### **3️⃣ Adding/Removing Servers**

* Adding/removing servers changes `N` → **all hashes shift!**
* Results in **massive remapping** of keys.

---

### **4️⃣ Pros**

✅ Fast and deterministic
✅ Simple to implement
✅ Data-aware (same key → same server)

---

### **5️⃣ Cons**

❌ High data movement when servers change
❌ Poor scalability
❌ Requires rebalancing entire dataset

---

### **6️⃣ When to Use**

* Cluster size rarely changes
* Small or fixed number of servers
* Systems where rehashing cost is acceptable

---

# 🗺️ **Mapping Table Load Balancing**

A **Mapping Table** explicitly stores which **key/user** belongs to which **server**.

---

### **1️⃣ How It Works**

A lookup table defines:

```
User/Key → Server
```

Every request performs a quick lookup.

---

### **2️⃣ Example**

| User | Server |
| ---- | ------ |
| u1   | A      |
| u2   | B      |
| u3   | C      |
| u4   | B      |
| u5   | A      |

---

### **3️⃣ Advantages**

✅ Complete control over mapping
✅ No hash dependency
✅ Perfect for **sticky sessions** and **custom routing**

---

### **4️⃣ Disadvantages**

❌ High memory usage for large datasets
❌ Operational overhead to maintain table
❌ Single point of failure unless replicated

---

### **5️⃣ When to Use**

* Stateful workloads (sessions, chat systems, custom shards)
* Fixed or small number of users
* Custom or manual routing policies

---

# 🌀 **Consistent Hashing**

Consistent hashing solves the **scalability problem** of modulo hashing by minimizing key movement when servers are added or removed.

---

### **1️⃣ Hash Function**

Maps keys and servers into a numeric space (e.g., 0 → 2³² − 1).

**Examples:**
`hash("ServerA")`, `hash("User123")` using MD5, SHA-1, MurmurHash.

---

### **2️⃣ Hash Ring**

* Imagine the numeric space as a **circular ring**.
* Both **servers** and **keys** are hashed and placed on this ring.
* A key belongs to the **first server clockwise** from its hash position.

---

### **3️⃣ Example**

| Entity   | Hash Position |
| -------- | ------------- |
| Server A | 10            |
| Server B | 50            |
| Server C | 80            |

Keys:

* Key k1 (15) → Server B
* Key k2 (75) → Server C
* Key k3 (5) → Server A

---

### **4️⃣ Virtual Nodes**

Each physical server can have multiple **virtual nodes (vnodes)** to achieve smoother load distribution.

Example:
Server A → hash(A1), hash(A2), hash(A3) …
Spreads load evenly across ring.

---

### **5️⃣ Adding/Removing Servers**

**Adding:**

* Insert new server on ring.
* Only keys between the new server and its predecessor move.

**Removing:**

* Keys on removed server move to its successor.

✅ Minimal reshuffling
✅ Great for dynamic clusters

---

### **6️⃣ Pros**

✅ Scales dynamically with minimal key movement
✅ Data-aware and deterministic
✅ Supports virtual nodes for fairness
✅ Perfect for caches, databases, and message systems

---

### **7️⃣ Cons**

❌ Slightly higher implementation complexity
❌ Needs a good hash function
❌ Slight imbalance in small clusters without vnodes

---

### **8️⃣ Used In**

* **Cassandra**, **DynamoDB**, **Redis Cluster**, **Kafka**, **Memcached**, **Elasticsearch**

---

# 🧮 **Comparison Table**

| Algorithm              | Data-Aware | Key Movement on Node Change | Complexity | Ideal For                          |
| ---------------------- | ---------- | --------------------------- | ---------- | ---------------------------------- |
| **Round Robin**        | ❌          | N/A                         | Simple     | Stateless web servers              |
| **Modulo / Bucketing** | ✅          | High (reshuffle all)        | Simple     | Small static clusters              |
| **Mapping Table**      | ✅          | Manual (low)                | Medium     | Sticky sessions, custom routing    |
| **Consistent Hashing** | ✅          | Minimal                     | Medium     | Large, dynamic distributed systems |

---

# ⚙️ **Stateless Servers**

A **stateless server** doesn’t store client-specific state between requests.
Each request is self-contained — it carries all data required for processing.

---

### **1️⃣ Characteristics**

* No session data in memory
* Requests contain authentication or context
* Servers can be freely added/removed
* Perfect for autoscaling environments

---

### **2️⃣ Examples**

* REST APIs (each request has JWT token)
* Microservices that query state from DB/cache instead of local memory

---

### **3️⃣ Pros**

✅ Easy horizontal scaling
✅ No session replication needed
✅ High availability and fault tolerance
✅ Simplifies load balancing (any node can serve any request)

---

### **4️⃣ Cons**

❌ State must live externally (DB, cache, session store)
❌ Slightly more network overhead (token verification, extra lookups)

---

### **5️⃣ When to Use**

* High-traffic systems (web APIs, cloud apps)
* Stateless microservices
* Auto-scaled server fleets
* Event-driven or ephemeral environments (e.g., AWS Lambda)

---

# 🧠 **Final Summary**

| Concept                | Purpose                       | Best Use Case                   |
| ---------------------- | ----------------------------- | ------------------------------- |
| **Round Robin**        | Simple even distribution      | Stateless workloads             |
| **Bucketing / Modulo** | Deterministic mapping         | Fixed cluster                   |
| **Mapping Table**      | Explicit control              | Sticky sessions, small clusters |
| **Consistent Hashing** | Scalable, minimal remap       | Caches, DBs, dynamic clusters   |
| **Stateless Servers**  | Scalability & fault tolerance | APIs, microservices             |

---
