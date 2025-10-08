# **1️⃣ CAP Theorem**

CAP Theorem is about **trade-offs in distributed systems**. It states:

> A distributed system can only guarantee **two out of three properties**:
> **Consistency (C), Availability (A), Partition Tolerance (P)**.

---

## **2️⃣ Consistency (C)**

Consistency ensures that **all nodes in a system see the same data at the same time**.

There are **three levels**:

1. **Immediate Consistency:**

   * Every read immediately reflects the most recent write.
   * System **always returns the latest value**.
   * Example: A single-node relational database without replication.

2. **Eventual Consistency:**

   * After some time, all nodes converge to the same value.
   * Reads may return **stale/old data temporarily**.
   * Example: Amazon DynamoDB, Cassandra, or any system using **asynchronous replication**.

3. **Data Loss / No Consistency:**

   * System does not guarantee any consistent view.
   * Can happen if nodes fail and no replication exists.
   * Example: A cache that doesn’t persist updates to the main database.

---

## **3️⃣ Availability (A)**

Availability ensures that **every request receives a response**, even if some nodes fail.

* The system **never refuses a request**.
* However, the response **may not reflect the latest write** (sacrificing consistency).
* Example: Web servers behind a load balancer; they always respond even if some nodes are outdated.

---

## **4️⃣ Partition Tolerance (P)**

Partition tolerance ensures that the system continues to operate **even if network failures occur** between nodes.

* **Network Partition:** Some nodes **cannot communicate** with others.
* **Partition Tolerance:** The system can **still serve requests** despite partitions.
* Example: A distributed database spread across regions; one region goes down but the system keeps working.

---

## **5️⃣ Availability vs Partition Tolerance**

* When a **network partition** occurs, the system must choose between:

  1. **Consistency:** Only serve correct data, but may refuse some requests.
  2. **Availability:** Serve requests, but data may be inconsistent temporarily.

This is the **core idea of CAP theorem in practice**: during partitions, you **cannot have both full consistency and full availability**.

---

# **CAP Theorem: System Types**

Remember: CAP = **Consistency, Availability, Partition Tolerance**. You can only fully achieve **two** at a time.

---

## **1️⃣ AP Systems (Availability + Partition Tolerance)**

* **Properties:**

  * Highly available → every request gets a response.
  * Partition tolerant → continues working even if network partition occurs.
  * **Consistency is sacrificed → eventual consistency.**

* **Behavior:**

  * Reads may return **stale data** temporarily, but system keeps serving requests.

* **Examples:**

  * **Cassandra**
  * **DynamoDB**
  * **Couchbase**

* **Use case:**

  * Systems that **cannot afford downtime**, e.g., social media feeds, DNS services.

---

## **2️⃣ CP Systems (Consistency + Partition Tolerance)**

* **Properties:**

  * Immediate consistency → all nodes see the same data.
  * Partition tolerant → system handles network failures.
  * **Availability is sacrificed → some requests may be rejected.**

* **Behavior:**

  * During partition, system **refuses some requests** to maintain consistency.

* **Examples:**

  * **HBase**
  * **MongoDB (with write concern “majority”)**
  * **Zookeeper**

* **Use case:**

  * Systems where **data correctness is critical**, e.g., banking transactions, inventory management.

---

## **3️⃣ AC Systems (Availability + Consistency)**

* **Properties:**

  * Immediate consistency → all nodes see the same data.
  * Highly available → serves all requests.
  * **Partition tolerance is sacrificed → cannot handle network partitions.**

* **Behavior:**

  * Works only if **network partition never occurs**.
  * Rarely achievable in distributed systems.

* **Examples:**

  * Single-node relational databases (PostgreSQL, MySQL) without replication.

* **Use case:**

  * Systems running **on a single reliable node** or **LAN environment**, where network partitions are very rare.

---

✅ **Key takeaway:**

* **AP → Availability over Consistency**
* **CP → Consistency over Availability**
* **AC → Not partition tolerant, works in stable networks only**

---

# **CAP Theorem (Another Definition)**

---

## **1️⃣ Why we can't have all 3?**

* CAP Theorem states that in a **distributed system**, you cannot simultaneously achieve:
  **Consistency (C), Availability (A), and Partition Tolerance (P)**.

* **Reason:**

  * In a distributed system, nodes communicate over a network.
  * **Network partitions** can happen (nodes can’t talk to each other).
  * During a partition, you have **two choices**:

    1. Serve requests → you **lose consistency** (data may differ across nodes).
    2. Maintain consistency → you **lose availability** (some requests are rejected).

* Therefore, **all three together are impossible**.

---

## **2️⃣ 1st definition: Pick any 2**

