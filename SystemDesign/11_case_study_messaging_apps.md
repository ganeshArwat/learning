# 📱 **Study Guide: Messaging Apps (System Design)**

---

## 🧩 **Problem Statement**

### 🧠 Reason by Analogy

Understand messaging apps by comparing them to existing products and their use cases.

| Category                   | Examples                                          | Characteristics                                                   |
| -------------------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| **Mobile-first Chat**      | WhatsApp, Telegram, Signal, Hike, iMessage        | - Realtime, low-latency chat<br>- Built as SMS replacement        |
| **Enterprise Chat**        | Slack, MS Teams, Flock                            | - B2B focus<br>- Group chat for workplace collaboration           |
| **Social Media Messaging** | Facebook Messenger, Instagram DMs, Orkut Messages | - Focus on connecting social users<br>- Primarily 1-to-1 messages |

---

## ⚙️ **Functional Requirements (FR)**

### 👥 Actors

* **User**: The primary participant in all messaging operations.

---

### 🚀 **MVP Features**

#### 1. Send Message (1-to-1)

```plaintext
sendMessage(sender_id: uuid, recipient_id: uuid, message: json) → ack/failure
```

* Allows one user to send a message to another.

#### 2. Receive and View Messages

```plaintext
getMessages(user_id: uuid, conversation_id: uuid, pagination_offset: int, pagination_limit: int) → list of messages
```

* Users can fetch past messages in a conversation (most recent first).
* Users can only access messages from conversations they are part of.

#### 3. View Conversations

```plaintext
getConversations(user_id: uuid, pagination_offset: int, pagination_limit: int) → list of conversations
```

* Lists all conversations the user participates in (most recent first).

#### 4. Group Messaging

```plaintext
sendMessageGroup(sender_id: uuid, group_id: uuid, message: json) → ack/failure
getMessagesGroup(user_id: uuid, group_id: uuid, pagination_offset: int, pagination_limit: int) → list of messages
```

* Enables sending and viewing messages in groups.
* Groups can scale to **100,000+ users**.

---

## 🌱 **Future Scope Features**

| Feature                     | Description                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------ |
| **Message Status Tracking** | Sent → Received by server<br>Delivered → Delivered to recipient<br>Read → Viewed by recipient    |
| **Edit/Delete Messages**    | Modify or remove sent messages (complex to implement reliably)                                   |
| **Notifications**           | In-App + Push notifications                                                                      |
| **Multi-Device Support**    | Sync across devices using **CRDTs** (Conflict-free Replicated Data Types) — very complex feature |

---

## 🚫 **Non-MVP / Out-of-Scope Features**

| Category                  | Examples                                               |
| ------------------------- | ------------------------------------------------------ |
| **Rich Messages**         | Emojis, Images, Videos, GIFs                           |
| **Profile Management**    | User bios, avatars, settings                           |
| **End-to-End Encryption** | Security-focused feature, hard to integrate early      |
| **Broadcast Messaging**   | Send same message to multiple users (batch processing) |


---

# ⚙️ **Non-Functional Requirements (NFR)**

---

## 🔁 **1. Message Order**

* The **order of messages** in a conversation is **critical**.
* **Meaning can change** if messages are displayed out of order.
  Example:

  > “I’m breaking up with you.” → “Just kidding 😂”
  > (If reversed, the meaning completely changes!)

✅ **Goal:** Ensure messages are always displayed in **the exact sequence they were sent**.

---

## 🔂 **2. Idempotency**

* Messaging apps must handle **network (n/w) failures** gracefully.
* Clients often **auto-retry** sending messages when acknowledgments (ACKs) aren’t received.

### ⚙️ **Auto-Retry Algorithm**

1. Client sends a request to the server.
2. Server processes the request successfully.
3. Server sends an **ACK** (acknowledgment).
4. Client receives ACK → request considered complete.
5. If ACK **isn’t received**, the client **retries** automatically.

---

### ⚠️ **Problem Scenario**

If:

* The original request **reaches the server**
* Server **stores the message** and **sends an ACK**
* But the **ACK is lost** (network failure)

Then:

* The **client thinks** the message failed.
* It **retries** the request.
* Server **stores the same message again** → **duplicate messages**.

---

### 💡 **Solution: Idempotency Handling**

