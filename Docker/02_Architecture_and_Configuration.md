# Docker Architecture

## 🧩 1. High-Level Overview

Docker has a **client-server architecture**:

```
Docker Client ↔ Docker Daemon ↔ Containers & Images
```

* **Docker Client (`docker`)**: The command-line tool you use to interact with Docker.
* **Docker Daemon (`dockerd`)**: Background service that builds, runs, and manages containers.
* **Containers**: Running instances of Docker images.
* **Images**: Read-only templates used to create containers.

> The client and daemon can run on the **same machine** or communicate over a network.

---

## ⚙️ 2. Key Components

### 2.1 Docker Client

* Users interact with Docker using the **CLI**: `docker run`, `docker build`, `docker ps`, etc.
* The client sends **REST API requests** to the Docker Daemon.

### 2.2 Docker Daemon

* Handles **building, running, and managing containers and images**.
* Manages Docker objects:

  * Images
  * Containers
  * Networks
  * Volumes
* Listens for requests from the Docker CLI or other clients.

### 2.3 Docker Images

* **Immutable templates** containing:

  * OS libraries and dependencies
  * Application code
  * Environment configuration
* Created from **Dockerfiles**.
* Stored locally or in registries (like Docker Hub).

### 2.4 Docker Containers

* **Running instances** of images.
* Isolated using **namespaces** (process, network, filesystem) and **cgroups** (resource limits).
* Can be stopped, started, and deleted without affecting the image.

### 2.5 Docker Registries

* Store Docker images for sharing and distribution.
* **Docker Hub** is the default registry.
* Can also use **private registries** for internal apps.

---

## 🧱 3. How Docker Components Interact

1. **You** run a CLI command (e.g., `docker run nginx`).
2. **Docker Client** sends the request to the **Docker Daemon**.
3. **Daemon** checks if the image exists locally:

   * If yes → creates a container.
   * If no → pulls the image from a **registry**.
4. **Daemon** starts the container using the **host OS kernel**.
5. You can then **interact with the container** using CLI commands or APIs.

---

## 🔍 4. Docker Architecture Diagram (Simplified)

```
+-----------------------------+
|       Docker CLI (Client)   |
+-----------------------------+
              |
              v
+-----------------------------+
|       Docker Daemon         |
| - Manages images            |
| - Runs containers           |
| - Manages networks & volumes|
+-----------------------------+
              |
      +-------+-------+
      |               |
+-------------+  +-------------+
|   Images    |  | Containers  |
+-------------+  +-------------+
      |
      v
+-----------------------------+
|       Docker Registry       |
+-----------------------------+
```

---

## ⚡ 5. Key Features of Docker Architecture

* **Client-Server model** → flexible for remote management.
* **Layered Images** → Docker images are made of **layers** (only changes are stored, saving space).
* **Isolation** → uses **namespaces** for separation and **cgroups** for resource control.
* **Portable** → containers run the same on any host OS with Docker installed.

---

## 🧠 6. Pro Tips

* Understand **image layers** → each Dockerfile command creates a new layer.
* Use `docker info` to see details about your Docker Daemon (storage driver, running containers, etc.).
* Use `docker system df` to check space used by images, containers, and volumes.

---

## 🧩 1. Key Difference Between Containers and VMs

| Feature            | Virtual Machines (VMs)                    | Docker Containers                                  |
| ------------------ | ----------------------------------------- | -------------------------------------------------- |
| **OS**             | Each VM runs a full guest OS              | Shares the host OS kernel                          |
| **Hypervisor**     | Uses hypervisor (VMware, VirtualBox, KVM) | No hypervisor needed                               |
| **Isolation**      | Hardware-level isolation                  | Process-level isolation                            |
| **Startup time**   | Minutes                                   | Seconds                                            |
| **Size**           | GBs (full OS + apps)                      | MBs (just app + dependencies)                      |
| **Resource usage** | High                                      | Low                                                |
| **Portability**    | Portable, but larger images               | Extremely portable, lightweight images             |
| **Best use**       | Running multiple OSes                     | Running microservices, apps, lightweight processes |

