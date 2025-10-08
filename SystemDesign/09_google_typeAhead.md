# TypeAhead

## Key difference b/w Typeahead & Autocomplete

* Autocomplete is typically **local** to your machine. Suggestions are specific to the user.
* Autocomplete is **standalone**, not tied to search.
* Typeahead is **associated with search**.
* Typeahead suggestions are **popular global queries** matching the typed prefix.

---

## Functional Requirements (FR)

### MVP Features

* Prefix-based suggestions: show top N matches.
* Suggestions ranked by popularity/frequency.
* Real-time or near real-time update of suggestions.
* Each query should return results with **< 10ms latency**.

### Future Scope Features

* Personalization based on user history.
* Trending queries & seasonal suggestions.
* Multi-language support.

### Bad / Non-MVP Features

* Heavy ML ranking at query-time.
* Complex personalization in MVP.
* Storing full query history in-memory.

---

## Non-Functional Requirements (NFR)

### PACELC

* **Consistency vs Availability:** Availability + Eventual Consistency (serve suggestions even if slightly stale).
* **Consistency vs Latency:** Ultra-low latency is critical; each query should return **< 10ms**.

---

## Scale Estimation

**Assumptions:**

* Google has **5 billion Monthly Active Users (MAU)**.
* **Daily Active Users (DAU):** 20% of MAU = **1 billion users**.

---

### 1️⃣ Amount of Load

**Requests per second (RPS) calculation:**

* Avg. searches per active user per day = 20
* Total searches per day = 20 × 1B = **20B searches/day**
* Avg. searches per second = 20B / 10⁵ ≈ **200,000 searches/sec**

**Typeahead queries per search:**

* Avg search length = 10 letters
* Suggestions start after 3 letters → ~7 typeaheads per search (rounded to 10)
* Avg typeahead RPS = 200,000 × 10 = **2M requests/sec**

---

### 2️⃣ Peak Load

* Assumption: **peak = 5× average**
* Peak typeahead load = 5 × 2M = **10M requests/sec**
* Peak log_search writes = 1M requests/sec

---

### 3️⃣ Amount of Data (in bytes)

* Search Query = 10B, Query Count = 8B → ~20B per entry
* % of new queries/day = 10% → 2B new entries/day
* Data per day = 2B × 20B = **40 GB/day**
* Total data over 20 years ≈ 40 GB × 20 × 400 days ≈ **320 TB**

**Sharding decision:**

* 320 TB could fit on a single server.
* **10M requests/sec cannot** → Sharding required

---

### 4️⃣ Read-heavy / Write-heavy

* **Read queries (typeahead):** 10M requests/sec peak
* **Write queries (log_search):** 1M requests/sec peak
* System is **read-heavy**, but writes are significant
* Strategy:

  * Absorb reads in cache (Redis, in-memory trie)
  * Optimize DB for writes (increment counters asynchronously)

---

## System Design — TypeAhead

### Approach 1 — Trie-based

**Trie Node Structure:**
Each node stores:

1. `children` — mapping of letters to child nodes
2. `isTerminal` — indicates end of a query
3. `count` — number of times this query was searched (only if `isTerminal`)

---

### Queries

**1️⃣ typeahead(partialQuery)**

1. Start from the root node.
2. Traverse down the trie following each letter of `partialQuery`.
3. Once at the matching node, all suggestions are in its **subtree**.
4. Traverse the subtree to find **top 5 suggestions** by count.

**2️⃣ log_search(searchQuery)**

1. Traverse to the node corresponding to `searchQuery`.
2. Increment the `count` at the terminal node.

---

### Sharding Strategy

* Shard by **first 3 letters** of the query.
* Each shard handles queries that start with the same prefix range (e.g., “aaa–aaz”, “aba–abz”).
* Benefits:

  * Distributes read/write load
  * Enables horizontal scaling for high QPS

---

### Approach 2 — HashMap / Key-Value

**Databases / Storage:**

1. **Search Frequency DB** — stores the search count for each query.
2. **Top Suggestions DB (cache)** — stores top k suggestions for each prefix.

---

### Queries

**1️⃣ typeahead(partial_query)**

* Lookup the partial query in **Top Suggestions DB**.
* **O(1) lookup** via hashmaps; no computation needed.
* Example: typing `"what i"` → fetch suggestions directly from cache.

**2️⃣ log_search(search_query)**

1. Increment count in **Search Frequency DB** (e.g., `redis.inc(searchQuery)`).
2. Update **Top Suggestions DB** for affected prefixes:

   * Only prefixes of the search query are affected:

     ```
     wha, what, what d, what do, ..., what does the fox say
     ```
   * Average query length = 10 letters → ~10 prefixes to update.
   * Total writes per log_search = 1 (freq DB) + 10 (cache updates) ≈ 11 writes.
   * With **1M searches/sec**, total writes ≈ **11M writes/sec** → system is **read & write heavy**.

---

### Sharding

* Automatic, based on `hash(key)` of the prefix or query.
* Distributes both reads and writes across multiple servers.

---

## Optimizing the System

### Read-heavy System

* If **eventual consistency** is acceptable → absorb reads in **cache**, optimize DB for writes.
* If **immediate consistency** is required → optimize DB for reads; both reads & writes go to DB (slower than cached approach).

### Write-heavy System

* Absorb reads in cache.
* Optimize DB for writes.

### Read & Write Heavy System

* Very difficult to handle.
* Strategies to reduce write load:

  * **Batching** — combine multiple updates before writing (forces eventual consistency).
  * **Sampling** — selectively process some requests (may cause data loss).
* If writes cannot be reduced → **shard more**, but joins across shards become inefficient.

---

### Optimizing Writes

* **Leverage eventual consistency & allowable data loss** to reduce write load.

* **Batch Processing**:

  * Instead of updating the suggestions DB on every `log_search`, update only after counts increase by a threshold (e.g., 1000).

* **Sampling**:

  * Process only a fraction of `log_search` requests.
  * Example:

```python
def search(query):
    ...
    if random() < 0.001:
        # with a probability of 1/1000, call the log_search endpoint
        typeahead_service.log_search(query)
```

* Both techniques reduce **write frequency**, making the system more manageable under high load.

---

## Future Scope

* **Recency Factor** — give higher weight to recent searches.
* **Geolocation-based Personalization** — suggest queries relevant to the user’s location.
* **User-based Personalization** — personalize suggestions using the user’s search history.
* **Handling Typos** — support fuzzy matching and spell correction.

---
