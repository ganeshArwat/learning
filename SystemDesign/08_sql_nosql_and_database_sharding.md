# 📌 Relational Databases (RDBMS)

---

## ✅ Strengths of RDBMS

_(apply best at low scale, when queries/sec and data size can be handled by a single server)_

### 1. **Normalization**

- Eliminates redundancy, ensures data integrity.
- Data is split into multiple related tables → avoids inconsistency.

### 2. **Strong Schema**

- Well-defined, static, enforced structure.
- Every row follows the schema strictly.
- Easy to validate and maintain data quality.

### 3. **ACID Transactions**

Guarantees correctness and reliability.

- **Atomicity** → All or nothing.
- **Consistency** → DB moves from one valid state to another.
- **Isolation** → Transactions don’t interfere.

  - Different isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable).

- **Durability** → Once committed, data is persisted.

### 4. **Powerful Querying Capabilities**

- Joins (inner, outer, cross)
- Filtering (WHERE clauses)
- Aggregations (COUNT, SUM, AVG, MIN, MAX)
- Grouping (GROUP BY, HAVING)
- Nested queries (subqueries)
- Recursive queries (CTEs, e.g. org chart, graph traversal)

### 5. **Extra Features**

- Full-text search
- Geospatial queries
- JSON support (modern RDBMS like PostgreSQL, MySQL 8+)
- Window functions (RANK, LEAD, LAG, etc.)
- Stored procedures, triggers

### 6. **Maturity & Ecosystem**

- Relational DB theory predates modern hardware.
- Extremely well battle-tested → used by millions of companies for decades.
- Large ecosystem (tools, connectors, ORMs).

---

## ❌ Weaknesses of RDBMS

_(show up at large scale, when data or requests/sec exceed single server limits)_

### 1. **Normalization → Expensive Joins**

- Frontend usually needs **denormalized data** (multiple entities in one response).
- Requires joins across multiple large tables.
- If data grows beyond a single server → joins become **cross-server joins** → extremely slow & network-heavy.

### 2. **Strong Schema → Inflexibility**

- Difficult to handle highly diverse/unstructured data.
- Example: Amazon product listings

  - 10M+ products, 10k+ categories.
  - Each category has different attributes (clothes vs electronics).
  - Hard to predefine one fixed schema.

### 3. **ACID Transactions at Scale**

- To scale, you need **sharding** (splitting data across multiple servers).
- Traditional SQL DBs guarantee ACID **only within a single server**.
- Distributed transactions (across shards) require 2-phase commit → very slow and complex.

### 4. **Vertical Scaling Limitations**

- RDBMS usually scale vertically (bigger machine, more RAM/CPU).
- Eventually you hit a hardware ceiling → can’t scale infinitely.

### 5. **Less Suited for Modern Workloads**

- Handling semi-structured data (logs, JSON, documents) is harder.
- Write-heavy workloads with massive concurrency are tricky to scale.
- Real-time analytics at huge scale better handled by specialized systems.

---

## ⚖️ Summary

- **RDBMS = Best choice at small/medium scale**, where strong schema, ACID guarantees, and powerful querying matter.
- **Weaknesses show at large scale** → joins across shards, rigid schema, distributed transactions.
- At that point, companies often move to **NoSQL systems** (for scale/flexibility) or a **polyglot persistence approach** (mix of RDBMS + NoSQL).

---

# 📌 NoSQL Databases

---

## ✅ What is NoSQL?

- **NoSQL** = _Not Only SQL_.
- Family of databases designed to handle **large-scale**, **high-concurrency**, and **semi/unstructured data** workloads.
- Examples: MongoDB (document), Cassandra (wide-column), Redis (key-value), Neo4j (graph).
- Trade-offs: weaker consistency (compared to RDBMS) but stronger scalability & flexibility.

---

## ✅ BaSE Model (alternative to ACID)

- **Basically Available** → System guarantees availability even under failures.
- **Soft State** → State of the system may change over time (eventual consistency).
- **Eventually Consistent** → If no new updates happen, eventually all replicas converge to the same state.

👉 Designed for distributed systems where strict ACID is expensive.

---

## ✅ Horizontally Scalable

- Unlike RDBMS (vertical scaling → bigger servers), NoSQL is designed for **horizontal scaling**.
- Add more commodity servers = more capacity.
- Makes it easier to handle:

  - Billions of rows / TB-PB of data.
  - Millions of queries per second.

---

## ✅ Denormalization & Replication

