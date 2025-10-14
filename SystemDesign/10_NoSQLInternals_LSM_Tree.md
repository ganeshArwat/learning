Here’s a polished and structured version of your **Update Problem** notes, keeping all your points and adding clarity, comparisons, and a few extra notes for visualization:

---

# The Update Problem

When updating data, SQL and NoSQL handle storage very differently due to **schema design** and **preallocation**.

---

## 1️⃣ SQL: Strong & Static Schema

**Characteristics:**

1. Schema is **known upfront**:

   * Tables, columns, and data types are fixed.
   * Row size is predictable and uniform.

Example:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,  -- 4 bytes
    name VARCHAR(20),        -- 20 bytes
    age BYTE                 -- 1 byte
);
```

* Each row = 25 bytes
* SQL **pre-allocates maximum space** for each column.
* If a value is smaller than max space → **null padding**.

**Updates:**

* Easy and safe: updating a value will not overflow into adjacent rows.
* If the value exceeds column size → **error or truncation** (expected, as schema enforces it).

**Adding/Deleting Columns:**

```sql
ALTER TABLE users ADD COLUMN gender BYTE;
```

* Existing rows are **packed sequentially on disk**.
* Adding a new column requires **rewriting the entire table** → slow.
* Schema migration is therefore expensive in SQL.

---

## 2️⃣ NoSQL: Schemaless / Semi-structured

**Characteristics:**

* Flexible, schema-less or semi-structured.
* Entry size is **variable and unknown**.

Example (key-value pairs):

| Key         | Value                             | Entry Size |
| ----------- | --------------------------------- | ---------- |
| item        | 10                                | 9 bytes    |
| preferences | {"theme":"dark","autoSave":false} | 62 bytes   |

* No **preallocation** (max value could be huge, e.g., Redis allows strings up to 500MB).

---

### Updates in NoSQL

* **Entry size can change** dynamically.
* If a new value is larger than the allocated space:

1. **Truncate:** Enforcing a max size is **unexpected behavior** → bad design.
2. **Shift:** Move subsequent entries to make space → very slow.

**Conclusion:** Traditional in-place updates are impractical in NoSQL.

---

### Why truncation works in SQL but not NoSQL

| SQL                           | NoSQL                                    |
| ----------------------------- | ---------------------------------------- |
| Fixed schema known by dev     | Schema unknown / flexible                |
| Truncation expected & safe    | Truncation unexpected → bad UX           |
| Preallocation avoids overflow | Cannot preallocate → updates must append |

---

### How NoSQL Handles Updates

* Entries are **immutable**; updates are **append-only**.
* Old entries may be marked as deleted or outdated (logical delete).
* Systems use **compaction / merging** later to reclaim space.

**Challenges:**

* How to efficiently perform **updates and deletes** when you cannot overwrite in-place.
* Must balance **write amplification** and **read efficiency**.

---

### 🔹 Key Takeaways

1. SQL → **preallocated, fixed-size, easy updates, expensive schema migration**.
2. NoSQL → **variable-size, append-only, immutable updates, compacted later**.
3. The **update problem** in NoSQL is solved via **append-only logs, WAL, or versioned entries**, not by overwriting existing data.

---


# Log-Structured Merge (LSM) tree

---

# LSM-Tree: Persistence & Update Flow

LSM (Log-Structured Merge) Trees are designed to efficiently handle **updates and inserts** in NoSQL databases with **append-only storage**.

---

## 1️⃣ Quick Persistence — WAL (Write-Ahead Log)

* Every write (insert/update/delete) is **appended** to the WAL file on disk.
* Sequential writes → **high throughput**.
* WAL file = **temporary storage**. Data is durable but **not yet fully merged** into the database.
* Typical WAL size: **100 MB**.
  When full → **dump into SSTable**.

**Properties:**

* Append-only → easy and fast writes
* Not sorted → cannot efficiently read directly
* Contains duplicates → multiple writes to same key

**Illustration:**

```
WAL (Append-Only Log)
---------------------
t0: u1 -> val1
t1: u2 -> val2
t2: u1 -> val3   <-- update
t3: u3 -> val4
```

**Resources:**

* Visualization of LSM Trees: [https://www.pragy.dev/blog/lsm-trees-visualized](https://www.pragy.dev/blog/lsm-trees-visualized)

---

## 2️⃣ Read Cache — MemTable

* In-memory **hashmap / BST / sorted linked list**.
* Reads served from **RAM** → fast.
* Eviction: **LRU**, size limited by available RAM.
* MemTable size usually > WAL → simplifies reads & eviction.

**Flow:**

```
Client Write
    |
    v
WAL (disk)  --> MemTable (RAM)
```

*Writes are immediately durable in WAL, visible for reads in MemTable.*

---

## 3️⃣ Long-Term Persistence — SSTables

* WAL contents are dumped into **immutable SSTables** on disk.
* SSTables are **sorted by key**, **duplicates removed**.
* Never updated in-place (immutable) → append-only design.

**Illustration:**

```
SSTable
--------
u1 -> val3
u2 -> val2
u3 -> val4
```

*Old versions removed during deduplication; sorting allows efficient merges.*

---

## 4️⃣ Removing Redundancy — Compaction

* Multiple SSTables → possible **duplicate keys** and **wasted space**.
* Compaction merges SSTables:

  * Sorted merge (like merge sort)
  * Keep only **latest entry** for duplicate keys
  * Old SSTables deleted after merge

**When to compact:**

* Table count threshold reached
* Scheduled time (e.g., midnight)
* Low-load period

**Strategies:**

1. **Levelling:** Compact as soon as 2 tables appear on a level
2. **Tiering:** Maintain threshold >2 tables per level

**Important:**

* Avoid cross-level compaction (sizes differ)
* Streaming merge → don’t load entire file into RAM

**Visualizations & References:**

* [LSM-Tree Compaction Visualization](https://disc-projects.bu.edu/compactionary/background.html)
* [Alibaba Cloud: LSM Compaction Mechanism](https://www.alibabacloud.com/blog/an-in-depth-discussion-on-the-lsm-compaction-mechanism_596780)
* [ScyllaDB LSM Compaction Video](https://www.youtube.com/watch?v=Xzcj663i9DM)

**Illustration:**

```
Level 0 SSTables (small)
-----------------------
u1 -> val1   u2 -> val2
u1 -> val3   u3 -> val4

Compaction --> Level 1 SSTable
-------------------------------
u1 -> val3
u2 -> val2
u3 -> val4
```

---

## 🔹 Summary of LSM Flow

```
Client Write
    |
    v
+--------+        +---------+
|  WAL   |  -->   | MemTable|  (RAM)
+--------+        +---------+
    |
    v
  SSTable (Immutable)  -> Compaction -> Merged SSTables
```

*Durable, append-only writes + fast reads + efficient storage.*

---

✅ Key Points:

* WAL = sequential disk writes → high throughput
* MemTable = fast in-memory cache for reads
* SSTable = immutable long-term storage
* Compaction = removes duplicates, maintains sorted order
* Efficient updates via **append-only + compaction**, no in-place updates

---
