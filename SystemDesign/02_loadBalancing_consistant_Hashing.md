# Load Balancing

Load balancing determines **which server should handle a particular request**.
It is tightly coupled with **how data is distributed** across servers. If a request is sent to the wrong server, it will not find the user’s data.

Example: If Sanjana’s request goes to a server storing Ashok’s data → request fails.

---

## 1️⃣ Data Sharding

Sharding is the process of **splitting data across multiple servers** to improve scalability and performance.

### Types of Sharding

1. **Vertical Partitioning (Normalization)**

   * Divide data by **columns**.
   * Example: `User(id, name, age, address)` → `UserBasic(id, name, age)` + `UserAddress(id, address)`.

2. **Horizontal Partitioning**

   * Divide data by **rows**.
   * Example: `User` table → Server1: users 1–1000, Server2: users 1001–2000.

3. **Vertical Partitioning (across servers)**

   * Each server holds **different columns** of the same table.

4. **Horizontal Partitioning (across servers)**

   * Each server holds **different rows** (subset of users, orders, etc.).

---

## 2️⃣ Sharding

Sharding ensures that each piece of data is placed on the correct server.

### Sharding Key

* The column or attribute used to determine the shard.
* Example: `user_id` for user-related data.

### Sharding and Routing

* The logic for sharding **must match the routing logic**.
* If sharding logic = A (e.g., hash(user_id) % N), then routing logic = A too.
* **Mismatch leads to wrong servers being queried** → failed requests or high latency.

---

## Routing Algorithm
### Characteristics of good Routing Algo
    - Fast
    - Equal distribution
    - We Should be able to freely add/remove servers
    - Minimal data Movement
    - Routing Should be derrministic without exchanging information


---
# Round Robin Load Balancing

Round Robin is one of the simplest and most widely used load balancing strategies.

---

## 1️⃣ How it works

* Requests are distributed **evenly across all available servers** in a **circular order**.
* Each new request goes to the **next server in the list**, then loops back to the first server once all servers have received a request.

---

## 2️⃣ Example

Assume 3 servers: **A, B, C**

Incoming requests: **R1, R2, R3, R4, R5, R6**

**Distribution:**

| Request | Server |
| ------- | ------ |
| R1      | A      |
| R2      | B      |
| R3      | C      |
| R4      | A      |
| R5      | B      |
| R6      | C      |

---

## 3️⃣ Initial Distribution

* When the load balancer starts, it maintains a **pointer to the next server**.
* Requests are sent **in order**, ensuring **fair initial distribution**.

---

## 4️⃣ Adding and Removing Servers

**Adding a server:**

* New server is appended to the rotation.
* Subsequent requests are distributed including the new server.

**Removing a server:**

* Removed server is skipped in the rotation.
* Requests continue to circulate among the remaining servers.

**Note:** Round Robin does **not automatically redistribute existing sessions** or handle session affinity.

---

## 5️⃣ Pros

* Simple and easy to implement
* Fair distribution when servers are roughly equal in capacity
* No special configuration required

---

## 6️⃣ Cons

* **Ignores server capacity** → can overload slow servers
* **Does not account for current load** → may send requests to busy servers
* **Not ideal for session persistence** → requires sticky sessions for stateful applications

---

## 7️⃣ When to Use Round Robin

* Servers are **homogeneous** (similar hardware & processing capacity)
* Requests are **stateless** or session state is stored externally
* Simple, **low-maintenance load balancing** is sufficient
* Traffic patterns are **relatively uniform**

---

# Bucketing Load Balancing

Bucketting (also called **consistent hashing**) is a strategy used to assign requests or users to servers using **hashing**. It’s widely used in distributed systems where **server churn** (adding/removing servers) occurs.

---

## 1️⃣ How it works

* Each server is assigned a **range of buckets** or **virtual nodes** on a hash ring.
* Each request or user is **hashed** to a bucket → routed to the server responsible for that bucket.
* Ensures **minimal redistribution** of keys when servers are added or removed.

---

## 2️⃣ Example

Servers: **A, B, C**

Buckets (0-9):

| Bucket | Server |
| ------ | ------ |
| 0-3    | A      |
| 4-6    | B      |
| 7-9    | C      |

User `u1` → hash(u1) = 2 → Server A
User `u2` → hash(u2) = 8 → Server C

---

## 3️⃣ Initial Distribution

* Assign each server to **one or more points** (buckets) on the hash ring.
* Each request is mapped to a **bucket via a hash function** → routed to the assigned server.
* Distribution depends on **hash function** and **number of virtual nodes per server**.

---

## 4️⃣ Adding and Removing Servers

**Adding a server:**

* Only **buckets assigned to the new server** are redistributed.
* Most existing requests/users continue to go to the **same server**, minimizing data movement.

**Removing a server:**

* Buckets of the removed server are **reassigned to remaining servers**.
* Again, only **affected buckets** are remapped → minimal impact.

---

## 5️⃣ Pros

* **Scales well** with server churn
* **Minimal remapping** → fewer cache misses or data migrations
* Works well for **stateful workloads** (user sessions, sharded data)
* Flexible with **virtual nodes** → better load distribution

---

## 6️⃣ Cons

* More **complex to implement** than Round Robin
* Slightly **uneven distribution** if virtual nodes are not used properly
* Hash function must be **consistent and stable**

---

## 7️⃣ When to Use Bucketing

* Servers **may frequently join or leave** (elastic systems)
* Workloads are **stateful**, e.g., user sessions, sharded databases
* Want **minimal movement of keys/data** on scaling events
* Need **better fault tolerance** than Round Robin

---

# Mapping Table Load Balancing

A **Mapping Table** (or **explicit lookup table**) is a strategy where each **request, user, or key** is explicitly mapped to a **specific server**. Unlike Round Robin or Bucketing, the mapping is **stored in a table** and used for routing.

