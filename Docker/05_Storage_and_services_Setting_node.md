# **Docker Storage**

---

## 🧩 1. Basics of Docker Storage

* **Containers are ephemeral:**

  * Any data written inside a container is **lost** when the container is deleted.

* Docker provides **persistent storage mechanisms**:

  1. **Volumes** (recommended)
  2. **Bind Mounts**
  3. **tmpfs mounts** (in-memory storage)

---

## ⚙️ 2. Volumes

* Managed by Docker, stored in Docker’s storage area (usually `/var/lib/docker/volumes`).
* Can be **shared between containers**.
* Docker handles **permissions, lifecycle, and isolation**.

**Create and use a volume:**

```bash
# Create a volume
docker volume create mydata

# Run a container using the volume
docker run -d -v mydata:/app/data --name web nginx
```

* `/app/data` inside the container is now **persistent**.
* Data stays even if the container is removed.

**Inspect a volume:**

```bash
docker volume inspect mydata
```

**Remove a volume:**

```bash
docker volume rm mydata
```

---

## 🧩 3. Bind Mounts

* Mount a **host directory** into the container.
* Useful for **development**, because changes on the host reflect immediately inside the container.

```bash
docker run -d -v /host/path:/container/path --name web nginx
```

* Host path: `/host/path`
* Container path: `/container/path`

💡 **Tip:** Volumes are preferred for production; bind mounts are convenient for development.

---

## ⚙️ 4. tmpfs Mounts

* Stores data **in memory only**.
* Data is **lost when container stops**, but it’s **fast**.

```bash
docker run -d --tmpfs /app/tmp:rw,size=100m nginx
```

* `/app/tmp` is in-memory storage of 100MB.

---

## 🔍 5. Using Storage with Databases

* Databases (MySQL, MongoDB) require **persistent storage**.
* Example: MySQL with a volume:

```bash
docker run -d \
  --name mysql \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=root \
  mysql:5.7
```

* Data persists even if the MySQL container is removed or updated.

---

## ⚡ 6. Best Practices

1. Use **named volumes** instead of anonymous volumes for easier management.
2. Avoid storing persistent data **inside container filesystem**.
3. Bind mounts are good for **dev environments**.
4. Use **tmpfs** for temporary data or caching.
5. Always back up volumes that contain critical data.

---

✅ **Summary of Docker Storage Types**

| Type       | Location       | Persistence | Use Case                   |
| ---------- | -------------- | ----------- | -------------------------- |
| Volume     | Docker managed | Yes         | Production persistent data |
| Bind Mount | Host directory | Yes         | Development, testing       |
| tmpfs      | Memory         | No          | Temporary/cache data       |

---

## 🧩 1. What is a Docker Storage Driver?

* Every Docker container has a **filesystem**, which is **built on top of image layers**.
* The **storage driver** determines **how these layers are stored and managed** on the host.
* It controls:

  * Layering (copy-on-write)
  * Performance
  * Disk usage

> Think of it as the **engine behind Docker images and container filesystems**.

---

## ⚙️ 2. Copy-on-Write (CoW) Concept

* Docker images are **read-only layers** stacked on top of each other.
* When a container is created, Docker adds a **read-write layer** on top.
* **Storage driver** manages this efficiently using **copy-on-write**.

**Example:**

```
Image Layer 1 (OS)
Image Layer 2 (App Dependencies)
Image Layer 3 (App Code)
+------------------+
Container RW Layer
```

* Only modified files are stored in the container’s writable layer.

---

## 🧩 3. Common Docker Storage Drivers

| Driver            | Supported OS | Description                                    | Notes                              |
| ----------------- | ------------ | ---------------------------------------------- | ---------------------------------- |
| **overlay2**      | Linux        | Uses OverlayFS, most modern and recommended    | Default on most Linux distros      |
| **aufs**          | Linux        | Advanced multi-layer filesystem                | Older, mostly replaced by overlay2 |
| **btrfs**         | Linux        | Copy-on-write filesystem, snapshot support     | Requires btrfs filesystem on host  |
| **zfs**           | Linux        | Supports snapshots, deduplication              | Requires ZFS on host               |
| **devicemapper**  | Linux        | Block-level storage, can use thin provisioning | Complex, older driver              |
| **windowsfilter** | Windows      | Windows containers                             | Native Windows support             |

