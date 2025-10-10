# Public & Private Repositories

## 🧩 1. What are Docker Registries?

A **Docker Registry** is a **storage and distribution system for Docker images**.

* You **push** images to a registry.
* You **pull** images from a registry to run containers.

There are **two main types of registries**:

1. **Public Registries**
2. **Private Registries**

---

## ⚙️ 2. Public Repositories

* **Docker Hub** is the most common public registry.
* Anyone can **pull images** for free.
* Examples of popular public images:

  * `nginx` → web server
  * `ubuntu` → Linux OS base image
  * `node` → Node.js runtime

**Commands:**

```bash
# Search for an image
docker search nginx

# Pull an image
docker pull nginx:latest

# Run a container from the image
docker run -d -p 8080:80 nginx
```

💡 **Tip:** Public images often have **tags** for versions (`nginx:1.25` vs `nginx:latest`). Always use specific tags in production.

---

## 🧩 3. Private Repositories

* Private registries are **restricted**; only authorized users can access them.
* Useful for **internal company apps** or sensitive projects.
* Can be hosted on:

  * Docker Hub (private repo feature)
  * Self-hosted using **Docker Registry**
  * Cloud providers: AWS ECR, Azure ACR, Google Artifact Registry

**Example: Docker Hub Private Repo**

```bash
# Login to Docker Hub
docker login

# Tag an image with your private repo
docker tag myapp username/myapp:1.0

# Push the image
docker push username/myapp:1.0

# Pull it later
docker pull username/myapp:1.0
```

**Self-hosted Private Registry**

```bash
# Run a private registry locally
docker run -d -p 5000:5000 --name registry registry:2

# Tag your image
docker tag myapp localhost:5000/myapp:1.0

# Push to local registry
docker push localhost:5000/myapp:1.0

# Pull from local registry
docker pull localhost:5000/myapp:1.0
```

---

## ⚡ 4. Key Differences: Public vs Private

| Feature  | Public Registry                      | Private Registry                 |
| -------- | ------------------------------------ | -------------------------------- |
| Access   | Anyone                               | Restricted to authorized users   |
| Cost     | Free (for public)                    | Paid or self-hosted              |
| Security | Open source images                   | Controlled, secure               |
| Use Case | Common base images, open-source apps | Proprietary apps, company images |

---

## ✅ 5. Pro Tips

1. Always use **version tags** instead of `latest` for stability.
2. For private repos, use **access tokens** instead of passwords.
3. Clean up unused images in your registry to save storage:

```bash
docker image prune -a
```

4. For internal apps, **self-hosted registries** give full control over security and storage.

---

## 🌍 Global Private Registry — Meaning

When you say **global private registry**, it usually means:

> “A secure, private image repository accessible from anywhere (cloud-hosted).”

You can host it:

1. On **Docker Hub (private repo)**
2. On **GitHub Container Registry**
3. On **AWS ECR (Elastic Container Registry)**
4. On **Google Artifact Registry / Container Registry**
5. On **Azure Container Registry**
6. Or your own **self-hosted registry** on a public cloud VM.

---

## ⚙️ Option 1: Using Docker Hub (simple global private registry)

### 🔹 Step 1: Create a private repository