- Instead of normalizing, NoSQL often uses **denormalized data** → duplicate fields across documents/rows.

  - Example: Store customer address inside each order (instead of joining).

- **Replication** ensures high availability:

  - Multiple copies of data across servers.
  - Enables fast reads and fault tolerance.

- Advantage: Fewer joins, faster lookups.
- Trade-off: Updates are more expensive (have to update multiple places).

---

## ❌ Weaknesses of NoSQL Databases

1. **Weaker consistency guarantees** (eventual consistency, conflicts possible).
2. **Complex querying is harder** (limited joins, aggregations).
3. **Application-side complexity** (must handle denormalization, consistency issues).
4. **Less mature** than RDBMS (though MongoDB, Cassandra, Redis are improving).
5. **Operational overhead** (tuning replication, sharding, consistency).

---

## ✅ Choosing a Sharding Key

_(critical for scaling NoSQL)_

### 🔑 Primary Key vs Sharding Key

- **Primary Key**: Uniquely identifies a record in a single database.
- **Sharding Key**: Decides how data is distributed across servers.
- Not always the same!

  - Example: UserID may be a good sharding key, but OrderID might not (if queries need to fetch by User).

### ✅ Characteristics of a "Good" Sharding Key

1. **Equal data & load distribution** → Avoids hot spots.

   - Example: If you shard by "Country", India/US will overload, while others stay idle.

2. **High Cardinality**

   - Cardinality = number of distinct values.
   - More unique values → better distribution.

3. **Present in every read/write request**

   - Otherwise → system won’t know which shard to query → leads to fan-out.

4. **No Fan-outs**

   - Fan-out = query hitting multiple shards = latency + network cost.
   - Good sharding key → most queries touch only 1 shard.

5. **Immutable**

   - Changing shard key = expensive re-sharding.

---

## ⚖️ Summary

- **NoSQL** = Designed for scale, availability, flexibility.
- Uses **BaSE** instead of ACID.
- **Denormalization + Replication** improves performance at the cost of complexity.
- **Sharding Key choice** is the most important design decision.

---

# 📌 Sharding Key Selection – Examples & Reasoning

Sharding is splitting data across multiple databases (shards). The **sharding key** determines how data is distributed. Choosing the right sharding key depends on:

- Most frequent queries & access patterns
- Avoiding hotspots (uneven data distribution)
- Supporting scalability & minimizing cross-shard queries

---

## 1. 🏦 Banking System

### Frequent Operations

- **Balance Query** → `(user_id, account_id)`
- **Fetch Transaction History** → `(user_id, account_id, date_range)`
- **Fetch Accounts of a User** → `(user_id)`
- **Create New Transaction** → `(sender_id, receiver_id, amount)`

  - Note: Both sender_id and receiver_id are composite → `(user_id, account_id)`

### Why Not Other Keys?

- **Location ID / Branch ID** ❌

  - A user can hold accounts in multiple cities/branches.
  - Would fragment a user’s data across shards → inefficient joins & queries.

### ✅ Best Choice: **`user_id`**

- Keeps all accounts & transactions of a user in the same shard.
- Simplifies balance queries & history fetch.

---

## 2. 🚖 Ride Booking (e.g., Uber)

### Frequent Operations

- **Search for Nearby Drivers** → `(user_lat, user_lon)` ⇒ returns list of driver_ids.

### ✅ Best Choice: **City ID / Location Grid**

- Geospatial queries dominate workload.
- Sharding by **city_id** (or geo-hash of location) clusters drivers/riders geographically.
- Ensures local lookups (nearby drivers) stay within the same shard.

---

## 3. 🚂 IRCTC (Railway Ticket Booking in India)

### Challenges

- Preventing **double booking** (seat allocation consistency).
- Handling **Tatkal peak load** (20x+ traffic spike).

### Frequent Operation

- **Book Ticket** → `(user_id, train_id, date_of_journey, class, seat_preference, …)`

### ✅ Best Choice: **`train_id`**

- All bookings for a given train should be in the same shard.
- Seat availability & allocation checks remain local to that shard.
- Handles high concurrency for popular trains during booking windows.

---

## 4. 💬 Facebook Messenger

### Frequent Operations

- **Send Message** → `(sender_id, recipient_id, message)`
- **View Messages** → `(user_id, other_person_id)`

### ✅ Best Choice: **`user_id`**

- All conversations (sent & received) by a user stay in the same shard.
- Reduces cross-shard reads for chat history.
- Drawback: A very popular user (celebrity) could become a **hotspot**, so may need secondary strategies (e.g., conversation-level sharding).

