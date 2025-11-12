
# 🧰 **SOP: Setup PuTTY for Passwordless SSH Login**

## 🔹 Objective

Configure PuTTY to connect to a remote Linux server **without typing the password** every time by using an **SSH key pair**.

---

## 🔹 Requirements

✅ Windows system with **PuTTY** and **PuTTYgen** installed
✅ SSH access (username & password available at least once)
✅ Remote Linux server running **SSH service**

---

## 🔹 Step 1: Generate SSH Key Pair using PuTTYgen

1. Open **PuTTYgen** (installed with PuTTY).
2. Under **“Parameters”**, select:

   * Type of key to generate → **RSA**
   * Number of bits → **2048** (or 4096 for stronger security).
3. Click **Generate** and **move your mouse** around the blank area to generate randomness.
4. Once done, you’ll see a **Public Key** displayed.

---

## 🔹 Step 2: Save Your Keys

1. Click **Save private key** → choose a safe location (e.g., `C:\Users\<YourName>\.ssh\myserver.ppk`).
2. (Optional) Leave **no passphrase** if you want true passwordless login.
3. Copy the **Public Key** from the top text box (it begins with `ssh-rsa`).

---

## 🔹 Step 3: Add Public Key to Your Linux Server

1. Open **PuTTY** and log in **once** using your username and password.
2. After login, create the `.ssh` directory (if not exists):

   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   ```
3. Open the authorized_keys file:

   ```bash
   nano ~/.ssh/authorized_keys
   ```
4. Paste the **public key** you copied from PuTTYgen.
5. Save and exit (`Ctrl + O`, `Enter`, `Ctrl + X`).
6. Set proper permissions:

   ```bash
   chmod 600 ~/.ssh/authorized_keys
   ```
7. Exit SSH:

   ```bash
   exit
   ```

---

## 🔹 Step 4: Configure PuTTY to Use the Private Key

1. Open **PuTTY**.
2. In the left pane, navigate to:

   ```
   Connection → SSH → Auth → Credentials
   ```
3. Under **Private key file for authentication**, click **Browse** and select your `.ppk` private key file (example: `C:\Users\<YourName>\.ssh\myserver.ppk`).

---

## 🔹 Step 5: Save PuTTY Session

1. Go back to **Session** (top of left sidebar).
2. Enter:

   * **Host Name (or IP address):** your.server.ip
   * **Port:** 22 (default for SSH)
   * **Connection type:** SSH
3. In the **Saved Sessions** box, type a name (e.g., `MyServer-SSH`)
4. Click **Save**.

Now you have a saved PuTTY profile that remembers your SSH key and server info.

---

## 🔹 Step 6: Test Connection

1. Double-click your saved session (e.g., `MyServer-SSH`).
2. You should be logged in directly **without entering a password** 🎉

---

## 🔹 Step 7 (Optional): Auto-Login with Username

To avoid even typing the username:

1. In PuTTY, go to:

   ```
   Connection → Data
   ```
2. Under **Auto-login username**, enter your server username (e.g., `ubuntu` or `root`).
3. Click **Session → Save** again.

Next time — just **double-click your saved session** and you’ll log in automatically. ✅

---

### 🧩 Summary

| Step | Description                                              |
| ---- | -------------------------------------------------------- |
| 1    | Generate SSH key pair with PuTTYgen                      |
| 2    | Save private key (.ppk) and copy public key              |
| 3    | Add public key to `~/.ssh/authorized_keys` on the server |
| 4    | Configure PuTTY to use private key                       |
| 5    | Save PuTTY session                                       |
| 6    | Test connection — passwordless login works               |
| 7    | (Optional) Add auto-login username                       |

---