---

## 1️⃣ How it works

* Maintain a **table in memory** or a fast lookup system:

  ```
  User/Key → Server
  ```
* When a request comes in, the system **looks up the server** in the mapping table → forwards the request.
* Provides **complete control** over which user/request goes to which server.

---

## 2️⃣ Example

Mapping Table:

| User | Server |
| ---- | ------ |
| u1   | A      |
| u2   | B      |
| u3   | C      |
| u4   | B      |
| u5   | A      |

* User `u1` → Server A
* User `u4` → Server B

---

## 3️⃣ Initial Distribution

* Precompute the mapping based on **hashing, load, or business rules**.
* Store mapping in **fast-access memory** (e.g., Redis, in-process hashmap).

---

## 4️⃣ Adding and Removing Servers

**Adding a server:**

* Update the mapping table to **assign some keys/users** to the new server.
* Other mappings **remain unchanged** → no remapping for unaffected users.

**Removing a server:**

* Update the mapping table to **reassign users/keys** of the removed server to remaining servers.
* Requires careful update to avoid **orphaned users**.

---

## 5️⃣ Pros

* **Complete control** over user-to-server assignment
* **Minimal redistribution** for scaling events
* Very predictable, useful for **stateful workloads**
* Works with **heterogeneous servers**

---

## 6️⃣ Cons

* Mapping table can **grow large** (memory overhead)
* Updating table is **manual/operationally heavier**
* Can become a **single point of failure** if not replicated
* Not suitable for **rapidly changing or large user base**

---

## 7️⃣ When to Use Mapping Table

* Workloads are **stateful** and require **sticky routing** (user sessions, sharded data)
* Need **fine-grained control** over which users go to which server
* Number of users/keys is **manageable**
* Minimal server churn, or when churn is controlled

---

# Consistent Hashing

Consistent Hashing is a strategy used to distribute keys (or users) across multiple servers in a **scalable and resilient** way. Unlike Round Robin or Bucketing, it **minimizes data movement** when servers are added or removed.

---

## 1️⃣ Hash Function

A hash function maps **keys or servers** to a numeric space (0 → max hash).

### Good Hash Function

* Uniformly distributes keys across the hash space.
* Deterministic: same key always maps to the same hash.
* Minimizes collisions.
* Examples: MD5, SHA-1, MurmurHash.

---

## 2️⃣ Hash Ring

* Imagine the hash space **0 → MAX** as a **circle**.
* Servers are placed on the **hash ring** using their hash values.
* Keys are also hashed and placed on the ring.

**Assignment Rule:**

* A key belongs to the **first server clockwise** from its position on the ring.

---

## 3️⃣ Consistent Hashing Algorithm

1. Hash each server → place on ring.
2. Hash each key → find the nearest server clockwise.
3. Assign key to that server.

**Virtual Nodes:**

* Each server can have **multiple virtual nodes** on the ring.
* Helps in **better load balancing** when server capacities differ.

---

## 4️⃣ Example

Hash ring (0 → 100):

```
Server A → 10
Server B → 50
Server C → 80
```

Keys:

* Key k1 → hash 15 → Server B
* Key k2 → hash 75 → Server C
* Key k3 → hash 5  → Server A

---

## 5️⃣ Initial Distribution

* Place all servers on the ring using their hashes.
* Map keys to servers using the clockwise rule.
* Virtual nodes can be added for **smoother distribution**.

---

## 6️⃣ Adding and Removing Servers

**Adding a server:**

* Place the new server on the ring.
* Only the keys **between the new server and its predecessor** need to move.
* Most keys remain unaffected → minimal redistribution.

**Removing a server:**

* Keys assigned to the removed server are **reassigned to its successor** on the ring.
* Again, most keys remain unaffected.

---

## 7️⃣ Pros

* Minimal data movement on server changes.
* Scales well for large numbers of servers/keys.
* Naturally balances load with virtual nodes.
* Supports **heterogeneous server capacities**.

---

## 8️⃣ Cons

* Slightly more complex to implement than Round Robin or Bucketing.
* Requires **good hash function** to prevent hotspots.
* Needs **virtual nodes** for small clusters to avoid imbalance.

---

## 9️⃣ When to Use Consistent Hashing

* Large-scale, distributed, or sharded databases.
* Systems with **frequent server additions/removals**.
* Load balancing for **cache systems** (Redis, Memcached).
* Eventual consistency systems with **replication across nodes**.

---


# Stateless Servers

Stateless servers are servers that **do not maintain any session or client-specific data** between requests. Each request is **independent** and contains all the information needed to process it.

---

## 1️⃣ Characteristics

* No client-specific state is stored on the server.
* All requests are **self-contained** (e.g., include authentication tokens, user info).
* Servers can be **added or removed** without affecting user sessions.
* Ideal for **horizontal scaling**.

---

## 2️⃣ Example

* REST APIs: each HTTP request carries authentication tokens and payload.
* Microservices: services process each request without relying on server memory.

---

## 3️⃣ Pros

* **Easy to scale horizontally**: add more servers without worrying about session replication.
* **High availability**: if a server crashes, another server can handle requests immediately.
* Simplifies **load balancing**: any server can handle any request.
* Reduces **memory overhead** on servers.

---

## 4️⃣ Cons

* All client-specific state must be stored **externally** (e.g., database, cache, distributed session store).
* Some requests may require **more data to be sent** in each request (tokens, metadata).

---

## 5️⃣ When to Use Stateless Servers

* Systems with **high traffic and need for horizontal scaling**.
* APIs and microservices architectures.
* Load-balanced web servers.
* Cloud-native applications where servers can be **ephemeral**.

---
