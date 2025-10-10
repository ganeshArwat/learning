# **Dockerfile**

A **Dockerfile** is a **text file** that contains instructions to build a Docker image.
Think of it as a **recipe** for your container.

---

## **1️⃣ Structure of a Dockerfile**

A Dockerfile has **commands** that tell Docker how to set up your image.
Here’s an example:

```dockerfile
# Use an official base image
FROM ubuntu:22.04

# Set environment variables
ENV APP_DIR=/app

# Set working directory
WORKDIR $APP_DIR

# Copy files from host to container
COPY . .

# Install packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Expose a port
EXPOSE 5000

# Default command to run
CMD ["python3", "app.py"]
```

---

### 🔹 Explanation of each instruction

| Instruction | Meaning                                                          |
| ----------- | ---------------------------------------------------------------- |
| `FROM`      | Base image to start from (e.g., Ubuntu, Alpine)                  |
| `ENV`       | Set environment variables                                        |
| `WORKDIR`   | Set working directory inside the container                       |
| `COPY`      | Copy files from host machine to container                        |
| `RUN`       | Run commands while building the image (like installing packages) |
| `EXPOSE`    | Declare which port the container will listen on                  |
| `CMD`       | Default command to run when container starts                     |

> There’s also `ENTRYPOINT`, `ADD`, `USER`, `VOLUME`, `ARG` for advanced setups.

---

## **2️⃣ Basic Dockerfile Example**

If you want a minimal Python app:

**Dockerfile**

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
```

* This Dockerfile:

  1. Uses a Python base image
  2. Sets `/app` as the working directory
  3. Installs dependencies
  4. Copies your app code
  5. Exposes port 8000
  6. Runs the app

---

## **3️⃣ Building an Image from a Dockerfile**

```bash
docker build -t myapp:latest .
```

* `-t myapp:latest` → tag the image with a name and version
* `.` → context (current directory; where Dockerfile lives)

---

## **4️⃣ Running Your Image**

```bash
docker run -it -p 8000:8000 myapp:latest
```

* `-p 8000:8000` → map host port 8000 to container port 8000

---

## **5️⃣ Best Practices for Dockerfiles**

1. **Use small base images** (like `alpine`) to reduce size.
2. **Minimize layers** — combine multiple `RUN` commands using `&&`.
3. **Use `.dockerignore`** to skip unnecessary files (like `.git`, `node_modules`).
4. **Pin versions** in `FROM` and dependencies to avoid breaking changes.
5. **Order instructions wisely** — Docker caches layers; put rarely changing layers first.

---

## **6️⃣ Common Instructions Cheat Sheet**

| Instruction  | Example                                         | Notes                                     |
| ------------ | ----------------------------------------------- | ----------------------------------------- |
| `FROM`       | `FROM ubuntu:22.04`                             | Base image                                |
| `RUN`        | `RUN apt-get update && apt-get install -y curl` | Run commands at build time                |
| `CMD`        | `CMD ["python", "app.py"]`                      | Default runtime command                   |
| `ENTRYPOINT` | `ENTRYPOINT ["python"]`                         | Makes container behave like an executable |
| `COPY`       | `COPY . /app`                                   | Copy files from host                      |
| `ADD`        | `ADD app.tar.gz /app`                           | Copy + extract archives, supports URLs    |
| `WORKDIR`    | `WORKDIR /app`                                  | Set working directory                     |
| `ENV`        | `ENV PORT=5000`                                 | Environment variables                     |
| `EXPOSE`     | `EXPOSE 5000`                                   | Open ports for container                  |

---

Dockerfiles are **the blueprint** for reproducible, version-controlled Docker images.

---

## **CMD vs ENTRYPOINT in Dockerfile**

Both `CMD` and `ENTRYPOINT` define **what command runs when the container starts**, but they behave differently.

---

## **1️⃣ CMD (Default Command)**

* `CMD` sets the **default command** for the container.
* It **can be overridden** when running `docker run`.

### 🔹 Example:

**Dockerfile**

```dockerfile
FROM ubuntu:22.04
CMD ["echo", "Hello from CMD"]
```

**Run**

```bash
docker run myimage
# Output: Hello from CMD
```

**Override CMD**

```bash
docker run myimage echo "Hi, overridden!"
# Output: Hi, overridden!
```

✅ **Key points about CMD**

* Provides default behavior
* Can be overridden at runtime
* Usually the last instruction in the Dockerfile

---

## **2️⃣ ENTRYPOINT (Fixed Command)**

* `ENTRYPOINT` sets a **fixed command** that **cannot be easily overridden**.
* CMD can still provide **default arguments** to ENTRYPOINT.

### 🔹 Example:

**Dockerfile**

```dockerfile
FROM ubuntu:22.04
ENTRYPOINT ["echo"]
CMD ["Hello from ENTRYPOINT"]
```

**Run**

```bash
docker run myimage
# Output: Hello from ENTRYPOINT

