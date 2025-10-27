# **Amazon EC2 – Instance Storage**

---

## **What’s an EBS Volume?**

* **EBS (Elastic Block Store)** = a **network drive** you can attach to your EC2 instance.
* Allows your instance to **persist data** even after termination.
* Can be attached to **only one instance** at a time (CCP level).
* Bound to a specific **Availability Zone (AZ)**.
* 💡 **Analogy:** Think of it as a **“network USB stick”** — plug it into an instance, store data, and remove when needed.

---

### 🔍 **EBS in Context (Diagram)**

```
          +--------------------------+
          |      EC2 Instance        |
          |--------------------------|
          |  OS + Applications       |
          |  Temporary Instance Data |
          +--------------------------+
                    │
                    │  (Network connection)
                    ▼
          +--------------------------+
          |      EBS Volume          |
          |--------------------------|
          |  Persistent Data Storage |
          |  Lives Independently     |
          |  AZ: us-east-1a          |
          +--------------------------+
```

---

## **EBS Volume Details**

* It’s a **network drive** (not physically attached).

  * Uses the **network** to communicate → may add slight **latency**.
  * Can be **detached** from one instance and **attached** to another quickly.

* **Locked to an Availability Zone (AZ)**:

  * Example: A volume in `us-east-1a` **cannot** be attached to `us-east-1b`.
  * To move across zones → **create a snapshot** and **restore** in another AZ.

* **Provisioned Capacity:**

  * Define **size (GB)** and **IOPS** when creating.
  * Billed for **all provisioned capacity**.
  * Capacity can be **increased** later if needed.

---

### 📊 **EBS Volume Lifecycle (Concept Flow)**

```
Create Volume → Attach to Instance → Use & Store Data
          │
          ├──> Detach & Reattach (same AZ)
          │
          └──> Snapshot → Copy → Create in another AZ/Region
```

---

## **EBS – Delete on Termination Attribute**

* Controls what happens to your **EBS volumes when EC2 terminates**.

| Volume Type            | Default Behavior | Delete on Termination |
| ---------------------- | ---------------- | --------------------- |
| **Root Volume**        | Deleted          | ✅ Enabled             |
| **Additional Volumes** | Preserved        | ❌ Disabled            |

* Can be modified via **AWS Console** or **AWS CLI**.
* **Use Case:** Keep root volume after termination for debugging or reuse.

---

### ⚙️ **Delete on Termination – Visual**

```
   +-------------------+
   | EC2 Instance      |
   +-------------------+
           │ Terminates
           ▼
   +-------------------+
   | Root Volume (EBS) | --> ❌ Deleted (default)
   +-------------------+
   | Data Volume (EBS) | --> ✅ Preserved (default)
   +-------------------+
```

---

## **EBS Snapshots**

* **Point-in-time backup** of an EBS volume.
* Can be taken **without detaching**, though detaching ensures data consistency.
* Snapshots can be **copied across AZs or Regions**.

---

### 📸 **Snapshot Workflow**

```
EBS Volume ──▶ Snapshot ──▶ Copy to Another AZ/Region ──▶ Restore to New Volume
```

---

## **EBS Snapshot Features**

### 🧊 **1. EBS Snapshot Archive**

* Move snapshots to **Archive Tier** (≈ 75% cheaper).
* Restore takes **24–72 hours**.
* Ideal for **long-term backups**.

---

### 🗑️ **2. Recycle Bin for Snapshots**

* Prevent accidental loss — set **retention policies** (1 day to 1 year).
* Recover deleted snapshots within retention window.

---

### ⚡ **3. Fast Snapshot Restore (FSR)**

* Pre-warms snapshots for **no latency** on first use.
* Costs extra — useful for **production-critical restores**.

---

### 🧩 **Snapshot Feature Summary**

| Feature               | Purpose              | Cost   | Restore Time |
| --------------------- | -------------------- | ------ | ------------ |
| **Standard Snapshot** | Normal backup        | 💲💲   | Immediate    |
| **Archive Snapshot**  | Long-term storage    | 💲     | 24–72 hrs    |
| **FSR**               | Zero-latency restore | 💲💲💲 | Instant      |

---

### 🧭 **EBS Storage Flow Summary (Visual Overview)**

