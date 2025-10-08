# 📨 Messaging Queues

---

### 🔹 Definition

* An **asynchronous communication mechanism**.
* Messages (data or events) are placed onto a queue by **producers** and later processed by **consumers**.

---

### 🔹 Key Idea

* Follows **Publisher-Subscriber (Pub-Sub / Producer-Consumer) pattern**.
* Decouples **sending** from **receiving**, allowing independent scaling.

---

### 🔹 Components

1. **Producers (Publishers / Senders)**

   * Push messages into the queue.

2. **Consumers (Subscribers / Receivers)**

   * Consume messages from the queue.
   * Process messages and acknowledge completion.

3. **Queue**

   * Holds messages in **FIFO order** (first-in, first-out).

---

✅ **Benefits:**

* Decouples services → improves scalability
* Enables asynchronous processing → reduces blocking
* Provides **reliability and fault tolerance** via message persistence

---

### Diff Between PubSub, Observer, Event Handler patterns

#### **1. Observer Pattern**

- **Intent:** Define a one-to-many dependency between objects so that when one object (the **subject**) changes state, all its dependents (**observers**) are notified automatically.
- **Structure:**

  - `Subject` maintains a list of `Observers`.
  - Observers register themselves with the subject.
  - When the subject’s state changes, it **pushes updates** to all observers.

- **Communication:** **Direct**; the subject knows its observers.
- **Coupling:** **Tightly coupled** (subject holds references to observers).
- **Use-case Examples:**

  - GUI frameworks: Button click updates multiple UI components.
  - Data binding in MVC/MVVM frameworks (React hooks, Vue watchers).

- **Analogy:** A teacher announces to the students in class whenever there’s an update.

---

#### **2. PubSub (Publisher-Subscriber) Pattern**

- **Intent:** Decouple the sender of messages (**publisher**) from the receivers (**subscribers**) via a **message broker**.
- **Structure:**

  - Publishers **publish messages** to a **channel/topic**.
  - Subscribers **subscribe to a channel/topic** to receive messages.
  - Publishers and subscribers **do not know about each other**.

- **Communication:** **Indirect** via a broker or event bus.
- **Coupling:** **Loosely coupled**; publisher doesn’t know who is listening.
- **Use-case Examples:**

  - Event-driven systems, microservices, message queues (Kafka, RabbitMQ).
  - Chat applications where multiple clients receive messages.

- **Analogy:** A radio station broadcasts to listeners; the station doesn’t know who is listening.

---

#### **3. Event Handler (Callback) Pattern**

- **Intent:** Execute a **callback function** in response to an event.
- **Structure:**

  - Register functions (handlers) for specific events.
  - When the event occurs, all registered functions are invoked.

- **Communication:** **Direct**; the event emitter calls registered handlers.
- **Coupling:** Varies; usually looser than Observer but tighter than PubSub.
- **Use-case Examples:**

  - DOM events in JavaScript (`button.onclick = handleClick`).
  - Node.js `EventEmitter`.

- **Analogy:** Pressing a button triggers a specific action (handler).

---

#### **Comparison Table**

| Feature                   | Observer                  | PubSub                               | Event Handler                  |
| ------------------------- | ------------------------- | ------------------------------------ | ------------------------------ |
| **Dependency**            | Subject → Observers       | None (via broker)                    | Emitter → Handlers             |
| **Coupling**              | Tight                     | Loose                                | Medium                         |
| **Direct/Indirect**       | Direct                    | Indirect                             | Direct                         |
| **Number of Subscribers** | Usually known             | Many, dynamic                        | Many, dynamic                  |
| **Who knows whom**        | Subject knows observers   | Neither knows each other             | Emitter knows handlers         |
| **Push vs Pull**          | Push updates              | Push events                          | Push events (callback invoked) |
| **Use-cases**             | GUI updates, data binding | Event-driven apps, messaging systems | DOM events, Node.js events     |

---

**Key Takeaways:**

- **Observer**: Tight coupling, direct, designed for objects within the same process.
- **PubSub**: Loose coupling, indirect, designed for distributed systems or decoupled modules.
- **Event Handler**: Lightweight, usually direct, mainly for handling events in a single process (like UI events).

---

Here’s your **Pub-Sub / Messaging Queue Benefits and Considerations** section formatted into a clean study guide note:

---

# 📬 Benefits & Considerations of Pub-Sub / Messaging Queues

---

## ✅ Benefits of Pub-Sub

1. **Decoupling**

   * Services can scale independently.
   * Improves fault tolerance: failure of one service does not block others.

2. **Load Leveling (Shock Absorber)**

   * Smooths spikes in traffic by queuing messages.

3. **Buffering & Reliability**

   * Messages persist in the queue until successfully processed.
   * Ensures reliable communication between systems.

---

## 🛠️ Use Cases

1. **Communication between microservices**

   * Decouples services and allows async interactions.

2. **Async Processing / Task Scheduling**

   * Offloads long-running tasks to background workers.

