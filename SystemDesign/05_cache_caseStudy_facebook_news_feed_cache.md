---

# **Facebook News Feed System Design**

---

## 🧩 **Situation**

* **Monthly Active Users (MAU):** ~3 Billion
* Users can **make posts** on someone’s profile.
* Facebook earns primarily via **ads** — showing people relevant content in their newsfeed.

---

### **Each Post Has**

* **Author:** Who made the post
* **Recipient:** Whose profile the post was made on
* **Content:** The actual text/media of the post

> Note: A user can post on their own profile → in that case, **author = recipient**

---

### **Friendship Graph**

* Users can be **friends** with other users
* On average, each user has **~1000 friends** in the Facebook social graph

---

### **Fun Fact**

> **Hypothesis:** “7 Degrees of Separation” — between any two people in the world, there are only 7 connections (friend → friend → friend …).

* Facebook tested this on its own social graph.
* Ignoring isolated users, they found the **average degree of separation ≈ 4**.
* In **Graph Theory**, this is referred to as the **diameter** of the graph.

---

## 🗄️ **Facebook Database Schema (Simplified)**

---

### **1️⃣ users_profiles**

Stores user information.

| Column Name  | Type                            | Description           |
| ------------ | ------------------------------- | --------------------- |
| `id`         | BIGINT (PK)                     | Unique user ID        |
| `name`       | VARCHAR                         | User’s name           |
| `gender`     | ENUM('male', 'female', 'other') | Gender                |
| `avatar_url` | VARCHAR                         | Profile picture URL   |
| `created_at` | DATETIME                        | Account creation time |
| `updated_at` | DATETIME                        | Last updated time     |

---

### **2️⃣ user_friends (Social Graph)**

Represents friendship connections between users.

| Column Name  | Type                            | Description                     |
| ------------ | ------------------------------- | ------------------------------- |
| `user_1_id`  | BIGINT (FK → users_profiles.id) | First user                      |
| `user_2_id`  | BIGINT (FK → users_profiles.id) | Second user                     |
| `created_at` | DATETIME                        | When the friendship was created |

**Notes:**

* Friendship is **bidirectional**, so both directions are stored.

**Example:**

| user_1_id | user_2_id | created_at |
| --------- | --------- | ---------- |
| Abhi      | Akshay    | 2020       |
| Akshay    | Abhi      | 2020       |

---

### **3️⃣ user_posts**

Stores all user-generated posts.

| Column Name  | Type                            | Description                       |
| ------------ | ------------------------------- | --------------------------------- |
| `post_id`    | BIGINT (PK)                     | Unique post ID                    |
| `author_id`  | BIGINT (FK → users_profiles.id) | Who made the post                 |
| `profile_id` | BIGINT (FK → users_profiles.id) | Whose profile it was posted on    |
| `content`    | JSON / TEXT                     | Post content (text, images, etc.) |
| `created_at` | DATETIME                        | Post creation time                |
| `updated_at` | DATETIME                        | Last updated time                 |

**Examples:**

| post_id | author_id | profile_id | content                |
| ------- | --------- | ---------- | ---------------------- |
| 1       | Abhi      | Akshay     | "Happy Birthday, bro!" |
| 2       | Akshay    | Akshay     | "Vacation time ☀️🏖️"  |

---

## 🧍‍♂️ **1️⃣ User Profile Feed**

Displays **all posts made on a user’s profile**, regardless of who wrote them.

### **Logic**

> Show any post where the **recipient = this user**.

### **SQL Query**

```sql
SELECT *
FROM user_posts
WHERE profile_id = [user_id];
```

### **Example**

* Tarun’s profile will show:

  * Posts made **by Tarun** on his own profile
  * Posts made **by Tarun’s friends** on Tarun’s profile

---

## 📰 **2️⃣ User Newsfeed**

Displays **recent & relevant posts** made by the user’s friends or followed users.

---

### **a. Get Recent Posts by Friends**

```sql
SELECT *
FROM user_posts
WHERE profile_id IN (
    SELECT user_2_id
    FROM user_friends
    WHERE user_1_id = [user_id]
)
AND updated_at > NOW() - INTERVAL 30 DAY;
```

* Gets all posts made in the **last 30 days** by the user’s friends.

---

### **b. Calculate Post Relevance (Ranking Factors)**

Each post is assigned a **relevance score** based on multiple signals:

| Factor                    | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| 📰 **News Factor**        | Type of content (status, image, trending topic, etc.)   |
| ⏰ **Recency**             | How recent the post is                                  |
| ⚡ **Shock Value**         | Emotional or viral potential                            |
| 💬 **User-User Affinity** | Interaction level between author and viewer             |
| 📍 **Geo-location**       | Proximity of the author to the viewer                   |
| 📊 **Other Signals**      | Facebook uses over **2000 ranking parameters** in total |

---