```
        +-----------------------------+
        |       Create Volume         |
        +-------------+---------------+
                      │
                      ▼
        +-----------------------------+
        |      Attach to EC2          |
        +-------------+---------------+
                      │
                      ▼
        +-----------------------------+
        |     Use & Store Data        |
        +-------------+---------------+
                      │
                      ▼
        +-----------------------------+
        |       Snapshot Backup       |
        +-------------+---------------+
                      │
        ┌─────────────┴───────────────┐
        ▼                             ▼
+----------------+          +---------------------+
| Archive Tier   |          | Copy / Restore      |
| (75% cheaper)  |          | Across AZ or Region |
+----------------+          +---------------------+
```

---

# **Amazon EC2 – Instance Storage**

---

## **1️⃣ AMI Overview**

* **AMI = Amazon Machine Image**
* Customization of an EC2 instance (includes OS + software + configs)
* Enables **faster boot** and **consistent configuration**
* AMIs are **region-specific** (but can be copied across regions)

### **AMI Types**

| Type                | Description                                |
| ------------------- | ------------------------------------------ |
| **Public AMI**      | Provided by AWS                            |
| **Custom AMI**      | Created & maintained by you                |
| **Marketplace AMI** | Created and possibly sold by third parties |

---

### **AMI Creation Process (from an EC2 instance)**

```
[1] Launch EC2 Instance
        ↓
[2] Customize (install software, config, etc.)
        ↓
[3] Stop Instance (for data integrity)
        ↓
[4] Create AMI → Generates EBS Snapshots
        ↓
[5] Launch New Instances from this AMI
```

✅ **Result:** Every new instance starts pre-configured — faster deployments.

---

## **2️⃣ EC2 Instance Store**

* High-performance **ephemeral storage** directly attached to host hardware.
* **Much faster** than EBS but **non-persistent** (data lost on stop or failure).

| Property       | EC2 Instance Store                       |
| -------------- | ---------------------------------------- |
| Type           | **Local physical disk**                  |
| Performance    | Very high (hardware-based)               |
| Persistence    | Lost when stopped / terminated           |
| Best for       | Buffers, cache, temp files, scratch data |
| Risk           | Data loss on hardware failure            |
| Responsibility | Backup & replication by user             |

---

### ⚙️ **Visual: EC2 Storage Options**

```
EC2 Instance
│
├── Instance Store (local disk, fast, ephemeral)
│
└── EBS Volume (network drive, persistent, slower)
```

---

## **3️⃣ EBS Volume Types**

EBS = **Elastic Block Store**
Used for **persistent block storage** attached to EC2 instances.

| Type                              | Medium | Use Case                                | Boot Volume | Max Size  |
| --------------------------------- | ------ | --------------------------------------- | ----------- | --------- |
| **gp2 / gp3 (SSD)**               | SSD    | General-purpose workloads               | ✅ Yes       | 16 TiB    |
| **io1 / io2 Block Express (SSD)** | SSD    | Mission-critical, low-latency workloads | ✅ Yes       | 16–64 TiB |
| **st1 (HDD)**                     | HDD    | Throughput-intensive, frequent access   | ❌ No        | 16 TiB    |
| **sc1 (HDD)**                     | HDD    | Infrequent access, archival             | ❌ No        | 16 TiB    |

---

### **📦 EBS Volume Types – General Purpose SSD (gp2/gp3)**

| Property       | gp2            | gp3            |
| -------------- | -------------- | -------------- |
| Size Range     | 1 GiB – 16 TiB | 1 GiB – 16 TiB |
| Baseline IOPS  | 3 IOPS per GB  | 3,000 IOPS     |
| Max IOPS       | 16,000         | 16,000         |
| Max Throughput | 250 MiB/s      | 1,000 MiB/s    |
| IOPS Scaling   | Tied to size   | Independent    |

**Use Cases:**
Boot volumes, virtual desktops, dev/test environments, low-latency workloads.

---

### **⚡ Provisioned IOPS (PIOPS) SSD – io1/io2**

| Property             | io1                             | io2 Block Express |
| -------------------- | ------------------------------- | ----------------- |
| Size                 | 4 GiB – 16 TiB                  | 4 GiB – 64 TiB    |
| Max IOPS             | 64,000 (Nitro) / 32,000 (other) | 256,000           |
| Latency              | < 1 ms                          | < 1 ms            |
| IOPS:GiB Ratio       | 50:1                            | 1,000:1           |
| Multi-Attach Support | ✅                               | ✅                 |