---

## ⚡ 4. Choosing a Storage Driver

* **overlay2** → Best for Linux, stable and fast
* **aufs** → Older systems, fallback option
* **btrfs/zfs** → Advanced features, snapshots, but more setup
* **devicemapper** → Rarely used now

**Check current storage driver:**

```bash
docker info | grep "Storage Driver"
```

---

## 🔧 5. Storage Driver Commands & Tips

1. Inspect container layers:

```bash
docker inspect <container_id>
```

2. Remove unused images/layers to save disk space:

```bash
docker system prune -a
```

3. Use **overlay2** whenever possible for **performance and stability**.

---

## ✅ 6. Summary

* **Storage drivers** manage **how images and container layers are stored** on the host.
* They implement **copy-on-write** to efficiently use disk space.
* Choosing the right driver affects **performance, disk usage, and features**.
* On Linux, **overlay2** is the default and recommended.

---

# ***Setting up Node.js, MongoDB, and NGINX in Docker***

---



## 🧩 1. Project Structure

```
myapp/
├── node-app/
│   ├── Dockerfile
│   ├── package.json
│   └── index.js
├── nginx/
│   ├── Dockerfile
│   └── default.conf
└── docker-compose.yml
```

We’ll use **Docker Compose** to simplify multi-container setup.

---

## 🧱 2. Step 1: Node.js App Dockerfile

**`node-app/Dockerfile`**:

```dockerfile
# Use official Node.js LTS image
FROM node:18-alpine

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy app code
COPY . .

# Expose app port
EXPOSE 3000

# Start the app
CMD ["node", "index.js"]
```

**`node-app/index.js`**:

```js
const express = require('express');
const mongoose = require('mongoose');

const app = express();
const port = 3000;

mongoose.connect('mongodb://mongo:27017/mydb')
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error(err));

app.get('/', (req, res) => {
  res.send('Hello from Node.js Docker App!');
});

app.listen(port, () => console.log(`App running on port ${port}`));
```

* Note: Database hostname is **`mongo`** — Docker Compose network will resolve it automatically.

---

## 🧩 3. Step 2: MongoDB Container

* We’ll use the **official MongoDB image**.
* Data will persist using a **named volume**.

```yaml
mongo:
  image: mongo:6.0
  container_name: mongo
  restart: always
  volumes:
    - mongo-data:/data/db
```

* `/data/db` inside container → persistent database storage.

---

## 🧩 4. Step 3: NGINX Container as Reverse Proxy

**`nginx/Dockerfile`**:

```dockerfile
FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

**`nginx/default.conf`**:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://node-app:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

* NGINX forwards requests to **Node.js app**.
* Use container name **`node-app`** for proxy_pass.

---

## 🧩 5. Step 4: Docker Compose File

**`docker-compose.yml`**:

```yaml
version: "3.9"

services:
  node-app:
    build: ./node-app
    container_name: node-app
    ports:
      - "3000:3000"
    networks:
      - appnet
    depends_on:
      - mongo

  mongo:
    image: mongo:6.0
    container_name: mongo
    volumes:
      - mongo-data:/data/db
    networks:
      - appnet

  nginx:
    build: ./nginx
    container_name: nginx
    ports:
      - "8080:80"
    networks:
      - appnet
    depends_on:
      - node-app

networks:
  appnet:
    driver: bridge

volumes:
  mongo-data:
```

* **Networks:** All services on `appnet` → containers communicate by name.
* **Volumes:** MongoDB persists data.
* **depends_on:** Ensures correct startup order.

---

## ⚡ 6. Run the Full Stack App

```bash
docker-compose up -d --build
```

* Node.js app → available internally on port 3000
* NGINX reverse proxy → host port 8080
* MongoDB → internal only, hostname `mongo`

Test in browser: `http://localhost:8080` → Should show **“Hello from Node.js Docker App!”**

---

## ✅ 7. Key Points

1. **Custom network** (`appnet`) allows Node.js ↔ MongoDB ↔ NGINX communication.
2. **Volumes** ensure MongoDB data persists across container restarts.
3. **NGINX** acts as a reverse proxy, exposing Node.js to the outside world.
4. **Docker Compose** simplifies multi-container orchestration.

---
