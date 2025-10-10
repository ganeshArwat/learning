# Docker Overview
---
## 🧩 1. What is Docker?

Docker is a **containerization platform** — it allows you to **package** an application and all its dependencies (libraries, system tools, runtime) into a single **container**.

So wherever you run that container — laptop, cloud, or production — it will behave **exactly the same**.

That’s why we say Docker solves the problem:

> “It works on my machine.”

---

## 🧠 2. Why We Need Docker

Before Docker, you had to:

* Install dependencies manually on every server.
* Handle version mismatches (e.g., Node 16 vs 18).
* Recreate identical setups manually.

Docker fixes that by:

* Creating a **standard environment**.
* Allowing **consistent deployments**.
* Running apps in **isolated containers**.

So every app runs independently — no dependency conflicts.

---

## ⚙️ 3. What Exactly Is a Container?

A **container** is just a **running process**, but isolated from others on the same system.
It has its own:

* File system
* Network
* System libraries

It uses the **host OS kernel**, so it’s lightweight (unlike VMs, which need a full OS for each instance).

Think of containers as:

> “Tiny, isolated computers running inside your real computer.”

---

## 🧱 4. How Docker Works (High-level)

1. You write a **Dockerfile** → a recipe of how to build your environment.
2. Docker reads it and creates an **Image** → a snapshot/template.
3. When you run the image, Docker creates a **Container** → a live, running instance.

Flow:

```
Dockerfile  →  Image  →  Container
```

---

## 🔍 5. Components of Docker

| Component                     | Role                                                               |
| ----------------------------- | ------------------------------------------------------------------ |
| **Docker CLI**                | The command-line tool you use (`docker run`, `docker build`, etc.) |
| **Docker Daemon (`dockerd`)** | Background process that builds/runs containers                     |
| **Images**                    | Blueprints (read-only templates)                                   |
| **Containers**                | Running instances of images                                        |
| **Docker Hub**                | A cloud registry where images are stored/pulled from               |

---

## 💻 6. Simple Example

Try this when Docker is installed:

```bash
docker run hello-world
```

What happens:

1. Docker checks if the image `hello-world` exists locally.
2. If not, it downloads it from **Docker Hub**.
3. It creates a container from that image.
4. The container prints “Hello from Docker!” and exits.

That’s your first container 🎉

---

## ⚖️ 7. Docker vs Virtual Machines

| Feature     | Docker Container      | Virtual Machine        |
| ----------- | --------------------- | ---------------------- |
| OS          | Shares host OS kernel | Has its own full OS    |
| Size        | Lightweight (MBs)     | Heavy (GBs)            |
| Start time  | Seconds               | Minutes                |
| Isolation   | Process-level         | Hardware-level         |
| Performance | Near-native           | Slower                 |
| Use Case    | Microservices, CI/CD  | Full OS virtualization |

---

## ⚡ 8. Key Benefits

* **Fast deployments**
* **Lightweight and portable**
* **Consistent environments**
* **Easy scaling**
* **Simpler DevOps and CI/CD pipelines**

---

## ✅ 9. Summary

Docker:

* Packages apps into containers.
* Runs them anywhere consistently.
* Uses host OS resources efficiently.
* Replaces heavy virtual machines with lightweight containers.

---
# Docker Installation
---
## 🧩 1. Supported Platforms

Docker runs on:

* **Linux** (Ubuntu, CentOS, Fedora, Debian, etc.)
* **Windows 10/11** (requires WSL2 for Windows Home)
* **macOS**

💡 **Note:** Docker Desktop is the easiest for Windows/macOS. On Linux, you install Docker Engine directly.

---

## 🧱 2. Installing Docker on Linux (Ubuntu Example)

### Step 1: Update Packages

```bash
sudo apt update
```

### Step 2: Install Prerequisites

```bash
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release -y
```