**Use Cases:**
Databases, critical apps, consistent high-performance workloads.

---

### **💽 HDD Volumes – st1 / sc1**

| Type                               | Description                               | Max Throughput | IOPS | Use Case        |
| ---------------------------------- | ----------------------------------------- | -------------- | ---- | --------------- |
| **st1 (Throughput Optimized HDD)** | Big data, log processing, data warehouses | 500 MiB/s      | 500  | Frequent access |
| **sc1 (Cold HDD)**                 | Archival, low-cost infrequent data        | 250 MiB/s      | 250  | Rare access     |

> ❌ HDD volumes **cannot be used as boot volumes**.

---

## **4️⃣ EBS Multi-Attach (io1 / io2 only)**

* Attach **one EBS volume to multiple EC2 instances** in the **same AZ**.
* All instances have **read/write** access.
* Up to **16 instances** per volume.

### **Use Cases:**

* High-availability **clustered Linux apps** (e.g., Teradata)
* Apps must **handle concurrent writes**

> Must use a **cluster-aware file system** (not XFS, EXT4).

---

## **5️⃣ Amazon EFS – Elastic File System**

* **Fully managed NFS (Network File System)** for **shared storage**.
* Accessible by **multiple EC2 instances** across **multiple AZs**.
* **Scales automatically** — pay per use.
* **For Linux-based AMIs** (POSIX compatible).

**Use Cases:**
Web content sharing, CMS, DevOps tools, data sharing (e.g., WordPress).

---

### **EFS – Performance & Storage Classes**

#### ⚙️ **Performance Mode (Set at Creation)**

| Mode                          | Description                                       |
| ----------------------------- | ------------------------------------------------- |
| **General Purpose (default)** | Low latency (web servers, CMS)                    |
| **Max I/O**                   | High throughput, higher latency (Big Data, media) |

#### 🚀 **Throughput Mode**

| Mode            | Description                                               |
| --------------- | --------------------------------------------------------- |
| **Bursting**    | Scales with storage size (1TB = 50MiB/s + burst 100MiB/s) |
| **Provisioned** | Fixed throughput (set manually)                           |
| **Elastic**     | Auto-scales up/down (up to 3 GiB/s reads, 1 GiB/s writes) |

#### 🧊 **Storage Classes**

| Class                      | Description                   |
| -------------------------- | ----------------------------- |
| **Standard**               | Frequently accessed files     |
| **Infrequent Access (IA)** | Lower cost, retrieval fee     |
| **Archive**                | Rarely accessed (50% cheaper) |

> Lifecycle rules move files between tiers after N days.

---

### **EFS Availability Options**

| Class        | AZ Scope  | Cost | Durability     |
| ------------ | --------- | ---- | -------------- |
| **Standard** | Multi-AZ  | 💲💲 | High           |
| **One Zone** | Single AZ | 💲   | Backup enabled |

> Up to **90% cost savings** with One Zone + IA.

---

## **6️⃣ EBS vs EFS – Key Differences**

| Feature     | **EBS (Elastic Block Store)**    | **EFS (Elastic File System)** |
| ----------- | -------------------------------- | ----------------------------- |
| Mount Type  | Single EC2 (except Multi-Attach) | 100s of EC2s                  |
| Scope       | Single AZ                        | Multi-AZ                      |
| OS Support  | Linux & Windows                  | Linux only                    |
| Performance | Block-level (low latency)        | Network file (higher latency) |
| Use Case    | Databases, boot volumes          | Shared file storage           |
| Pricing     | Lower                            | Higher (per GB/month)         |
| Scalability | Manual (resize, snapshot)        | Automatic                     |
| Backup      | Snapshots                        | Lifecycle tiers               |

---

### ⚙️ **Migration Tip**

To move EBS across AZs:

1. Take **snapshot**
2. **Copy** snapshot to another AZ or Region
3. **Restore** as new volume

> Avoid snapshots during high I/O — it consumes bandwidth.

---

### **Quick Visual Summary**

```
EC2 Storage Options
│
├── Instance Store → Fast, Ephemeral, Local
├── EBS → Persistent Block Storage (Single AZ)
│     ├── gp2/gp3 → General Purpose SSD
│     ├── io1/io2 → High-Perf IOPS SSD
│     └── st1/sc1 → HDD Options
└── EFS → Network File System, Multi-AZ, Shared Access
```

---

