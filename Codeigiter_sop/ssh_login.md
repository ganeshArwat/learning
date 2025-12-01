# **SOP: Configure SSH Key-Based Authentication (Windows → Linux Server)**

### **Purpose**

To set up secure password-less SSH login from a Windows system to a Linux server using an **ED25519** SSH key.

---
# **1. For Putty**

## **1. Install PuTTY & PuTTYgen**

1. Download PuTTY installer from the official website (includes PuTTY + PuTTYgen).
2. Install using default settings.

---

## **2. Generate SSH Keys using PuTTYgen**

1. Open **PuTTYgen**.
2. Under **Parameters**, keep:

   * **Type of key**: *ED25519* (recommended)
3. Click **Generate** → Move mouse randomly to generate entropy.
4. When generated:

   * **Public Key** → copy the whole key text (starts with `ssh-ed25519`).
   * **Key Comment** → Enter a name like:
     `ganeshpc`
   * **Save private key** → Save as `ganeshpc.ppk`
   * **Save public key** → Save as `ganeshpc.pub` (optional)

---

## **3. Upload Public Key to Linux Server**

1. Open Linux server terminal (normal SSH first).
2. Create `.ssh` directory (if not exists):

   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   ```
3. Open `authorized_keys` file:

   ```bash
   nano ~/.ssh/authorized_keys
   ```
4. Paste **the public key copied from PuTTYgen**.
5. Save and exit.
6. Set permissions:

   ```bash
   chmod 600 ~/.ssh/authorized_keys
   ```

---

## **4. Configure PuTTY for Password-less Login**

1. Open **PuTTY**.
2. In **Host Name**, enter your server IP:

   ```
   root@<server-ip>
   ```
3. On the left side menu go to:
   **Connection → SSH → Auth → Credentials**
4. Click **Browse** and select your private key (`ganeshpc.ppk`).
5. Go to:
   **Connection → Data**

   * Set **Auto-login username**:
     `root` (or your user)
6. Save the session:

   * Go back to **Session**
   * Enter a session name like **MyServer-SSH-Key**
   * Click **Save**

---

## **5. Test Password-less SSH**

1. Double-click the saved PuTTY session.
2. It should login directly **without asking for a password**.

🎉 **Your SSH password-less login using PuTTY is ready!**

---
# **2. For Terminal**

## **1. Generate SSH Key on Windows**

1. Open **Windows Terminal / PowerShell**.
2. Run the following command to generate an ED25519 SSH key:

```sh
ssh-keygen -t ed25519 -C "NameITD"
```

3. When prompted:

   * Press **Enter** to save in the default location:
     `C:\Users\<username>\.ssh\id_ed25519`
   * Press **Enter** again for **no passphrase** (optional).

---

## **2. Copy Public Key to Clipboard**

Move into the `.ssh` folder:

```sh
cd ~/.ssh
```

Copy the public key:

```sh
cat .\id_ed25519.pub | Set-Clipboard
```

Your SSH public key is now in your clipboard.

---

## **3. Log in to the Linux Server**

Use your password one last time:

```sh
ssh root@<SERVER-IP>
```

---

## **4. Add the Public Key to Linux Authorized Keys**

1. Go to the SSH directory:

```sh
cd ~/.ssh
```

2. Open (or create) the authorized keys file:

```sh
sudo nano authorized_keys
```

3. Paste your public key (right-click to paste).
4. Save & exit:

   * **CTRL + O** → Enter
   * **CTRL + X**

---

## **5. Test Password-less SSH Login**

From your Windows machine:

```sh
ssh root@<SERVER-IP>
```

You should now log in **without password**.

---

# **End of SOP**