---

## 5. 👩‍💻 Slack (Group Messaging System)

### Frequent Operations

- **Group Chats** → Up to 100,000 participants per group.
- **1-1 Messages**

### ✅ Best Choice: **`group_id`**

- All messages for a group remain in the same shard.
- Avoids cross-shard reads when loading a channel.
- For 1-1 messages, group_id can still be applied if we treat each conversation as a "group".

---

# 🔑 Key Takeaways for Choosing a Sharding Key

1. **Follow the most frequent query pattern** (optimize for reads/writes that dominate traffic).
2. **Avoid scattering related data across shards** (to reduce cross-shard joins).
3. **Prevent hotspots** (one shard getting overloaded due to skewed data like celebrity accounts).
4. Sometimes, **multi-level sharding** (e.g., user_id + date range, or geo-hash + user_id) is needed to balance load.

---

## Types of NoSQL Databases

## 🔑 Key-Value Databases

### ✅ What is a Key-Value DB?

- A **Key-Value Database** stores data as **pairs of unique keys and associated values**.
- The **key** acts like an ID (must be unique).
- The **value** can be anything: string, JSON, blob, or binary data.
- Think of it as a **giant distributed HashMap** that spans across multiple servers.

---

### 💡 Examples

- **Redis** → In-memory, extremely fast, supports persistence to disk.
- **Memcached** → In-memory cache only (no persistence).
- **DynamoDB** (AWS) → Persistent, highly available, cloud-managed service.

---

### 📦 How is Data Stored?

- Stored as `{ key → value }`.
- **Keys** are hashed → decides which shard/server stores the data.
- **Values** are opaque to the DB (the database doesn’t care about the structure).

  - Example:

    ```
    "user:101" → { "name": "Alice", "age": 25, "city": "Pune" }
    "session:xyz" → "loggedIn=true"
    ```

---

### 💪 Strengths

- **Super-fast performance** (O(1) access when key is known).
- **Massively scalable** (easy to distribute across servers).
- **Simple design** (no schema, flexible value types).
- Great for **caching, sessions, leaderboards, shopping carts, pub/sub**.
- High availability and replication possible.

---

### 🔍 Queries

- Only **by key** (no complex queries).
- Examples:

  ```bash
  GET user:101       # Fetch value by key
  SET cart:200 "5 items"
  DEL session:xyz
  ```

- No filtering or searching by values (must fetch by key).

---

### ⚠️ Weaknesses

- Cannot query by value or run complex queries.
- No secondary indexes.
- Data modeling depends entirely on key design.
- Hotspot problem: if one key is accessed too much, that shard/server gets overloaded.
- In-memory systems (like Memcached) lose data on crash.

---

### 🔑 Sharding Key

- **The Key itself is the sharding key.**
- Example: `"user:101"` is hashed → assigned to a specific shard.

---

### 🔑 Primary Key

- **The Key is the Primary Key.**
- Only one unique key per value.

---

### 🕒 When to Use

- **Caching** (Redis, Memcached).
- **Session management** (store user login sessions, tokens).
- **Shopping carts / temporary states**.
- **Leaderboards & rankings** (real-time gaming).
- **Message queue / pub-sub** (Redis Streams, Redis Pub/Sub).
- **User profile lookups** when always queried by user_id.

---

# 📄 Document-Oriented NoSQL Databases

### ✅ What is a Document DB?

- A **Document Database** stores data in the form of **documents** (usually JSON, BSON, or XML).
- Each document is a **self-contained unit** (like a row in RDBMS, but more flexible).
- Think of it as a **giant collection of JSON objects** distributed across servers.
- Supports **nested structures** (arrays, objects) without needing JOINs.

---

### 💡 Examples

- **MongoDB** → most popular, BSON format, flexible schema.
- **CouchDB** → JSON storage, RESTful API.
- **Firestore (Google Firebase)** → cloud-based, real-time sync.

---

### 📦 How is Data Stored?

- Data is stored as **collections** (like tables), each containing multiple **documents** (like JSON objects).
- Each document has a **unique `_id`** (primary key).
- Example:

  ```json
  {
    "_id": "user:101",
    "name": "Alice",
    "age": 25,
    "address": {
      "city": "Pune",
      "zip": "411001"
    },
    "hobbies": ["reading", "gaming"]
  }
  ```

---

### 💪 Strengths

