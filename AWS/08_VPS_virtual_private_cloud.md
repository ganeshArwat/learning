# 🏗️ **Amazon VPC (Virtual Private Cloud)**

---

## 🚀 **VPC Introduction**

A **VPC (Virtual Private Cloud)** is your **own isolated virtual network** within AWS. It allows you to:

* Launch AWS resources (like EC2, RDS, Lambda) in a **controlled environment**.
* Define **IP address ranges, subnets, route tables, firewalls**, and more.
* Securely **connect** your cloud resources to the **internet**, **other VPCs**, or **on-premises networks**.

🟩 **Key Concept:**
VPC is a **regional resource** — it spans **all Availability Zones (AZs)** within a region.

---

## 🌐 **VPC & Subnets Primer**

| Concept            | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| **VPC**            | A private network to deploy AWS resources.                                                        |
| **Subnet**         | A logical partition of your VPC (tied to one Availability Zone).                                  |
| **Public Subnet**  | Connected to the **Internet Gateway (IGW)** — accessible from the internet.                       |
| **Private Subnet** | No direct internet access — typically used for databases, backend services.                       |
| **Route Table**    | Defines how traffic is directed (e.g., to the Internet Gateway, NAT Gateway, or between subnets). |

🧭 **Tip:**
Each subnet must be explicitly associated with a route table. Otherwise, it uses the **main route table** by default.

---

## 🗺️ **VPC Diagram (Conceptual)**

```mermaid
graph TD
  A[Internet] -->|Inbound/Outbound| B[Internet Gateway]
  B -->|Route| C[Public Subnet]
  C -->|SSH/HTTP| D[EC2 - Web Server]
  C -->|Private Communication| E[Private Subnet]
  E -->|DB Connection| F[RDS Database]
  E -->|Outbound Access| G[NAT Gateway]
  G -->|Route to| B
```

---

## 🌉 **Internet Gateway (IGW) & NAT Gateways**

### 🛰️ Internet Gateway

* Enables instances in **public subnets** to access the internet.
* One Internet Gateway per VPC.
* Must be attached to the VPC and referenced in a **route table**.

### 🔒 NAT Gateway / NAT Instance

* Allows **private subnet instances** to **initiate** outbound traffic to the internet.
* Prevents **inbound** connections from the internet.
* **NAT Gateway** is AWS-managed (highly available, scalable, pay-per-use).
* **NAT Instance** is self-managed, customizable, but less reliable.

📘 **Example:**

| Subnet Type    | Internet Access  | Uses                       |
| -------------- | ---------------- | -------------------------- |
| Public Subnet  | Direct via IGW   | Web servers, bastion hosts |
| Private Subnet | Outbound via NAT | Databases, backend apps    |

---

## 🔐 **Network ACLs (NACL) & Security Groups**

| Feature     | **Network ACL (NACL)**                    | **Security Group (SG)**   |
| ----------- | ----------------------------------------- | ------------------------- |
| Level       | Subnet                                    | Instance / ENI            |
| Rules       | Allow **and** Deny                        | Allow **only**            |
| Stateful?   | ❌ Stateless                               | ✅ Stateful                |
| Rule Order  | Processed in order                        | Evaluates all rules       |
| Association | Auto-applies to all instances in a subnet | Must be manually attached |

### 🧩 Example:

* **NACL:** Blocks a specific IP range across the subnet.
* **Security Group:** Allows SSH (port 22) only from your office IP.

🧠 **Tip:**
Combine both — NACLs as coarse subnet firewalls, SGs for fine-grained instance-level security.

---

## 📊 **VPC Flow Logs**

* Capture detailed information about **IP traffic** within your VPC.
* Can be created at **VPC**, **Subnet**, or **ENI (Elastic Network Interface)** level.
* Used for:

  * Network troubleshooting
  * Security auditing
  * Traffic pattern analysis

📦 **Destinations:**

* Amazon **CloudWatch Logs**
* **S3** bucket
* **Kinesis Data Firehose**

✅ **Covers AWS-managed resources too** — like Load Balancers, RDS, ElastiCache, etc.

---

## 🤝 **VPC Peering**

* Connect **two VPCs** privately over AWS’s internal network.
* Enables instances to communicate as if on the same network.
* **No internet needed.**
* **Non-transitive:** Each pair of VPCs must have its own peering connection.
* **No overlapping CIDR blocks** allowed.

📘 **Use Case:**
Connecting a **dev VPC** and **prod VPC** for resource sharing (e.g., logging server).

---

## 🛜 **VPC Endpoints**

* Provide **private access** to AWS services **without using the public internet.**
* Improve **security** and **latency**.

| Type                   | Used For                | Description                                    |
| ---------------------- | ----------------------- | ---------------------------------------------- |
| **Gateway Endpoint**   | S3, DynamoDB            | Route traffic through a private gateway target |
| **Interface Endpoint** | Most other AWS services | Uses an ENI in your subnet with a private IP   |

🧠 **Example:**
Use an **S3 Gateway Endpoint** so EC2 in a private subnet can access S3 **without IGW/NAT**.

---

## 🌍 **Site-to-Site VPN & Direct Connect**