3. **Event-Driven Pipelines / Event Tracking**

   * Captures and processes events (e.g., user actions, notifications).

4. **Data-Driven Pipelines**

   * Feeds data to multiple downstream systems asynchronously.

5. **Logging**

   * Collect logs reliably from multiple services for processing/analytics.

---

## ⚠️ Cons / Limitations

1. Cannot perform synchronous tasks.

2. **Higher latency** compared to direct API calls

   * Latency = time from adding task to queue → task processed by consumer.
   * Usually small (<2ms if queue is empty).

3. **Additional infrastructure required**

   * Messaging queues often run on clusters of servers.

4. **Higher network overhead**

   * Extra communication between producers, queue, and consumers.

---

## 💡 Need to Justify

* Do **not use message queues unnecessarily**.
* They are **complex to setup, use, and maintain**.
* Must have a clear **justification** for using them.

---

## 📌 Most Common Message Queues

1. **Apache Kafka**

   * Most popular, scalable, feature-rich.
   * Can deploy self-managed or use **managed services** like Confluent.

2. **RabbitMQ**

   * Common, simpler, less powerful than Kafka.

3. **Amazon SQS**

   * Fully managed service, no setup required.
   * Internally uses Kafka and other technologies.

---

# 🟢 Apache Kafka

---

### 🔹 Overview

* **Open Source:** Originally built at LinkedIn, now part of Apache.
* **High Throughput:** Can handle **up to 10M messages/sec** (trillions/day).
* **Ultra Low Latency:** Typically **<2ms** from insertion to consumption if queue is empty.
* **Horizontal Scalability:**

  * Manages partitions automatically across brokers.
  * Supports **1000s of brokers**, **100,000s of partitions**, **petabytes of data**.
* **Fault Tolerant:**

  * Replicates messages across multiple servers.
  * Stores messages on disk.
* **High Availability:** Clusters can be deployed across multiple availability zones.
* **Persistent:**

  * Messages are saved to disk.
  * Multiple consumer groups can consume the same message.
* **Message Ordering:** Strict ordering **within each partition**.
* **Battle-tested:** Used by major companies and thousands of others.

---

### 🔹 Message (Record / Event / Task)

* Records that **“something happened”** in the system or business.

**Structure:**

```json
{
  "topic": "...",      // queue/topic for this message
  "value": "...",      // payload (JSON / string / binary)
  "timestamp": "...",  // creation or append time (auto-filled)
  "key": "...",        // optional, for partitioning
  "headers": "..."     // optional, routing/processing info
}
```

**Kafka Notes:**

* Append-only log
* Strict FIFO reads **within a partition**
* Cannot update, delete, or search messages
* Messages auto-delete after ~7 days
* Message size should be **a few KBs at most**

---
## 🔹 Producers & Consumers

### Producers

* Applications that **publish/write events** to Kafka.
* Fully decoupled from consumers — they **never wait** for consumers to process messages.

### Consumers

* Applications that **subscribe/read and process events** from Kafka.
* Fully decoupled from producers.

---

# 🔹 Consumer Groups (Scalability)

**Challenges:**

1. A single consumer may not handle all messages (e.g., 10M/sec).
2. Multiple types of consumers may need the same messages.

**Solution:**

* Use **multiple consumers per task category**.
* Consumers must provide a **group.id** when joining.
* Kafka assigns a **coordinator** for each consumer group.

  * Consumers send **heartbeats** to the coordinator to remain alive.
* Messages are **distributed among consumers** in a group, allowing **parallel processing**.

---

# 🔹 Topics

* Messages are categorized into **topics**.
* Each message belongs to **exactly one topic**.
* Think of a topic as a **folder**, and messages as **files** (Kafka literally stores them like this).

