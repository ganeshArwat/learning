# ***Docker Toolbox***

## 🧠 **1. What Is Docker Toolbox?**

**Docker Toolbox** was an **older installation package** used to run Docker on:

* **Windows 7 / 8 / old MacOS systems**
* Systems **without Hyper-V** or **Docker Desktop** support

It bundled multiple tools to emulate a Linux environment for Docker.

---

## ⚙️ **2. Components of Docker Toolbox**

| Component           | Purpose                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------- |
| **Docker Engine**   | The core daemon that runs and manages containers.                                             |
| **Docker Machine**  | Creates & manages Docker hosts (VMs) on your local machine or cloud.                          |
| **Docker Compose**  | Defines and runs multi-container apps with YAML.                                              |
| **Kitematic (GUI)** | Simple desktop interface to manage containers visually.                                       |
| **VirtualBox**      | Provides the Linux VM where Docker Engine runs (since Windows 7 lacked native Linux support). |
| **Docker CLI**      | Command-line tool to talk to the Docker Engine inside the VM.                                 |

---

## 🧩 **3. Architecture Overview**

```
Your Windows Host
│
├── VirtualBox VM (Boot2Docker Linux)
│     ├── Docker Engine (Daemon)
│     └── Containers (Apps)
│
└── Docker CLI (on Host)
       ↳ communicates with VM over TCP (port 2376)
```

---

## 🪜 **4. Basic Workflow (If You Were Using It)**

> You can still test this on legacy systems or use it conceptually.

1. **Install Docker Toolbox**

   * It installs VirtualBox, Docker Machine, and Kitematic.

2. **Create a Docker Host VM**

   ```bash
   docker-machine create --driver virtualbox default
   ```

3. **List Docker Machines**

   ```bash
   docker-machine ls
   ```

4. **Connect to the Docker VM**

   ```bash
   docker-machine env default
   eval "$(docker-machine env default)"  # Linux/macOS
   ```

   or on Windows:

   ```bash
   @FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd default') DO @%i
   ```

5. **Run Containers Inside VM**

   ```bash
   docker run hello-world
   ```

6. **Get VM IP Address**

   ```bash
   docker-machine ip default
   ```

   Use that IP (e.g., `http://192.168.99.100:8080`) to access web apps.

---

## 💡 **5. Why It’s Deprecated**

* Modern Docker Desktop (for Windows 10+, macOS, Linux) runs Docker directly on your OS using **WSL 2** or native virtualization.
* Docker Toolbox is **no longer maintained**.
* But understanding it helps you:

  * Work with **Docker Machine** (still usable on cloud VMs).
  * Understand **remote Docker hosts**.
  * Learn legacy infrastructure and migration paths.

---

## 🧰 **6. Modern Equivalent Skills to Practice**

| Toolbox Concept | Modern Equivalent                              |
| --------------- | ---------------------------------------------- |
| Docker Machine  | Docker context + remote API hosts              |
| VirtualBox VM   | WSL 2 backend (Windows) / native Docker Engine |
| Kitematic       | Docker Desktop GUI                             |
| Boot2Docker     | Lightweight Linux image used in Docker Machine |

---

## 🧑‍💻 **Mini-Practice Task**

Even though Toolbox is deprecated, you can try the modern version of its logic:

1. Create a remote Docker host using Docker Machine:

   ```bash
   docker-machine create --driver generic --generic-ip-address=<REMOTE_IP> --generic-ssh-user=<USER> my-remote
   ```

2. Connect to it:

   ```bash
   docker-machine env my-remote
   ```

3. Deploy a container remotely:

   ```bash
   docker run -d -p 8080:80 nginx
   ```

This simulates the same environment Toolbox used—**Docker running remotely, controlled from your CLI.**

---

# Docker Cloud

## 🌥️ **What Is Docker Cloud?**

**Docker Cloud** was an **online platform** created by Docker, Inc.
It allowed you to **build, deploy, and manage Docker containers** on **remote cloud servers** — like AWS, Azure, or DigitalOcean — directly from a **web dashboard** or CLI.

Think of it like this:

> 🧩 “Docker Cloud was a control center on the internet that let you run Docker containers on your cloud machines, without managing the infrastructure manually.”