docker run myimage "Hi again!"
# Output: Hi again!
```

✅ **Key points about ENTRYPOINT**

* Makes the container behave like a single executable
* CMD provides default arguments to ENTRYPOINT
* Ideal for containers meant to run **one main task**

---

## **3️⃣ Combining ENTRYPOINT + CMD**

* ENTRYPOINT defines the executable
* CMD defines default parameters

**Dockerfile Example**

```dockerfile
FROM ubuntu:22.04
ENTRYPOINT ["python3"]
CMD ["app.py"]
```

**Run**

```bash
docker run myimage
# Runs: python3 app.py

docker run myimage other_script.py
# Runs: python3 other_script.py
```

> This pattern is very common for production-ready images.

---

## **4️⃣ Summary Table**

| Feature   | CMD                        | ENTRYPOINT                                 |
| --------- | -------------------------- | ------------------------------------------ |
| Purpose   | Default command            | Fixed command / executable                 |
| Override  | Yes                        | Difficult (needs `--entrypoint`)           |
| CMD usage | `CMD ["args"]`             | Often used to supply default args          |
| Example   | `CMD ["python", "app.py"]` | `ENTRYPOINT ["python"]` + `CMD ["app.py"]` |

---

✅ **Rule of Thumb:**

* Use **CMD** if you want a **default command that the user can easily override**.
* Use **ENTRYPOINT** if you want your container to **always run a specific executable**, optionally with CMD as default arguments.

---

# **Building Dockerfiles**

When you write a Dockerfile, you **build it** to create a Docker image using `docker build`.

---

## **1️⃣ Basic Build Command**

```bash
docker build -t myimage:latest .
```

### 🔹 Explanation:

| Part                | Meaning                                                        |
| ------------------- | -------------------------------------------------------------- |
| `docker build`      | Command to build an image from a Dockerfile                    |
| `-t myimage:latest` | Tag the image with name `myimage` and version `latest`         |
| `.`                 | Context directory — Docker looks here for Dockerfile and files |

> The **build context** (`.`) is the folder Docker can access.
> Only files inside this context can be copied into the image (`COPY` / `ADD`).

---

## **2️⃣ Build Output**

During the build, Docker prints **each instruction** as a **layer**:

Example:

```
Step 1/6 : FROM ubuntu:22.04
 ---> 123abc456def
Step 2/6 : WORKDIR /app
 ---> Running in 789xyz
Step 3/6 : COPY . .
 ---> Using cache
Step 4/6 : RUN apt-get update && apt-get install -y python3
 ---> Running in 456ghj
Step 5/6 : EXPOSE 5000
 ---> Running in 234klm
Step 6/6 : CMD ["python3", "app.py"]
 ---> Running in 567nop