### Step 3: Add Docker’s Official GPG Key

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker.gpg
```

### Step 4: Add Docker Repository

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Step 5: Install Docker Engine

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

### Step 6: Start and Enable Docker

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

### Step 7: Verify Installation

```bash
docker --version
sudo docker run hello-world
```

✅ If you see “Hello from Docker!”, it means Docker is installed and working.

---

## 🧩 3. Optional: Run Docker Without `sudo`

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Now you can use `docker run` without `sudo`.

---

## 💻 4. Installing Docker on Windows/macOS

1. Go to [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Download and install the version for your OS.
3. Start Docker Desktop.
4. Verify installation:

```bash
docker version
docker run hello-world
```

💡 **Tip:** On Windows, make sure WSL2 is enabled for best performance.

---

## ⚡ 5. Pro Tips

* Always use **stable Docker versions** for production.
* Use `docker info` to check the daemon status, storage driver, and resources.
* Remove unused images/containers periodically with:

```bash
docker system prune -a
```

---

# Docker Hub

---

## 🧩 1. What is Docker Hub?

**Docker Hub** is a **cloud-based registry** for Docker images.
It allows you to:

* **Store** images (publicly or privately)
* **Share** images with others
* **Pull** images to use locally
* **Collaborate** in teams

Think of it as **GitHub for Docker images**.

---

## ⚙️ 2. Why Docker Hub is Important

* Lets you **reuse pre-built images** like `nginx`, `ubuntu`, `node`, etc.
* Makes **deployment easy** — just pull the image wherever you need it.
* Supports **automated builds** from GitHub/GitLab.
* Can create **private repositories** for proprietary apps.

---

## 🧩 3. Docker Hub Terminology

| Term           | Meaning                                                              |
| -------------- | -------------------------------------------------------------------- |
| **Repository** | A collection of Docker images, usually for one app/service.          |
| **Tag**        | A version of an image (e.g., `nginx:latest` or `node:18-alpine`).    |
| **Namespace**  | Your Docker Hub username or organization name.                       |
| **Registry**   | Where images are stored — Docker Hub is the default public registry. |

---

## 💻 4. Basic Commands

### Login to Docker Hub

```bash
docker login
```

* Enter your username and password (or access token).
* After login, you can push/pull images.

### Search for an Image

```bash
docker search nginx
```

* Finds images on Docker Hub matching the name.

### Pull an Image

```bash
docker pull nginx:latest
```

* Downloads the image from Docker Hub to your local system.

### List Local Images

```bash
docker images
```

### Tag an Image (for pushing)

```bash
docker tag myapp:1.0 username/myapp:1.0
```

### Push an Image to Docker Hub

```bash
docker push username/myapp:1.0
```

---

## 🧩 5. Example: Using Docker Hub Images

```bash
# Pull nginx image
docker pull nginx

# Run nginx container
docker run -d -p 8080:80 nginx
```

* Open `http://localhost:8080` — you’ll see the default NGINX page.
* Docker pulled the image automatically from Docker Hub.

---

## ⚡ 6. Pro Tips

* Always use **specific tags** instead of `latest` in production (`nginx:1.25`).
* Use **.dockerignore** to avoid sending unnecessary files when building images for Hub.
* For private images, use **Docker Hub Access Tokens** instead of your password.

---

# Containers & Working with Containers

---

## 🧩 1. What is a Container?

A **container** is a **running instance of a Docker image**.

Key points:

* Containers are **isolated processes** — they have their own filesystem, libraries, and network stack.
* Containers **share the host OS kernel**, making them lightweight compared to VMs.
* Typically, **one container runs one service or process**.

> Think of containers as **tiny, portable, self-contained mini-servers**.

---

## ⚙️ 2. Lifecycle of a Container

A container goes through these stages:

1. **Create** → `docker create <image>` (prepares a container but doesn’t start it)
2. **Start** → `docker start <container>` (starts a stopped container)
3. **Stop** → `docker stop <container>` (stops a running container)
4. **Restart** → `docker restart <container>`
5. **Remove** → `docker rm <container>` (deletes the container)

💡 **Tip:** Containers are **ephemeral** — when deleted, all changes inside are lost unless you use **volumes**.

---

## 💻 3. Basic Commands for Containers

### Run a Container

```bash
docker run -it ubuntu /bin/bash
```

* `-i` → interactive
* `-t` → terminal
* `/bin/bash` → starts a bash shell inside the container

### Run in Detached Mode (Background)

```bash
docker run -d nginx
```

* `-d` → detached mode
* Useful for running services like web servers in the background.

### List Containers

```bash
docker ps          # Running containers
docker ps -a       # All containers (including stopped)
```

### Stop / Start / Remove

```bash
docker stop <container_id_or_name>
docker start <container_id_or_name>
docker rm <container_id_or_name>
```

---

## 🧩 4. Inspecting and Accessing Containers

### Access a Running Container

```bash
docker exec -it <container_id_or_name> /bin/bash
```

* Opens a shell inside the container.

### View Container Logs

```bash
docker logs <container_id_or_name>
```

### Inspect Container Details

```bash
docker inspect <container_id_or_name>
```

* Shows IP, volumes, environment variables, network info, etc.

---

## 🔗 5. Connecting Containers

* Containers can communicate via **Docker networks**.
* By default, Docker creates a **bridge network** for containers to talk to each other on the same host.
* Example:

```bash
docker network ls         # List networks
docker network create mynet
docker run -d --name web --network mynet nginx
docker run -it --name client --network mynet ubuntu /bin/bash
```

* The `client` container can now ping `web` by name.

---

## ⚡ 6. Pro Tips

* Use **meaningful names** for containers (`--name webserver`).
* Avoid running multiple services in one container — use one container per service.
* Remember that containers are **stateless by default**; use volumes for persistent data.
* Clean up unused containers/images regularly:

```bash
docker system prune -a
```

---