* Use **unique message IDs (UUIDs)** per request.
* Before storing a message, the server should:

  * **Check** if that message ID already exists.
  * If yes → **ignore the duplicate**.
  * If no → **store and acknowledge**.

✅ **Result:** Prevents accidental duplicates caused by automatic retries.

---

### 😅 **Exception: Intentional Re-sends**

* If a **user intentionally** sends the same message multiple times (e.g., “Hi” spam),
  the system **should allow it**.
* Only **automatic retry duplicates** should be filtered out — not **user-initiated repeats**.

---
# ⚖️ **Consistency vs Availability**

---

## 🧠 **1. Consistency**

### 🧩 What Does *Eventual Consistency* (Stale Reads) Mean?

In distributed systems, **eventual consistency** means that all nodes will *eventually* reflect the same data — but **temporary stale reads** may occur.

In a messaging app, this can cause serious confusion and poor user experience.

---

### 💬 **Examples of Stale Reads**

#### 🧍‍♂️ **Sender Side Example**

* Shaurya sends a message to Harpal at **t = 0**.
* The **server ACKs** (acknowledges) the message.
* Shaurya reloads his app at **t = 1**, but **cannot see** the message he just sent.
* He thinks the message was **deleted or lost**, but in reality:

  * The message **exists**.
  * It just hasn’t **replicated** to all databases yet.
  * After some delay, he’ll **eventually see it**.

✅ **Solution:**
Use **Read-Your-Write Consistency**, ensuring that a user can **immediately read their own writes**.

---

#### 👥 **Receiver Side Example**

* Shaurya sends a message to Harpal at **t = 0**.
* Server **ACKs** the message.
* At **t = 1**, Harpal opens the chat — but **doesn’t see** the message yet.
* Shaurya insists he sent it, but Harpal’s app still hasn’t updated.
* Again, the message is **not lost**, only **delayed** due to eventual consistency.

⚠️ This delay can break the illusion of real-time chat — unacceptable in communication apps.

---

### 🚫 **Conclusion**

> Messaging apps **cannot afford** stale reads.
> Real-time communication demands **strong consistency** to ensure both sender and receiver see the same message state instantly.

---

## ⏱️ **2. Consistency vs Latency**

### ⚔️ **The Trade-Off**

According to the **PACELC Theorem**:

> *If there’s a network Partition (P), you must choose between Availability (A) and Consistency (C).
> Else (E), you must choose between Latency (L) and Consistency (C).*

| Goal                                | Challenge                                           |
| ----------------------------------- | --------------------------------------------------- |
| **Strong Consistency**              | Increases latency — messages take longer to confirm |
| **Low Latency & High Availability** | Can cause stale or out-of-order reads               |

---

### 💡 **Practical Reality**

* It’s **impossible** to achieve **high consistency**, **high availability**, and **low latency** *simultaneously*.
* But… we can **create the illusion of consistency** through design techniques such as:

  * Caching with background sync
  * Message queues with delivery guarantees
  * Local echo (showing sent message instantly)

✅ **Goal:**
Sacrifice a *tiny bit* of real consistency, but make the system **appear perfectly consistent** to users **99.999% of the time**.

---
# 📊 **Scale Estimation**

---

## 🌍 Assumptions

* Total Users (Web/Planet Scale): **2 billion**
* Daily Active Users (DAU): **80% of total = 1.6 billion ≈ 2 billion**

---

## 1️⃣ Amount of Load

**Average number of messages per active user per day:** 10–20 messages

**Total number of messages per day:**
= 20 messages × 2 billion active users
= **40 billion messages per day**

**Average messages per second:**
= 40 billion / 100,000 seconds
= 4 × 10⁵ messages/second
= **400,000 messages per second**

**API Load (Average):**

* sendMessage(...): 400,000/sec
* getMessages(...): 2× sendMessage = 800,000/sec
* getConversations(...): only when user reopens the app

So, the system handles roughly **400K writes/sec** and **800K reads/sec** on average.

---

## 2️⃣ Peak Load

* During global events like New Year or pandemic spikes, assume **5× average load**.
* Peak = 5 × 400,000 = **2 million messages per second**

This shows the system must **scale horizontally** to manage extreme peaks.

---

## 3️⃣ Amount of Data (Over 20 Years)

**Message object:**

