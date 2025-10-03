# ⚡ 5 Step Process to Cache Design

---

## **1. Establish the Need for Caching**

Cache when recomputation or data fetch is expensive:

* **Heavy Computation**

  * Don’t recompute on every request if it’s costly.
  * Example: DB joins across many tables.

  ```java
  public HTTPResponse getQuestionsPage(question_id) {
      cached_response = redis.get(question_id);
      if (cached_response != null)
          return cached_response;

      rows = sql_client.execute(`
          select *
          from questions
          join ...
          join ...
          -- imagine 100 joins here
      `);

      response = CreateQuestionHTMLPage(rows);
      redis.set(question_id, response); // cache it
      return response;
  }
  ```

* **Large Input Data, Small Response**

  * If computing response requires **fetching a lot of data** repeatedly, cache the result instead of re-fetching.

---

## **2. Determine the Type of Cache**

### Local vs Global

* **Local Cache (in-app memory/disk)**

  * Good when **data transferred per request is large** (avoid network overhead).
  * Good for immediate consistency (since only one server handles it).

* **Global Cache (e.g., Redis, Memcached)**

  * Preferred if request/response data is small.
  * Shared across all servers.
  * May add network hop, but ensures consistency across app servers.

### Single vs Distributed (only for Global)

* **Single Cache Server**

  * Works if data is small and request load is low (< 50k req/sec).

* **Distributed Cache**

  * Required if:

    1. Data too large for one server → **Sharding**.
    2. Requests too high for one server → **Replication**.

---

## **3. Identify the Invalidation Algorithm**

Depends on **consistency requirements**:

* **Eventual Consistency (stale reads acceptable)**

  * If query is **simple & fast** → use **TTL** (auto expiry).
  * If query is **slow/complex** → use **Write-Around** (background recompute & store).

* **Immediate Consistency (must always be fresh)**

  * Use **Write-Through** (update DB + cache on every write).
  * Works well with **local caches** (atomic updates in RAM/disk).

* **Write-Back (rarely used)**

  * Use only if:

    1. Okay with **data loss** risk.
    2. Only care about **trends/analytics**, not exact values.
    3. Need **very high write throughput**.

---

## **4. Identify the Eviction Algorithm**

* ✅ Default: **LRU (Least Recently Used)**

  * Simple, efficient, widely supported in Redis/Memcached.

---

## **5. Think About Cache Load Balancer**

* **Single Cache** → No load balancer needed.

* **Distributed Cache** → Depends on reason for distribution:

  1. **Sharding (data too large)** → Use **Consistent Hashing** to map keys to shards.
  2. **Replication (too many requests)** → Use **Round Robin** to balance requests across replicas.
  3. **Sharding + Replication** →

     * Consistent Hashing across shards (pick correct shard).
     * Round Robin across replicas of each shard.

---

✅ This process gives a **step-by-step decision framework** for cache design — from **why cache is needed** to **what eviction & load balancing strategy to use**.

---