# **AWS Cloud Overview**

---

## **1️⃣ AWS Cloud History**

| Year | Event                                                               |
| ---- | ------------------------------------------------------------------- |
| 2002 | Internally launched                                                 |
| 2003 | Amazon infrastructure recognized as a core strength; idea to market |
| 2004 | Launched publicly with **SQS**                                      |
| 2006 | Re-launched publicly with **SQS, S3 & EC2**                         |
| 2007 | Launched in **Europe**                                              |

---

## **2️⃣ AWS Cloud Use Cases**

* Build sophisticated, scalable applications
* Applicable across diverse industries
* **Examples:**

  * Enterprise IT, Backup & Storage, Big Data analytics
  * Website hosting, Mobile & Social Apps
  * Gaming

---

## **3️⃣ AWS Global Infrastructure**

* **AWS Regions** – Cluster of data centers in a geographic area
* **AWS Availability Zones (AZs)** – Isolated data centers within a region
* **AWS Data Centers** – Physical facilities for compute, storage, and networking
* **AWS Edge Locations / Points of Presence (PoPs)** – For low-latency content delivery

---

### **3.1 AWS Regions**

* AWS has regions worldwide (e.g., `us-east-1`, `eu-west-3`)
* A region is a **cluster of data centers**
* Most AWS services are **region-scoped**

**How to choose a region:**

1. Compliance with data governance and legal requirements
2. Proximity to customers (reduce latency)
3. Available services (new services may not be in all regions)
4. Pricing (varies by region, check AWS pricing page)

---

### **3.2 AWS Availability Zones (AZs)**

* Each region has **usually 3–6 AZs** (minimum 3)
* Example AZs: `ap-southeast-2a`, `ap-southeast-2b`, `ap-southeast-2c`
* Each AZ is **one or more discrete data centers** with:

  * Redundant power
  * Networking
  * Connectivity
* AZs are **isolated from each other** to prevent disasters
* Connected via **high bandwidth, ultra-low latency networking**

---

## **4️⃣ Tour of the AWS Console**

* **Global Services (accessible from any region):**

  * Identity and Access Management (**IAM**)
  * Route 53 (DNS service)
  * CloudFront (Content Delivery Network)
  * WAF (Web Application Firewall)

* **Region-Scoped Services:**

  * Amazon EC2 (**IaaS**)
  * Elastic Beanstalk (**PaaS**)
  * Lambda (**FaaS / Serverless**)
  * Rekognition (**SaaS**)

* **Region Table:** [AWS Regional Product Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services)

---