- **Flexible schema** (no need to predefine columns).
- **Rich queries** → filter by fields inside documents.
- Supports **indexes** on fields (not just primary key).
- Good for **hierarchical and nested data**.
- Easy to map to application objects (JSON ↔ JavaScript/React).
- Horizontal scaling possible with **sharding**.

---

### 🔍 Queries

- Queries can target **fields inside documents**, unlike key-value DBs.
- Examples (MongoDB-style):

  ```js
  db.users.find({ age: { $gt: 20 } }); // Query by field
  db.users.find({ "address.city": "Pune" }); // Query nested field
  db.users.updateOne({ _id: "user:101" }, { $set: { age: 26 } });
  ```

- Can use **secondary indexes** for faster queries.

---

### ⚠️ Weaknesses

- More complex than Key-Value stores (slower if just fetching by key).
- Joins are limited (denormalization often required).
- Document size limits (e.g., MongoDB max 16MB per document).
- Sharding and replication setup can be tricky at scale.

---

### 🔑 Sharding Key

- A chosen **field in the document** (e.g., `user_id`, `region`, `email`).
- Important to pick carefully to avoid hotspots.

---

### 🔑 Primary Key

- Usually the **`_id` field** in MongoDB (or equivalent unique ID in others).
- Acts as the **unique identifier** for each document.

---

### 🕒 When to Use

- **User profiles** (flexible attributes per user).
- **Content management systems** (blogs, product catalogs).
- **E-commerce product catalogs** (nested attributes, variants).
- **IoT / sensor data** (semi-structured, fast ingestion).
- **Mobile/web apps** (natural JSON format for frontend).

## **Why MongoDB Has a 16MB Document Limit**

1. **Document-level Read/Write**

   - In document databases, **operations happen at the document level**, not the field level.
   - If you **modify one field inside a document**, the database has to **rewrite the entire document** on disk.
   - If you **read one field**, the database reads the **entire document into memory**.

2. **Impact of Large Documents**

   - If a document is huge (e.g., 100MB), even a tiny update requires rewriting 100MB.
   - Reading a huge document is inefficient because it consumes more **RAM, network bandwidth, and CPU cycles**.
   - The 16MB limit is a **practical constraint** to ensure performance and prevent resource overuse.

---

## **Analogy with Boolean Size**

- You might think a `boolean` should take **1 bit**, but in reality:

  - **Java/C++/C/Rust:** boolean = **1 byte** (7 bits wasted)
  - **Python:** boolean = **4 bytes**

- **Why?** Because **all memory is byte-addressable**, meaning you can read/write **whole bytes**, not individual bits.

---

### **Relation to Databases**

| DB Type           | Granularity of Read/Write                                  |
| ----------------- | ---------------------------------------------------------- |
| Key-Value DB      | Entire key-value entry                                     |
| SQL DB            | Entire row                                                 |
| Document DB       | Entire document                                            |
| Specialized types | Can sometimes modify parts in-place (like Redis bitfields) |

- Just like memory is **byte-addressable**, documents are **document-addressable**.
- This design choice makes **document DBs simple and fast**, but it limits **maximum document size**.

---

### **Key Takeaways**

- MongoDB 16MB limit = practical performance constraint.
- You **cannot partially read/write fields** inside a document; the DB treats the document as a single unit.
- If you need to store bigger data (like videos or logs), you should **split across multiple documents** or use **GridFS** in MongoDB.

---

# 🗄️ Column-Family / Wide-Column Databases

### ✅ What are Column-Family / Wide-Column DBs?

- A **Column-Family (Wide-Column) Database** stores data in **tables, but organized by columns instead of rows**.
- Each **row has a unique key**, but the **columns can vary per row** (flexible schema).
- Designed for **high write throughput and analytical queries** over large datasets.
- Think of it as a **spreadsheet where each row can have different columns** and you can query by column efficiently.

---

### 💡 Examples

- **Apache Cassandra** → highly available, distributed, designed for large-scale workloads.
- **HBase** → Hadoop ecosystem, column-oriented, suitable for big data.
- **ScyllaDB** → drop-in replacement for Cassandra, very high performance.
- **Google BigTable** → the original inspiration for wide-column stores.

---

### 📦 How is Data Stored?

- Data is stored in **tables → rows → column families → columns**.
- A **row key** uniquely identifies each row.
- Each **column family** contains related columns, and each column can have multiple **versions** (timestamps).
- Example (Cassandra-style):

