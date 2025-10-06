## **What and Why of HLD**

### 1. **DSA (Data Structures & Algorithms)**

* **Purpose**: Solving computational problems efficiently.
* **Scope**: Focused on *individual program logic*, not full system.
* **Examples**: Sorting, searching, graph algorithms, dynamic programming.
* **Use Case in Interviews**: Checks if you can write optimal, bug-free code.

👉 Think of **DSA** as your *toolbox* (arrays, stacks, trees, graphs, etc.).

---

### 2. **LLD (Low-Level Design)**

* **Purpose**: Converting requirements into **detailed object-oriented design**.
* **Scope**:

  * Classes, methods, relationships (inheritance, composition).
  * Design patterns (Factory, Singleton, Observer, etc.).
  * UML diagrams.
* **Example**:
  If requirement is “build a Parking Lot system”:

  * Define classes like `ParkingLot`, `Vehicle`, `Ticket`, `Payment`.
  * Define how they interact.

👉 **LLD ensures code is maintainable, reusable, and extendable.**

---

### 3. **HLD (High-Level Design)**

* **Purpose**: Designing **system architecture** at a macro level.
* **Scope**:

  * Components, APIs, databases, communication between services.
  * Non-functional requirements (scalability, availability, reliability, performance).
  * Trade-offs between SQL vs NoSQL, caching strategies, load balancing, etc.
* **Example**:
  If requirement is “design YouTube”:

  * Identify components → Video Service, User Service, Recommendation Service.
  * Decide storage → Blob storage for videos, DB for metadata.
  * Handle scaling → CDN, sharding, replication.

👉 **HLD ensures the system works at scale and meets business needs.**

---

### ⚖️ DSA vs LLD vs HLD (Quick Table)

| Level   | Focus                                      | Example Question                    | Output                      |
| ------- | ------------------------------------------ | ----------------------------------- | --------------------------- |
| **DSA** | Algorithms & data structures               | "Find the shortest path in a graph" | Code function               |
| **LLD** | Classes, methods, OOP design               | "Design a parking lot system"       | Class diagrams + methods    |
| **HLD** | Architecture, scaling, distributed systems | "Design Instagram backend"          | System diagram + components |

---

✅ **Why HLD is Important?**
Because companies like Google, Amazon, Uber, Netflix deal with **millions of users**. Without HLD:

* Apps crash under load.
* Data may be lost.
* Latency increases → bad UX.



## Case Study of del.icio.us


## 🌐 How the Internet Works

### 1. **ISP (Internet Service Provider)**

* ISP = the company that connects you to the internet (Airtel, Jio, BSNL, Comcast, etc.).
* When you type a website URL:

  1. Your device sends a request to ISP.
  2. ISP routes it to the global internet backbone.
  3. Response comes back to you through ISP.
* ISPs maintain **gateways, routers, DNS resolvers**.

---

### 2. **IP Addresses**

* Every device on the internet has an **IP address**.

#### 🔹 IPv4

* 32-bit addresses.
* Format: `xxx.xxx.xxx.xxx` (e.g., `192.168.0.1`).
* Total \~4.3 billion addresses.
* **Problem**: Ran out of addresses (too many devices).

#### 🔹 IPv6

* 128-bit addresses.
* Format: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.
* Almost unlimited (3.4 × 10³⁸ addresses).
* Built-in **security & auto-configuration** features.

---

### 3. **Domain Names**

* IP addresses are hard to remember → we use **human-friendly names**.
* Example:

  * IP: `142.250.182.14`
  * Domain: `google.com`.
* Domain names are just a **mask** over IP addresses.

---

### 4. **DNS (Domain Name System)**

Like a **phonebook of the internet**.

* Converts **domain names → IP addresses**.
* Without DNS, you would need to type IPs instead of `youtube.com`.

#### 🔹 What is DNS?

* A **distributed system** of servers that resolve domain names.
* When you type `facebook.com`:

  1. Browser checks cache (local DNS).
  2. If not found → ISP’s DNS resolver.
  3. Resolver queries **Root → TLD → Authoritative DNS**.
  4. Returns the IP address.

---

#### 🔹 DNS Structure

* **Root Servers** (`.`) → global starting point.
* **TLD Servers** (`.com`, `.org`, `.in`).
* **Authoritative Servers** → hold actual IP mappings for domains.
* **Resolver** → the middleman (usually your ISP).

---

#### 🔹 DNS Records & Types

DNS servers store **records**. Important ones:

1. **A Record (Address Record)**

   * Maps **domain name → IPv4 address**.
   * Example: `example.com → 93.184.216.34`.