Successfully built abcdef123456
Successfully tagged myimage:latest
```

* Each instruction creates a **layer**.
* Layers are cached; if nothing changes in a step, Docker **reuses the layer** (faster rebuilds).

---

## **3️⃣ Useful Build Options**

| Option        | Example                                         | Meaning                          |
| ------------- | ----------------------------------------------- | -------------------------------- |
| `--file`      | `docker build -f Dockerfile.dev -t mydevapp .`  | Use a specific Dockerfile        |
| `--no-cache`  | `docker build --no-cache -t myapp:latest .`     | Ignore cache, rebuild all layers |
| `--build-arg` | `docker build --build-arg PORT=5000 -t myapp .` | Pass build-time variables        |
| `-t`          | `docker build -t myimage:v1 .`                  | Tag image with name:version      |

---

## **4️⃣ Using Build Arguments**

```dockerfile
# Dockerfile
ARG PORT=8080
ENV APP_PORT=$PORT
EXPOSE $APP_PORT
```

Build with a custom port:

```bash
docker build --build-arg PORT=5000 -t myapp:5000 .
```

---

## **5️⃣ Checking Built Images**

List images:

```bash
docker images
```

Example output:

```
REPOSITORY    TAG       IMAGE ID       SIZE
myapp         latest    abcdef123456   120MB
ubuntu        22.04     123abc456def  75MB
```

* `IMAGE ID` → Unique ID of your image
* `TAG` → Version / label
* `REPOSITORY` → Image name

---

## **6️⃣ Running Built Images**

```bash
docker run -it -p 5000:5000 myapp:latest
```

* Maps host port 5000 → container port 5000
* Starts container with CMD/ENTRYPOINT defined in Dockerfile

---

## **7️⃣ Best Practices for Building Dockerfiles**

1. **Minimize layers** → Combine `RUN` commands with `&&`.
2. **Use `.dockerignore`** → Skip unnecessary files (node_modules, logs).
3. **Tag versions** → Avoid `latest` in production.
4. **Leverage caching** → Place rarely changing layers (like `apt-get install`) first.
5. **Use small base images** → Alpine, slim variants.

---

✅ **Summary Flow**

1. Write Dockerfile → define instructions
2. Build image → `docker build -t myimage:tag .`
3. Docker processes each instruction → creates layers
4. Check images → `docker images`
5. Run container → `docker run`

---

# **Full Docker Workflow Example**

## **1️⃣ Step 1 – Create a Project**

Create a folder for your app:

```bash
mkdir myapp
cd myapp
```

Inside, create two files:

**`app.py`**

```python
print("Hello Docker World!")
```

**`requirements.txt`**
(empty for now or add packages if needed)

---

## **2️⃣ Step 2 – Write a Dockerfile**

Create **`Dockerfile`**:

```dockerfile
# Step 1: Base image
FROM python:3.12-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files
COPY . .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port (optional, not used here)
EXPOSE 5000

