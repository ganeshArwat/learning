# Backend Machine Coding Round: Overview & Case Studies 🚀

#### A Backend Machine Coding Round tests your ability to design and implement a small but functional backend system in a limited time (usually 60–120 minutes). It evaluates:

- ✅ API Design & RESTful Principles
- ✅ Database Schema Design & Query Optimization
- ✅ Authentication & Authorization
- ✅ Error Handling & Edge Cases
- ✅ Scalability & Performance Optimizations
- ✅ Code Readability & Best Practices

## 🔹 Types of Backend Machine Coding Problems

1. URL Shortener (like Bit.ly)
2. Rate Limiter (Throttle API requests)
3. CRUD API (User Management, Blog, Product Catalog, etc.)
4. Order Management System
5. Authentication System (JWT, OAuth)
6. Message Queue System (RabbitMQ, Kafka-like simulation)
7. Real-time Chat App Backend (WebSockets, Socket.io)
8. File Upload & Storage API
9. Background Job Scheduler
10. Leaderboard System (Caching, Ranking Algorithms)

---

### 🔹 How to Ace Backend Machine Coding Rounds?

- ✅ Understand requirements clearly (Ask clarifying questions)
- ✅ Choose the right tech stack (Node.js, Express, FastAPI, Spring Boot, etc.)
- ✅ Plan Database Schema first (SQL vs. NoSQL)
- ✅ Handle edge cases (Invalid input, API failures, security threats)
- ✅ Optimize performance (Caching, Pagination, Load Balancing)
- ✅ Write modular, reusable code (Follow SOLID principles)

---

## 🔹 Case Study 1: URL Shortener (Node.js + Express + MongoDB)

### Requirements:

- ✅ Shorten a given long URL (like Bit.ly)
- ✅ Retrieve the original URL from the short URL
- ✅ Track the number of visits
- ✅ Handle duplicate URLs

### Implementation Plan

1. Database Schema (MongoDB)

```json
{
  "originalUrl": "https://example.com/some-long-url",
  "shortUrl": "xyz123",
  "clicks": 0,
  "createdAt": "2025-03-23T00:00:00Z"
}

```

2. API Endpoints

   - POST /shorten → Shortens a given URL
   - GET /:shortUrl → Redirects to the original URL & updates visit count

3. Key Challenges & Solutions
   - Handling duplicates (Check if the URL already exists in the DB)
   - Efficient short URL generation (Use crypto.randomBytes)
   - Performance Optimization (Cache frequent lookups using Redis)

---

## 🔹 Case Study 2: Rate Limiter (Express + Redis)

### Requirements:

- ✅ Limit API requests per user (e.g., 100 requests per hour)
- ✅ Return 429 Too Many Requests if the limit is exceeded
- ✅ Store rate limit data efficiently

### Implementation Plan

1. Middleware for Rate Limiting

```js
const rateLimit = (req, res, next) => {
  const ip = req.ip;
  const currentTime = Math.floor(Date.now() / 1000); // Current time in seconds

  redis.get(ip, (err, data) => {
    if (data && data >= 100) {
      return res.status(429).json({ message: "Rate limit exceeded!" });
    } else {
      redis.incr(ip);
      redis.expire(ip, 3600); // Expire after 1 hour
      next();
    }
  });
};
```

2. Apply Middleware to APIs

```js
app.use("/api", rateLimit);
```

3. Key Challenges & Solutions
   - Handling High Traffic → Use Redis for fast lookups
   - User-based Rate Limiting → Use API keys or JWT-based tracking
