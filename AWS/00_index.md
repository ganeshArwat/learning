## Chapter 1 – Getting Started With AWS

* [AWS Cloud History](01_getting_started_with_aws.md#-aws-cloud-history)
* [AWS Cloud Use Cases](01_getting_started_with_aws.md#-aws-cloud-use-cases)
* [AWS Global Infrastructure](01_getting_started_with_aws.md#-aws-global-infrastructure)
  * [AWS Regions](01_getting_started_with_aws.md#-aws-regions)
  * [AWS Availability Zones (AZs)](01_getting_started_with_aws.md#-aws-availability-zones-azs)
* [Tour of the AWS Console](01_getting_started_with_aws.md#-tour-of-the-aws-console)

---

## **Chapter 2: IAM (Identity and Access Management)**  

* [IAM: Users & Groups](02_IAM_Identity_Access_Management.md#1️⃣-iam-users--groups)  
* [IAM: Permissions](02_IAM_Identity_Access_Management.md#2️⃣-iam-permissions)  
* [IAM Policies Structure](02_IAM_Identity_Access_Management.md#3️⃣-iam-policies-structure)  
* [IAM Password Policy](02_IAM_Identity_Access_Management.md#4️⃣-iam-password-policy)  
* [Multi-Factor Authentication (MFA)](02_IAM_Identity_Access_Management.md#5️⃣-multi-factor-authentication-mfa)  
* [How Users Access AWS](02_IAM_Identity_Access_Management.md#6️⃣-how-users-access-aws)  
* [AWS CLI & SDK](02_IAM_Identity_Access_Management.md#7️⃣-aws-cli--sdk)  
* [IAM Roles for Services](02_IAM_Identity_Access_Management.md#8️⃣-iam-roles-for-services)  
* [IAM Security Tools](02_IAM_Identity_Access_Management.md#9️⃣-iam-security-tools)  
* [IAM Best Practices](02_IAM_Identity_Access_Management.md#🔟-iam-best-practices)  
* [Shared Responsibility Model (IAM)](02_IAM_Identity_Access_Management.md#1️⃣1️⃣-shared-responsibility-model-iam)  
* [IAM Summary](02_IAM_Identity_Access_Management.md#1️⃣2️⃣-iam-summary)  
* [Extra Tips / Real-world Examples](02_IAM_Identity_Access_Management.md#extra-tips--real-world-examples)

---

## Chapter 3 – Elastic Compute Cloud (EC2)

* [What EC2 Really Is](03_Ec2.md#-what-ec2-really-is)
* [Key EC2 Components](03_Ec2.md#️-key-ec2-components)
* [EC2 User Data (Bootstrapping)](03_Ec2.md#-ec2-user-data-bootstrapping)
* [EC2 Instance Types — Choosing the Right One](03_Ec2.md#-ec2-instance-types--choosing-the-right-one)
* [Example Comparison Table](03_Ec2.md#-example-comparison-table)
* [EC2 = Foundation of Cloud Architecture](03_Ec2.md#-ec2--foundation-of-cloud-architecture)
* [What is a Security Group (SG)?](03_Ec2.md#-what-is-a-security-group-sg)

  * [Simple Mental Model](03_Ec2.md#-simple-mental-model)
  * [Core Rules](03_Ec2.md#-core-rules)
  * [Security Group Rule Example](03_Ec2.md#-security-group-rule-example)
  * [Key Concepts to Remember](03_Ec2.md#-key-concepts-to-remember)
  * [Troubleshooting with SGs](03_Ec2.md#️-troubleshooting-with-sgs)
  * [Classic Port Numbers to Remember](03_Ec2.md#️-classic-port-numbers-to-remember)
  * [SSH (Secure Shell) Access Methods](03_Ec2.md#-ssh-secure-shell-access-methods)
  * [Quick Visual Summary](03_Ec2.md#-quick-visual-summary)

* [EC2 Purchasing Options — The Big Picture](03_Ec2.md#-ec2-purchasing-options--the-big-picture)

  * [EC2 On-Demand Instances](03_Ec2.md#️-1️⃣-ec2-on-demand-instances)
  * [Reserved Instances (RIs)](03_Ec2.md#-2️⃣-reserved-instances-ris)
  * [Convertible Reserved Instances](03_Ec2.md#-convertible-reserved-instances)
  * [Savings Plans](03_Ec2.md#-3️⃣-savings-plans)
  * [Spot Instances](03_Ec2.md#-4️⃣-spot-instances)
  * [Dedicated Hosts](03_Ec2.md#-5️⃣-dedicated-hosts)
  * [Dedicated Instances](03_Ec2.md#-6️⃣-dedicated-instances)
  * [Capacity Reservations](03_Ec2.md#-7️⃣-capacity-reservations)
  * [Easy Hotel Analogy](03_Ec2.md#-easy-hotel-analogy-perfect-for-remembering)
  * [Example Price Comparison](03_Ec2.md#-example-price-comparison-m4large--us-east-1)
  * [In Short — Choosing Strategy](03_Ec2.md#-in-short--choosing-strategy)

---

## Chapter 4 – Amazon EC2: Instance Storage

* [What’s an EBS Volume?](04_Ec2_Instance_Storage.md#-whats-an-ebs-volume)
* [EBS Volume Details](04_Ec2_Instance_Storage.md#-ebs-volume-details)
* [EBS – Delete on Termination Attribute](04_Ec2_Instance_Storage.md#-ebs--delete-on-termination-attribute)
* [EBS Snapshots](04_Ec2_Instance_Storage.md#-ebs-snapshots)
* [EBS Snapshot Features](04_Ec2_Instance_Storage.md#-ebs-snapshot-features)
* [AMI Overview](04_Ec2_Instance_Storage.md#-1%EF%B8%8F%E2%83%A3-ami-overview)
* [EC2 Instance Store](04_Ec2_Instance_Storage.md#-2%EF%B8%8F%E2%83%A3-ec2-instance-store)
* [EBS Volume Types](04_Ec2_Instance_Storage.md#-3%EF%B8%8F%E2%83%A3-ebs-volume-types)
* [EBS Multi-Attach (io1/io2 only)](04_Ec2_Instance_Storage.md#-4%EF%B8%8F%E2%83%A3-ebs-multi-attach-io1--io2-only)
* [Amazon EFS – Elastic File System](04_Ec2_Instance_Storage.md#-5%EF%B8%8F%E2%83%A3-amazon-efs--elastic-file-system)
* [EBS vs EFS – Key Differences](04_Ec2_Instance_Storage.md#-6%EF%B8%8F%E2%83%A3-ebs-vs-efs--key-differences)

---

# 🧭 Chapter 5 – Availability and Scalability (Index)

1. [Concept Overview](05_High_Availability_Scalability.md#-concept-overview)
2. [Scalability & High Availability](05_High_Availability_Scalability.md#scalability--high-availability)

   * [Vertical Scalability](05_High_Availability_Scalability.md#-vertical-scalability)
   * [Horizontal Scalability](05_High_Availability_Scalability.md#horizontal-scalability)
   * [High Availability (HA)](05_High_Availability_Scalability.md#high-availability-ha)
   * [HA & Scalability for EC2](05_High_Availability_Scalability.md#high-availability--scalability-for-ec2)
3. [Load Balancing](05_High_Availability_Scalability.md#what-is-load-balancing)

   * [Why Use a Load Balancer](05_High_Availability_Scalability.md#why-use-a-load-balancer)
   * [Elastic Load Balancer (ELB)](05_High_Availability_Scalability.md#why-use-an-elastic-load-balancer-elb)
   * [Health Checks](05_High_Availability_Scalability.md#health-checks)
   * [Types of Load Balancer](05_High_Availability_Scalability.md#types-of-load-balancer-on-aws)
   * [Load Balancer Security Groups](05_High_Availability_Scalability.md#load-balancer-security-groups)
   * [Classic Load Balancer (CLB)](05_High_Availability_Scalability.md#classic-load-balancer-clb)
   * [Application Load Balancer (ALB)](05_High_Availability_Scalability.md#application-load-balancer-alb)

     * [Target Groups](05_High_Availability_Scalability.md#target-groups)
     * [Traffic Flow](05_High_Availability_Scalability.md#http-based-traffic-flow)
   * [Network Load Balancer (NLB)](05_High_Availability_Scalability.md#network-load-balancer-nlb)
   * [Gateway Load Balancer (GWLB)](05_High_Availability_Scalability.md#gateway-load-balancer-gwlb)
   * [Quick Summary](05_High_Availability_Scalability.md#quick-summary-)
4. [Sticky Sessions (Session Affinity)](05_High_Availability_Scalability.md#-sticky-sessions-session-affinity)

   * [Cookie Names](05_High_Availability_Scalability.md#-sticky-sessions--cookie-names)
5. [Cross-Zone Load Balancing](05_High_Availability_Scalability.md#-cross-zone-load-balancing)
6. [SSL/TLS Basics](05_High_Availability_Scalability.md#-ssltls-basics)

   * [Load Balancer SSL Certificates](05_High_Availability_Scalability.md#-load-balancer-ssl-certificates)
   * [Server Name Indication (SNI)](05_High_Availability_Scalability.md#-server-name-indication-sni)
   * [ELB SSL Certificate Comparison](05_High_Availability_Scalability.md#-elastic-load-balancers--ssl-certificate-comparison)
7. [Connection Draining / Deregistration Delay](05_High_Availability_Scalability.md#-connection-draining-deregistration-delay)
8. [Auto Scaling Group (ASG)](05_High_Availability_Scalability.md#-whats-an-auto-scaling-group-asg)

   * [ASG Diagram](05_High_Availability_Scalability.md#-auto-scaling-group--basic-diagram)
   * [ASG with Load Balancer](05_High_Availability_Scalability.md#-auto-scaling-group-with-load-balancer)
   * [ASG Attributes](05_High_Availability_Scalability.md#-asg-attributes)
   * [Auto Scaling with CloudWatch](05_High_Availability_Scalability.md#-auto-scaling-with-cloudwatch-alarms)
   * [Scaling Policies](05_High_Availability_Scalability.md#-scaling-policies)

     * [Dynamic Scaling](05_High_Availability_Scalability.md#1-dynamic-scaling)
     * [Scheduled Scaling](05_High_Availability_Scalability.md#2-scheduled-scaling)
     * [Predictive Scaling](05_High_Availability_Scalability.md#3-predictive-scaling)
   * [Good Metrics to Scale On](05_High_Availability_Scalability.md#-good-metrics-to-scale-on)
   * [Scaling Cooldowns](05_High_Availability_Scalability.md#-scaling-cooldowns)
   * [Instance Refresh](05_High_Availability_Scalability.md#-instance-refresh)

---

## 🗄️ Chapter 6 – Amazon RDS, Aurora & ElastiCache

* [Amazon RDS Overview](06_RDS_Aurora_and_ElastiCache.md#-amazon-rds-overview)
* [RDS vs EC2 Database Hosting](06_RDS_Aurora_and_ElastiCache.md#-rds-vs-ec2-database-hosting)

  * [RDS Features](06_RDS_Aurora_and_ElastiCache.md#-rds-features)
  * [EC2 with Self-Managed Database](06_RDS_Aurora_and_ElastiCache.md#-ec2-with-self-managed-database)
  * [RDS vs EC2 – Architectural Comparison](06_RDS_Aurora_and_ElastiCache.md#-rds-vs-ec2--architectural-comparison)
* [RDS High Availability and Read Scaling](06_RDS_Aurora_and_ElastiCache.md#-rds-high-availability-and-read-scaling)

  * [RDS Multi-AZ Deployment](06_RDS_Aurora_and_ElastiCache.md#-rds-multi-az-deployment)
  * [RDS Read Replicas](06_RDS_Aurora_and_ElastiCache.md#-rds-read-replicas)
* [Amazon Aurora](06_RDS_Aurora_and_ElastiCache.md#-amazon-aurora)

  * [Aurora High Availability and Read Scaling](06_RDS_Aurora_and_ElastiCache.md#-aurora-high-availability-and-read-scaling)
  * [Aurora DB Cluster Architecture](06_RDS_Aurora_and_ElastiCache.md#-aurora-db-cluster-architecture)
  * [Aurora Features](06_RDS_Aurora_and_ElastiCache.md#-features-of-aurora)
* [RDS & Aurora Security](06_RDS_Aurora_and_ElastiCache.md#-rds--aurora-security)
* [Amazon RDS Proxy](06_RDS_Aurora_and_ElastiCache.md#-amazon-rds-proxy)
* [Amazon ElastiCache Overview](06_RDS_Aurora_and_ElastiCache.md#-amazon-elasticache-overview)

  * [ElastiCache – DB Cache Architecture](06_RDS_Aurora_and_ElastiCache.md#-elasticache-solution-architecture---db-cache)
  * [ElastiCache – User Session Store](06_RDS_Aurora_and_ElastiCache.md#-elasticache-solution-architecture--user-session-store)
  * [Redis vs Memcached](06_RDS_Aurora_and_ElastiCache.md#-elasticache--redis-vs-memcached)
* [Caching Implementation Patterns](06_RDS_Aurora_and_ElastiCache.md#-caching-implementation-considerations)

  * [Lazy Loading / Cache-Aside](06_RDS_Aurora_and_ElastiCache.md#-lazy-loading--cache-aside--lazy-population)
  * [Write-Through Pattern](06_RDS_Aurora_and_ElastiCache.md#️-7-write-through-pattern)
  * [Cache Evictions & TTL](06_RDS_Aurora_and_ElastiCache.md#-cache-evictions-and-time-to-live-ttl)
* [Amazon MemoryDB for Redis](06_RDS_Aurora_and_ElastiCache.md#-amazon-memorydb-for-redis)
* [Final Words of Wisdom](06_RDS_Aurora_and_ElastiCache.md#-final-words-of-wisdom)

---

## 🧭 Chapter 7 – Amazon Route 53

* [What is DNS?](07_Amazon_Route_53.md#-what-is-dns)

  * [Hierarchical Naming Structure](07_Amazon_Route_53.md#-hierarchical-naming-structure)
* [DNS Terminologies](07_Amazon_Route_53.md#-dns-terminologies)
* [How DNS Works](07_Amazon_Route_53.md#-how-dns-works)
* [Amazon Route 53 Overview](07_Amazon_Route_53.md#-amazon-route-53-overview)
* [DNS Record Structure](07_Amazon_Route_53.md#-dns-record-structure)
* [Must-Know DNS Records](07_Amazon_Route_53.md#-must-know-dns-records)
* [Advanced DNS Records](07_Amazon_Route_53.md#-advanced-dns-records)
* [Hosted Zones in Route 53](07_Amazon_Route_53.md#-hosted-zones-in-route-53)

  * [Public vs Private Hosted Zone Diagram](07_Amazon_Route_53.md#diagram-public-vs-private-hosted-zone)
* [TTL (Time To Live)](07_Amazon_Route_53.md#️-route-53--ttl-time-to-live)

  * [TTL Impacts](07_Amazon_Route_53.md#-ttl-impacts)
* [CNAME vs Alias](07_Amazon_Route_53.md#-cname-vs-alias)

  * [Alias Record Targets](07_Amazon_Route_53.md#-alias-record-targets)
  * [Alias vs CNAME Visual](07_Amazon_Route_53.md#-visual-alias-vs-cname)
* [Summary Diagram](07_Amazon_Route_53.md#-summary-diagram)
* [Routing Policies & Health Checks](07_Amazon_Route_53.md#-amazon-route-53--routing-policies--health-checks)

  * [Supported Routing Policies](07_Amazon_Route_53.md#-supported-routing-policies)
  * [Routing Policy Highlights](07_Amazon_Route_53.md#-routing-policy-highlights)

    * [Simple](07_Amazon_Route_53.md#-simple)
    * [Weighted](07_Amazon_Route_53.md#-weighted)
    * [Latency-based](07_Amazon_Route_53.md#-latency-based)
    * [Failover](07_Amazon_Route_53.md#-failover)
    * [Geolocation](07_Amazon_Route_53.md#-geolocation)
    * [Geoproximity](07_Amazon_Route_53.md#-geoproximity-via-traffic-flow)
    * [IP-based](07_Amazon_Route_53.md#-ip-based)
    * [Multi-Value Answer](07_Amazon_Route_53.md#-multi-value-answer)
  * [Health Checks](07_Amazon_Route_53.md#️-health-checks)

    * [What They Do](07_Amazon_Route_53.md#-what-they-do)
    * [Types](07_Amazon_Route_53.md#-types)
    * [Endpoint Details](07_Amazon_Route_53.md#-endpoint-details)
    * [Calculated Health Checks](07_Amazon_Route_53.md#-calculated-health-checks)
    * [Private Resources](07_Amazon_Route_53.md#-private-resources)
* [Traffic Flow](07_Amazon_Route_53.md#-traffic-flow)
* [Domain Registrar vs DNS Service](07_Amazon_Route_53.md#-domain-registrar-vs-dns-service)

  * [Connecting Registrar & Route 53](07_Amazon_Route_53.md#-steps-to-connect)
* [Example: DNS Flow](07_Amazon_Route_53.md#-example-dns-flow)

---

## 🏗️ Chapter 8 – Amazon VPC (Virtual Private Cloud)

* [VPC Introduction](08_VPC_virtual_private_cloud.md#-vpc-introduction)
* [VPC & Subnets Primer](08_VPC_virtual_private_cloud.md#-vpc--subnets-primer)
* [VPC Diagram (Conceptual)](08_VPC_virtual_private_cloud.md#-vpc-diagram-conceptual)
* [Internet Gateway (IGW) & NAT Gateways](08_VPC_virtual_private_cloud.md#-internet-gateway-igw--nat-gateways)

  * [Internet Gateway](08_VPC_virtual_private_cloud.md#-internet-gateway)
  * [NAT Gateway / NAT Instance](08_VPC_virtual_private_cloud.md#-nat-gateway--nat-instance)
* [Network ACLs (NACL) & Security Groups](08_VPC_virtual_private_cloud.md#-network-acls-nacl--security-groups)

  * [Example & Tips](08_VPC_virtual_private_cloud.md#-example)
* [VPC Flow Logs](08_VPC_virtual_private_cloud.md#-vpc-flow-logs)
* [VPC Peering](08_VPC_virtual_private_cloud.md#-vpc-peering)
* [VPC Endpoints](08_VPC_virtual_private_cloud.md#-vpc-endpoints)

  * [Gateway Endpoint](08_VPC_virtual_private_cloud.md#-gateway-endpoint)
  * [Interface Endpoint](08_VPC_virtual_private_cloud.md#-interface-endpoint)
* [Site-to-Site VPN & Direct Connect](08_VPC_virtual_private_cloud.md#-site-to-site-vpn--direct-connect)
* [VPC Summary (Cheat Sheet)](08_VPC_virtual_private_cloud.md#-vpc-summary-cheat-sheet)
* [Typical 3-Tier Architecture (VPC)](08_VPC_virtual_private_cloud.md#-typical-3-tier-architecture-vpc)
* [LAMP Stack on AWS EC2](08_VPC_virtual_private_cloud.md#-lamp-stack-on-aws-ec2)
* [WordPress on AWS – Basic Architecture](08_VPC_virtual_private_cloud.md#-wordpress-on-aws--basic-architecture)
* [WordPress on AWS – Scalable Architecture](08_VPC_virtual_private_cloud.md#-wordpress-on-aws--scalable-architecture)
* [Example: 3-Tier VPC Architecture](08_VPC_virtual_private_cloud.md#-example-3-tier-vpc-architecture)
* [Explanation of 3-Tier Design](08_VPC_virtual_private_cloud.md#-explanation)

---

## ☁️ Chapter 9 – Amazon S3 (Simple Storage Service)

* [Introduction](09_S3_Simple_Storage_Service.md#-introduction)
* [Common Use Cases](09_S3_Simple_Storage_Service.md#-common-use-cases)
* [Amazon S3 Buckets](09_S3_Simple_Storage_Service.md#-amazon-s3-buckets)

  * [Bucket Naming Rules](09_S3_Simple_Storage_Service.md#-bucket-naming-rules)
* [Amazon S3 Objects](09_S3_Simple_Storage_Service.md#-amazon-s3-objects)

  * [Object Keys (Paths)](09_S3_Simple_Storage_Service.md#-object-keys-paths)
  * [Object Details](09_S3_Simple_Storage_Service.md#-object-details)
  * [Multi-Part Upload](09_S3_Simple_Storage_Service.md#-multi-part-upload-for-large-files)
  * [Visual Overview – How S3 Organizes Data](09_S3_Simple_Storage_Service.md#-visual-overview--how-s3-organizes-data)
* [Amazon S3 Security](09_S3_Simple_Storage_Service.md#-amazon-s3--security)

  * [Access Control Overview](09_S3_Simple_Storage_Service.md#-1-access-control-overview)
  * [IAM Policy (User-Based)](09_S3_Simple_Storage_Service.md#-iam-policy-user-based)
  * [Bucket Policy (Resource-Based)](09_S3_Simple_Storage_Service.md#-bucket-policy-resource-based)
  * [Access Control Lists (ACLs)](09_S3_Simple_Storage_Service.md#-access-control-lists-acls)
  * [Access Evaluation Logic](09_S3_Simple_Storage_Service.md#-access-evaluation-logic)
  * [Encryption in S3](09_S3_Simple_Storage_Service.md#-encryption-in-s3)
  * [Bucket Policy Structure](09_S3_Simple_Storage_Service.md#-2-bucket-policy-structure)
  * [Common Access Scenarios](09_S3_Simple_Storage_Service.md#-3-common-access-scenarios-with-diagrams)
  * [Block Public Access (BPA)](09_S3_Simple_Storage_Service.md#-4-block-public-access-bpa)
  * [Security Best Practices](09_S3_Simple_Storage_Service.md#-security-best-practices)
* [Static Website Hosting](09_S3_Simple_Storage_Service.md#-static-website-hosting)
* [Versioning](09_S3_Simple_Storage_Service.md#-versioning)
* [Replication (CRR & SRR)](09_S3_Simple_Storage_Service.md#-replication-crr--srr)
* [Storage Classes Overview](09_S3_Simple_Storage_Service.md#-storage-classes-overview)

  * [S3 Durability and Availability](09_S3_Simple_Storage_Service.md#-s3-durability-and-availability)
  * [S3 Standard – General Purpose](09_S3_Simple_Storage_Service.md#-s3-standard--general-purpose)
  * [Infrequent Access (IA) Classes](09_S3_Simple_Storage_Service.md#-infrequent-access-ia-classes)
  * [Glacier Family (Archival Storage)](09_S3_Simple_Storage_Service.md#-glacier-family-archival-storage)
  * [Intelligent-Tiering](09_S3_Simple_Storage_Service.md#-intelligent-tiering)
  * [S3 Storage Class Comparison](09_S3_Simple_Storage_Service.md#-s3-storage-class-comparison)

---