---

## 🧱 2. Architecture Layers

### Virtual Machine Architecture

```
+-----------------------------+
| Guest OS 1                 |
|  + Applications            |
+-----------------------------+
| Hypervisor                 | → Manages multiple VMs
+-----------------------------+
| Host OS                    |
+-----------------------------+
| Physical Hardware           |
+-----------------------------+
```

* Each VM has a **full OS**, making it heavy.
* Hypervisor handles virtualization and allocates CPU, memory, and I/O.

---

### Docker Container Architecture

```
+-----------------------------+
| Container 1 (App + Libs)   |
| Container 2 (App + Libs)   |
+-----------------------------+
| Docker Engine (Daemon + CLI)|
+-----------------------------+
| Host OS (Kernel)            |
+-----------------------------+
| Physical Hardware           |
+-----------------------------+
```

* Containers **share the same host OS kernel**.
* Only the **application and dependencies** are added in each container.
* Docker Engine manages **images, containers, networking, and storage**.

💡 **Result:** Docker containers are **much lighter, start faster, and use fewer resources** than VMs.

---

## ⚡ 3. Advantages of Containers over VMs

1. **Faster startup:** Containers start in seconds; VMs take minutes.
2. **Smaller footprint:** MBs vs GBs for VMs.
3. **Better resource utilization:** Containers share kernel; no duplicate OS overhead.
4. **Portability:** Easily move container images across environments.
5. **Microservices-friendly:** One service per container allows scaling and updating independently.

---

## 🧠 4. Key Takeaways

* **VMs = full OS virtualization** → heavier, slower, isolated at hardware level.
* **Docker Containers = process-level isolation** → lightweight, fast, portable.
* **Docker architecture** relies on **Docker Daemon + Engine + Host OS Kernel**, not a hypervisor.
* Understanding this difference helps you design **efficient microservices and CI/CD pipelines**.

---

# Containers and Hosts

---
## 🧩 1. How Containers Interact with the Host

Containers are **isolated processes**, but they **share the host OS kernel**. Docker uses several Linux features to provide this isolation:

1. **Namespaces** – provide isolation for:

   * **PID namespace** → separate process IDs per container
   * **Mount namespace** → separate filesystem view
   * **Network namespace** → separate network interfaces and IPs
   * **UTS namespace** → separate hostname and domain
   * **IPC namespace** → separate inter-process communication
   * **User namespace** → map container users to host users

2. **Cgroups (Control Groups)** – limit and isolate resource usage:

   * CPU
   * Memory
   * Disk I/O
   * Network bandwidth

> Namespaces = isolation
> Cgroups = resource control

---

## ⚙️ 2. Filesystem Interaction

* Containers have their **own filesystem** built from **image layers**.
* Changes made inside a container are **ephemeral** unless you use **volumes or bind mounts**.

**Example:**

```bash
# Mount a host folder inside container
docker run -v /host/data:/container/data -it ubuntu /bin/bash
```

* `/host/data` on the host maps to `/container/data` inside the container.
* Any changes persist even if the container is deleted.

---

## 🌐 3. Networking Interaction

* Each container gets its **own virtual network interface**.
* By default, Docker creates a **bridge network**.
* Containers on the same bridge can communicate using their **container names as hostnames**.

**Example:**

```bash
docker network create mynet
docker run -d --name web --network mynet nginx
docker run -it --name client --network mynet ubuntu /bin/bash
```

* Inside `client` container, you can ping `web` → `ping web`

* **Ports:** Expose container ports to the host:

```bash
docker run -p 8080:80 nginx
```

* Maps **host port 8080** → **container port 80**

---

## 🔧 4. Process Interaction