| Row Key  | Personal Info:Name | Personal Info:Age | Address:City | Address:Zip |
| -------- | ------------------ | ----------------- | ------------ | ----------- |
| user:101 | Alice              | 25                | Pune         | 411001      |
| user:102 | Bob                | 30                | Mumbai       | 400001      |

- Here, `Personal Info` and `Address` are **column families**.

---

### 💪 Strengths

- **Highly scalable** → designed for distributed environments.
- **Efficient for read/writes of columns** (can fetch only needed columns instead of entire row).
- **Flexible schema** → different rows can have different columns.
- **Great for time-series, logging, and large datasets**.
- **Tunable consistency** → Cassandra allows eventual or strong consistency per query.

---

### ⚠️ Weaknesses

- Complex data modeling compared to document or key-value DBs.
- Not ideal for ad-hoc queries that aren’t planned in advance.
- No joins like relational DBs → denormalization often required.
- Querying non-primary key columns without indexes can be slow.

---

### 🕒 When to Use

- **Time-series data** → IoT sensors, metrics, logs.
- **Event tracking / analytics** → clickstreams, user activity.
- **Large-scale applications** → social media feeds, recommendation engines.
- **Situations needing high write throughput** and distributed storage.

---

# 📦 Large File / Object Databases

### ✅ What are Large File / Object DBs?

- These databases are designed to **store and manage large binary files or unstructured objects**, often too big to fit inside normal documents or rows.
- Sometimes called **Blob Stores** or **Object Stores**.
- Data is usually **stored as objects with metadata**, rather than structured rows/columns.

---

### 💡 Examples

- **Amazon S3** → object storage service for files of any size.
- **Azure Blob Storage** → cloud-based object storage.
- **Google Cloud Storage** → highly scalable object store.
- **MongoDB GridFS** → splits files into chunks stored as documents.

---

### 📦 How is Data Stored?

- Each **file or object** is stored as a **binary blob**, often with **metadata** (filename, type, size, creation date).
- Large files are sometimes **split into chunks** for efficient storage and retrieval (GridFS does this).
- Objects are **key-addressable**, so you retrieve them by a unique identifier (like a filename or UUID).
- Example (pseudo-structure):

  ```json
  {
    "id": "file123",
    "filename": "video.mp4",
    "size": 50000000,
    "content": <binary data>,
    "uploaded_at": "2025-10-03"
  }
  ```

---

### 💪 Strengths

- Can handle **very large files** efficiently.
- **Highly scalable** → store petabytes of data across servers.
- **Metadata support** → easy to search and organize objects.
- Good for **unstructured data** (images, videos, PDFs, backups).
- Often integrates with **CDNs** for fast content delivery.

---

### ⚠️ Weaknesses

- Not optimized for **small, frequent updates**.
- Limited query support beyond metadata.
- Reading/writing large files may be **slower than in-memory databases**.
- No complex relationships between objects (unlike relational DBs).

---

### 🕒 When to Use

- **Media storage** → images, videos, audio files.
- **Backups and archives** → system or database backups.
- **Content delivery** → serving files via web/CDN.
- **IoT / sensor large-data storage** → raw logs, recordings.
- **Any situation where data is unstructured and very large**.

---

# 🌐 Other NoSQL Types

---

## 1️⃣ Graph Databases

### ✅ What is it?

- Stores data as **nodes (entities) and edges (relationships)**.
- Optimized for **highly connected data**.
- Queries focus on **relationships** rather than individual records.

### 💡 Examples

- Neo4j, Amazon Neptune, ArangoDB, JanusGraph

### 📦 How is data stored

- **Nodes** = entities (e.g., user, product)
- **Edges** = relationships between nodes (e.g., follows, bought)
- **Properties** = key-value attributes on nodes/edges

### 💪 Strengths

- Excellent for **relationships** (social networks, recommendations, fraud detection)
- **Fast graph traversals**
- Schema-flexible

### ⚠️ Weaknesses

- Not ideal for bulk data analytics
- Can be complex to scale horizontally

### 🕒 When to Use

- Social networks, recommendation engines, fraud detection, knowledge graphs

---

## 2️⃣ Vector Databases

### ✅ What is it?

- Stores **vector embeddings** for high-dimensional data.
- Optimized for **similarity search** (nearest neighbor search).

### 💡 Examples

- Pinecone, Milvus, Weaviate, Vespa

### 📦 How is data stored

- Each entry = **vector (array of floats) + optional metadata**
- Supports **distance metrics** (cosine similarity, Euclidean distance)

