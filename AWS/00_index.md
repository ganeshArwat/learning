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