---

## ⚙️ **Key Features (When It Existed)**

| Feature                            | Description                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| 🖥️ **Node Management**            | Connect your cloud VMs (nodes) and manage them from one dashboard.             |
| 📦 **Service Management**          | Deploy and scale your containers/services directly from the UI.                |
| 🔁 **Continuous Deployment**       | Automatically redeploy containers when a new image is pushed to Docker Hub.    |
| 👥 **Team Collaboration**          | Invite teammates and manage access roles.                                      |
| 🔗 **Integration with Docker Hub** | Seamlessly build and pull images stored in Docker Hub.                         |
| ☁️ **Cloud Provider Integration**  | Connect directly with AWS, Azure, or DigitalOcean to spin up new Docker nodes. |

---

## 🧱 **Architecture Overview**

```
Docker Cloud (Control Plane)
│
├── Connected Nodes (Docker Hosts in AWS/Azure/etc.)
│     ├── Docker Engine
│     ├── Containers & Services
│
└── Linked with Docker Hub (for images)
```

So instead of SSHing into your EC2 instance to run containers manually, Docker Cloud could:

* Create the VM for you
* Install Docker
* Deploy your app
* Monitor and scale it — all from the browser

---

## ⚰️ **Current Status**

> ❌ **Docker Cloud was officially discontinued in 2019**.

The functionality was merged into **Docker Hub** and **Docker Desktop**, and the orchestration/deployment parts were replaced by modern tools like:

| Old Docker Cloud Feature | Modern Replacement                           |
| ------------------------ | -------------------------------------------- |
| Node management          | Docker Context / Docker Machine / Kubernetes |
| Service orchestration    | Docker Swarm / Kubernetes                    |
| Auto-deploy on push      | GitHub Actions / GitLab CI / Jenkins         |
| Image hosting            | Docker Hub / GHCR / AWS ECR                  |

---

## ⚡ **Example of Modern Equivalent**

What Docker Cloud did:

1. You pushed an image →
2. It deployed automatically to a connected server.

Today you can do the same via:

* **Docker Hub + GitHub Actions + Cloud VM**
  (build → push → auto-deploy script)
* Or use **Docker Compose on AWS ECS** or **Azure Container Apps**

---

## 🧠 **In Summary**

| Question                   | Answer                                                                                                         |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **What is Docker Cloud?**  | A hosted platform to manage Docker containers on cloud servers.                                                |
| **Who built it?**          | Docker, Inc.                                                                                                   |
| **What did it do?**        | Automated container deployment, scaling, and monitoring in the cloud.                                          |
| **Is it still available?** | No — discontinued, replaced by Docker Hub + modern CI/CD + Swarm/Kubernetes.                                   |
| **Why learn about it?**    | It helps you understand the evolution of Docker’s cloud ecosystem and remote container orchestration concepts. |

---

build a **modern Docker Cloud equivalent using GitHub Actions + Docker Hub + a Cloud VM (e.g., AWS EC2)**.

This setup will let you automatically:
✅ Build your Docker image when you push code →
✅ Push it to Docker Hub →
✅ Deploy it to your cloud server via SSH

This is exactly what Docker Cloud used to do — now fully automated using GitHub Actions.

---

## 🌐 **Goal**

You’ll set up **Continuous Deployment (CD)** for your app:
Whenever you push to `main`, your app automatically rebuilds and redeploys on your cloud instance.

---

## 🧩 **Architecture**

```
GitHub Repo (Source Code)
   ↓ push to main
GitHub Actions Workflow
   ① Build Docker image
   ② Push to Docker Hub
   ③ SSH into Cloud Host
   ④ Pull & restart container
Cloud Host (EC2 / Droplet)
   ↳ Runs your live container
```

---

## ⚙️ **Step 1 – Prerequisites**

