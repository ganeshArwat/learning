# **AWS IAM (Identity and Access Management) – Complete Guide**

---

## **1️⃣ IAM: Users & Groups**

**Concept:** IAM is like the **security guard and HR system** for your AWS account. It manages **who can do what** in your cloud environment.

* **Root Account:**

  * Created automatically when you open AWS.
  * Has full access to everything.
  * **Best practice:** Don’t use daily; only for account setup.

* **Users:** Represent **individual people** or applications that need AWS access.

* **Groups:** Collections of users to simplify permission management.

* **Key rules:**

  * Groups **cannot contain other groups**.
  * Users **can belong to multiple groups**.
  * Users **don’t have to belong to a group**, but groups simplify permissions.

**Example:**

* Alice is in the “Developers” group, which allows EC2 access.
* Bob is in both “Developers” and “QA” groups, inheriting permissions from both.

---

## **2️⃣ IAM: Permissions**

Permissions are **policies** (JSON documents) that define **what actions a user or group can perform**.

**Example Policy (EC2 + CloudWatch + ELB permissions):**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:Describe*",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "elasticloadbalancing:Describe*",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:ListMetrics",
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:Describe*"
      ],
      "Resource": "*"
    }
  ]
}
```

**Key Points:**

* Follow **least privilege principle** → give only necessary permissions.
* Policies can be **attached to users, groups, or roles**.

---

## **3️⃣ IAM Policies Structure**

**A Policy has three main parts:**

1. **Version:** Policy language version (`2012-10-17` – always include).
2. **Id:** Optional identifier for the policy.
3. **Statement:** One or more permission rules.

**Statement Components:**

* **Sid:** Optional statement identifier.
* **Effect:** Allow or Deny.
* **Principal:** User/service this applies to.
* **Action:** List of allowed/denied actions.
* **Resource:** AWS resources affected.
* **Condition:** Optional conditions when the policy applies.

**Example Explanation:**

* Action `"ec2:Describe*"` → allows reading EC2 information, but not changing anything.
* Effect `"Allow"` → grants permissions.

---

## **4️⃣ IAM Password Policy**

Strong passwords protect your AWS account.

**AWS allows you to enforce:**

* Minimum password length
* Include uppercase, lowercase, numbers, special characters
* Users can change their own passwords
* Expiration and prevent reuse

**Tip:** A strong password + MFA drastically reduces risk of account compromise.

---

## **5️⃣ Multi-Factor Authentication (MFA)**

* MFA = **something you know (password) + something you own (device)**
* Protects accounts even if the password is stolen.
* Device options:

  * Virtual MFA device (Google Authenticator)
  * U2F Security Key
  * Hardware Key Fob (AWS GovCloud compatible)

**Example:**
Even if Alice’s password is stolen, she cannot access AWS without the MFA code.

---

## **6️⃣ How Users Access AWS**

* **AWS Management Console:** Web interface (protected by password + MFA)
* **AWS CLI (Command Line Interface):** Script and command-based access (protected by access keys)
* **AWS SDK (Software Development Kit):** Programmatic access via code

**Access Keys:**

* Access Key ID ≈ username
* Secret Access Key ≈ password
* Keep them secret; never share

---

## **7️⃣ AWS CLI & SDK**

* **AWS CLI:**

  * Direct access to AWS APIs using terminal commands
  * Automate tasks with scripts
  * Open-source: [AWS CLI GitHub](https://github.com/aws/aws-cli)

* **AWS SDK:**

  * Language-specific libraries for programmatic AWS access
  * Supports Python, JavaScript, Java, .NET, Go, Ruby, PHP, Node.js, C++
  * SDK for mobile apps and IoT devices
  * AWS CLI is built on top of the Python SDK

---

## **8️⃣ IAM Roles for Services**

**Roles** are like **temporary identities** for AWS services to act on your behalf.

**Common Use Cases:**

* EC2 instances need to access S3 → assign EC2 Role
* Lambda functions accessing DynamoDB → assign Lambda Role
* CloudFormation performing automated tasks → assign Role

---

## **9️⃣ IAM Security Tools**

* **IAM Credentials Report (account-level):** Lists all users and credential status
* **IAM Access Advisor (user-level):** Shows which services a user has accessed and when
* Helps **audit permissions** and apply least privilege

---

## **🔟 IAM Best Practices**

* Don’t use the root account except for setup
* One physical user = One AWS user
* Assign users to groups and assign permissions to groups
* Enforce strong password policies
* Enable MFA for all accounts
* Use roles for AWS services
* Use access keys for programmatic access
* Audit regularly with Credentials Report & Access Advisor
* Never share users or access keys

---

## **1️⃣1️⃣ Shared Responsibility Model (IAM)**

| **AWS**                                | **You**                              |
| -------------------------------------- | ------------------------------------ |
| Infrastructure security & compliance   | User/group/role management           |
| Configuration & vulnerability analysis | Enable MFA, rotate keys              |
| Global network security                | Review permissions & access patterns |

---

## **1️⃣2️⃣ IAM Summary**

* **Users:** Individual accounts with passwords
* **Groups:** Collections of users for simplified permissions
* **Policies:** JSON documents defining permissions
* **Roles:** Temporary identities for services or instances
* **Security:** MFA + Password policies
* **AWS CLI & SDK:** Access AWS programmatically
* **Access Keys:** Needed for CLI/SDK
* **Audit:** Credentials Report & Access Advisor

---

### **Extra Tips / Real-world Examples**

1. **Scenario:**

   * EC2 instance needs to read files from S3 → create an **EC2 Role** with S3 read permission.
   * No need to embed credentials in code → safer & easier to manage.

2. **Password + MFA:**

   * Alice’s account is compromised via phishing → MFA prevents login.

3. **Policy Design Principle:**

   * Avoid “AdminAccess” unless absolutely needed.
   * Prefer small, focused policies for each user/group.

---

