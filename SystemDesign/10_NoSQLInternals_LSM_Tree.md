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

# Optimizing Disk Reads – Sparse Indices

Binary Search O(log n) is ultra fast compared to Linear Search O(n).

* Example: Database with 1 trillion entries:

  * Binary Search → log₂(10¹²) ≈ 40 steps
  * Linear Search → 1 trillion steps
  * **Binary Search is 25 billion times faster than Linear Search** in this case!

**Problem:** Binary Searching the SSTable is expensive for large tables.

* Typical WAL size = 100MB
* SSTable sizes:

  * Level 1 ≤ 100MB (from WAL)
  * Level 2 ≤ 200MB (from 2 Level-1 SSTables)
  * Level 3 ≤ 400MB (from 2 Level-2 SSTables)

**Example:** SSTable of 100GB, average entry = 100 bytes → 1B entries

* Binary search iterations = log₂(10⁹) ≈ 30
* Each iteration is a disk random read ~18ms
* Total time per SSTable = 30 × 18ms = **540ms**
* 10 SSTables → worst-case read = **5.4s**

---

## Idea: Use an In-Memory Index

* Avoid binary search for each SSTable → direct RAM lookup
* Each SSTable lookup now ~18ms
* 10 SSTables → 180ms total worst-case → **30x faster**

> Most reads served from MemTable (RAM cache, ~0.1ms)
> Only ~10% hits disk → worst-case 180ms → effective average ~20ms

---

## Full Index

* Hashmap {key → offset} for **every key in SSTable**
* Reads: O(1) per SSTable → very fast
* Memory-heavy:

```
1B entries × (20B key + 8B offset) = 28GB per 100GB SSTable
10 SSTables → 280GB RAM → impractical
```

---

## Sparse Index

* Built **per SSTable**, stored in RAM
* Maintain **only first key of each block**

**Assumptions:**

* Block size = 4KB
* Average entry = 100 bytes → 40 entries per block
* Sparse index → 25M entries (~100MB for 100GB SSTable)

**Sparse Index = sorted list of first key of each block**

---

### 1️⃣ Problem Sparse Index Solves

* In **LSM Trees**, data is stored on disk in **sorted SSTables**
* To **find a key**, reading the whole file is slow
* Sparse index allows jumping closer to the key → minimal disk reads

---

### 2️⃣ Dense vs Sparse Index

| Index Type | Memory Usage | Notes                                                  |
| ---------- | ------------ | ------------------------------------------------------ |
| Dense      | Large        | Every key stored, very fast                            |
| Sparse     | Small        | Only first key per block, read small block to find key |

**Book analogy:**

* Dense → every word in the book listed in index
* Sparse → first word on each page → jump to page, read locally

---

### 3️⃣ How Sparse Index Works

1. SSTable divided into **blocks/pages**
2. Sparse index stores **first key of each block** + block location
3. To find a key:

   * Look in sparse index → find closest block ≤ key
   * Read **only that block** from disk → find key

---

### 4️⃣ Example

SSTable keys (sorted):

```
A, B, C, D, E, F, G, H
```

Blocks of 2 keys:

```
Block1: A, B
Block2: C, D
Block3: E, F
Block4: G, H
```

Sparse Index stores first key of each block:

```
A → Block1
C → Block2
E → Block3
G → Block4
```

Find `F`:

* Sparse index → closest key ≤ `F` is `E` → Block3
* Read Block3 (`E, F`) → find `F`

✅ Only **1 block read** instead of entire file

---

### 5️⃣ Why It’s Good

* Less memory usage than full index
* Minimal disk reads (1 block per query)
* Works well with **Bloom filters** → avoid reading blocks if key absent
* Efficient for **LSM Trees** with append-only sorted files

---

Think of it as a **table of contents in a book**: only first word of each chapter, jump to chapter, read locally.

---

# Deletion – Tombstones

### Naive Approaches

**1️⃣ Delete from MemTable only**

* Delete the key from MemTable
* ❌ Will this work? **No**
* Why? After the delete, reads will still search the SSTables → key is not truly deleted
* Effectively, this only undoes the last value in memory

---

**2️⃣ Delete from MemTable, WAL, and all SSTables**