# Step 6: Default command
CMD ["python", "app.py"]
```

---

## **3️⃣ Step 3 – Build the Docker Image**

```bash
docker build -t myapp:1.0 .
```

Output shows each Dockerfile instruction as a **layer**.

* `myapp` → image name
* `1.0` → tag/version

Check the image:

```bash
docker images
```

---

## **4️⃣ Step 4 – Run the Container**

```bash
docker run --name myapp-container myapp:1.0
```

Output:

```
Hello Docker World!
```

> Container ran, executed CMD, and exited (because the script finished).

If you want it **interactive**:

```bash
docker run -it myapp:1.0 /bin/bash
```

* Opens a shell inside the container
* You can explore `/app`, run Python, etc.

---

## **5️⃣ Step 5 – Updating the Image**

Suppose you change `app.py`:

```python
print("Hello Docker World! Updated version")
```

Rebuild the image:

```bash
docker build -t myapp:1.1 .
```

* Tag it `1.1` to version it
* Docker caches unchanged layers, so rebuild is faster

Run the new container:

```bash
docker run myapp:1.1
```

Output:

```
Hello Docker World! Updated version
```

✅ Your changes are now reflected in a new container image.

---

## **6️⃣ Step 6 – Cleaning Up**

Remove stopped containers:

```bash
docker container prune
```

Remove old images:

```bash
docker image prune -a
```

---

## **7️⃣ Optional – Push to Registry**

Tag for a registry:

```bash
docker tag myapp:1.1 username/myapp:1.1
docker push username/myapp:1.1
```

> Now your image is stored on Docker Hub or private registry and can be pulled anywhere.

---

## **8️⃣ Summary of Workflow**

1. **Write Dockerfile** → define environment & commands
2. **Build image** → `docker build -t name:tag .`
3. **Run container** → `docker run`
4. **Update app/code** → modify files
5. **Rebuild image** → `docker build -t name:newtag .`
6. **Run updated container** → new changes applied
7. **Push to registry** → share images globally

---

This is **the complete build and run cycle** that you’ll repeat for any app.

---

# **Docker Instruction Commands**

---

## 🧩 1. FROM

* Specifies the **base image** to use for your new image.
* Every Dockerfile should start with a `FROM` instruction.

```dockerfile
FROM ubuntu:20.04
FROM node:18-alpine
```

💡 **Tip:** Use official images whenever possible (`ubuntu`, `alpine`, `node`, `nginx`).

---

## 🧩 2. RUN

* Executes commands **during image build**, typically to install software.
* Each `RUN` command creates a new **layer** in the image.

```dockerfile
RUN apt-get update && apt-get install -y python3 python3-pip
RUN npm install -g yarn
```

💡 **Tip:** Combine commands with `&&` to reduce layers and image size.

---

## 🧩 3. CMD

* Specifies the **default command** to run when the container starts.
* Only **one CMD** per Dockerfile (last one wins).

```dockerfile
CMD ["echo", "Hello World"]
CMD ["python3", "app.py"]
```

💡 Difference between `CMD` and `RUN`:

* `RUN` → executed at **build time** (creates layers)
* `CMD` → executed at **container start**

---

## 🧩 4. COPY / ADD

* **COPY** → copies files/folders from your host into the image.
* **ADD** → like COPY, but can also extract **tar archives** and fetch remote URLs.

```dockerfile
COPY ./app /app
ADD https://example.com/file.tar.gz /tmp/
```

💡 **Best practice:** Prefer `COPY` unless you need archive extraction or URL fetching.

---

## 🧩 5. WORKDIR

* Sets the **working directory** inside the container.
* All subsequent instructions (`RUN`, `CMD`, etc.) use this as the default directory.

```dockerfile
WORKDIR /app
```

---

## 🧩 6. ENV

* Sets **environment variables** inside the image.

```dockerfile
ENV PORT=8080
ENV NODE_ENV=production
```

---

## 🧩 7. EXPOSE

* Documents which **port the container will listen on**.
* Does **not actually publish the port**; you need `-p` in `docker run`.

```dockerfile
EXPOSE 80
EXPOSE 443
```

---

## 🧩 8. ENTRYPOINT

* Defines the **main executable** for the container.
* Unlike `CMD`, arguments passed to `docker run` are appended to `ENTRYPOINT`.

```dockerfile
ENTRYPOINT ["python3", "app.py"]
```

* Combine with `CMD` to pass default arguments:

```dockerfile
ENTRYPOINT ["python3", "app.py"]
CMD ["--port", "8080"]
```

---

## 🧩 9. VOLUME

* Defines **mount points** for persistent or shared data.

```dockerfile
VOLUME ["/data"]
```

* You can then mount host directories when running:

```bash
docker run -v /host/data:/data myapp
```

---

## 🧩 10. USER

* Switches to a **non-root user** for security.

```dockerfile
USER node
```

💡 Always run apps as **non-root** unless necessary.

---

## 🧩 11. ARG

* Defines **build-time variables**.

```dockerfile
ARG APP_VERSION=1.0
RUN echo $APP_VERSION
```

* Unlike `ENV`, `ARG` variables are **not available after the image is built** unless passed to `ENV`.

---

## ⚡ Key Tips for Dockerfile Instructions

* **Minimize layers:** combine multiple commands in a single `RUN`.
* **Order matters:** Docker caches layers, so put rarely changing commands at the top.
* **Security:** avoid storing secrets in Dockerfile; use environment variables or secret managers.
* **Clean up:** remove package lists and temp files in the same `RUN` to reduce image size.

---

✅ **Summary of Common Dockerfile Instructions:**

| Instruction  | Purpose                            |
| ------------ | ---------------------------------- |
| `FROM`       | Base image                         |
| `RUN`        | Execute commands during build      |
| `CMD`        | Default command at container start |
| `COPY/ADD`   | Copy files into image              |
| `WORKDIR`    | Set working directory              |
| `ENV`        | Set environment variables          |
| `EXPOSE`     | Document ports                     |
| `ENTRYPOINT` | Main executable                    |
| `VOLUME`     | Define mount points                |
| `USER`       | Specify user to run container      |
| `ARG`        | Build-time variable                |

---

# **building a Dockerfile for a web server**

---

## 🧩 1. Goal

* Build a **Docker image** that runs a **web server** (NGINX).
* Serve static HTML from a folder on your host.
* Run it in a container that maps **host port 8080 → container port 80**.

---

## 🧱 2. Project Structure

```
web-server/
├── Dockerfile
└── html/
    └── index.html