```
{
  sender_id: uuid (16B)
  receiver_id/group_id/conversation_id: uuid (16B)
  message_id: uuid (16B)
  text: string (200B avg)
  when: timestamp (8B)
  where: geolocation (16B)
  delivery_status: enum (1B)
  attachment_url: string (200B avg)
}
```

**Average size:** ~500 bytes/message

**Data per day:**
500 bytes × 40 billion messages = **20 TB/day**

**Data over 20 years:**
20 TB/day × 365 days × 20 years ≈ **200 Petabytes (PB)**

A single server can store up to ~2 PB, far below the total requirement.
Even with enough capacity, a single server can’t handle **2 million messages/sec**.

✅ **Conclusion:** We definitely need **sharding** — distributing both storage and load across multiple servers.

---

## 4️⃣ Read-heavy or Write-heavy?

* Writes (sendMessage): 400K/sec avg → 2M/sec peak
* Reads (getMessages): 800K/sec avg → 4M/sec peak

Both reads and writes are significant; **neither dominates** the workload.
This system is **both read- and write-heavy**.

We can’t reduce writes (each message must be sent).
To optimize, we reduce **database reads** by caching.

✅ **Final Insight:**
We’ll use **lots of caching** to absorb reads and keep the database optimized for high write throughput.

---

# 🏗️ **System Design**

---

## 🔁 **Idempotency & Message Order**

---

### 🆔 **Message Identification**

* Every message must have a **unique `message_id`**, generated on the **client side** (not server side).
* This ensures that retries or resends can be tracked precisely and deduplicated safely.

---

## 🔄 **Idempotency**

* When the backend receives a `sendMessage()` API call:

  * It checks if the `message_id` already exists in the database.
  * **If not present:** it stores the message normally.
  * **If already present:** it **ignores** the request but still sends a **success response** to the client.

✅ This behavior prevents **duplicate messages** caused by automatic retries from the frontend when acknowledgments (ACKs) are delayed or lost.

💡 **Goal:**
Avoid duplicate message storage while ensuring client-side retries stop after the first successful send.

---

## 🧩 **Message Order**

### 1️⃣ **Why Simple Sorting Fails**

* Sorting messages based on `created_time` or timestamps **does not work** reliably.
* The recipient doesn’t even know that a new message exists until it’s delivered.
* By the time a delayed (older) message arrives, **newer messages** may already have been shown in the chat.
* The backend (message queue, SQS, or buffer) **cannot fix this** — it only processes messages once they arrive.

  * By then, the order issue has already occurred.

---

### 2️⃣ **Why Backend Solutions Don’t Help**

* Even if you use backend buffering or reordering logic:

  * The server still doesn’t know about a message until it arrives.
  * Once later messages are already delivered to clients, it’s **too late** to reinsert an older one in sequence.

---

### 💡 **Solution: Create a Message Chain**

* Every new message includes a reference to its **`previous_message_id`**.
* On the recipient’s side:

  * The app **won’t display** a message until its **previous message** has also arrived and been displayed.
  * If messages arrive **out of order**, the app shows a **“waiting for messages…”** placeholder.
  * Once all previous messages are received, the full chat appears in the correct order.

✅ **Result:**
This client-side chaining ensures **correct message ordering** even with **network delays** or **out-of-order delivery**.

---

## 🧩 Sharding

### 🔑 Sharding Key: `user_id`

**Meaning:**
All data (messages sent and received) of a particular user is stored within the same shard.

#### 🗨️ 1-to-1 Messages

* **`getMessages(user_id, conversation_id, …)`** → Query only the user’s shard.
* **`sendMessage(sender_id, receiver_id, …)`** → Write to both sender and receiver shards (data replication).
* **`recentConversations(user_id)`** → Query only the user’s shard.

#### 👥 Group Messages

* **`getMessages(user_id, group_id, …)`**

  1. **Store in Sender Only:**

     * Each sender’s messages stay in their own shard.
     * Leads to **fan-out reads** (messages spread across shards).
  2. **Store in All Participants:**

     * Fast reads (can read from any shard).
     * But causes **fan-out writes** (message replicated across all shards).

* **`sendMessage(sender_id, group_id, …)`**

  1. **Store in Sender Only:**

     * Stored only in sender’s shard.
  2. **Store in All Participants’ Shards:**

     * Causes fan-out writes.

* **`recentConversations(…)`**

  * Sharding by `user_id` **does not work well for group chats**.
  * Either reads or writes become fan-out operations.