* Delete the key from MemTable
* Delete from WAL
* Delete from all SSTables
* ✅ This works but is **incredibly expensive**

  * SSTables are immutable → cannot shift data to fill gaps → disk fragmentation
  * Deletion becomes very slow for large datasets

---

### Tombstones: The Efficient Way

* **Tombstone** (aka sentinel, flag, marker) is a special entry marking that a value is deleted
* Deletes are implemented as **writes**, not physical removal

**Example:**

```cpp
TOMBSTONE = "PZpaIBk8rbaIQVoUqGD2NS04qD3gONn0QH1Cm2DKBkoktwGuEt"
// Practically impossible to collide with real data

void set(key, value) {
    ...
}

void delete(key) {
    set(key, TOMBSTONE)
}

string _get(key) {
    // check MemTable
    // check SSTables
    // ...
}

string get(key) {
    value = _get(key)
    if (value == TOMBSTONE) {
        raise KeyNotFoundError()
    }
    return value
}
```

---

### Important Notes

* **Compaction** can remove tombstones only from the **oldest SSTable** (SSTable 0)
* For newer SSTables, tombstones must still be preserved → ensures correctness during reads
* This allows deletion to be handled **efficiently** without rewriting all SSTables

---

## **LSM Tree: Final Structure & Algorithm (Simplified)**

### **1. Writes**

1. **WAL (Write-Ahead Log)**

   * Append the entry to WAL → ensures **durability** (nothing is lost if crash happens).

2. **MemTable**

   * Insert the entry into **MemTable** → fast, in-memory access.

3. **Optional triggers after write**

   * **Flush:** WAL full → flush MemTable to **new SSTable** on disk.
   * **Compaction:** Too many SSTables → merge them to reduce number of files.
   * **Eviction:** MemTable full → remove **oldest entries** using **LRU**.

4. **Deletions**

   * Mark deleted keys with **TOMBSTONE**.

5. **Bloom Filter**

   * Updated for each write → allows **quick "key not present" checks** before touching disk.

✅ Writes are **fast and durable**.

---

### **2. Reads**

#### **Step 1: Check MemTable**

* Acts as **cache** in RAM.
* If found → return immediately (O(1) in memory).
* If recently accessed → guaranteed in MemTable.
* Also update **last accessed timestamp** (for LRU eviction).

#### **Step 2: Check SSTables (if not in MemTable)**

* Skip WAL → MemTable already contains all WAL entries.
* Scan SSTables **from newest → oldest**.

For **each SSTable**:

1. **Sparse Index (in RAM)** tells **which block** might contain the key.
2. **Read block from disk** → only **1 disk access**.
3. **Binary search inside RAM block** → extremely fast.
4. If key found:

   * If value = TOMBSTONE → return **KeyNotFoundError**.
   * Else → return value and update MemTable for future fast access.
5. If not found → continue to next older SSTable.

If key not found in **any SSTable** → raise **KeyNotFoundError**.

---

### **3. Why reading multiple SSTables isn’t slow**

* **Compaction** reduces the total number of SSTables. Typical LSM database → ≤10 SSTables.
* **Sparse Index** avoids full disk scan:

  * Only **1 block** per SSTable is read.
  * Binary search in **RAM block** is negligible compared to disk read.

---

### **4. Optimizations**

1. **Bloom Filter:** Quickly tells if key is definitely not in SSTable → avoids unnecessary reads.
2. **Sparse Index:** Only store **first key of each block** → reduces disk reads to **1 per block**.
3. **Compaction:** Merges SSTables → reduces number of files to scan.

---

### ✅ **Summary (Intuition)**

* Writes → fast in **MemTable + WAL**, deletion = TOMBSTONE.
* Reads → fast if in **MemTable**, otherwise scan **few SSTables + few blocks**.
* Sparse Index + Bloom Filter + Compaction → keeps disk scans minimal.
* Even though SSTables are immutable and reads may involve scanning multiple files, optimizations make LSM Trees **efficient for high write workloads**.

---

# Optimizing Containment Checks – Bloom Filter

### Problem

* Reading a key that was **never inserted** is the **slowest possible read** in an LSM Tree:

  1. Check MemTable → not found
  2. Scan each SSTable one by one → not found

* Common example: **signing up with a unique username**

  * User enters `Ganesh1234`
  * Database must check that this username **does not exist**

---