1. Go to [https://hub.docker.com](https://hub.docker.com)
2. Sign in / create an account
3. Create a new repository → Choose **Private**

### 🔹 Step 2: Login to Docker Hub from CLI

```bash
docker login
```

Enter your Docker Hub username & password (or access token).

### 🔹 Step 3: Tag your image

```bash
docker tag myimage username/myimage:latest
```

### 🔹 Step 4: Push it

```bash
docker push username/myimage:latest
```

✅ Now your image is stored in your private Docker Hub repo — globally accessible (only with login).

---

## ⚙️ Option 2: Self-hosted Global Private Registry

You can also **host your own registry** (just like Docker Hub but private) on a cloud server — for example on an AWS EC2, GCP VM, or DigitalOcean droplet.

### 🔹 Step 1: Run the registry container

```bash
docker run -d -p 5000:5000 --name my-registry registry:2
```

This starts a Docker registry service on port `5000`.

### 🔹 Step 2: (Optional) Secure it with SSL and Authentication

You’d typically:

* Use **Nginx reverse proxy** with SSL (Let’s Encrypt)
* Add **basic auth** for security
  (so only authorized users can push/pull)

### 🔹 Step 3: Push an image

```bash
docker tag myimage my-server-ip:5000/myimage
docker push my-server-ip:5000/myimage
```

Now any Docker client that can reach your server can pull that image:

```bash
docker pull my-server-ip:5000/myimage
```

✅ You’ve just built a **global private Docker registry**.

---

## 🧩 Comparison Table

| Type                                                  | Example                   | Accessible From   | Security          |
| ----------------------------------------------------- | ------------------------- | ----------------- | ----------------- |
| **Local Registry**                                    | `localhost:5000`          | Only your machine | Local only        |
| **Global Private Registry (Docker Hub private repo)** | `docker.io/username/repo` | Anywhere          | Managed by Docker |
| **Self-hosted Private Registry (Cloud)**              | `mydomain.com:5000/repo`  | Anywhere          | You control it    |

---

# ***Managing Ports***

---

## 🧩 1. Understanding Ports in Docker

* Containers run in **isolated networks**.
* Each container can have its own **internal ports**.
* To access services from the **host machine or external clients**, you need to **map container ports to host ports**.

> Think of it as **forwarding traffic** from the host to the container.

---

## ⚙️ 2. Port Mapping Syntax

```bash
docker run -p <host_port>:<container_port> <image>
```

* `<host_port>` → port on your local machine
* `<container_port>` → port inside the container

**Example:**

```bash
docker run -d -p 8080:80 nginx
```

* NGINX runs on **port 80 inside the container**
* Host port **8080** is mapped → access via `http://localhost:8080`

---

## 🔍 3. Exposing Multiple Ports

* You can map multiple ports for one container:

```bash
docker run -d -p 8080:80 -p 8443:443 nginx
```

* Maps **HTTP** (80) and **HTTPS** (443) to host ports **8080** and **8443**.

---

## 🧩 4. EXPOSE Instruction in Dockerfile

* `EXPOSE <port>` **documents** which port the container listens on.
* It **does NOT publish** the port automatically — you still need `-p` when running.

```dockerfile
FROM nginx:alpine
EXPOSE 80
EXPOSE 443
```

---

## ⚡ 5. Listing Port Mappings

* To see which host ports are mapped to container ports:

```bash
docker ps
```

Sample output:

```
CONTAINER ID   IMAGE   PORTS
a1b2c3d4e5f6   nginx   0.0.0.0:8080->80/tcp
```

* Detailed inspection:

```bash
docker port <container_name_or_id>
```

---

## 🔧 6. Dynamic Port Mapping

* Docker can assign a **random available host port** using `-P` (uppercase):

```bash
docker run -d -P nginx
```

* Docker will map **container ports to random host ports** automatically.
* Use `docker ps` to see which port was assigned.

---

## ✅ 7. Pro Tips

1. Always use **specific host ports** in production (`-p 8080:80`) for predictability.
2. Avoid conflicts: multiple containers cannot use the same host port.
3. Combine with **Docker networks** for internal communication instead of exposing ports externally.
4. For development, **dynamic ports (`-P`)** are convenient.

---

# Container Linking

---

## 🧩 1. What is Container Linking?

* Container Linking allows **one container to connect to another**.
* Docker provides **built-in networking features** so containers can see each other by **name or alias**.
* Useful when running **multi-container apps**, e.g., a web server container talking to a database container.

> Note: Modern Docker recommends **user-defined networks** instead of legacy `--link`.

---

## ⚙️ 2. Using Legacy `--link` (Old Way)

```bash
# Run a MySQL container
docker run -d --name mydb -e MYSQL_ROOT_PASSWORD=root mysql:5.7

# Run a web app and link to MySQL
docker run -d --name webapp --link mydb:db nginx
```

* `--link mydb:db` → creates environment variables inside `webapp` with connection info.
* Not recommended for new projects — replaced by **Docker networks**.

---

## 🧩 3. Recommended Way: User-Defined Bridge Network

1. **Create a network**

```bash
docker network create mynet
```

2. **Run containers on the network**

```bash
docker run -d --name mydb --network mynet -e MYSQL_ROOT_PASSWORD=root mysql:5.7
docker run -d --name webapp --network mynet nginx
```

* Both containers are on `mynet` network.
* `webapp` can reach `mydb` using its **container name** (`mydb`) as hostname.

---

## 🔍 4. Inspect Container Linking / Network

* List networks:

```bash
docker network ls
```

* Inspect network details:

```bash
docker network inspect mynet
```

* Output shows all connected containers and their IPs.

---

## ⚡ 5. Networking Tips for Linking Containers

1. Use **user-defined bridge networks** for easier DNS-based linking.
2. Avoid hardcoding IPs — use **container names** for hostname resolution.
3. You can link **multiple containers** to the same network.
4. Use **environment variables** for credentials and config, not hardcoding.

---

## 🧱 6. Example: Web + Database Container

```bash
# Create network
docker network create appnet

# Run MySQL container
docker run -d --name mysql --network appnet -e MYSQL_ROOT_PASSWORD=root mysql:5.7

# Run Node.js web app container
docker run -d --name webapp --network appnet -p 3000:3000 my-node-app
```

* Inside `webapp`, you can connect to the database using **hostname `mysql`**.

---

✅ **Summary**

* **Legacy `--link`** exists but is deprecated.
* **User-defined networks** are the modern and preferred way to link containers.
* Containers on the same network can **communicate by name**, without exposing ports to host.
* Proper linking is essential for **multi-container apps** (web + DB + cache, etc.).

---

# Docker Networking

---

## 🧩 1. Why Docker Networking Matters

* Containers are **isolated by default**.

* Networking determines:

  * How containers **talk to each other**
  * How containers **access the internet**
  * How **external clients** reach your services

* Docker provides **network drivers** to handle these scenarios.

---

## ⚙️ 2. Docker Network Drivers

Docker has several **built-in network drivers**:

| Driver      | Scope       | Description                                     | Use Case                                                 |
| ----------- | ----------- | ----------------------------------------------- | -------------------------------------------------------- |
| **bridge**  | Single host | Default network for containers                  | Simple container-to-container communication on same host |
| **host**    | Single host | Container shares host network stack             | High-performance networking, bypass container NAT        |
| **overlay** | Multi-host  | Connect containers across multiple Docker hosts | Swarm/Kubernetes services, distributed apps              |
| **macvlan** | Single host | Container gets a real network interface         | When container needs its own MAC/IP                      |
| **none**    | Single host | No network                                      | Isolated container, no networking                        |

---

## 🧩 3. Bridge Network (Default)

* Each container gets a **private IP** on the bridge network.
* Containers can communicate **by IP**.
* Port mapping is required to access containers from host:

```bash
docker run -d --name web -p 8080:80 nginx
```

* Internal container IP: `172.17.0.X`

* External access via host port `8080`

* Create a custom bridge network:

```bash
docker network create mybridge
docker run -d --name web --network mybridge nginx
docker run -it --network mybridge alpine /bin/sh
```

* Containers on `mybridge` can communicate **by name**.

---

## 🔍 4. Host Network

* Container **shares host network**. No NAT, no port mapping needed.

```bash
docker run -d --network host nginx
```

* Fastest networking, but **less isolation**.
* Not recommended for untrusted containers.

---

## 🧩 5. Overlay Network

* Used for **multi-host container communication**.
* Requires **Docker Swarm or Kubernetes**.
* Useful for **microservices** spread across multiple machines.

```bash
docker network create -d overlay myoverlay
```

* Containers connected to `myoverlay` can communicate **across hosts** securely.

---

## ⚡ 6. Macvlan Network

* Assigns a **real MAC address** and IP from your LAN to container.
* Makes the container appear as a **physical device** on your network.

```bash
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 mymacvlan
```

* Rarely used; mostly for legacy systems requiring unique IPs.

---

## 🔧 7. Inspecting Networks

* List all networks:

```bash
docker network ls
```

* Inspect a network:

```bash
docker network inspect mybridge
```

* Disconnect a container:

```bash
docker network disconnect mybridge web
```

---

## ✅ 8. Pro Tips

1. Use **custom user-defined networks** for better DNS-based container communication.
2. Avoid exposing all ports; use **internal networks** whenever possible.
3. Overlay networks are best for **distributed multi-host setups**.
4. Use **`docker-compose` networks** to automatically connect multi-container apps.

---

✅ **Summary**

* Docker networking allows **container isolation, inter-container communication, and host/external access**.
* **Bridge, Host, Overlay, Macvlan** are key drivers.
* Use **custom networks** for predictable DNS resolution and better security.

---


## 🧩 1. Why Use Custom Networks?

* Default bridge network works, but **container names are not automatically resolved by DNS** on default bridge.
* **Custom networks** allow:

  * Containers to communicate **by name**
  * Automatic DNS resolution
  * Better network isolation and security
  * Easier multi-container orchestration

> Think of a custom network as a **private virtual LAN** for your containers.

---

## ⚙️ 2. Creating a Custom Network

```bash
docker network create mynetwork
```

* By default, this creates a **bridge network**.
* You can specify a **subnet and gateway** if needed:

```bash
docker network create \
  --driver bridge \
  --subnet 172.25.0.0/16 \
  --gateway 172.25.0.1 \
  mynetwork
```

* `--driver bridge` → network type (bridge is default)
* `--subnet` and `--gateway` → control IP addressing

---

## 🧩 3. Running Containers on a Custom Network

```bash
docker run -d --name web --network mynetwork nginx
docker run -it --name app --network mynetwork alpine /bin/sh
```

* Containers **`web`** and **`app`** are now on the same network.
* They can communicate using **container names**:

```bash
ping web
```

* No port mapping is needed for internal communication.

---

## 🔍 4. Inspecting a Custom Network

```bash
docker network ls         # List all networks
docker network inspect mynetwork
```

* Shows:

  * Connected containers
  * Subnet and gateway
  * IP addresses assigned to containers

---

## ⚡ 5. Connecting and Disconnecting Containers

* Connect an existing container to a network:

```bash
docker network connect mynetwork mycontainer
```

* Disconnect a container:

```bash
docker network disconnect mynetwork mycontainer
```

---

## 🧱 6. Advantages of Custom Networks

1. **Container name resolution:** No need to hardcode IPs.
2. **Isolation:** Different networks for dev, staging, production.
3. **Security:** Restrict which containers can communicate.
4. **Scalability:** Easily add more containers to the network.

---

## ✅ 7. Example: Web + Database on Custom Network

```bash
# Create network
docker network create appnet

# Run MySQL container
docker run -d --name mysql --network appnet -e MYSQL_ROOT_PASSWORD=root mysql:5.7

# Run Node.js app container
docker run -d --name nodeapp --network appnet -p 3000:3000 my-node-app
```

* Inside `nodeapp`, connect to database using hostname: `mysql`
* No port mapping needed for internal communication; host only accesses Node.js on port 3000.

---

Custom networks are the **best practice** for multi-container apps because they give **predictable connectivity, security, and DNS resolution**.

---

## 🧩 1. Communication Basics

* By default, each container is **isolated**.
* Communication requires them to be on the **same network**.
* Docker provides **internal DNS** so containers can reach each other **by name**, not just IP.

**Key components enabling communication:**

1. **Bridge Networks** – default network for containers on the same host.
2. **Custom Networks** – user-defined bridge or overlay networks with DNS.
3. **Network Drivers** – bridge, overlay, host, macvlan.
4. **Port Mapping** – expose ports to the host if external access is needed.

---

## ⚙️ 2. Communication on Default Bridge Network

* Containers can communicate **only via IP address** by default.
* Example:

```bash
docker run -d --name web nginx
docker run -it --name client alpine /bin/sh
ping <web_container_IP>
```

* Limitation: If `web` container restarts, IP may change → not reliable.

---

## 🧩 3. Communication on Custom Network (Recommended)

1. Create a network:

```bash
docker network create mynet
```

2. Run containers on that network:

```bash
docker run -d --name db --network mynet mysql
docker run -d --name app --network mynet my-node-app
```

3. **Internal DNS Resolution:**

* `app` can connect to `db` using the **container name `db`**.
* No need to know the IP address.

**Example (Node.js connecting to MySQL):**

```js
const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'db',         // container name
  user: 'root',
  password: 'root',
  database: 'mydb'
});
```

---

## 🔍 4. Communication Across Hosts

* Requires **overlay networks** or **Docker Swarm/Kubernetes**.
* Overlay networks connect containers across **multiple Docker hosts**.
* Docker manages **routing and DNS**, so containers can still use names to reach each other.

---

## ⚡ 5. Container-to-Container Communication Summary

| Scenario                         | How to Communicate                         | Notes                                   |
| -------------------------------- | ------------------------------------------ | --------------------------------------- |
| Same host, default network       | By IP                                      | IP can change on restart → not reliable |
| Same host, custom bridge network | By container name                          | Recommended for stability and DNS       |
| Different hosts                  | Overlay network / Swarm                    | Name resolution works across hosts      |
| Host ↔ Container                 | Port mapping (`-p hostPort:containerPort`) | For external access                     |

---

## ✅ 6. Practical Example

```bash
# Create a network
docker network create appnet

# Run database
docker run -d --name mysql --network appnet -e MYSQL_ROOT_PASSWORD=root mysql:5.7

# Run Node.js app
docker run -d --name nodeapp --network appnet -p 3000:3000 my-node-app
```

* Inside `nodeapp`, connect to database using **hostname `mysql`**.
* No ports need to be exposed to the host for internal communication.

---

💡 **Key Point:**
**Containers communicate using container names via Docker’s internal DNS** if they are on the same user-defined network. IP addresses are optional but less reliable.

---