### 💪 Strengths

- Fast similarity search for **ML/AI applications**
- Scales for millions/billions of vectors

### ⚠️ Weaknesses

- Not for traditional CRUD operations
- Requires understanding of embeddings and distance metrics

### 🕒 When to Use

- Semantic search, recommendation systems, AI/ML embeddings, image/text similarity

---

## 3️⃣ Object-Oriented Databases

### ✅ What is it?

- Stores data as **objects**, similar to objects in programming languages.
- Integrates **directly with object-oriented code** (no mapping like ORM needed).

### 💡 Examples

- db4o, ObjectDB, Versant

### 📦 How is data stored

- Data = **objects with fields and methods**
- Objects can reference other objects

### 💪 Strengths

- Seamless integration with OOP languages
- Supports complex data types and relationships

### ⚠️ Weaknesses

- Less common → fewer tools/support
- Not as scalable as modern NoSQL DBs

### 🕒 When to Use

- Applications with heavy **OOP design**, CAD/CAM systems, scientific simulations

---

## 4️⃣ Multimodal Databases

### ✅ What is it?

- Supports **multiple data models in one database** (document, graph, key-value, vector).
- Useful when your application needs **different types of queries** on the same dataset.

### 💡 Examples

- ArangoDB, OrientDB, Cosmos DB (Azure)

### 📦 How is data stored

- Different models stored **together or linked**, supporting queries across models
- Example: Graph relationships + document attributes + vector embeddings

### 💪 Strengths

- Flexible → supports **multiple workloads in one DB**
- Reduces need to maintain multiple databases

### ⚠️ Weaknesses

- Complexity in design
- Can be slower than specialized single-model DBs

### 🕒 When to Use

- Applications requiring **heterogeneous data**: social media + recommendations + analytics
- Use cases needing **graph + document + vector queries**

---

# 🗄️ Choosing the Right Database

---

## **1️⃣ Twitter Hashtag Storage**

### **Requirements**

- Store the **most popular and most recent tweets** for each hashtag.
- Support **paginated queries** (first 20 tweets, next 20 tweets, etc.).
- **Very large volume of tweet writes** (high write throughput).

### **Recommended DB: Column-Family / Wide-Column**

- **Example:** HBase, Cassandra
- **Why it fits:**

  - Optimized for **high write throughput**.
  - Supports **pagination and sorted queries by row key or timestamp**.
  - Can handle **very large datasets** distributed across multiple servers.

- **Schema Example:**

  | Row Key (Hashtag) | Timestamp | Tweet ID | Content | Likes | Retweets |
  | ----------------- | --------- | -------- | ------- | ----- | -------- |

---

## **2️⃣ Live Scores of Sports / Matches**

### **Requirements**

- Given a recent match, show the **ongoing score information** in real-time.
- Data is **small (few KB)**, high update frequency, mostly read by key.

### **Recommended DB: Key-Value**

- **Key:** `match_id`
- **Value:** JSON object containing all info to display on page (~10KB).
- **Why it fits:**

  - Extremely **fast reads/writes by key**.
  - Ideal for **real-time updates**.
  - Simple structure, minimal overhead.

- **Example Value:**

  ```json
  {
    "teamA": "India",
    "teamB": "Australia",
    "scoreA": 120,
    "scoreB": 118,
    "overs": "18.3"
  }
  ```

---

## **3️⃣ Cab Location in Uber**

### **Requirements**

1. Show **current location** of a cab.

   - **Key-Value DB:**

     - Key: `driver_id`
     - Value: `{ latitude, longitude }`
     - Fast, real-time access to **current positions**.

2. Show **historical location** of a cab by date or recency.

   - **Column-Family DB:**

     - Store **GPS sensor data** with timestamp as part of the row key.
     - High write throughput, supports **pagination** and **time-based queries**.

- **Why Column-Family fits:**

  - Can efficiently store **large, time-series datasets**.
  - Supports **range queries by time** (e.g., last 7 days of location data).

---

## **Additional Notes / Examples**

- **Key-Value DBs:** Best for **real-time, small-sized data** where access is by unique key.
- **Column-Family DBs:** Best for **high-write, time-series, or analytical workloads** with large datasets.
- **Document DBs:** Best when you need **flexible schemas and nested objects**, e.g., user profiles, product catalogs.
- **Graph DBs:** Best for **relationship-heavy queries**, e.g., social networks, recommendation engines.
- **Object / Large File DBs:** For **unstructured, large data** like videos, images, backups.