| Feature      | Site-to-Site VPN           | AWS Direct Connect                            |
| ------------ | -------------------------- | --------------------------------------------- |
| Connectivity | Over public internet       | Dedicated private fiber link                  |
| Encryption   | Encrypted (IPSec)          | Private link (can add VPN for extra security) |
| Setup Time   | Minutes                    | Weeks                                         |
| Speed        | Moderate (up to 1.25 Gbps) | High (1–100 Gbps)                             |
| Use Case     | Quick hybrid setup         | Long-term high-throughput private link        |

---

## 🧾 **VPC Summary (Cheat Sheet)**

| Component                  | Purpose                                |
| -------------------------- | -------------------------------------- |
| **VPC**                    | Virtual network environment            |
| **Subnet**                 | AZ-tied network partition              |
| **Internet Gateway**       | Provides internet access               |
| **NAT Gateway / Instance** | Outbound internet for private subnets  |
| **NACL**                   | Stateless firewall at subnet level     |
| **Security Group**         | Stateful firewall at instance level    |
| **VPC Peering**            | Private link between two VPCs          |
| **VPC Endpoint**           | Private AWS service access             |
| **VPC Flow Logs**          | Traffic monitoring and troubleshooting |
| **VPN / Direct Connect**   | Connect on-premises network to AWS     |

---

## 🏗️ **Typical 3-Tier Architecture (VPC)**

```mermaid
graph TD
    A["Internet"] --> B["Internet Gateway"]
    B --> C["Public Subnet - Web Tier"]
    C -->|"Load Balancer"| D["EC2 Web Servers"]
    D --> E["Private Subnet - App Tier"]
    E --> F["EC2 App Servers"]
    F --> G["Private Subnet - DB Tier"]
    G --> H["RDS / Aurora Database"]
    E --> I["ElastiCache (Redis / Memcached)"]

    subgraph Monitoring
        J["CloudWatch Logs"]
    end

    G --> J
    E --> J

```

---

## 🧩 **LAMP Stack on AWS EC2**

| Component                         | Description                               |
| --------------------------------- | ----------------------------------------- |
| **Linux**                         | OS running on EC2 instances               |
| **Apache**                        | Web server serving HTTP requests          |
| **MySQL**                         | Database layer (preferably hosted on RDS) |
| **PHP**                           | Application logic, hosted on EC2          |
| **ElastiCache (Redis/Memcached)** | Optional caching layer                    |
| **EBS Volume**                    | Persistent storage for EC2                |

🧠 **Architecture Tip:**
Place Apache/PHP in a **public subnet**, MySQL in a **private subnet**, and connect through internal routing.

---

## 📰 **WordPress on AWS – Basic Architecture**

```mermaid
graph TD
    A["User Browser"] --> B["CloudFront CDN"]
    B --> C["ALB (Application Load Balancer)"]
    C --> D["EC2 WordPress Instances (Public Subnet)"]
    D --> E["RDS MySQL Database (Private Subnet)"]
    D --> F["S3 Media Storage"]
    F --> G["CloudFront Cache"]
```

---

## 🧱 **WordPress on AWS – Scalable Architecture**

```mermaid
graph TD
    A["User Browser"] --> B["Route 53 DNS"]
    B --> C["CloudFront CDN"]
    C --> D["ALB (Load Balancer)"]
    D --> E["Auto Scaling Group (EC2 WordPress)"]
    E --> F["EFS (Shared File Storage)"]
    E --> G["RDS (Multi-AZ MySQL)"]
    E --> H["ElastiCache (Redis)"]
    E --> I["S3 (Media Backup)"]
    E --> J["Private Subnet (App & DB)"]

    subgraph Monitoring
        K["CloudWatch, VPC Flow Logs, GuardDuty"]
    end

    J --> K

```

---
---

### 🏗️ **Example: 3-Tier VPC Architecture**

```mermaid
graph TD

  subgraph "VPC (10.0.0.0/16)"
  
    A["Internet"] -->|"HTTP/HTTPS"| IGW["Internet Gateway"]

    %% Public Subnet
    IGW --> RT1["Route Table: Public Routes"]
    RT1 -->|"Route to IGW"| PUB["Public Subnet (10.0.1.0/24)"]
    PUB -->|"Web Traffic"| EC2_1["EC2 Web Server"]
    PUB -->|"Outbound Access"| NAT["NAT Gateway"]

    %% Private App Subnet
    NAT -->|"Outbound Internet"| APP["Private Subnet - App Tier (10.0.2.0/24)"]
    APP -->|"Internal Traffic"| EC2_2["EC2 App Server"]

    %% Private DB Subnet
    APP -->|"DB Connection (Port 3306)"| DB["Private Subnet - DB Tier (10.0.3.0/24)"]
    DB --> RDS["RDS MySQL Database"]

  end

  %% External
  EC2_1 -->|"Response"| A

  %% Styling
  classDef public fill:#d4f8d4,stroke:#4CAF50,stroke-width:2px;
  classDef private fill:#fff4cc,stroke:#FFB300,stroke-width:2px;
  classDef db fill:#d4e4ff,stroke:#1565C0,stroke-width:2px;

  class PUB public;
  class APP private;
  class DB db;


```

---

### 🧠 **Explanation**

* **Public Subnet:** Hosts web servers that serve internet traffic.
* **Private Subnet (App):** Hosts backend app logic. Communicates only internally.
* **Private Subnet (DB):** Contains the RDS database, isolated from the internet.
* **NAT Gateway:** Allows outbound internet from private subnets for updates.
* **Internet Gateway:** Enables inbound/outbound traffic to public resources.

---

