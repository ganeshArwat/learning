
# AVAILABILITY AND SCALABILITY

---

## 🧠 Concept Overview

When you deploy apps in the cloud (like EC2, RDS, etc.), two critical goals are:

1. **Scalability** → Can my system handle more load when users increase?
2. **High Availability (HA)** → Will my system keep working if one part fails?

Think of it like this:

> **Scalability = Grow bigger**
> **High Availability = Stay alive**

Let’s learn both — step by step 👇

---

# Scalability & High Availability

• Scalability means that an application/system can handle greater loads by adapting.
• There are two kinds of scalability:

* **Vertical Scalability**
* **Horizontal Scalability (= elasticity)**
  • Scalability is linked but different from High Availability.
  • Example analogy: **Call Center**
* More callers coming in?

  * Add more phone lines (vertical)
  * Add more agents (horizontal)

---

## 🧩 Vertical Scalability

### 🔹 Concept:

• Vertically scalability means **increasing the size** of the instance.
• Example:

* Your app runs on a **t2.micro**
* Scaling vertically → move to **t2.large**

### 🔹 Real-world Analogy:

Like upgrading your laptop — same user, more RAM and CPU.

### 🔹 In AWS:

• Common for **non-distributed systems**, like **databases** (RDS, ElastiCache).
• Limited by **hardware ceiling** — you can’t grow infinitely.

---

### ⚙️ Example:

| Instance Type | vCPU | RAM   |
| ------------- | ---- | ----- |
| t2.micro      | 1    | 1 GB  |
| t3.medium     | 2    | 4 GB  |
| m6i.4xlarge   | 16   | 64 GB |

> If your app needs more power → move up instance family = **Vertical Scale Up**

---

### 📊 Diagram (Mental Model)

```
Vertical Scaling
   ↑ Power
   │
   │     +---------+
   │     | t2.nano |
   │     +---------+
   │     | t2.micro|
   │     +---------+
   │     | t2.large|
   │     +---------+
   │
   └──────────────▶
      Same server, more resources
```

---

## Horizontal Scalability

### 🔹 Concept:

• Increase the **number of instances** for your application.
• Implies **distributed system design**.
• Common for **web apps** and **microservices**.
• The cloud (like AWS EC2) makes this **easy and dynamic**.

### 🔹 Analogy:

Like adding more employees instead of making one person work harder.

### 🔹 Example:

* Instead of 1 large EC2 → run 10 smaller EC2s behind a **Load Balancer**.

---

### 📊 Diagram:

```
Horizontal Scaling
   ┌──────────────┐
   │ Load Balancer│
   └──────┬───────┘
          │
 ┌────────┴─────────┐
 │ EC2 #1  EC2 #2   │
 │ EC2 #3  EC2 #4   │
 └───────────────────┘
        ↑ Same size, more nodes
```

---

## High Availability (HA)

### 🔹 Concept:

• **High Availability** means your app can **survive data center failures**.
• Run in **multiple Availability Zones (AZs)**.
• Usually pairs with **horizontal scaling**.

### 🔹 Example:

* 1 EC2 instance in **us-east-1a**
* 1 EC2 instance in **us-east-1b**
* If one AZ goes down, the other still runs your app.

### 🔹 In AWS:

* Use **Auto Scaling Groups (ASG)** across AZs.
* Use **Load Balancer** to route requests to healthy instances.

---

### 📊 Diagram:

```
     Multi-AZ High Availability
 ┌──────────────┐        ┌──────────────┐
 │ AZ-1 (East-1a)│       │ AZ-2 (East-1b)│
 │   EC2 #1      │       │   EC2 #2      │
 └──────┬────────┘       └──────┬────────┘
        │                       │
        └───────▶ Load Balancer ◀────────┘
```

---

## High Availability & Scalability for EC2

| Concept                | Action                             | AWS Service         |
| ---------------------- | ---------------------------------- | ------------------- |
| **Vertical Scaling**   | Change instance type               | EC2                 |
| **Horizontal Scaling** | Add/Remove instances automatically | Auto Scaling Group  |
| **High Availability**  | Deploy across multiple AZs         | ASG + Load Balancer |

---

# What is Load Balancing?

• Load Balancers are servers that **forward traffic** to multiple backend servers (EC2 instances).
• Example: You have 5 servers running your app → Load Balancer decides who handles which request.

---

### Why Use a Load Balancer?

✅ **Distribute traffic** evenly
✅ **Single DNS endpoint** for users
✅ **Health checks** – remove bad instances automatically
✅ **Handle HTTPS (SSL termination)**
✅ **Support sticky sessions**
✅ **Enable high availability**
✅ **Split public vs. private traffic**

---

### Why Use an Elastic Load Balancer (ELB)?

• **Managed by AWS** → No manual setup, patching, or scaling.
• Integrated with:

* EC2
* Auto Scaling
* ECS
* ACM (SSL)
* CloudWatch
* Route 53
* WAF
* Global Accelerator
  • **Tradeoff:** You pay more but manage nothing yourself.

---

### Health Checks

• Load Balancers test instance health via:

* Port + Route (e.g., `/health`)
* Expected response: **200 OK**
  • If not healthy → traffic is rerouted to others.

---

## Types of Load Balancer on AWS

| Type     | Layer   | Protocol               | Year | Use Case                            |
| -------- | ------- | ---------------------- | ---- | ----------------------------------- |
| **CLB**  | L4 & L7 | HTTP, HTTPS, TCP, SSL  | 2009 | Legacy                              |
| **ALB**  | L7      | HTTP, HTTPS, WebSocket | 2016 | Web apps, microservices             |
| **NLB**  | L4      | TCP, UDP, TLS          | 2017 | High performance, millions of req/s |
| **GWLB** | L3      | IP (GENEVE)            | 2020 | Firewalls, network appliances       |

> Use ALB/NLB for new workloads — CLB is outdated.

---

## Load Balancer Security Groups

• Always allow **inbound** traffic from clients
• Allow **outbound** to backend EC2 instances
• Instances should allow traffic **only from the Load Balancer SG**

---

## Classic Load Balancer (CLB)

• Supports TCP (L4), HTTP/HTTPS (L7)
• Health checks: TCP or HTTP
• Fixed hostname:
`xxx.region.elb.amazonaws.com`

---

## Application Load Balancer (ALB)

• Operates at **Layer 7 (HTTP)**
• Supports **HTTP/2 and WebSocket**
• Perfect for **microservices, ECS, or containers**
• Can **route based on:**

* Path (`/users`, `/posts`)
* Hostname (`api.example.com`, `admin.example.com`)
* Query String / Headers
  • **Dynamic Port Mapping** (great for ECS)

---

### Target Groups

* EC2 instances
* ECS tasks
* Lambda functions
* Private IPs
* Each target group has **its own health check**

---

### HTTP-Based Traffic Flow

```
Client → ALB → Target Group → EC2 / ECS / Lambda
```

---

### Good to Know

• ALB hostname: `xxx.region.elb.amazonaws.com`
• Client IP seen via headers:

* `X-Forwarded-For` → Client IP
* `X-Forwarded-Port` → Port
* `X-Forwarded-Proto` → Protocol (HTTP/HTTPS)

---

## Network Load Balancer (NLB)

• Operates at **Layer 4 (TCP/UDP)**
• **Handles millions of requests/sec**
• **Ultra-low latency**
• One **static IP per AZ** (or assign Elastic IPs)
• Used for:

* Gaming
* IoT
* Financial apps needing high performance

---

## Gateway Load Balancer (GWLB)

• Operates at **Layer 3 (IP layer)**
• Combines:

* Transparent Network Gateway
* Load Balancer
  • Used for:
* Firewalls
* Intrusion detection
* Deep packet inspection
  • Uses **GENEVE protocol (port 6081)**

---

## Quick Summary 🧾

| Concept                | Meaning                  | Example AWS Service |
| ---------------------- | ------------------------ | ------------------- |
| **Vertical Scaling**   | Increase instance size   | EC2, RDS            |
| **Horizontal Scaling** | Add more instances       | EC2 + ASG           |
| **High Availability**  | Survive AZ failures      | ASG + ELB           |
| **Load Balancer**      | Distribute traffic       | ALB, NLB            |
| **Managed ELB**        | AWS handles HA + scaling | ELB (ALB/NLB/GWLB)  |

---

## 🔁 Sticky Sessions (Session Affinity) {#sticky-sessions}

Sticky Sessions (Session Affinity) ensure that a **client always connects to the same backend instance** for the duration of their session.

This is useful when the backend stores session data **locally** (e.g., shopping cart, user login session).

Works with:

* **Classic Load Balancer (CLB)**
* **Application Load Balancer (ALB)**
* **Network Load Balancer (NLB)**

> ⚠️ Stickiness can cause **uneven load** between servers if not managed properly.

---

### 🧠 How It Works

1. The load balancer issues a cookie to the client.
2. The client sends that cookie in each request.
3. The load balancer uses the cookie to route requests to the same instance.

```
User                ELB                 EC2A                EC2B
 |                   |                   |                   |
 |----Request-------->|                   |                   |
 |                    |---Forward-------->|                   |
 |                    |<--Response+Cookie-|                   |
 |<---Response(Set-Cookie)----------------|                   |
 |                   |                   |                   |
 |----Next Request(with Cookie)---------->|                   |
 |                    |---Forward-------->|                   |
 |                    |<--Response--------|                   |
 |<---Response----------------------------|                   |
 |                   |                   |                   |
```


---