---

# 💾 How Storage Works

---

## **1️⃣ Magnetic Storage**

### 📺 Recommended Video Resource

[![Everything you need to know about solid-state drives (SSD) | Arts ...](https://tse4.mm.bing.net/th/id/OIP.abiE0g_8iZg9EQRJrsf47gHaIH?cb=12&pid=Api)](https://uwaterloo.ca/arts-computing-newsletter/winter-2018/feature/everything-you-need-know-about-solid-state-drives-ssd?utm_source=chatgpt.com)

[How do Hard Disk Drives Work?](https://www.youtube.com/watch?v=wtdnatmVdIg&utm_source=chatgpt.com)

- **Examples:** HDD (Hard Disk Drives), Magnetic tapes
- **How it works:**

  - Uses **magnetic fields to store data** on spinning platters or tape.
  - Each bit is represented by **magnetized domains** (north/south polarity).

- **Characteristics:**

  - Non-volatile → data persists without power.
  - Slower read/write compared to SSD and RAM.
  - Cheap and high capacity.

- **Use cases:**

  - Archival storage, backups, bulk storage of databases.

---

## **2️⃣ Solid State Storage**

### 📺 Recommended Video Resource

[How do SSDs Work? | How does your Smartphone store data? | Insanely Complex Nanoscopic Structures!](https://www.youtube.com/watch?v=5Mh3o886qpg)

- **Examples:** SSDs, NVMe drives, Flash drives
- **How it works:**

  - Uses **NAND flash memory** (transistors) to store electrical charges.
  - Data is stored in **cells**; reading/writing is electronic, no moving parts.

- **Characteristics:**

  - Non-volatile → retains data without power.
  - Faster than magnetic storage (especially random access).
  - More expensive per GB than HDD.

- **Use cases:**

  - OS drives, databases requiring fast access, high-performance applications.

---

## **3️⃣ RAM (Random Access Memory)**


## 📺 Recommended Video Resource

[![The Ultimate Guide: Understanding the Diagram of Computer Memory](https://tse2.mm.bing.net/th/id/OIP.XNtQdMK7InI5jirMsHzytQHaFj?cb=12\&pid=Api)](https://electraschematics.com/diagram-of-computer-memory.html?utm_source=chatgpt.com)

[How does Computer Memory Work?](https://www.youtube.com/watch?v=7J7X7aZvMXQ)

- **Examples:** DDR4, DDR5, LPDDR
- **How it works:**

  - Volatile memory → loses data when power is off.
  - Stores data in **capacitors and transistors**.
  - CPU can read/write **any memory cell in constant time** (random access).

- **Characteristics:**

  - Extremely fast read/write speeds.
  - Limited capacity compared to HDD/SSD.
  - Expensive per GB.

- **Use cases:**

  - Active processes, CPU caches, in-memory databases, temporary buffers.

---

### **Quick Comparison Table**

| Type        | Volatility   | Speed     | Cost/GB   | Use Case                  |
| ----------- | ------------ | --------- | --------- | ------------------------- |
| Magnetic    | Non-volatile | Slow      | Cheap     | Bulk storage, backups     |
| Solid State | Non-volatile | Fast      | Medium    | OS, databases, apps       |
| RAM         | Volatile     | Very fast | Expensive | Active processes, caching |

---

# 🔄 Sequential vs Random Access

### **1️⃣ Sequential Access**

- **Definition:** Reading/writing **data in continuous blocks** (like reading an entire track on a disk).
- **Characteristics:**

  - Very fast because the read/write head doesn’t move much.
  - Limited by **rotation speed of the disk** and **disk interface throughput**.

**Example Calculations (HDD):**

- Typical HDD: 7200 RPM (rotations per minute) → 120 rotations per second

  - **Time for 1 full spin:**
    [
    \text{Time per spin} = \frac{1 \text{ sec}}{120} \approx 8.33 \text{ ms}
    ]

- **Time to move the read head (seek time):**

  - Average seek time ≈ **9 ms** (depends on HDD, typical 5–15ms)

- **Time to read 100 MB sequentially:**

  - Suppose disk throughput ≈ **100 MB/s**
  - Time = ( \frac{100 \text{ MB}}{100 \text{ MB/s}} = 1 \text{ second} )
  - Very efficient because disk spins continuously; minimal head movement.

---

### **2️⃣ Random Access**

- **Definition:** Reading/writing **small chunks of data scattered across the disk**.
- **Characteristics:**

  - Each access may require **moving the read/write head** + waiting for **disk rotation**.
  - Much slower than sequential access.

**Example Calculation (HDD):**

- **Read 4 KB random data:**

  1. **Seek time:** ~9 ms (average)
  2. **Rotational latency:** ~4.16 ms (half of 8.33 ms spin time)
  3. **Data transfer time:** negligible for 4 KB at 100 MB/s
     [
     4 \text{ KB} = 0.004 \text{ MB}, \quad \text{transfer time} = \frac{0.004}{100} = 0.00004 \text{ s} \approx 0.04 \text{ ms}
     ]

- **Total time:**
  [
  9 + 4.16 + 0.04 \approx 13.2 \text{ ms per 4 KB random read}
  ]

- **Observation:** Sequential reads are **~250× faster** than random reads for small blocks on HDDs.

---

### **Summary Table**

| Access Type | Operation                 | Time Estimate (HDD) | Notes                                    |
| ----------- | ------------------------- | ------------------- | ---------------------------------------- |
| Sequential  | Read 100 MB track         | ~1 s                | Minimal head movement, continuous blocks |
| Random      | Read 4 KB scattered block | ~13 ms              | Seek + rotational latency dominate       |
| Spin Time   | Time for 1 full rotation  | ~8.33 ms            | 7200 RPM disk                            |
| Seek Time   | Move head to track        | ~9 ms               | Average across disk                      |

---

✅ **Key Takeaways**

- **Sequential = fast**, head barely moves, perfect for large continuous data.
- **Random = slow**, dominated by seek + rotation, bad for small scattered reads.
- SSDs/Flash memory remove the mechanical latency → random reads are almost as fast as sequential reads.

---

# 🔹 SQL Wide-Row vs Wide-Column Databases

---

## **1️⃣ Wide-Row (SQL Database)**

### **How it works:**

* Data is stored in **rows**. Each row contains all column values for a single entity.
* Example table: `product_listing`

| product_id | name  | count | price | category  |
| ---------- | ----- | ----- | ----- | --------- |
| 123        | Chair | 10    | 50    | Furniture |
| 124        | Table | 5     | 100   | Furniture |

* Rows are the **basic unit of storage**, indexed by primary key (here `product_id`).

---

### **Query 1 - Fetch a row (fast)**

```sql
SELECT * FROM product_listing WHERE product_id = 123;
```

* Indexed by `product_id` → **direct lookup**
* Only **one row is read** → very fast

---

### **Query 2 - Analytics query (slow)**

```sql
SELECT SUM(count) FROM product_listing;
```

* Database has to **scan all rows** because aggregation is across the entire table
* Performance is **slow on huge datasets** unless extra indexing or materialized views are used

✅ **Summary:** Row-store = **fast for row lookups, slow for column aggregations**

---

## **2️⃣ Wide-Column Database**

### **How it works:**

* Data is stored in **column families** rather than rows.
* Columns are stored **together on disk** per column family, not per row.
* Example column family: `product_listing`

```
RowKey: product_id:123
Columns: name=Chair, count=10, price=50, category=Furniture
```

* Columns are stored **contiguously by column** → efficient for **column-based scans**

---

### **Query 1 - Fetch a row (moderately slow)**

```sql
SELECT * FROM product_listing WHERE product_id = 123;
```

* Columnar storage means data for one row is **spread across multiple places on disk**
* Need to read multiple columns → slower than a row-store fetch

---

### **Query 2 - Aggregation query (fast)**

```sql
SELECT SUM(count) FROM product_listing;
```

* Data for `count` column is **stored contiguously**
* Database can **scan only that column** without touching other data → very fast
* Perfect for analytics and aggregations

✅ **Summary:** Column-store = **fast for aggregations, slower for full-row lookups**

---

### **Key Difference Visual**

| Feature                 | Wide-Row (SQL)       | Wide-Column DB          |
| ----------------------- | -------------------- | ----------------------- |
| Data layout             | Row-oriented         | Column-oriented         |
| Fetch full row by key   | Very fast            | Moderately fast         |
| Aggregate single column | Slow (full row scan) | Very fast (column scan) |
| Best use case           | OLTP (transactions)  | OLAP / analytics        |

---

💡 **Analogy:**

* **Row-oriented:** Think of a **spreadsheet row** – fetching a whole row is easy, summing one column means scanning every row.
* **Column-oriented:** Think of a **spreadsheet column** – summing one column is super fast, fetching a full row means piecing together multiple columns.

---