### Bloom Filter: Key Idea

* **Probabilistic Data Structure**
* Only supports:

  * **Insert**
  * **Containment checks**
* Does **not support**:

  * Reads
  * Updates
  * Deletes
  * Iteration

**Guarantees:**

| Result         | Meaning                                                                           |
| -------------- | --------------------------------------------------------------------------------- |
| False Positive | Key not in DB, but Bloom filter says it exists → triggers unnecessary read (rare) |
| False Negative | Impossible → if key was inserted, Bloom filter will always say it exists          |

---

### How It Works

* Bloom filter = **bit array**
* **Insert key** → mark multiple bits in the array using hash functions
* **Check key** → if any corresponding bit is 0 → key definitely not present

**LSM Tree Integration:**

* **Insert:** Add key to LSM Tree **and** to Bloom Filter
* **Read:**

  ```cpp
  string get(key) {
      if (!bloom_filter.contains(key))
          raise KeyNotFound!
      // Otherwise, read from LSM Tree
  }
  ```
* False positives are rare → worst-case read
* False negatives are impossible → never miss existing keys

**Memory Usage:**

* Properly tuned Bloom filter uses **~10 bits per inserted key**

---

### Example Use Case

* Checking if a username exists on signup

  * Bloom filter first → fast check in RAM
  * Only if Bloom filter says “maybe exists” → read the SSTables

---

### Resources (Optional)

* Quick Demo: [llimllib.github.io/bloomfilter-tutorial](https://llimllib.github.io/bloomfilter-tutorial/)
* Math & Code: [Brilliant – Bloom Filter](https://brilliant.org/wiki/bloom-filter/)
* Video Tutorials:

  * [How to Use Bloom Filters in Redis](https://www.youtube.com/watch?v=Z9_wrhdbSC4)
  * [Bloom Filters | Algorithms You Should Know #2](https://www.youtube.com/watch?v=V3pzxngeLqw)
  * [Bloom Filters Explained by Example](https://www.youtube.com/watch?v=gBygn3cVP80)
  * [Probabilistic Data Structures: Bloom Filters](https://www.youtube.com/watch?v=-jiOPKt7avE)
* Calculate optimal capacity & number of hash functions: [hur.st/bloomfilter](https://hur.st/bloomfilter/)

---
    
# Extending to Other Databases

Beyond key-value NoSQL stores, LSM concepts like WAL, MemTable, and compaction apply to **Document DBs** and **Column Family DBs** as well.

---

## 1️⃣ WAL in SQL Databases

While WAL files are commonly associated with NoSQL LSM trees, **SQL databases also use WAL files extensively** for durability and performance.

### Why WAL is needed in SQL

* SQL tables are **contiguous on disk**.
* SQL databases maintain **B+ tree indexes** for fast queries.
* Updates in SQL can trigger **multiple random reads and writes**:

Example for a single row update:

1. Update the row → **1 random read + 1 random write**

2. Update all B+ tree indexes (say 3 indexes):

   * For each index:

     * Traverse tree → O(log n) random reads
     * Update node → 1 random write
     * Re-balance (if needed) → additional O(log n) reads/writes

3. A transaction touching multiple rows multiplies the above cost

**Worst case:** 20–30 random reads/writes → 3–5 seconds

---

### WAL to the rescue

* Instead of performing all random reads/writes immediately:

  * Append **all changes sequentially** to the WAL file
  * Sequential writes are **very fast** (10–20 ms vs 3–5 s)
  * Bookkeeping (updating rows, B+ tree nodes) can be done **later as a batch**

* Advantages of batch processing:

  * Reduces **random I/O**
  * Enables optimizations like **better disk-seeking algorithms**

* Typical WAL size: **100MB**

  * Once full, the database flushes WAL contents to tables and indexes in batch

---

## 2️⃣ Master-Slave Replication in SQL

* Naive approach: running `SELECT * FROM all_tables WHERE modified_at > now()-1h` on master to sync slaves is **expensive** → slows down the master.

* Efficient approach: **slave tracks offset in master’s WAL file**

  * Slave requests only the **new data since last offset**
  * Avoids scanning all tables → fast and incremental

**Takeaway:** WAL provides **high write throughput**, **durability**, and **efficient replication** in both SQL and NoSQL databases.

---