2. **AAAA Record**

   * Maps domain → IPv6 address.

3. **CNAME (Canonical Name Record)**

   * Maps one domain to another (alias).
   * Example: `blog.company.com → company.com`.

4. **MX Record (Mail Exchange)**

   * Defines email servers for a domain.

5. **NS Record (Name Server)**

   * Points to authoritative DNS servers.

6. **TXT Record**

   * Stores arbitrary text (used for verification, SPF, DKIM for emails).

---

#### 🔹 Domain Extensions

* The **last part of a domain name**:

  * `.com`, `.org`, `.edu`, `.gov`, `.net`.
  * Country codes: `.in` (India), `.uk`, `.jp`.
  * New TLDs: `.app`, `.dev`, `.io`.

---

✅ **Quick Example: Visiting `www.youtube.com`**

1. You type `www.youtube.com`.
2. Browser → checks cache.
3. ISP DNS Resolver → queries Root → `.com` TLD → YouTube’s DNS.
4. Gets IP → `142.250.190.46`.
5. Browser connects to server → YouTube loads.

---

# ⚡ Types of Scaling

### 1. **Vertical Scaling (Scale Up)**

* Increase **power of a single server**.
* Add more **CPU, RAM, Storage**.
* ✅ Pros: Simple, no code change, single machine.
* ❌ Cons: Expensive, hardware limits, single point of failure.
* Example: Moving from 8 GB RAM → 64 GB RAM.

---

### 2. **Horizontal Scaling (Scale Out)**

* Add **more servers** to handle load.
* Distribute requests among them.
* ✅ Pros: High availability, fault tolerance, theoretically infinite scaling.
* ❌ Cons: More complexity (sync, caching, data consistency).
* Example: Instead of 1 big DB → use 10 smaller DB shards.

---

### 3. **Which Scaling to Use?**

* **Start with Vertical Scaling** → easier, cheaper for small scale.
* **Switch to Horizontal Scaling** → when traffic grows beyond single machine’s capacity.
* Real systems (Google, Netflix, Amazon) → rely on **Horizontal Scaling**.

---

# ⚡ Challenges with Horizontal Scaling

👉 **Which server IP should the DNS register?**

* If you have 100 servers → you cannot map domain → 100 IPs.
* **Solution**: Register **Load Balancer IP** in DNS.

  * Client → DNS → **Load Balancer** → routes request to servers.

---

# ⚡ Load Balancing

Load balancer distributes traffic across servers.

### 1. **Heartbeat (Push-based)**

* Each server **pushes heartbeat signals** to LB.
* If LB doesn’t get a heartbeat → assumes server is dead.

### 2. **Health Check (Pull-based)**

* LB **pings servers regularly** (HTTP / TCP checks).
* If no response → remove from rotation.

### 3. **What if the Load Balancer Crashes?**

* LB itself can be a **Single Point of Failure (SPOF)**.
* Solutions:

  * Multiple LBs in **Active-Passive** or **Active-Active** mode.
  * Use **DNS-based Load Balancing (GeoDNS)**.
  * Cloud providers (AWS ELB, GCP LB) give managed redundant LBs.

### 4. **Geo DNS**

* DNS resolves domain to **nearest server region** (India user → India DC).
* Improves **latency & performance**.

### 5. **Other DNS-based balancing**

* Weighted round robin DNS.
* Anycast routing (one IP, many servers globally).

### 6. **Active-Passive Rollover (Rare)**

* Have a backup LB in passive mode.
* If primary LB fails → switch DNS to passive LB.

### 7. **Common Load Balancers**

* Nginx, HAProxy, Envoy.
* Cloud LBs: AWS ELB/ALB, GCP LB, Azure LB.

---

# ⚡ Routing Algorithms

### 1. **Round Robin**

* Requests go to servers in **circular order**.
* Example: Req1 → S1, Req2 → S2, Req3 → S3, Req4 → S1 …
* ✅ Simple, fair.
* ❌ Doesn’t consider server load differences.

### 2. **Consistent Hashing**

* Requests are mapped to servers using **hashing**.
* Good for caching systems (e.g., distributed caches, CDNs).
* ✅ Reduces re-mapping when servers join/leave.
* Example: `hash(user_id) % N` → decides which server.

---

✅ **Takeaway:**

* Scaling is crucial → vertical for small scale, horizontal for large scale.
* Load balancers solve the “which IP to hit?” problem.
* Routing algorithms decide how to distribute traffic efficiently.

---