* Each container runs its **own main process** (PID 1 in container).
* Containers cannot see processes in other containers unless configured.
* Example: Inspect running processes inside a container:

```bash
docker exec -it <container> ps aux
```

* You can **limit CPU/memory** per container using cgroups:

```bash
docker run -it --memory="500m" --cpus="1.0" ubuntu
```

---

## ⚡ 5. Pro Tips

* Use **volumes for persistent data**; don’t store important files inside container filesystem.
* Map only necessary **ports** for security.
* Use **namespaces** and **cgroups** wisely to isolate and limit resources.
* Always monitor container usage:

```bash
docker stats
```

---

✅ Key Takeaways:

* Containers share the **host kernel**, but everything else is isolated.
* **Namespaces** = separation, **Cgroups** = resource limits.
* **Volumes** = persistent storage, **Port mapping** = host communication.
* Properly configured containers are secure, efficient, and portable.

---

# Docker Configuration

---

# **Docker Configuration**

Docker configuration is about controlling how Docker **behaves on your system**, including storage, networking, daemon settings, logging, and registry access.

---

## **1️⃣ Docker Daemon Configuration**

The **Docker daemon** (`dockerd`) runs in the background and manages containers, images, networks, and storage.
You can configure it via a **JSON config file**.

### 🔹 Location of config file

* **Linux:** `/etc/docker/daemon.json`
* **Windows:** `%programdata%\docker\config\daemon.json`

### 🔹 Example `daemon.json`

```json
{
  "registry-mirrors": ["https://mirror.gcr.io"],
  "insecure-registries": ["myregistrydomain.com:5000"],
  "log-level": "warn",
  "storage-driver": "overlay2"
}
```

### 🔹 Explanation

| Key                   | Meaning                                                             |
| --------------------- | ------------------------------------------------------------------- |
| `registry-mirrors`    | Use a mirror to speed up image downloads                            |
| `insecure-registries` | Registries without HTTPS                                            |
| `log-level`           | Control Docker daemon logs (debug, info, warn, error)               |
| `storage-driver`      | How Docker stores image & container layers (`overlay2` recommended) |

After editing:

```bash
sudo systemctl restart docker
```

---

## **2️⃣ Docker CLI Configuration**

The Docker CLI can also be configured using `~/.docker/config.json`.

### 🔹 Example `config.json`

```json
{
  "auths": {
    "myregistrydomain.com:5000": {
      "auth": "BASE64(username:password)"
    }
  },
  "credsStore": "desktop"
}
```

### 🔹 Explanation

| Key          | Meaning                                    |
| ------------ | ------------------------------------------ |
| `auths`      | Stores credentials for registries          |
| `credsStore` | Use OS credential manager for secure login |

---

## **3️⃣ Configuring Docker Networks**

Docker creates networks for containers by default:

* **bridge** → Default network for standalone containers
* **host** → Uses host networking
* **none** → No networking

You can **create custom networks**:

```bash
docker network create my-network
docker run --network my-network nginx
```

Custom networks allow better **isolation and communication** between containers.

---

## **4️⃣ Configuring Docker Storage**

Docker stores images, containers, and volumes.

* Default location: `/var/lib/docker`
* Can be changed in `daemon.json`:

```json
{
  "data-root": "/mnt/docker-data"
}
```

---

## **5️⃣ Configuring Logging**

Docker containers generate logs. You can configure log driver in `daemon.json`:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

* `max-size` → Maximum size per log file
* `max-file` → Maximum number of log files

---

## **6️⃣ Configuring Access to Private Registries**

1. Login to registry:

```bash
docker login myregistrydomain.com:5000
```

2. Tag images before push:

```bash
docker tag myimage myregistrydomain.com:5000/myimage
```

3. Push image:

```bash
docker push myregistrydomain.com:5000/myimage
```

4. Pull image on another machine:

```bash
docker pull myregistrydomain.com:5000/myimage
```