## 🍪 Sticky Sessions – Cookie Names {#cookie-names}

There are **two types** of cookies used for stickiness.

### 🔹 Application-based Cookies

| Type                   | Generated By      | Cookie Name             | Description                     |
| ---------------------- | ----------------- | ----------------------- | ------------------------------- |
| **Custom Cookie**      | Target (your app) | Any name (not reserved) | Use your own cookie attributes. |
| **Application Cookie** | Load Balancer     | `AWSALBAPP`             | Managed by ALB.                 |

### 🔹 Duration-based Cookies

| Type    | Generated By  | Cookie Name |
| ------- | ------------- | ----------- |
| **ALB** | Load Balancer | `AWSALB`    |
| **CLB** | Load Balancer | `AWSELB`    |

> 💡 Use **application cookies** for user-specific behavior and **duration cookies** for general stickiness.

---

## 🌐 Cross-Zone Load Balancing {#cross-zone-lb}

### 🎯 What It Does

With **Cross-Zone Load Balancing**, each load balancer node **routes traffic evenly across all registered instances** in **all Availability Zones (AZs)**.

Without it, requests are distributed **only within the same AZ** as the load balancer node — which can lead to imbalance.


```
                 ┌────────────────────────────────┐
                 │          Client Requests        │
                 └────────────────────────────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
 ┌──────────────────────────┐       ┌──────────────────────────┐
 │     ALB Node (AZ1)       │       │     ALB Node (AZ2)       │
 └──────────────────────────┘       └──────────────────────────┘
              │                                 │
       ┌──────┴────────────┬──────────────┐─────┴──────────────┐
       │                   │              │                    │
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ EC2 in AZ1   │   │ EC2 in AZ2   │   │ EC2 in AZ1   │   │ EC2 in AZ2   │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

| Load Balancer Type | Default    | Cross-Zone LB                | Inter-AZ Data Cost |
| ------------------ | ---------- | ---------------------------- | ------------------ |
| **Application LB** | ✅ Enabled  | Can disable per Target Group | ❌ No charge        |
| **Network LB**     | ❌ Disabled | Optional                     | 💲 Charged         |
| **Gateway LB**     | ❌ Disabled | Optional                     | 💲 Charged         |
| **Classic LB**     | ❌ Disabled | Optional                     | ❌ No charge        |

---

## 🔐 SSL/TLS Basics {#ssl-tls}

SSL/TLS ensures **data encryption in transit** between clients and the load balancer.

| Concept                            | Meaning                                      |
| ---------------------------------- | -------------------------------------------- |
| **SSL (Secure Sockets Layer)**     | Older encryption protocol                    |
| **TLS (Transport Layer Security)** | Newer, secure version of SSL                 |
| **Certificate Authority (CA)**     | Issues trusted certificates                  |
| **Examples**                       | DigiCert, GlobalSign, Let’s Encrypt, GoDaddy |

> 🔒 Always use **TLS** (SSL is outdated). Certificates expire and must be renewed.

---

## 🔑 Load Balancer SSL Certificates {#lb-ssl-certs}

Managed via **AWS Certificate Manager (ACM)** or uploaded manually.

### 🔸 HTTPS Listener Configuration

* Specify a **default certificate**.
* Optionally add **multiple certificates** for multi-domain support.
* Clients use **SNI (Server Name Indication)** to identify the hostname.
* Choose a **security policy** (e.g., TLS 1.2 only).

```
                  ┌────────────────────────────────────┐
                  │            Clients                 │
                  └────────────────────────────────────┘
                           │                 │
                           │                 │
           https://site1.com│                 │https://site2.com
                           ▼                 ▼
                    ┌────────────────────────────┐
                    │     ALB Listener : 443     │
                    └────────────────────────────┘
                           │                 │
                           │                 │
                ┌──────────┘                 └──────────┐
                ▼                                       ▼
     ┌────────────────────────┐           ┌────────────────────────┐
     │ Cert1 — site1.com      │           │ Cert2 — site2.com      │
     │ (HTTPS termination)    │           │ (HTTPS termination)    │
     └────────────────────────┘           └────────────────────────┘