1. **Docker Hub account**

   * Create one at: [https://hub.docker.com](https://hub.docker.com)
   * Create a repository, e.g. `my-backend`

2. **Cloud VM**

   * AWS EC2 / DigitalOcean / etc.
   * SSH access (e.g. `ubuntu@<cloud-ip>`)
   * Install Docker:

     ```bash
     sudo apt update
     sudo apt install docker.io -y
     sudo systemctl enable docker
     sudo systemctl start docker
     ```

3. **GitHub Repository**

   * Push your Node.js / Python / whatever app code to GitHub.

---

## 🧱 **Step 2 – Create Secrets in GitHub**

Go to your repo →
**Settings → Secrets and variables → Actions → New repository secret**

Add these:

| Secret Name          | Description                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| `DOCKERHUB_USERNAME` | Your Docker Hub username                                                                            |
| `DOCKERHUB_TOKEN`    | Docker Hub access token *(get it from Docker Hub → Account Settings → Security → New Access Token)* |
| `CLOUD_HOST`         | Your VM IP (e.g., `18.210.x.x`)                                                                     |
| `SSH_PRIVATE_KEY`    | Private key for your EC2 (copy contents of your `.pem` file)                                        |

---

## 🧾 **Step 3 – Create GitHub Actions Workflow**

Create file in your repo:
`.github/workflows/deploy.yml`

```yaml
name: CI/CD Deploy to Cloud

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Build Docker Image
        run: docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/my-backend:latest .

      - name: Login to Docker Hub
        run: echo ${{ secrets.DOCKERHUB_TOKEN }} | docker login -u ${{ secrets.DOCKERHUB_USERNAME }} --password-stdin

      - name: Push Docker Image
        run: docker push ${{ secrets.DOCKERHUB_USERNAME }}/my-backend:latest

      - name: Deploy to Cloud Host
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.CLOUD_HOST }}
          username: ubuntu
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            docker pull ${{ secrets.DOCKERHUB_USERNAME }}/my-backend:latest
            docker stop backend || true
            docker rm backend || true
            docker run -d -p 80:3000 --name backend ${{ secrets.DOCKERHUB_USERNAME }}/my-backend:latest
```

---

## 🧪 **Step 4 – Test the Workflow**

1. Commit and push code to `main`:

   ```bash
   git add .
   git commit -m "CI/CD setup"
   git push origin main
   ```

2. Go to your GitHub repo → **Actions tab**

   * You’ll see your workflow running.
   * It will:

     1. Build your Docker image
     2. Push to Docker Hub
     3. SSH into your cloud server
     4. Redeploy the new version

3. Visit your server IP in the browser — your app should be live! 🌍

---

## 🧰 **Step 5 – Optional Enhancements**

| Feature                      | Add-on                                                         |
| ---------------------------- | -------------------------------------------------------------- |
| Use private Docker Hub repo  | Add `--password-stdin` auth (already supported)                |
| Add staging environment      | Create separate workflow for `staging` branch                  |
| Add database (MongoDB, etc.) | Use Docker Compose in remote script                            |
| Add zero-downtime deploy     | Use `docker-compose up -d` instead of single container restart |

---

## ✅ **You Just Rebuilt Docker Cloud!**

| Old Docker Cloud Feature | GitHub Actions + Docker Hub + VM |
| ------------------------ | -------------------------------- |
| Build image              | GitHub Actions build step        |
| Store image              | Docker Hub repository            |
| Deploy to node           | SSH deploy step                  |
| Auto-deploy on push      | Trigger on `push` event          |
| Manage nodes             | Cloud provider or Docker context |

---

# Logging

---

1. **Types of logs in Docker** (based on *where they come from*)
2. **Levels of logs** (based on *how severe or important* they are)

---

## 🧱 **1. Types of Logs in Docker**

There are **three main categories** of logs you’ll encounter in Docker:

| Type                        | Description                                                          | Source                                     | Example                                                |
| --------------------------- | -------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------ |
| **Container Logs**          | Logs generated *inside containers* by the application running in it. | Application (Node.js, Nginx, Python, etc.) | `console.log('User logged in')`                        |
| **Docker Daemon Logs**      | Logs produced by the Docker Engine itself.                           | Docker service (dockerd)                   | “Container created”, “Image pulled”, “Network created” |
| **System Logs (Host Logs)** | Logs from the underlying host OS and system components.              | OS-level tools (journald, syslog)          | Kernel events, daemon restarts, etc.                   |

Let’s see each in more detail 👇

---

### 🧩 **(a) Container Logs**

* These are the **stdout** and **stderr** outputs of the container process.
* Collected automatically by Docker.
* Stored (by default) in:

  ```
  /var/lib/docker/containers/<container_id>/<container_id>-json.log
  ```

**Example command:**

```bash
docker logs my-app
```

**Used for:** debugging your app or checking runtime behavior.

---

### ⚙️ **(b) Docker Daemon Logs**

* These come from the **Docker Engine** itself.
* They show Docker’s own internal events and errors.

On Linux:

```bash
sudo journalctl -u docker.service
```

or

```
/var/log/docker.log
```

**Used for:** diagnosing Docker issues — like container creation failures, daemon crashes, image pull errors, etc.

---

### 🧰 **(c) System Logs**

* These are **OS-level logs** — not specific to Docker but often relevant.
* Includes kernel messages, network issues, file system problems, etc.

Check them with:

```bash
sudo journalctl -xe
sudo dmesg
cat /var/log/syslog
```

**Used for:** detecting system-wide problems that affect Docker or containers indirectly (like out-of-memory errors).

---

## ⚡ **2. Logging Levels**

Now, every log message has a **level** — which indicates how important or severe it is.
Docker (and most systems) follow **standard logging levels**, similar to what’s used in syslog or app frameworks.

Here’s a clear breakdown:

| Level                 | Purpose                                             | Example Message                                  |
| --------------------- | --------------------------------------------------- | ------------------------------------------------ |
| **DEBUG**             | Detailed internal info — used for debugging.        | “Creating container from image nginx:latest”     |
| **INFO**              | Normal operational messages.                        | “Container started successfully”                 |
| **NOTICE**            | Something notable happened, but not an error.       | “Low disk space detected”                        |
| **WARNING**           | Something unexpected happened but Docker recovered. | “Image not found locally, pulling from registry” |
| **ERROR**             | Operation failed, needs attention.                  | “Failed to start container”                      |
| **CRITICAL**          | Severe failure — may crash or corrupt something.    | “Docker daemon out of memory”                    |
| **ALERT / EMERGENCY** | System is unusable.                                 | “Docker daemon crashed”                          |

---

### 💡 Where to Set Docker Logging Level

You can set the Docker **daemon log level** globally in the Docker service configuration file:

Edit:

```
/etc/docker/daemon.json
```

Add:

```json
{
  "log-level": "debug"
}
```

Then restart Docker:

```bash
sudo systemctl restart docker
```

Now Docker daemon will produce more detailed logs (helpful for troubleshooting).

---

## 🧠 **Summary**

| Category               | Description                        | Access Command                      |
| ---------------------- | ---------------------------------- | ----------------------------------- |
| **Container Logs**     | Output from app inside container   | `docker logs <container>`           |
| **Docker Daemon Logs** | Events from Docker Engine          | `journalctl -u docker.service`      |
| **System Logs**        | OS-level messages affecting Docker | `sudo dmesg`, `cat /var/log/syslog` |

| Level        | Severity               | Used For         |
| ------------ | ---------------------- | ---------------- |
| **DEBUG**    | Detailed internal info | Debugging        |
| **INFO**     | Normal activity        | Monitoring       |
| **WARNING**  | Minor issue            | Caution          |
| **ERROR**    | Operation failure      | Troubleshooting  |
| **CRITICAL** | Major system failure   | Immediate action |

---

✅ **In short:**

* **Types** = Where logs come from (container, daemon, system)
* **Levels** = How important each log entry is (debug → critical)

---

# 🧱 Docker Compose

**what it is**, to **how it works**, to **hands-on project setup** (like Node.js + MongoDB + Nginx).

---

## ⚙️ **1. What is Docker Compose?**

Docker Compose is a **tool to define and manage multi-container applications** using a single configuration file — usually named `docker-compose.yml`.

Instead of running multiple `docker run` commands manually, you can describe everything — images, networks, volumes, dependencies — in one file, and launch it with:

```bash
docker-compose up
```

---

## 📄 **2. The docker-compose.yml File**

The file is written in **YAML format** and defines:

* **Services** → Each container (like `web`, `db`, `nginx`)
* **Networks** → How they communicate
* **Volumes** → Shared or persistent data
* **Environment Variables**, **Ports**, etc.

---

## 🧩 **3. Basic Example**

Let’s create a simple **Node.js + MongoDB** setup.

### 📁 Folder Structure:

```
project/
 ├── docker-compose.yml
 ├── backend/
 │   ├── Dockerfile
 │   └── app.js
```

### **backend/app.js**

```js
const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello from Node + MongoDB + Compose!'));
app.listen(3000, () => console.log('Server running on port 3000'));
```

### **backend/Dockerfile**

```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["node", "app.js"]
```

### **docker-compose.yml**

```yaml
version: '3.9'

services:
  backend:
    build: ./backend
    ports:
      - "3000:3000"
    depends_on:
      - mongo
    environment:
      - MONGO_URL=mongodb://mongo:27017/mydb
    networks:
      - mynet

  mongo:
    image: mongo
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db
    networks:
      - mynet

volumes:
  mongo-data:

networks:
  mynet:
```

---

## 🚀 **4. Commands You’ll Use Often**

| Command                              | Description                                    |
| ------------------------------------ | ---------------------------------------------- |
| `docker-compose up`                  | Start all services (builds if needed)          |
| `docker-compose up -d`               | Start in detached mode                         |
| `docker-compose down`                | Stop and remove all containers, networks, etc. |
| `docker-compose ps`                  | List running services                          |
| `docker-compose logs`                | View logs of all services                      |
| `docker-compose exec <service> bash` | Enter a running container                      |
| `docker-compose build`               | Rebuild services manually                      |

---

## 🔗 **5. How Services Communicate**

* Compose automatically creates a **custom network**.
* Each service can reach others by **service name** (not IP).
* Example:
  Node.js connects to Mongo using `mongodb://mongo:27017/mydb`
  (because the service name is `mongo`)

You **don’t need to expose ports** to communicate *inside* the network — only for access from outside (like the host browser).

---

## 💾 **6. Volumes and Data Persistence**

* Defined under `volumes:` section.
* Keeps MongoDB data even if the container restarts.

```yaml
volumes:
  mongo-data:
```

---

## 🧠 **7. Environment Variables**

You can define `.env` file:

```
PORT=3000
MONGO_URL=mongodb://mongo:27017/mydb
```

Then reference it in `docker-compose.yml`:

```yaml
env_file:
  - .env
```

---

## ⚡ **8. Scaling Services**

You can easily run multiple instances:

```bash
docker-compose up --scale backend=3
```

Docker Compose will create:

```
backend_1, backend_2, backend_3
```

They all share the same network — great for load balancing setups.

---

## 📦 **9. Logs and Monitoring**

You can view logs for one or all services:

```bash
docker-compose logs
docker-compose logs backend
docker-compose logs -f mongo
```

Combine with grep to filter levels:

```bash
docker-compose logs backend | grep ERROR
```

---

## 🧪 **10. Hands-On Task**

### 🧰 Task:

1. Create `project/` folder.
2. Add the three files (`app.js`, `Dockerfile`, `docker-compose.yml`).
3. Run:

   ```bash
   docker-compose up --build
   ```
4. Visit: [http://localhost:3000](http://localhost:3000) → You’ll see your message.
5. Run:

   ```bash
   docker-compose ps
   docker-compose logs -f
   docker-compose exec backend bash
   ```
6. Stop and clean:

   ```bash
   docker-compose down -v
   ```

---

## ✅ **Summary**

| Concept                    | Description                              |
| -------------------------- | ---------------------------------------- |
| **Docker Compose**         | Tool to run multi-container apps         |
| **Service**                | One container (like backend or database) |
| **Network**                | Lets services talk by name               |
| **Volume**                 | Persistent storage                       |
| **depends_on**             | Defines startup order                    |
| **docker-compose up/down** | Start and stop the whole app             |

---

# 🚀 **Continuous Integration (CI) with Docker**

---

## 🧠 **1. What is Continuous Integration (CI)?**

**Continuous Integration (CI)** is the process of automatically building, testing, and verifying your code every time someone pushes changes to a repository (like GitHub or GitLab).

Goal:

> Catch bugs early and ensure every code commit can be built and deployed successfully.

---

## ⚙️ **2. Where Docker Fits in CI**

Docker makes CI **consistent and reproducible**.

In a CI pipeline, Docker is used to:

1. **Build the app inside a container** → so no local dependencies needed.
2. **Run tests inside the same container**.
3. **Build Docker images** automatically.
4. **Push those images to a registry** (like Docker Hub or GHCR).
5. Optionally, **deploy the container** to staging or production.

So your entire pipeline is portable — it works the same locally, on GitHub, or in the cloud.

---

## 🧩 **3. CI Workflow Overview (GitHub Actions Example)**

Here’s what a typical CI process looks like:

```
Developer commits code → 
GitHub Action triggers →
1️⃣ Checkout repo
2️⃣ Build Docker image
3️⃣ Run tests
4️⃣ Push image to registry
5️⃣ (optional) Deploy
```

---

## 🧱 **4. Example Project Setup**

Let’s assume you have this:

```
project/
 ├── backend/
 │   ├── Dockerfile
 │   ├── app.js
 │   └── package.json
 ├── docker-compose.yml
 └── .github/
     └── workflows/
         └── ci.yml
```

### 🐳 **backend/Dockerfile**

```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]
```

---

## ⚙️ **5. Creating a CI Pipeline (GitHub Actions)**

### 📄 **.github/workflows/ci.yml**

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-test-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and Push Docker Image
        uses: docker/build-push-action@v6
        with:
          context: ./backend
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/node-backend:latest

      - name: Run Container and Test
        run: |
          docker run -d --name backend -p 3000:3000 ${{ secrets.DOCKERHUB_USERNAME }}/node-backend:latest
          sleep 5
          curl -f http://localhost:3000 || (echo "App failed to start" && exit 1)
```

---

## 🔐 **6. Set Up Docker Hub Secrets**

In your GitHub repo:

1. Go to **Settings → Secrets → Actions**
2. Add:

   * `DOCKERHUB_USERNAME`
   * `DOCKERHUB_TOKEN` (create from Docker Hub → Account Settings → Access Tokens)

---

## 🧪 **7. Run the Pipeline**

Now push your code:

```bash
git add .
git commit -m "Setup CI pipeline"
git push origin main
```

GitHub will:

* Build the Docker image
* Push it to Docker Hub
* Test if the container runs successfully

You can monitor it in **GitHub → Actions → CI Pipeline**.

---

## 🧰 **8. Optional: Add Testing Step**

If you have unit tests (like Jest or Mocha for Node), you can run them inside Docker before pushing:

```yaml
- name: Run Tests
  run: |
    docker build -t test-image ./backend
    docker run test-image npm test
```

---

## 🌐 **9. Extend CI to CD (Continuous Deployment)**

Once your CI works, you can extend it to **Continuous Deployment (CD)** — automatically deploying to production or staging environments.

For example:

* Push image to AWS ECS, GCP Cloud Run, or Kubernetes.
* SSH into a remote server and pull the new image.

Example:

```yaml
- name: Deploy to Server
  run: |
    ssh user@server "docker pull ${{ secrets.DOCKERHUB_USERNAME }}/node-backend:latest && docker compose up -d"
```

---

## ✅ **10. Summary**

| Stage       | Purpose                    | Docker’s Role                        |
| ----------- | -------------------------- | ------------------------------------ |
| **Build**   | Compile app or image       | Docker builds consistent environment |
| **Test**    | Run unit/integration tests | Containers isolate dependencies      |
| **Push**    | Publish image              | Send to Docker Hub / GHCR            |
| **Deploy**  | Run on server              | Pull and start image                 |
| **Monitor** | Check logs, health         | Docker logs & monitoring             |

---

## 🧠 **Key Takeaways**

* CI = automatic **build + test** on every code change.
* Docker ensures **consistent builds** across environments.
* GitHub Actions + Docker = simple, powerful CI setup.
* Use **Docker Hub / GHCR** to store built images.
* Extend to CD for full automation pipeline.

---