**Reference:** [Kafka ProducerRecord JavaDoc](https://kafka.apache.org/39/javadoc/org/apache/kafka/clients/producer/ProducerRecord.html)

**Rules:**

* Producers **must specify the topic** when sending a message.
* Topics can have:

  * Zero, one, or many **producers** writing events.
  * Zero, one, or many **consumers** subscribing to events.

---

# **Kafka: Partitions (Message Ordering & Scalability)**

### 🔹 **Challenge**

1. A single server is **not enough** to store all messages in a topic.

   * Topics like `"1-1 chat messages"` or `"tweets"` can contain **billions of events**.
   * Hence, topics must be **partitioned** to distribute storage across multiple brokers (servers).

2. Sometimes, we need **strict message ordering** (e.g., chat messages, GPS coordinates).

   * Ensuring strict ordering across servers requires **distributed locks**, which are **slow and complex**.

---

### 🔹 **Solution**

* A **topic** is divided into multiple **partitions**.
* Each **partition** is stored entirely on a **single Kafka broker**.

  * It can be **replicated** to other brokers for **fault tolerance**.
* **Publishers and consumers** can read/write across multiple partitions, giving **high throughput**.
* Kafka guarantees **ordering only within a single partition** (not across partitions).

---

### 🔹 **Partition Assignment (Which partition gets the message?)**

* If the event has a **key**, Kafka uses:

  ```
  partition = hash(key) % number_of_partitions
  ```
* If the event has **no key**, Kafka uses **round-robin assignment** to partitions.
* All messages with the **same key** always go to the **same partition**, preserving ordering.

**Example message:**

```json
{
  "key": "conversation_id",
  "topic": "messages",
  "value": {
    "message": "Hi",
    "prev_message_id": "...",
    "attachment_url": "...",
    "geolocation": "..."
  },
  "timestamp": "...",
  "headers": { }
}
```

---

### 🔹 **Consumer–Partition Mapping & Consumer Offsets**

* Each **partition** in a topic is consumed by **exactly one consumer** in a **consumer group**.
* Kafka maintains a **consumer offset** (integer) for every *(partition, consumer)* pair → tells the consumer which message to read next.
* Offsets are stored in a special topic: `__consumer_offsets`.

**Rules:**

* Same partition → only one consumer per group.
* Same consumer → can consume from multiple partitions.
* Multiple groups can consume from the same partition independently.

---

### 🔹 **Best Practices**

* Ensure:

  ```
  #partitions ≥ #consumers
  ```

  * Extra consumers = idle.
  * A consumer can handle multiple partitions, but a partition can’t go to multiple consumers.

* Create **more partitions than needed** at the start (scales better later).

  * Changing partition count later is **possible but risky**:

    * May cause **downtime**.
    * May **break delivery guarantees** (offsets change).

---

### 🔹 **Rebalancing**

* When a consumer **joins or leaves** a group, Kafka **reassigns partitions** among remaining consumers.
* A **group coordinator** broker manages this, maintaining **heartbeats** to track active consumers.

---

### 🔹 **Partition Facts**

* Number of partitions = configured **per topic**.
* A single **Kafka broker** can store **multiple partitions**.
* Each partition lives **fully inside one broker**, but is **replicated** to others.
* Kafka uses **partition-based sharding** with **master-slave replication** for fault tolerance.

---

Here’s your **Kafka Delivery Guarantees** section — fully formatted into a clear, concise **study guide style**, matching your previous sections (no tables, just structured markdown):

---

# **Kafka Delivery Guarantees**

Kafka provides three types of message delivery guarantees:

### 🔹 **1. At Most Once**

* Messages **may be lost**, but **never redelivered**.
* Delivery count: **0 or 1**, never more than once.
* No duplicates, but possible data loss.

### 🔹 **2. At Least Once**

* Messages are **never lost**, but **may be redelivered**.
* Delivery count: **1 or more times** (duplicates possible).
* Safe but can cause duplicate processing.

### 🔹 **3. Exactly Once**

* Each message is **delivered once and only once**.
* No data loss, no duplication.
* This is the **ideal** guarantee most systems want.

---

## **Producer Delivery Guarantees**

When a **producer or Kafka broker** crashes, message delivery reliability depends on how Kafka handles failures.

### 💡 **Possible Failure Scenarios**

1. **Producer fails** before sending message → message never reaches Kafka.
2. **Network fails** → Kafka never receives the request.
3. **Kafka broker receives message but crashes before saving** → message lost.
4. **Kafka saves message but crashes before acknowledging** → uncertain delivery.
5. **Kafka saves & acknowledges, but ack never reaches producer** → producer retries.

### 🔸 **How Kafka Handles It**

* Kafka **commits messages to disk** for durability.
* **Producer retries** automatically on failure.
* Kafka producers can use **idempotent mode**:

  * Retries won’t create duplicates — same message written only once.
  * Can be disabled for lower latency (but increases duplicate risk).

✅ **Result:**

* Thanks to retries + idempotency → **Producers achieve “exactly once” delivery** (to Kafka).

---

## **Consumer Delivery Guarantees**

Consumers must **commit offsets** to Kafka to track progress.
Depending on when this happens, delivery semantics change.

### **a. Read → Commit → Process**

➡️ **At Most Once Delivery**

* Message might be lost if consumer crashes before processing.
* Consumer commits offset early, so replacement consumer skips that message.

### **b. Read → Process → Commit**

➡️ **At Least Once Delivery**

* Safe against data loss, but duplicates possible.
* If crash happens before committing, new consumer will reprocess same message.

---

## **Exactly Once Delivery (End-to-End)**

To achieve **exactly once** semantics end-to-end:

* Use **Kafka Transactions** (supported in Kafka Streams).
* Or, store the **consumer offset and output data together atomically** (custom implementation).
* This ensures each message is processed and recorded exactly once.

---

## **Kafka’s Default Behavior**

* By default, Kafka provides **At-Least-Once** delivery:

  * Producers retry on failure.
  * Consumers process before committing offset.

**Implications:**

* Safe from data loss.
* But **duplicate messages** can occur.

---

## **Important Note**

* Kafka guarantees depend on **how producers and consumers are configured**.
* A consumer can even **manually reset or skip offsets** for reprocessing.
* Therefore, the **true delivery guarantee** is ultimately determined by your **application logic**.

---

# **Kafka Brokers (Sharding & Replication)**

### 🔹 **What is a Broker?**

* A **Broker** in Kafka is simply a **server** running the Kafka software.
* Each broker:

  * Stores messages in **logs**.
  * Manages partitions of topics assigned to it.
  * Handles both **producer writes** and **consumer reads**.

---

## **1. Sharding**

* Kafka **shards** data by:

  * **Topic** → Logical grouping of messages.
  * **Partition** → Subset of a topic, distributed across brokers.
* Each broker holds **one or more partitions** of different topics.

---

## **2. Replication**

* Each partition is **replicated across multiple brokers** to ensure **fault tolerance**.
* Replication follows a **master-slave (leader-follower)** model:

  * **Leader (master)** handles all reads and writes for that partition.
  * **Followers (slaves)** replicate data from the leader.

### **Write & Read Behavior**

* **Writes:** Go to the **leader** and (optionally) to a **majority of replicas**.
* **Reads:** Served from any **in-sync replica (ISR)**, typically the leader.
* A message is considered **“committed”** only when:

  * It’s successfully written to **all replicas** (leader + followers).

### **Producer & Consumer Interaction**

* **Producer options:**

  * Can choose to wait for **full replication (strong consistency)** before acknowledging success.
  * Or return **quick acknowledgment** after writing only to the leader (faster but less consistent).
* **Consumer behavior:**

  * Consumers only read **committed messages** — ensuring they see consistent data.

---

## **3. Replication Details**

* **Replication factor:** Configurable per topic (commonly 3 for production).
* **Master distribution:** Kafka evenly distributes leaders across brokers for load balancing.
* **Consistency preference:** Kafka prioritizes **consistency over availability** (especially during partitions).

---

## **4. Message Retention Policy**

* Kafka retains messages for a **default of 7 days**.
* During this retention window:

  * Messages can be consumed **by any number of consumers**, but only **once per consumer group**.
* After the retention period:

  * Kafka **automatically deletes** the messages, regardless of whether they were consumed.

### **Retention Configuration**

* Can be configured by:

  * **Time-based retention** (e.g., 7 days, 24 hours)
  * **Size-based retention** (e.g., 1GB per partition)

---

✅ **Summary**

* Kafka brokers form the backbone of Kafka clusters.
* They manage **sharding (partitions)** and **replication (redundancy)**.
* Kafka ensures **fault tolerance**, **high throughput**, and **consistent reads** through leader-based replication and configurable retention.

---

# 🧩 Kafka Core Relationships Explained

---

## **1️⃣ Topic — The Logical Channel**

Think of a **topic** as a **category** or **stream name**.

📦 Example:
A topic named `"user-signups"` stores all signup events.

* It’s **just a logical name** — like a folder name.
* Inside it, Kafka physically stores data in **partitions**.

```
Topic: user-signups
 ├── Partition 0
 ├── Partition 1
 └── Partition 2
```

---

## **2️⃣ Partition — The Unit of Parallelism**

Each **topic** is divided into **partitions**.

* A **partition** is an **ordered, immutable log** of messages.
* Every message inside a partition gets a **unique offset** (0, 1, 2, …).
* Kafka **appends** new messages to the **end** of a partition.
* Each partition is stored **on one broker (leader)** and replicated to others (followers).

### 📘 Why partitions matter:

* **Scalability:** More partitions = more parallel reads/writes.
* **Ordering:** Kafka guarantees **message order only within a partition**, not across partitions.

---

## **3️⃣ Broker — The Physical Server**

A **broker** is simply a Kafka **server**.

Each broker:

* Stores **one or more partitions**.
* Acts as the **leader** for some partitions and **follower** for others.
* Communicates with other brokers to **replicate data** and ensure fault tolerance.

### Example:

| Broker   | Partitions Hosted | Role                           |
| -------- | ----------------- | ------------------------------ |
| Broker 1 | P0, P3            | Leader for P0, Follower for P3 |
| Broker 2 | P1, P0(replica)   | Leader for P1, Follower for P0 |
| Broker 3 | P2, P1(replica)   | Leader for P2, Follower for P1 |

🧠 So, a **topic is distributed** across multiple brokers using **partitions**.

---

## **4️⃣ Consumer & Consumer Groups**

### 🎯 **Consumer**

A **consumer** reads messages from a **topic’s partitions**.

* It remembers where it left off using **offsets**.
* It only reads **committed messages** (replicated and acknowledged).

---

### 👥 **Consumer Group**

A **consumer group** is a **set of consumers working together** to read from a topic **in parallel**.

Kafka assigns **each partition to exactly one consumer** in the group.

| Topic: user-signups | Partitions | Assigned Consumer |
| ------------------- | ---------- | ----------------- |
| Partition 0         | Consumer A |                   |
| Partition 1         | Consumer B |                   |
| Partition 2         | Consumer C |                   |

💡 Rules:

1. **Each partition → only one consumer** in a consumer group.
2. But **multiple consumer groups** can consume the same topic independently.

So:

* Consumer Group 1 (for analytics)
* Consumer Group 2 (for monitoring)
  Both can read the same topic — Kafka will maintain separate offsets.

---

## **5️⃣ Relationship Overview**

Let’s visualize it together 👇

```
                ┌────────────────────────────┐
                │         TOPIC: orders      │
                └────────────────────────────┘
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
      Partition 0                    Partition 1
   (Leader: Broker 1)             (Leader: Broker 2)
       ▲      ▲                        ▲      ▲
Follower│      │Follower          Follower│      │Follower
Broker 2│      │Broker 3          Broker 1│      │Broker 3

          (Replication between brokers)

Consumer Group 1:
   Consumer A → Partition 0
   Consumer B → Partition 1

Consumer Group 2:
   Consumer X → Partition 0
   Consumer Y → Partition 1
```

---

## **6️⃣ Golden Rules Summary**

| Concept            | Rule                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------- |
| **Topic**          | Logical channel for messages (split into partitions)                                  |
| **Partition**      | Ordered log of messages; order guaranteed *within* partition                          |
| **Broker**         | Kafka server storing partitions (leaders & replicas)                                  |
| **Replication**    | Each partition is copied across brokers for fault tolerance                           |
| **Consumer**       | Reads data from partitions                                                            |
| **Consumer Group** | Ensures each partition is processed by only one consumer within the group             |
| **Offset**         | Position marker of a consumer within a partition                                      |
| **Ordering**       | Only guaranteed within a single partition                                             |
| **Parallelism**    | Number of partitions = max number of consumers that can read in parallel (in a group) |

---

## **7️⃣ Example Summary Scenario**

🧩 Topic: `"payments"`
🧩 Partitions: 3
🧩 Brokers: 3
🧩 Replication factor: 3
🧩 Consumer Group: `"payment-processor"` with 3 consumers

* Each partition lives on a different broker (with replicas on others).
* Each consumer in the group gets **one partition**.
* All consumers together read the entire topic **in parallel**.
* If a consumer crashes, Kafka **reassigns** its partition to another consumer automatically.

---

✅ **TL;DR:**

* **Topic:** logical stream
* **Partition:** subset of topic (enables scaling)
* **Broker:** server storing partitions
* **Consumer Group:** set of consumers dividing the partitions
* **Rule:** one partition → one consumer (per group)
* **Result:** Kafka scales horizontally, keeps order per partition, and allows multiple independent consumer groups.

---

# 🧭 Kafka Cluster Coordination: ZooKeeper vs KRaft

---

## 🧱 1️⃣ Why Kafka Needed ZooKeeper

Kafka itself is a **distributed system** — meaning it runs across many brokers (servers).
To work properly, it needs a **single source of truth** for cluster coordination.

Kafka brokers need to know:

* Which brokers are alive?
* Which broker is the **leader** for each partition?
* Where is each **replica** stored?
* What’s the **offset** of each consumer group?
* What **topics** exist and how many **partitions** they have?

Kafka didn’t originally include a built-in coordination system — so it used **ZooKeeper**.

---

## ⚙️ 2️⃣ What ZooKeeper Does (in Kafka)

ZooKeeper maintains **metadata** and does **cluster coordination** for Kafka.

| Responsibility                     | Description                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| 🧠 **Broker registry**             | Keeps track of which brokers are alive (via heartbeats).                                         |
| 🗂️ **Topic & partition metadata** | Stores info about which topics exist, how many partitions each has.                              |
| 🧭 **Partition leadership**        | Keeps info about which broker is the **leader** and which are **followers** for every partition. |
| 👥 **Consumer group coordination** | Maps which consumer owns which partition (consumer rebalancing).                                 |
| 📍 **Offsets tracking**            | Keeps last committed offset for each (consumer group, topic, partition).                         |
| 🔐 **Access control & quotas**     | Stores ACLs, quotas, configurations, etc.                                                        |

🧩 ZooKeeper is basically a **configuration & coordination database** for Kafka.

---

## ⚡ 3️⃣ How Kafka & ZooKeeper Communicate

### Simplified flow:

1. Kafka broker starts → registers itself in ZooKeeper.
2. ZooKeeper tracks broker health using **heartbeats**.
3. When a broker dies, ZooKeeper tells other brokers to **elect a new leader** for its partitions.
4. When new topics or partitions are created, ZooKeeper stores this configuration.
5. Kafka Controller (a special broker) gets metadata from ZooKeeper and manages replication & rebalancing.

So ZooKeeper was **central to everything**, but this also led to **scalability issues**.

---

## ⚠️ 4️⃣ Limitations of ZooKeeper

| Problem                         | Description                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| 🧩 **Two systems = complexity** | Kafka had to run **and manage ZooKeeper** separately. Harder to maintain and secure. |
| 🐢 **Performance bottleneck**   | ZooKeeper couldn’t handle frequent writes (like offset commits) at high scale.       |
| 🧱 **Scalability limit**        | Kafka clusters with >200,000 partitions caused ZooKeeper lag and instability.        |
| 🧠 **Split-brain risks**        | In network failures, ZooKeeper and Kafka controller could get out of sync.           |
| 🧰 **Manual recovery**          | Recovering from ZooKeeper corruption was painful and required manual fixes.          |

---

## 🚀 5️⃣ Enter KRaft (Kafka Raft Metadata Mode)

Starting from **Kafka 2.8 (2021)**, Kafka introduced **KRaft mode** —
Kafka’s own internal **metadata quorum** based on the **Raft consensus algorithm**.

🧠 **KRaft = Kafka + Raft**

It **removes the need for ZooKeeper entirely** and lets Kafka manage itself.

---

## 🧩 6️⃣ What KRaft Does

Everything ZooKeeper did — but *inside Kafka itself* using Raft.

| Function             | ZooKeeper (old)            | KRaft (new)                 |
| -------------------- | -------------------------- | --------------------------- |
| Metadata store       | Separate ZooKeeper cluster | Stored inside Kafka itself  |
| Consensus algorithm  | ZooKeeper’s Zab protocol   | Raft consensus protocol     |
| Cluster coordination | External process           | Internal Kafka quorum       |
| Controller           | One broker elected via ZK  | One broker elected via Raft |
| Scalability          | ~200K partitions           | Millions of partitions      |
| Recovery             | Manual, fragile            | Automated, self-healing     |

---

## ⚙️ 7️⃣ Raft Consensus in KRaft (simplified)

Raft ensures **consistency** and **high availability** of metadata.

1. Kafka cluster has **Controller Quorum Nodes** (a few brokers dedicated to metadata).
2. One becomes the **Controller Leader**.
3. All metadata changes (like new topic, partition reassignment, etc.) go through the leader.
4. The leader replicates metadata logs to the follower nodes.
5. If leader fails, followers elect a **new leader** automatically (via Raft election).

---

## 🧩 8️⃣ Timeline Summary

| Kafka Version | Coordination Mode          | Notes                        |
| ------------- | -------------------------- | ---------------------------- |
| ≤ 2.7         | ZooKeeper only             | Standard setup               |
| 2.8           | KRaft introduced (preview) | Dual support                 |
| 3.5           | ZooKeeper deprecated       | Use KRaft for new clusters   |
| 4.0 (≈2025)   | KRaft only                 | ZooKeeper completely removed |

---

## 🧮 9️⃣ How to Choose Today

| Use Case                                    | Recommendation                             |
| ------------------------------------------- | ------------------------------------------ |
| New Kafka cluster (2025+)                   | ✅ Use KRaft only                           |
| Legacy Kafka cluster                        | ☑️ Upgrade gradually using migration tools |
| Want simplicity (no ZooKeeper ops)          | ✅ KRaft mode is ideal                      |
| Need ultra-large cluster (>200k partitions) | ✅ KRaft required                           |

---

## 🧠 TL;DR Summary

| Concept                     | ZooKeeper                           | KRaft                        |
| --------------------------- | ----------------------------------- | ---------------------------- |
| Purpose                     | External metadata store             | Internal Raft-based metadata |
| Protocol                    | Zab (ZooKeeper Atomic Broadcast)    | Raft Consensus               |
| Setup                       | Requires separate ZooKeeper servers | Integrated in Kafka brokers  |
| Scalability                 | Limited to ~200k partitions         | Millions of partitions       |
| Failure handling            | Slower, manual                      | Automatic Raft re-election   |
| Introduced in               | Kafka 0.x (original)                | Kafka 2.8 (2021)             |
| Fully replaces ZooKeeper in | Kafka 4.0 (2025)                    | —                            |

---

### 🔄 ZooKeeper vs KRaft — Additional Reference

* For more details on the **Raft Consensus Algorithm**, see the official Raft website:
  [https://raft.github.io](https://raft.github.io)

---

# 🦓 ZooKeeper

## Overview

**ZooKeeper** is a **distributed coordination service** used by distributed applications to handle:

* Synchronization
* Configuration management
* Naming and group services

> ⚠️ **Note:**
> ZooKeeper is **NOT a database**.
> It is meant for **storing backend configuration and coordination data**, **not** business or user-generated data.

ZooKeeper ensures **immediate consistency** across distributed backends.

---

## 🗂️ ZooKeeper Filesystem

ZooKeeper exposes a **special filesystem-like structure** accessible over the network through APIs.

### 🧱 Core Concepts

#### 🔹 ZNodes

* Every file or directory in ZooKeeper is called a **ZNode**.
* ZNodes can be of two types:

  1. **Persistent ZNodes** – regular files or directories that remain even after the client disconnects.
  2. **Ephemeral ZNodes** – temporary files/directories **owned by a server**.

     * Exist only as long as the session with the owning server is alive.
     * If the server disconnects or fails, ZooKeeper automatically deletes its ephemeral nodes.
     * Each ephemeral ZNode has exactly **one owner**.
     * Only the owner can **modify** it; others can **read** or **watch** it.

---

### 📦 What Can Be Stored

You can store **small configuration files** (typically a few KBs, up to a few MBs).
✅ Suitable for:

* Backend configuration data
* Metadata (master-slave configs, secrets, service locations)

🚫 Not suitable for:

* User data
* Business logic data

---

### 🗃️ Example ZooKeeper Structure

```
/
|-- db_secret_key.txt
|-- openai_api_key.txt
|-- aws_iam_key.txt
|-- master_slave_config/
|   |-- master_ip
|   |-- slaves/
|       |-- a3b2c_ip.txt
|       |-- 2ccfd_ip.txt
|       |-- 13aa4_ip.txt
|       |-- dd12f_ip.txt
```

---

## 🧠 Example Scenario: Watching for Key Changes

### Scenario:

An application server needs to use an **OpenAI API key** stored in ZooKeeper.

When the server starts:

* It retrieves the key from ZooKeeper.
* It **sets a “watch”** on the key so that if the key changes, ZooKeeper pushes the updated value automatically.

---

### 🖥️ Code Flow (Conceptual)

```java
String key = zookeeperClient.setWatch("/openai_api_key.txt", handleKeyChange);
```

#### On Each User Request

```java
void handleUserRequest() {
    openAiClient.call(OpenAiApiKey, "<System Prompt>");
}
```

> ❌ The app should **NOT fetch the key every time** from ZooKeeper.
> ✅ Instead, it should keep a **local copy** and **update it automatically** when ZooKeeper notifies of a change.

---

### 🧩 How Watching Works

Clients (servers) can **set a watch** on a ZNode.

If the node’s data changes:

* ZooKeeper **pushes the new value** to the client via the persistent session.

#### Example Pseudocode:

```java
string open_ai_api_key = "";

void fetch_openai_key() {
    zookeeperClient.setWatch("/openai_api_key", onKeyUpdate);
}

void onKeyUpdate(value) {
    open_ai_api_key = value;
}

onServerStart => {
    zookeeperClient.initialize();
    fetch_openai_key();

    zookeeperClient.onDisconnect(() => {
        open_ai_api_key = ""; // prevent using stale data
    });
}
```

---

✅ **Summary**

* ZooKeeper acts as a **coordination layer**, not a database.
* Data is stored as **ZNodes** (persistent or ephemeral).
* Servers can **watch nodes** for real-time configuration updates.
* Ephemeral nodes are automatically deleted when their owning server fails.

---

Here’s a **clean, structured version** of your Zookeeper replication & master-slave configuration notes, keeping all technical details and links intact:

---

# 🧭 Zookeeper — Replication & Master-Slave Management

## 🔹 Replication

* Zookeeper itself is **replicated** using a **Master-Slave (Quorum)** configuration.
* Ensures **high availability** and fault tolerance.
* Writes are only allowed to the **leader/master**, while reads can be served by followers.

---

## 🔹 Sharding

* **Zookeeper is NOT sharded!**
* It’s **not a database** — only designed for **small configuration data** (few MBs).
* Use nested ZNodes if you want logical separation (e.g., per shard).

---

## 🔹 Managing Master-Slave Configuration via Zookeeper

Zookeeper can maintain your **custom Master-Slave system**, e.g., for a database shard.

### Steps for Master Election

1. Maintain a **master-slave config** in Zookeeper.
2. Master must own a **`master_ip` ephemeral ZNode**.
3. All slaves set a **watch** on the `master_ip` node.
4. If the master crashes:

   * Heartbeats stop → Zookeeper deletes the **ephemeral node**.
   * Zookeeper notifies all slaves.
5. All slaves attempt to **create the `master_ip` node** with their own IP.
6. The **first slave** to succeed becomes the new master.

   * Zookeeper ensures only **one owner** can modify ephemeral nodes.
7. Zookeeper notifies all slaves of the new master.

🔗 **Optimized leader election recipe:** [Zookeeper Leader Election](https://zookeeper.apache.org/doc/current/recipes.html#sc_leaderElection)

---

### Handling Master Recovery

* When the old master comes back online, it **joins as a slave**.
* **Data consistency:**

  * Slaves might have stale data individually.
  * Majority of replicas are up-to-date → system consistency maintained.
* **Challenge:** New master cannot immediately accept writes if it may be stale.

  * Developer must implement a **catch-up mechanism**.

🔗 **Sample approach:** [Kafka Leader Recovery](https://kafka.apache.org/documentation/#design:~:text=But%20followers%20themselves,these%20for%20now)
🔗 **Kafka approach:** [Kafka Leader Election](https://kafka.apache.org/documentation/#design:~:text=Kafka%20takes%20a,losing%20committed%20messages)

---

### Failure Scenarios

1. **Only Master crashes**

   * Slaves compete for election → one succeeds → new master elected. ✅

2. **Zookeeper master crashes**

   * Does **not affect your application data**.
   * Zookeeper only stores **internal config**, not user data.
   * Cannot perform **writes/changes** until Zookeeper leader is re-elected.
   * Reads still work.

3. **Both Master & Zookeeper leader crash simultaneously**

   * Master re-election must **wait for Zookeeper leader recovery**.
   * Slightly higher latency for master election. ⚠️

---

### Managing Multiple Shards with Replication

* Simply **nest shard data** in Zookeeper:

```
/
|--- shard_1/
|    |--- master_ip.txt
|    |--- slaves/
|        |--- ...
|--- shard_2/
|    |--- master_ip.txt
|    |--- slaves/
|        |--- ...
```

* Each shard can have **its own master-slave election** independently.
* Zookeeper handles ephemeral nodes and notifications for all shards.

---

# 📚 Kafka Resources

### 1️⃣ Basics

* [Kafka Fundamentals – Basic Terminology](https://www.conduktor.io/kafka/kafka-fundamentals/)
* [Kafka Motivation & Opinionated Design](https://kafka.apache.org/documentation/#design)

### 2️⃣ Partitions & Topics

* [How to Choose the Number of Topics/Partitions in a Kafka Cluster | Confluent](https://www.confluent.io/blog/how-to-choose-the-number-of-partitions-in-a-kafka-cluster/)
* Note: Apache Kafka supports **up to 200K partitions per cluster**.

### 3️⃣ Replication

* [Choosing the Replication Factor and Partition Count](https://kafka.apache.org/documentation/#replication)

### 4️⃣ Offset Management

* [Kafka Consumer for Confluent Platform](https://docs.confluent.io/platform/current/clients/consumer.html)
* [Kafka – When to Commit? | Quarkus](https://quarkus.io/guides/kafka#consumer-offset-management)

### 5️⃣ Message Retention & Deletion

* [Kafka Topic Configuration: Log Retention](https://kafka.apache.org/documentation/#topicconfigs_retention)
* [Kafka Retention — Types, Challenges, Alternatives](https://www.confluent.io/blog/kafka-retention-deletion/)

### 6️⃣ Kafka as a Service

* [Confluent Kafka Overview](https://docs.confluent.io/kafka/overview.html)

### 7️⃣ Kafka vs Other MQs

* [Kafka vs RabbitMQ vs SQS | Ably](https://ably.com/topic/apache-kafka-vs-rabbitmq-vs-aws-sns-sqs)
* [AWS Compare RabbitMQ & Kafka](https://aws.amazon.com/compare/the-difference-between-rabbitmq-and-kafka/)
* [Kafka vs SQS | Svix](https://www.svix.com/resources/faq/kafka-vs-sqs/)
* [RabbitMQ vs SQS | Svix](https://www.svix.com/resources/faq/rabbitmq-vs-sqs/)

---

# 🧭 Zookeeper Resources

### 1️⃣ Overview & Design

* [Zookeeper Design Goals](https://zookeeper.apache.org/doc/current/zookeeperOver.html#sc_designGoals)

### 2️⃣ Data Model

* [Persistent & Ephemeral Nodes Overview](https://zookeeper.apache.org/doc/r3.4.13/zookeeperOver.html#sc_dataModelNameSpace)
* [Programmer’s Guide – Data Model](https://zookeeper.apache.org/doc/r3.4.13/zookeeperProgrammers.html#ch_zkDataModel)

### 3️⃣ Recipes & Use Cases

* [Distributed Priority Queue](https://zookeeper.apache.org/doc/r3.4.13/recipes.html#sc_recipes_Queues)
* [Distributed Locks](https://zookeeper.apache.org/doc/r3.4.13/recipes.html#sc_recipes_Locks)
* [Two-Phase Commit](https://zookeeper.apache.org/doc/r3.4.13/recipes.html#sc_recipes_twoPhasedCommit)
* [Master Election in Master-Slave](https://zookeeper.apache.org/doc/r3.4.13/recipes.html#sc_leaderElection)

### 4️⃣ Implementation & Code (Optional)

* **Observer pattern**

  * ObserverBean.java
  * WatchManager.java
* **File structure / DataTree**

  * [Data Model Namespace](https://zookeeper.apache.org/doc/r3.9.1/zookeeperOver.html#sc_dataModelNameSpace)
  * DataNode.java
  * DataTree.java
* **Leader Election**

  * Algorithm overview: [Quora Explanation](https://www.quora.com/How-is-a-leader-elected-in-Apache-ZooKeeper)
  * FastLeaderElection.java

---