### **c. Sort Posts by Relevance**

```sql
ORDER BY relevance_score DESC;
```

---

### **d. Paginate the Data**

For performance and UX:

```sql
LIMIT 20 OFFSET [page_number];
```

---

### **Hence the Need for Caching ⚙️**

* Computing relevance scores and aggregating posts from thousands of friends is **expensive**.
* To reduce load:

  * Pre-compute and **cache the newsfeed** for each user (e.g., in Redis or Memcached).
  * Update incrementally when new posts appear or users interact.

---

✅ **Summary**

| Component             | Purpose                                                         |
| --------------------- | --------------------------------------------------------------- |
| **User Profile Feed** | Shows all posts made *on the user’s profile*                    |
| **User Newsfeed**     | Shows *recent and relevant* posts from *friends/followed users* |
| **Caching**           | Reduces recomputation and improves response time                |

---

## 📊 **Scale Estimation**

**Assumptions:**

* **Monthly Active Users (MAU):** ~3 Billion
* **Daily Active Users (DAU):** ~2 Billion

---

### **1️⃣ Daily Content Creators**

Applying the **80-20-1 principle**:

| User Type               | % of DAU  | Behavior                                                              |
| ----------------------- | --------- | --------------------------------------------------------------------- |
| Passive Watchers        | 80%       | Scroll through feed, watch reels, rarely interact                     |
| Active Watchers         | 20%       | Interact with content (like, comment, share), but rarely create posts |
| Active Content Creators | 1% of DAU | Regularly create posts                                                |

**Number of active content creators per day:**
```
= 1% of 2 Billion
= ~20 Million
```

---

### **2️⃣ Posts per Day**

* **Average posts per active user per day:** 5
* **Total posts per day:**
```
(5 posts / active user / day) * (20 M active users)
= 100 Million posts / day
```
---

### **3️⃣ Total Posts over 20 Years**

* Approximate days per year: 400 (rounded)
* **Total posts:**
```
(100 Million posts / day) * (20 years)
= (100 Million posts / day) * (20 * 365 days)
365 ~ 400
= (100 Million posts / day) * (20 * 400 days)
= ~800 Billion posts
```

---

### **4️⃣ Average Size of a Post**

| Field            | Size      |
| ---------------- | --------- |
| `post_id`        | 16 bytes  |
| `author_id`      | 16 bytes  |
| `profile_id`     | 16 bytes  |
| `content`        | 100 bytes |
| `attachment_url` | 200 bytes |
| `created_at`     | 16 bytes  |
| `updated_at`     | 16 bytes  |
| `location`       | 16 bytes  |
| `feeling`        | 1 byte    |

**Total per post:** ~500 bytes

---

### **5️⃣ Total Data Size**

```
Total amount of post data (over 20 years) = (800 billion posts) * (500 bytes per post)
                                           = (8 * 10^11 posts) * (5 * 10^2 bytes per post)
                                           = 40 * 10^13 bytes
                                           = 400 TB
```


> 💡 This gives a rough estimate of storage needed for **post data** over 20 years.

---


## ⚡ **Need for Caching**

---

### **Q1: Does all the data fit on a single machine?**

* **No.**

  * Modern tech might allow storing all data on a single server.
  * **Problem:** Even if it fits, a single server **cannot handle queries for billions of users**.
  * It also becomes a **bottleneck** and a **single point of failure**.

✅ **Solution:** Shard & replicate data across multiple servers.

---

### **Q2: Ideal Sharding Key**

* **Shard by `user_id`**: Each user's data lives entirely inside a single shard.

**User’s data includes:**

1. All posts made by the user (on their own or others’ profiles)
2. All posts made **on the user’s profile**

**Example Posts:**

| Post | Author → Recipient  | Content                      |
| ---- | ------------------- | ---------------------------- |
| P1   | Mukesh → Shubhadeep | Hi, how are you              |
| P2   | Shubhadeep → Mukesh | Doing fine, wassup with you? |
| P3   | Dinesh → Mukesh     | We’re both …kesh             |
| P4   | Vinetha → Harshit   | Happy B’day                  |
| P5   | Harshit → Mukesh    | Bro, today’s my B’Day        |

**Sharding & Replication:**

| Shard / Server               | Posts Stored   |
| ---------------------------- | -------------- |
| Mukesh (Server 1)            | P1, P2, P3, P5 |
| Shubhadeep (Server 2)        | P1, P2         |
| Vinetha & Harshit (Server 2) | P4, P5         |

> **Replication:** Each post is stored in **two shards** (author + recipient) so that a user’s data is always quickly accessible.

**Note:** A single server stores **multiple users’ data**.

---

### **Q3: Server Storage Estimation**

* Each server has **1 TB storage**
* Each post ≈ **500 bytes**

```
Number of posts per server = 1TB / (500 bytes per post)
                           = 1 * 10^12 bytes / (500 bytes per post)
                           = 2 billion posts
```


