# **SOP: Configure SSH Key-Based Authentication (Windows → Linux Server)**

### **Purpose**

To set up secure password-less SSH login from a Windows system to a Linux server using an **ED25519** SSH key.

---

# **Step-by-Step Procedure**

## **1. Generate SSH Key on Windows**

1. Open **Windows Terminal / PowerShell**.
2. Run the following command to generate an ED25519 SSH key:

```sh
ssh-keygen -t ed25519 -C "ganeshITD"
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

## **5. Set Correct Permissions**

Run:

```sh
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

---

## **6. Test Password-less SSH Login**

From your Windows machine:

```sh
ssh -i ~/.ssh/id_ed25519 root@<SERVER-IP>
```

You should now log in **without password**.

---

## **7. (Optional) Give Custom Name to the Key**

If you want the key filename to identify your PC (e.g., *ganeshpc*):

```sh
ssh-keygen -t ed25519 -C "ganeshITD" -f ~/.ssh/id_ed25519_ganeshpc
```

Then connect using:

```sh
ssh -i ~/.ssh/id_ed25519_ganeshpc root@<SERVER-IP>
```

---

# **End of SOP**