> This works for both **local private** and **global private** registries.

---

## ✅ Summary

| Config Area | Where                     | Purpose                                           |
| ----------- | ------------------------- | ------------------------------------------------- |
| Daemon      | `/etc/docker/daemon.json` | Control registry mirrors, storage, logs, security |
| CLI         | `~/.docker/config.json`   | Store login credentials & CLI preferences         |
| Network     | `docker network`          | Container communication & isolation               |
| Storage     | `daemon.json`             | Change Docker’s data root                         |
| Logging     | `daemon.json`             | Control container log retention & format          |
| Registry    | `docker login` + tagging  | Access private registries                         |

---

# Containers and Shells

---

# **Containers and Shells in Docker**

A **container** is a lightweight, isolated environment that runs your application.
A **shell** inside a container lets you interact with it like a normal Linux system.

---

## **1️⃣ Running a Container**

Basic command to run a container:

```bash
docker run -it ubuntu
```

### 🔹 Explanation

| Option       | Meaning                                          |
| ------------ | ------------------------------------------------ |
| `docker run` | Create and start a container from an image       |
| `-i`         | Interactive mode (keeps STDIN open)              |
| `-t`         | Allocate a pseudo-TTY (gives you a shell prompt) |
| `ubuntu`     | Image name to run                                |

> Combining `-it` gives you an interactive shell inside the container.

---

## **2️⃣ Attaching to a Container**

If a container is running in the background (detached mode), you can attach to it:

```bash
docker attach <container_id_or_name>
```

* This lets you **see logs and interact** with the container.
* Exit safely without stopping the container: press **`Ctrl+P Ctrl+Q`**.

---

## **3️⃣ Using `docker exec`**

Better than attach for running commands inside a running container:

```bash
docker exec -it <container_id_or_name> /bin/bash
```

* `exec` → run a new command inside an existing container
* `-it` → interactive shell
* `/bin/bash` → shell inside the container

This is how you can explore a container, debug it, or install packages.

---

## **4️⃣ Detached Containers**

Run a container in the background:

```bash
docker run -d --name my-nginx nginx
```

* `-d` → detached mode (container runs in the background)
* `--name` → assign a custom name to the container

You can check running containers:

```bash
docker ps
```

Check all containers (including stopped):

```bash
docker ps -a
```

---

## **5️⃣ Stopping and Removing Containers**

Stop a running container:

```bash
docker stop <container_id_or_name>
```

Remove a container:

```bash
docker rm <container_id_or_name>
```

Remove all stopped containers:

```bash
docker container prune
```

---

## **6️⃣ Understanding Shell Types**

Containers are Linux-based, so you can use different shells:

| Shell | Command Example | Notes                             |
| ----- | --------------- | --------------------------------- |
| Bash  | `/bin/bash`     | Most common                       |
| Sh    | `/bin/sh`       | Lightweight, minimal shells       |
| Zsh   | `/bin/zsh`      | If installed inside the container |

> Use `docker exec -it <container> /bin/bash` for most Linux containers.

---

## **7️⃣ Viewing Logs**

To see container output (logs):

```bash
docker logs <container_id_or_name>
```

* Add `-f` to follow logs in real-time:

```bash
docker logs -f <container_id_or_name>
```

---

## **8️⃣ Summary Commands Cheat Sheet**

| Task                        | Command                                   |
| --------------------------- | ----------------------------------------- |
| Run container interactively | `docker run -it ubuntu`                   |
| Run container detached      | `docker run -d --name mycontainer ubuntu` |
| Attach to running container | `docker attach <id>`                      |
| Exec a shell in container   | `docker exec -it <id> /bin/bash`          |
| List running containers     | `docker ps`                               |
| List all containers         | `docker ps -a`                            |
| Stop container              | `docker stop <id>`                        |
| Remove container            | `docker rm <id>`                          |
| Follow logs                 | `docker logs -f <id>`                     |

---