---

### 🔑 Sharding Key: `conversation_id`

**Meaning:**
All messages within a conversation (1-to-1 or group) go to the same shard.

* For **groups**, `conversation_id = group_id`
* For **1-1 chats**, `conversation_id` = unique ID for the user pair

#### 🗨️ 1-to-1 Messages

* **`getMessages(user_id, conversation_id, …)`** → Query the conversation’s shard.
* **`sendMessage(sender_id, receiver_id, …)`** → Write to the conversation’s shard.

  * Conversation ID = pair (`sender_id`, `receiver_id`)
* **`recentConversations(user_id)`**

  * Requires **fan-out** across shards → inefficient.
  * ✅ **Solution:** Maintain a **separate `recentConversations` DB** that tracks last message timestamps for all conversations.
  * Every `sendMessage` updates this DB.
  * The name “recentConversations DB” reflects its usage, not its data scope.

#### 👥 Group Messages

* **`getMessages(user_id, group_id, …)`** → Query the group’s shard.
* **`sendMessage(sender_id, group_id, …)`** → Write to the group’s shard.
* **`recentConversations(user_id)`**

  * Updating this for large groups (e.g., 100K members) leads to **massive fan-out**.
  * ❌ Avoid this API for groups.
  * ✅ Instead, the **frontend** maintains a **local cache of recent conversations**, updated via **notifications**.

---

### ⚖️ Choosing the Right Sharding Key

| Use Case                          | Best Sharding Key | Reason                                                         |
| --------------------------------- | ----------------- | -------------------------------------------------------------- |
| **Facebook Messenger / WhatsApp** | `user_id`         | Groups are small; user-centric sharding works well.            |
| **Slack / Microsoft Teams**       | `conversation_id` | Groups are large; conversation-centric sharding scales better. |

---

## ⚖️ Consistency

### 🧩 PACELC: Consistency vs Availability/Latency

**Problem:**
We want strong consistency across shards, but maintaining it atomically hurts latency and availability.

---

### Option 1: Two-Phase Commit (2PC)

* Write atomically to both shards.
* ❌ **Extremely slow:** low throughput, high latency.
* ❌ **Low availability:** locks resources during commit.

---

### 💡 Alternative: Illusion of Consistency

Instead of atomic writes, we **write one shard at a time** to balance speed and availability.

---

### ✉️ Write to **Sender’s Shard First**

1. **Write to Sender’s shard**

   * **Failure (low latency):**
     → Immediately return failure → client retries.
   * **Success:**

     * Can we return success yet?
       ❌ No, because the message isn’t in the receiver’s shard yet.

       * Sender believes the message was sent.
       * Receiver doesn’t see it → **inconsistent state.**

         * Sender: “I sent it.”
         * Receiver: “I didn’t get it.”

2. **Then write to Receiver’s shard**

   * **Success (low latency):**
     → Return success (both shards updated).
   * **Failure (high latency):**

     * Data inconsistent → message in sender’s shard but missing in receiver’s.
     * Must **retry** or **rollback.**

       * Retry: sender waits = **high latency**.
       * Rollback: locks sender’s shard until rollback finishes → **slow reads.**

➡️ **Verdict:** Writing sender first causes high latency and temporary inconsistency.

---

### ✉️ Write to **Receiver’s Shard First**

1. **Write to Receiver’s shard**

   * **Failure (low latency):**
     → Return failure immediately → sender retries.
   * **Success:**

     * Recipient can already see the message!
     * ✅ Return **success immediately** (even before writing sender’s shard).
     * Very **low latency**.

2. **(Async) Write to Sender’s shard**

   * **Success:** done.
   * **Failure:** retry silently; sender already got ACK, so no waiting.

⚠️ **Edge Case:**
If writing to receiver succeeds but writing to sender fails,
→ When sender reloads, they don’t see their sent message → confusion.

✅ **Fix:** Frontend cache in the client app.

* Cache stores all sent messages that were acknowledged.
* Even if `getMessages` API doesn’t show it yet, the app displays it from cache.

---

### 🪄 Result

By writing to the **receiver’s shard first** and using a **frontend cache** for the sender,
we achieve the **illusion of immediate consistency** —
high availability and low latency without full atomic writes.

---

### ⚙️ Consistency vs Availability (Partition Scenario)