* Average posts per user (lifetime): **5000 posts**
* Users per server:

```
Number of users per server = (2 billion posts per server) / (5000 posts per user)
                           = 2 billion / 5000 users per server
                           = 400,000 users per server
```

---

### **Q4: Fetching a User’s Profile**

* **Easy:** All posts on a user’s profile live in **that user’s shard**
* Example: Viewing **Tarun’s profile** → query **Tarun’s shard only**
* ✅ Only 1 DB shard hit needed

---

### **Q5: Fetching Data for Newsfeed**

* **Requirement:** All recent posts by **all friends of the user** (friends’ posts on any profile)
* **Challenge:**

  * Friends can reside in **any shard**
  * Retrieving their posts requires hitting **every shard** → **very expensive**

✅ **Solution:** **Caching**

* Precompute & store newsfeed data
* Reduces read latency and avoids repeated fan-out queries

---

## ⚡ Caching the Newsfeed for All Users

Fetching a user’s newsfeed requires:

* Reading posts from all shards (**fan-out**)
* Scoring posts against **2000+ parameters** (recency, shock value, etc.)

This is **expensive**, so we cache results.

---

### **Newsfeed Size Estimation**

* **Posts per page:** 10
* **Max pages:** 50
* **User example:** 1000 friends, each with 10 recent posts → 10,000 posts → limit to top 500 posts

**Total newsfeed data size**:

```
Total Newsfeed size = (500 bytes/post) * (10 posts/page) * (50 pages/user) * (3 billion users)
                    = 75 * 10,000 billion bytes
                    = 750 TB
```

> ⚠️ Note: 20 years of posts = 400TB, but the newsfeed cache (recent posts replicated per user) = 750TB
> Reason: Each post is potentially replicated in thousands of users’ newsfeeds.

---

### **Challenges with Caching Entire Newsfeed**

1. Every new post invalidates friends’ newsfeeds (~1000 friends per user)
2. Frequent updates to ranking algorithm (4–5 times/day) would invalidate the entire cache
3. Precomputing and caching **all users’ newsfeeds** is impractical

**Optimization Idea (Mukesh):**

* Cache only the **first 5 pages** instead of all 50
* Reduces cache size **10x** → from 750TB to ~75TB
* High hit rate maintained

---

### **Optimizing Newsfeed Calculation**

* Only **recent posts** matter (e.g., last 30 days)
* **Size of recent 30 days of posts**:

```
Recent post data = 100 million posts/day * 500 bytes/post * 30 days
                 = 15 * 10^5 million bytes
                 = 1.5 TB
```

* 1.5TB easily fits on a single server
* No need to shard the **recent posts DB** → no fan-out needed
* Multiple read replicas can handle high request volume

---

### **Recent Posts DB Flow**

1. Post is stored in user DB shards (author + recipient)
2. Post is also inserted into **recent_posts_db**
3. Profile queries still hit user shards
4. Newsfeed queries now hit **recent_posts_db** → avoids fan-out

> **Recent_posts_db** = SQL database, but used as a **cache** for faster access

---

### **Schema for Recent Posts DB**

Same as user shards:

```
users
  id, name, gender, ...
user_friends
  user_1_id, user_2_id, created_at
user_posts
  post_id, author_id, profile_id, content
```

---

### **Eviction Policy**

* Recent posts < 1.5TB → eviction not required
* Optionally: set TTL to remove posts older than 30 days
* If HDD full → evict **least recently updated** posts
* Eviction happens **lazily** during inserts, not reads

---

### **Invalidation Policy**

1. **Older posts**:

   * Cron job at midnight removes posts older than 30 days

   ```
   DELETE FROM recent_posts_db.user_posts
   WHERE updated_at < (NOW() - INTERVAL 30 DAY)
   ```

   * Or use TTL for lazy deletion

2. **Edited posts**:

   * Update user DB shards (author + recipient)
   * Periodically replicate into **recent_posts_db**
   * **Write-around caching**

---

### **Consistency Requirements**

* **Eventual consistency** is acceptable:

  * A post may take time to appear in friends’ newsfeeds
  * Edited posts may temporarily show old versions

---

### **Learning**

* Precomputing full newsfeed is **impractical**
* Cache **recent posts** only → smaller, manageable, and fast

---

### **Mandatory Reading / References**

* [Scaling with Redis – Eviction Policies & Cluster Mode](https://docs.google.com/document/d/1k4nzubvtX_yLctUT4VWK8ZJt4KCcOEdRJdxQgWCaiU8/edit?tab=t.0#heading=h.jyks8brdqpi5)
* Backend Benchmarks: [TechEmpower](https://www.techempower.com/benchmarks/)
* Frontend Framework Benchmarks: [JS Framework Benchmark](https://krausest.github.io/js-framework-benchmark/)

---