* This is the **classic CAP definition**:

  * You can design your system to guarantee **any two properties**:

    | Choice | Behavior                                    |
    | ------ | ------------------------------------------- |
    | C + A  | Not partition tolerant                      |
    | C + P  | May reject some requests (low availability) |
    | A + P  | Eventual consistency, but always available  |

* **Implication:** You must **compromise one property** depending on your system needs.

---

## **3️⃣ 2nd definition: During a network partition, choose between C or A**

* More practical definition:

  * **Partition tolerance (P)** is unavoidable in real-world networks.
  * So the real **trade-off is only between C and A** during network partitions:

    * **Choose C → reject requests to maintain correctness**
    * **Choose A → serve requests, may return stale data**

* **Example:**

  * A banking system during network issues → chooses **C** (reject writes if nodes can’t sync).
  * A social media feed during network issues → chooses **A** (serve posts, even if slightly outdated).

---

✅ **Key takeaway:**

* CAP is not about always choosing between C, A, and P.
* **Partition tolerance is mandatory** in distributed systems.
* The **real choice is between consistency and availability** during network failures.

---

# **PACELC Theorem**

PACELC is an extension of CAP proposed by Daniel Abadi. It addresses a limitation of CAP:

* **CAP only considers trade-offs during network partitions**, but in real systems, **latency is always a concern**, even when there’s no partition.

---

## **PACELC Components**

PACELC stands for:

```
P → Partition
A → Availability
C → Consistency
E → Else
L → Latency
C → Consistency
```

* **Interpretation:**

  * **P**: If a network **partition occurs**, you must choose between:

    * **A (Availability)** → serve requests even if data may be stale
    * **C (Consistency)** → reject some requests to maintain correctness
  * **ELC (Else Latency vs Consistency):**

    * **Else** (when there’s **no partition**) → you must still choose a trade-off between:

      * **L (Low latency)** → serve requests faster, possibly sacrificing consistency
      * **C (Consistency)** → ensure latest data, possibly increasing latency

---

## **Key Idea**

* CAP = trade-offs **only during network partitions**.
* PACELC = trade-offs **always, including normal operations**.
* Helps system designers **tune for performance and consistency** in all situations.

---

## **Examples**

| System    | Partition Trade-off (P) | Normal Operation (ELC)              |
| --------- | ----------------------- | ----------------------------------- |
| DynamoDB  | AP                      | Eventual consistency / low latency  |
| HBase     | CP                      | Strong consistency / higher latency |
| Cassandra | AP                      | Eventual consistency / low latency  |

---

✅ **Key takeaway:**

* PACELC gives a **more complete view** of distributed systems trade-offs.
* Helps decide **consistency vs availability vs latency**, not just during partitions.

---

# **Replication in Distributed Systems**

Replication is the process of **copying data across multiple nodes** to improve **availability, fault tolerance, and performance**.

---

## **1️⃣ Replication vs Sharding**

| Feature        | Replication                              | Sharding (Partitioning)                        |
| -------------- | ---------------------------------------- | ---------------------------------------------- |
| **Definition** | Copy the **same data** to multiple nodes | Split **different parts of data** across nodes |
| **Purpose**    | High availability, fault tolerance       | Scalability, performance                       |
| **Read**       | Can be served from **any replica**       | Only the shard holding the data can serve it   |
| **Write**      | Must update **all replicas** (or quorum) | Write goes only to the shard owning the data   |
| **Example**    | Master-Slave replication in MySQL        | Horizontal partitioning in MongoDB, Cassandra  |

> **Summary:** Replication = multiple copies of same data.
> Sharding = splitting data across nodes to balance load.

---

## **2️⃣ Master-Slave Replication**

* **Architecture:**

  * **Master Node:** Handles all **writes**.
  * **Slave Nodes:** Replicate data from master, handle **reads**.
  * Helps **scale read operations** while maintaining a single source of truth.

* **Workflow:**

  1. Write goes to **master**.
  2. Master propagates changes to **slaves** asynchronously or synchronously.
  3. Reads can be served from **slaves** (read scaling).

---

### **Advantages**

* Improves **read scalability**.
* Provides **data redundancy**.
* Can implement different **consistency models** (immediate, eventual, tunable).

### **Disadvantages**

* Master can become a **single point of failure**.
* Writes can be delayed on slaves → **stale reads** (if eventual consistency).

---

# **Master-Slave Replication & Consistency Models**

---

## **1️⃣ Master-Slave with No Consistency**

* **Behavior:**

  * Writes go to the master.
  * Slaves replicate **eventually**, but some reads may **never be consistent**.
  * No guarantee that slaves reflect the master data.

* **Pros:**

  * Very fast writes.
  * Highly available for reads (slaves always respond).

* **Cons:**

  * Data may be **stale or lost**.
  * Suitable only when **consistency is not critical**.

* **Example Use Case:**

  * Logging systems or caching layers where **exact accuracy is not critical**.