```
---

## 🌍 Server Name Indication (SNI) {#sni}

SNI allows multiple SSL/TLS certificates on a **single load balancer**, enabling support for multiple domains.

| Works With   | Supported? |
| ------------ | ---------- |
| **ALB (v2)** | ✅ Yes      |
| **NLB (v2)** | ✅ Yes      |
| **CLB (v1)** | ❌ No       |

> Example:
> You can host both `api.myapp.com` and `shop.myapp.com` on one ALB using different certificates.

---

## 🧱 Elastic Load Balancers – SSL Certificate Comparison {#elb-ssl-comparison}

| Load Balancer | SSL Support                | Multiple Certs | Uses SNI |
| ------------- | -------------------------- | -------------- | -------- |
| **CLB (v1)**  | One cert per LB            | ❌              | ❌        |
| **ALB (v2)**  | Multiple listeners & certs | ✅              | ✅        |
| **NLB (v2)**  | Multiple listeners & certs | ✅              | ✅        |

---

## ⏳ Connection Draining (Deregistration Delay) {#connection-draining}

When an instance is being removed or marked unhealthy, **Connection Draining** ensures it can complete in-flight requests before stopping new ones.

| Term                     | Applies To | Default | Range      |
| ------------------------ | ---------- | ------- | ---------- |
| **Connection Draining**  | CLB        | 300 sec | 1–3600 sec |
| **Deregistration Delay** | ALB / NLB  | 300 sec | 1–3600 sec |

> 🔧 Set to **lower values** (e.g., 60s) for short requests, or **higher** for long-running APIs.

```
Load Balancer                     EC2 Instance
      |                                 |
      |------ Ongoing Requests -------->| 
      |                                 |
      |         [Instance becomes unhealthy] 
      |                                 |
      |<----- Stop sending new requests  |
      |------ Wait for active requests -->|
      |<----- Active requests complete ---|
      |------ Deregister instance -------->|
      |                                 |
```

---

## 🧠 What’s an Auto Scaling Group (ASG)?

* In real life, the load on your website or application can **change dynamically**.
* In the **cloud**, you can easily **add or remove servers** as needed.

### 🎯 Goal of an ASG

* **Scale Out** → Add EC2 instances when load increases
* **Scale In** → Remove EC2 instances when load decreases
* Maintain a **minimum** and **maximum** number of instances
* Automatically **register new instances** with a Load Balancer
* **Replace unhealthy instances** automatically
* ✅ ASG itself is **free**, you only pay for the EC2s.

---

### 📊 Auto Scaling Group – Basic Diagram

```
        +----------------------+
        |   Auto Scaling Group |
        +----------------------+
          |       |        |
      +------+ +------+ +------+
      | EC2  | | EC2  | | EC2  |
      +------+ +------+ +------+
```

---

### 💡 Auto Scaling Group with Load Balancer

```
              +--------------------+
              |   Load Balancer    |
              +---------+----------+
                        |
        +---------------+---------------+
        |      Auto Scaling Group        |
        +-------------------------------+
          |         |          |
      +-------+  +-------+  +-------+
      | EC2-1 |  | EC2-2 |  | EC2-3 |
      +-------+  +-------+  +-------+
```

---

## ⚙️ ASG Attributes

* **Launch Template** (replaces old Launch Configurations)

  * AMI + Instance Type
  * EC2 User Data
  * EBS Volumes
  * Security Groups
  * SSH Key Pair
  * IAM Roles
  * Network/Subnets Info
  * Load Balancer Info

* **Size Settings:**

  * Minimum size
  * Maximum size
  * Desired capacity

* **Scaling Policies:** Define how/when to scale.

---

## 📈 Auto Scaling with CloudWatch Alarms

* Scaling can be **triggered automatically** using **CloudWatch alarms**.
* Alarms monitor metrics such as:

  * CPU Utilization
  * Network Traffic
  * Custom Metrics

**Example:**

* If average CPU > 70% → Add instances (Scale Out)
* If average CPU < 30% → Remove instances (Scale In)

---

## 🔄 Scaling Policies

### 1. **Dynamic Scaling**

* **Target Tracking**

  * Automatically adjusts capacity to maintain a metric target.
  * Example: Keep average CPU at 40%.

* **Simple / Step Scaling**

  * Manual thresholds with defined steps.
  * Example: CPU > 70% → Add 2 instances
    CPU < 30% → Remove 1 instance

---

### 2. **Scheduled Scaling**

* Scale ahead of time based on known traffic patterns.

  * Example: Increase min capacity to 10 at 5 PM on Fridays.

---

### 3. **Predictive Scaling**

* Uses **machine learning** to forecast demand and scale ahead automatically.

---

## 📊 Good Metrics to Scale On

* `CPUUtilization` → Avg CPU across instances
* `RequestCountPerTarget` → Requests per EC2 instance
* `NetworkIn / NetworkOut` → For network-bound apps
* Any **custom metric** from CloudWatch

---

## 🕒 Scaling Cooldowns

* After a scaling action, ASG enters a **cooldown** (default **300 sec**).
* During cooldown, no new scaling happens — allows metrics to stabilize.
* ✅ Tip: Use **ready-to-use AMIs** to reduce setup time & cooldown.

---

## 🔁 Instance Refresh

* Used to **update** EC2 instances after changing launch templates.
* ASG automatically **replaces instances gradually**.
* You can set:

  * **Minimum healthy percentage** (how many must stay active)
  * **Warm-up time** (time until new instance is ready)

---
