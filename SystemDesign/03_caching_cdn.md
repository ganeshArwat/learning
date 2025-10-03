
## Cache

A **cache** is a high-speed storage layer that temporarily stores frequently accessed data to reduce latency, decrease load on underlying storage, and improve system performance. Caches are used in various layers such as memory, database, and web applications.

---

## Need for Caching

Caching is essential because:

1. **Reduce Latency:** Data retrieval from cache is faster than from the primary storage.
2. **Reduce Database Load:** Frequent queries can be served from cache, reducing backend stress.
3. **Improve Scalability:** Cached responses allow the system to handle more requests efficiently.
4. **Cost Efficiency:** Reduces expensive operations like database reads or remote API calls.

---

## Content Delivery Network (CDN)

A **Content Delivery Network (CDN)** is a network of servers distributed across different geographic locations that **store cached copies of your content**. The main goal is to serve content **faster and more reliably** to users by delivering it from the **nearest server** rather than the origin server.

**Key Points:**

* Reduces latency and improves website load times.
* Offloads traffic from the origin server.
* Commonly used for static assets like images, videos, CSS, JavaScript, and sometimes dynamic content.
* Examples: Cloudflare, Akamai, AWS CloudFront.

In short: **CDN = faster content delivery + less load on your servers.**

Here’s how a **CDN works** in simple terms:

1. **Content Replication:**

   * The origin server (your main server) sends copies of your website’s static content (images, CSS, JS, videos) to multiple CDN **edge servers** located around the world.

2. **User Request Routing:**

   * When a user requests content, the CDN automatically **routes the request** to the nearest edge server instead of your origin server.

3. **Cache Hit or Miss:**

   * **Cache Hit:** If the edge server already has the requested content, it serves it immediately.
   * **Cache Miss:** If the content isn’t cached, the edge server fetches it from the origin server, serves it to the user, and stores a copy for future requests.

4. **Content Updates / Invalidation:**

   * When content changes on the origin server, CDNs can **invalidate or refresh** cached copies to ensure users get updated content.

5. **Benefits:**

   * Faster load times (content served from nearest server).
   * Reduced bandwidth and load on origin server.
   * Better handling of high traffic spikes.

**Analogy:** Think of a CDN as multiple **mini-stores around the city**. Instead of everyone going to the main warehouse (origin server), they go to the nearest store (edge server) to get what they need quickly.

---

## Backend Cache

Backend caches store data closer to the application to improve response times and reduce backend load. Examples include Redis and Memcached.

### Local vs Global

* **Local Cache:** Stored in the application memory or process.

  * Fastest access.
  * Limited by application memory.
  * Example: In-memory cache like `Node.js` LRU cache.
* **Global Cache:** Shared across multiple instances of the application.

  * Slightly slower than local cache.
  * Allows consistency across multiple servers.
  * Example: Redis cluster shared across servers.

### Single vs Distributed

* **Single Cache Instance:** All data resides on a single cache server.

  * Simple setup.
  * Risk: Single point of failure.
* **Distributed Cache:** Data is distributed across multiple servers.

  * High availability.
  * Scalability for large datasets.
  * Example: Redis Cluster, Memcached Cluster.

---

## Cache Invalidation

Cache invalidation determines **when cached data should be removed or updated** to prevent serving stale information.

### Time to Live (TTL)

* Each cache entry has a TTL value.
* Once TTL expires, the cache automatically deletes the entry.
* Ensures data freshness.

### Write Around

* Writes bypass the cache and go directly to the database.
* Cache is updated only when the data is read next.
* Pros: Reduces write load on cache.
* Cons: First read after write is slower.

### Write Through

* Data is written to the cache **and** the database simultaneously.
* Ensures cache is always updated.
* Pros: Strong consistency.
* Cons: Write latency increases.

### Write Back (Write Behind)

* Data is written only to the cache initially.
* Cache asynchronously writes to the database later.
* Pros: Fast writes.
* Cons: Risk of data loss if cache fails before writing to DB.

---

## Cache Eviction

When the cache is full, eviction policies determine **which data to remove**:

1. **LRU (Least Recently Used):** Removes the data least recently accessed.
2. **LFU (Least Frequently Used):** Removes the data accessed least often.
3. **FIFO (First In First Out):** Removes the oldest data.
4. **Random:** Removes random entries when cache is full.

---