---

## **2️⃣ Master-Slave with Eventual Consistency**

* **Behavior:**

  * Writes go to the master.
  * Slaves **eventually replicate** changes.
  * Reads from slaves may temporarily return old data, but eventually all nodes **converge**.

* **Pros:**

  * Good **read scalability**.
  * Reasonable **fault tolerance**.

* **Cons:**

  * Reads can be **stale**.
  * Conflicts may arise if multiple writes are done in different partitions.

* **Example Use Case:**

  * Social media timelines, product catalogs, distributed caches.

---

## **3️⃣ Master-Slave with Immediate Consistency – Write Everywhere**

* **Behavior:**

  * Every write is sent to **all replicas (master + slaves)** before being acknowledged.
  * Guarantees that **all nodes are immediately consistent**.

* **Pros:**

  * Strong consistency (C).
  * Reads from any node always return **latest data**.

* **Cons:**

  * Slower writes → need **all replicas to acknowledge**.
  * Less available during network failures (P is sacrificed).

* **Example Use Case:**

  * Banking transactions, inventory management.

---

## **4️⃣ Master-Slave with Immediate Consistency – Quorum**

* **Behavior:**

  * Writes and reads require a **quorum** (majority of nodes) to acknowledge.
  * Ensures strong consistency **without requiring all nodes** to respond.

* **Pros:**

  * Balances **availability and consistency**.
  * Faster than write-everywhere but still **consistent**.

* **Cons:**

  * Slightly more complex logic for quorum management.
  * Some latency depending on cluster size.

* **Example Use Case:**

  * Cassandra, Riak (configurable consistency), distributed databases with **tunable consistency**.

---

✅ **Key takeaway:**

* **No consistency:** fast, unreliable.
* **Eventual consistency:** slow convergence, read scaling.
* **Immediate consistency (write everywhere):** strong consistency, slower writes.
* **Immediate consistency (quorum):** compromise between availability, latency, and consistency.

---
# **Tunable Consistency**

Tunable consistency allows you to **choose the consistency level for reads and writes** dynamically, instead of sticking to a single model (strong, eventual, etc.).

---

## **1️⃣ Concept**

* In a **replicated distributed database**, data is stored on **N nodes**.

* When performing **read or write**, you can specify how many nodes must **acknowledge** the operation.

* **Notation:**

  * **N** = total number of replicas
  * **W** = number of nodes that must acknowledge a **write**
  * **R** = number of nodes that must acknowledge a **read**

* **Consistency rule:**
  [
  R + W > N \implies Strong consistency
  ]

  * If **R + W ≤ N**, you get **eventual consistency**.

---

## **2️⃣ Examples of Consistency Levels**

| Consistency Level | Description                                               | Use Case                                  |
| ----------------- | --------------------------------------------------------- | ----------------------------------------- |
| **ONE**           | Only 1 node must respond                                  | Fast reads/writes, eventual consistency   |
| **QUORUM**        | Majority of nodes must respond                            | Balanced consistency & availability       |
| **ALL**           | All replicas must respond                                 | Strong consistency, slower writes/reads   |
| **LOCAL_QUORUM**  | Majority of nodes in local datacenter must respond        | Reduce latency in geo-distributed systems |
| **ANY**           | Write succeeds if any node responds (even hinted handoff) | High availability, low consistency        |

---

## **3️⃣ How it Works**

1. **Write operation:**

   * If **W = 3** and **N = 5**, the write is considered successful after **3 replicas acknowledge**.

2. **Read operation:**

   * If **R = 3**, the read fetches data from **3 replicas** and returns the **latest version** using a conflict resolution strategy (e.g., last-write-wins).

3. **Strong consistency example:**

   * N = 5, W = 3, R = 3 → R + W = 6 > 5 → **guaranteed strong consistency**

4. **Eventual consistency example:**

   * N = 5, W = 1, R = 1 → R + W = 2 < 5 → **eventual consistency**

---

## **4️⃣ Advantages of Tunable Consistency**

* **Flexible:** Adjust based on workload (read-heavy vs write-heavy).
* **Performance optimization:** Can trade consistency for **latency or availability**.
* **Supports hybrid models:** Strong consistency for critical operations, eventual consistency for non-critical ones.

---

✅ **Key takeaway:**

* Tunable consistency is **a practical way to implement CAP/PACELC trade-offs**.
* By tuning **R and W**, you can choose **strong consistency, eventual consistency, or something in between**.

---

* **Users submit solutions** → stored in **DB**
* **Background service (every 10 mins)** → fetches submissions, computes ranklist
* **Ranklist stored in Redis (global cache)**
* **Clients (participants)** → fetch leaderboard directly from **Redis**

This ensures **eventual consistency** with high read performance 🚀