**Example:**
Harini → “Hi” → Aditi

* App Server 1 receives Harini’s message.
* Network partition: Server can reach **Aditi’s shard**, but not **Harini’s shard**.

**Process:**

1. Server writes to Aditi’s shard → ✅ success.
2. Returns success to Harini.
3. Queues a background task to write the message to Harini’s shard later (async).

✅ **Outcome:**

* System remains available:

  * Aditi can see the message (recipient write succeeded).
  * Harini sees it too (via frontend cache).
* Gives illusion of **immediate consistency** even during a partition.

❌ If write to Aditi’s shard fails → return error → Harini retries.

---

### ⚡ Consistency vs Latency

* No atomic writes, no waiting for rollback/retry.
* Return success as soon as recipient’s shard write succeeds.
* ✅ **Very low latency** and practically consistent for users.

---

## 🗄️ Choosing the Right Database

---

### ⚡ Workload Overview

* **Writes (`sendMessage`)**: 400,000/sec avg, 2 million/sec peak
* **Reads (`getMessages`)**: 800,000/sec avg, 4 million/sec peak
* **Observation:** Both **read- and write-heavy** — no single database excels at both natively.

---

### 🔧 Optimizing Reads & Writes

**Can we optimize writes?**

* **Batching:** reduces write calls but causes stale reads → ❌ not acceptable
* **Sampling:** reduces write volume but risks data loss → ❌ not acceptable

**Can we optimize reads?**

* ✅ Absorb most reads via **cache layer**
* With reads handled by cache, the **database can be optimized for writes**

---

### 🏆 Requirements for the Database

1. High write throughput (~400K/sec avg)
2. No joins required (queries are scoped to a conversation)
3. No need for search (can add separate search service later)
4. Supports paginated reads (by timestamp)
5. No need for transactions
6. Disk persistence required

---

### 🔹 Database Options

* **SQL**

  * Strengths: ACID transactions, normalization, joins
  * Weaknesses: Low throughput, difficult horizontal scaling

* **Key-Value**

  * Strengths: High throughput, simple
  * Weaknesses: No joins, no search, no native pagination → ❌ we need pagination

* **Document**

  * Strengths: Schemaless, search, local indexes
  * Weaknesses: No joins, limited pagination → ❌ we need pagination, search not required

* **Column-Family / Wide Column DB**

  * Strengths: Fast writes, time-based pagination, fast aggregates
  * Weaknesses: No joins, no search → ✅ matches our requirements perfectly

---

### ✅ **Ideal Choice**

* **Wide Column Database** (HBase, Cassandra, ScyllaDB)
* Optimized for **write-heavy workloads**, supports **time-based pagination**, and scales horizontally.

---

## 🗂️ Cache

---

### 🔹 Local vs Global Cache

* **Single Global Cache:** ❌ Not feasible

  * With billions of users and high throughput, one server cannot hold all cached data.
  * Would create wasted app servers (just forwarding requests to cache servers).

* **Distributed Global Cache:** ✅ Feasible, but:

  * App servers mostly forward requests → underutilized.
  * Requires double infrastructure (app servers + cache servers).

* **Local Cache (preferred):** ✅

  * Each app server doubles as cache.
  * Reduces network overhead and infrastructure cost.
  * Handles most read requests efficiently (`getMessages(user_id, conversation_id, pagination)`).

---

### 🔹 Invalidation

* Goal: **Immediate consistency** without high latency.
* Separate cache server requires 2-phase commit → high latency.
* Local cache allows **write-through invalidation**:

  * Writing to the cache always succeeds.
  * Keeps cache and database consistent without 2PC.

---

### 🔹 Eviction

* Use **LRU (Least Recently Used)** strategy to evict old messages.

---

### 🔹 Routing

* App servers are **stateful**.
* If an app server holds a user’s messages in its cache:

  * All requests for that user should be routed to the same app server.
  * **Consistent hashing** ensures this.

**Example Flow:**

1. **getMessages(user_id, conversation_id)**

   * Routed to the shard + app-server holding the local cache.
2. **sendMessage(sender_id, recipient_id)**

   * Routed to the **recipient’s shard + cache first**.
   * Data is then asynchronously replicated to the **sender’s shard + cache** via a message queue.

✅ **Benefits:**

* Low latency reads
* Immediate consistency
* Efficient replication

---
