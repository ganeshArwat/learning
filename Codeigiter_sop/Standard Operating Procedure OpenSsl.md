## Standard Operating Procedure: OpenSSL 3.0 Server-Side Workaround for Legacy Renegotiation

### Objective

To configure OpenSSL 3.0 to permit unsafe legacy renegotiation on your Linux server, preventing SSL handshake failures for older legacy connections or CodeIgniter 3 applications without rewriting core code.

### Prerequisites

* Root or `sudo` access to the Ubuntu server.
* OpenSSL 3.0 or higher installed.

---

### Step-by-Step Procedure

1. **Edit openssl.cnf:** Open the OpenSSL configuration.
Open your system's OpenSSL configuration file using a text editor:

```bash
sudo nano /etc/ssl/openssl.cnf

```

*(Verify success: The file opens in your terminal for editing).*


2. **Configure the top of the file:** Add the global configuration pointer.
At the **very top** of the file, add the following configuration line:

```ini
openssl_conf = default_conf

```

*(Verify success: The pointer is added above all existing sections).*


3. **Configure the bottom of the file:** Append the default and SSL sections.
At the **very bottom** of the file, add the mapping blocks and the legacy renegotiation option:

```ini
[default_conf]
ssl_conf = ssl_sect

[ssl_sect]
system_default = system_default_sect

[system_default_sect]
Options = UnsafeLegacyRenegotiation

```

Save and exit the editor (`Ctrl+O`, `Enter`, then `Ctrl+X`).
*(Verify success: The changes are written to disk).*


4. **Apply changes:** Restart the web server.
Restart Apache to load the updated OpenSSL configuration:

```bash
sudo systemctl restart apache2

```

*(Verify success: Apache restarts cleanly without configuration errors).*