```

Example `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Web Server</title>
</head>
<body>
  <h1>Hello from Docker Web Server!</h1>
</body>
</html>
```

---

## 🧩 3. Dockerfile for NGINX

```dockerfile
# Step 1: Base Image
FROM nginx:alpine

# Step 2: Set working directory (optional)
WORKDIR /usr/share/nginx/html

# Step 3: Copy HTML files into container
COPY ./html /usr/share/nginx/html

# Step 4: Expose port 80
EXPOSE 80

# Step 5: Start NGINX (default in image)
CMD ["nginx", "-g", "daemon off;"]
```

### Explanation:

1. **FROM nginx:alpine** → Use lightweight NGINX image as base.
2. **WORKDIR** → Set the directory where HTML files will live.
3. **COPY** → Copy your static website files from host to container.
4. **EXPOSE 80** → Tell Docker this container listens on port 80.
5. **CMD** → Run NGINX in the foreground so container stays alive.

---

## 🧩 4. Build the Docker Image

From the project root (`web-server/`):

```bash
docker build -t my-web-server .
```

* `-t my-web-server` → tag the image as `my-web-server`.
* `.` → current folder contains the Dockerfile.

---

## 🧩 5. Run the Web Server Container

```bash
docker run -d -p 8080:80 --name webserver my-web-server
```

* `-d` → run in detached mode
* `-p 8080:80` → map host port 8080 → container port 80
* `--name webserver` → assign a container name

---

## 🔍 6. Test

* Open your browser: `http://localhost:8080`
* You should see **“Hello from Docker Web Server!”**

---

## ⚡ 7. Pro Tips

* For development, use **bind mounts** to update HTML without rebuilding:

```bash
docker run -d -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html --name webserver nginx:alpine
```

* For production, **build static content into the image** for immutability.
* Always clean up unused containers/images:

```bash
docker rm -f webserver
docker rmi my-web-server
```

---

✅ **Summary**

1. Use **official NGINX base image** (`FROM nginx:alpine`).
2. Copy your website files using `COPY`.
3. Expose the port your app uses (`EXPOSE 80`).
4. Use `CMD` to start the server (`nginx -g 'daemon off;'`).
5. Build and run the image with `docker build` and `docker run`.

---

