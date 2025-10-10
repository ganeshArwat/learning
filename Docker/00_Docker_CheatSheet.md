
# 🐳 **Docker Cheat Sheet (2025 Edition)**

---

## ⚙️ **1. Basic Docker Commands**

| Command            | Description               |
| ------------------ | ------------------------- |
| `docker --version` | Check Docker version      |
| `docker info`      | Show system-wide info     |
| `docker login`     | Log in to Docker Hub      |
| `docker logout`    | Log out of Docker Hub     |
| `docker help`      | List commands or get help |

---

## 📦 **2. Images**

| Command                           | Description                  |
| --------------------------------- | ---------------------------- |
| `docker images`                   | List all images              |
| `docker pull <image>`             | Download image from registry |
| `docker build -t <name>:<tag> .`  | Build image from Dockerfile  |
| `docker rmi <image_id>`           | Remove an image              |
| `docker tag <src> <repo>:<tag>`   | Tag image for registry       |
| `docker push <repo>:<tag>`        | Push image to registry       |
| `docker save -o file.tar <image>` | Save image to tar file       |
| `docker load -i file.tar`         | Load image from tar file     |

---

## 🧱 **3. Containers**

| Command                               | Description                    |
| ------------------------------------- | ------------------------------ |
| `docker ps`                           | List running containers        |
| `docker ps -a`                        | List all containers            |
| `docker run <image>`                  | Run container from image       |
| `docker run -d <image>`               | Run in background              |
| `docker run -it <image> bash`         | Run interactively              |
| `docker stop <id>`                    | Stop running container         |
| `docker start <id>`                   | Start a stopped container      |
| `docker restart <id>`                 | Restart container              |
| `docker rm <id>`                      | Remove a container             |
| `docker exec -it <container> bash`    | Enter a running container      |
| `docker attach <container>`           | Attach to container’s terminal |
| `docker cp <container>:/path ./local` | Copy files from container      |
| `docker rename old_name new_name`     | Rename container               |

---

## 🧩 **4. Dockerfile Essentials**

| Instruction   | Description                           |
| ------------- | ------------------------------------- |
| `FROM`        | Base image                            |
| `WORKDIR`     | Set working directory                 |
| `COPY`        | Copy files to image                   |
| `ADD`         | Copy files (supports URLs & archives) |
| `RUN`         | Execute command during build          |
| `CMD`         | Default command when container runs   |
| `ENTRYPOINT`  | Executable for container start        |
| `EXPOSE`      | Document port                         |
| `ENV`         | Set environment variables             |
| `ARG`         | Define build-time variable            |
| `VOLUME`      | Mount point for data                  |
| `USER`        | Specify user                          |
| `LABEL`       | Metadata for image                    |
| `HEALTHCHECK` | Container health command              |

**Example:**

```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

---

## 🌐 **5. Networking**

| Command                                           | Description                 |
| ------------------------------------------------- | --------------------------- |
| `docker network ls`                               | List networks               |
| `docker network create <name>`                    | Create custom network       |
| `docker network inspect <name>`                   | Show network details        |
| `docker network connect <network> <container>`    | Attach container to network |
| `docker network disconnect <network> <container>` | Detach container            |

**Default Networks**

* `bridge` → default container-to-container network
* `host` → use host’s network stack
* `none` → no network access

---

## 💾 **6. Volumes & Storage**

| Command                             | Description         |
| ----------------------------------- | ------------------- |
| `docker volume ls`                  | List volumes        |
| `docker volume create <name>`       | Create volume       |
| `docker volume inspect <name>`      | Show volume details |
| `docker volume rm <name>`           | Remove volume       |
| `docker run -v myvol:/data <image>` | Mount volume        |
| `docker run -v $(pwd):/app <image>` | Mount local folder  |

**Volume Types**

* **Anonymous**: created automatically
* **Named**: explicitly created (persistent)
* **Bind mount**: link host path to container path

---

## 🪵 **7. Logging**

| Command                                              | Description               |
| ---------------------------------------------------- | ------------------------- |
| `docker logs <container>`                            | View container logs       |
| `docker logs -f <container>`                         | Follow logs live          |
| `docker logs --since 10m <container>`                | Logs since specific time  |
| `docker inspect --format='{{.LogPath}}' <container>` | Log file path             |
| `docker system df`                                   | Show log size, image size |
| `docker-compose logs`                                | Logs for all services     |

**Log Drivers:**
`json-file`, `syslog`, `journald`, `fluentd`, `gelf`, `awslogs`, `none`

---

## 🧰 **8. Docker Compose**

| Command                              | Description                        |
| ------------------------------------ | ---------------------------------- |
| `docker-compose up`                  | Start all services                 |
| `docker-compose up -d`               | Detached mode                      |
| `docker-compose down`                | Stop & remove containers, networks |
| `docker-compose ps`                  | List running services              |
| `docker-compose logs`                | View logs of all services          |
| `docker-compose exec <service> bash` | Access container                   |
| `docker-compose build`               | Build services                     |
| `docker-compose restart`             | Restart services                   |

**Compose File Example**

```yaml
version: "3.9"
services:
  web:
    build: ./app
    ports:
      - "3000:3000"
    depends_on:
      - db
  db:
    image: mongo
    volumes:
      - mongo-data:/data/db
volumes:
  mongo-data:
```

---

## 🧮 **9. Resource Management**

| Command                  | Description               |
| ------------------------ | ------------------------- |
| `docker stats`           | Show live resource usage  |
| `docker system df`       | Show disk usage           |
| `docker system prune`    | Clean up unused data      |
| `docker container prune` | Remove stopped containers |
| `docker image prune`     | Remove unused images      |

**Limit resources:**

```bash
docker run -m 512m --cpus="1.0" nginx
```

---

## ☁️ **10. Registries (Public & Private)**

| Command                                 | Description            |
| --------------------------------------- | ---------------------- |
| `docker login`                          | Login to registry      |
| `docker tag myimg localhost:5000/myimg` | Tag for local registry |
| `docker push localhost:5000/myimg`      | Push to local registry |
| `docker run -d -p 5000:5000 registry`   | Run private registry   |

**Global Private Registries:**

* Docker Hub (hub.docker.com)
* GitHub Container Registry (`ghcr.io`)
* AWS ECR / GCP Artifact Registry / Azure ACR

---

## 🔄 **11. Continuous Integration (CI)**

**Common Workflow (GitHub Actions Example):**

```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: user/app:latest
```

---

## 🧹 **12. System Cleanup**

| Command                  | Description                                    |
| ------------------------ | ---------------------------------------------- |
| `docker system prune -a` | Remove all unused images, containers, networks |
| `docker volume prune`    | Remove unused volumes                          |
| `docker builder prune`   | Clean build cache                              |

---

## 🧠 **13. Useful Shortcuts**

| Shortcut            | Description                 |
| ------------------- | --------------------------- |
| `-d`                | Detached mode               |
| `-it`               | Interactive terminal        |
| `--rm`              | Remove container after exit |
| `--name`            | Assign container name       |
| `-p host:container` | Map ports                   |
| `-v host:container` | Mount volume                |

---

## 🧩 **14. Inspect & Debug**

| Command                      | Description                  |
| ---------------------------- | ---------------------------- |
| `docker inspect <container>` | Show full container metadata |
| `docker history <image>`     | Show image build layers      |
| `docker top <container>`     | Show running processes       |
| `docker events`              | Stream Docker events live    |
| `docker diff <container>`    | Show filesystem changes      |

---

## 🧱 **15. Dockerfile Best Practices**

✅ Use small base images (`alpine`)
✅ Combine `RUN` commands to reduce layers
✅ Add `.dockerignore` to skip unwanted files
✅ Use multi-stage builds for optimized images
✅ Always specify image versions
✅ Avoid `latest` tag in production

---

## 🚀 **16. Quick Example: Full-Stack App**

**docker-compose.yml**

```yaml
version: "3.9"
services:
  backend:
    build: ./backend
    ports:
      - "3000:3000"
    depends_on:
      - mongo
  mongo:
    image: mongo
    volumes:
      - mongo-data:/data/db
  nginx:
    image: nginx
    ports:
      - "80:80"
    depends_on:
      - backend
volumes:
  mongo-data:
```

---

## 🎯 **17. Troubleshooting**

| Problem                     | Fix                                    |
| --------------------------- | -------------------------------------- |
| Container exits immediately | Use `-it` or check `CMD`               |
| Port already in use         | Change mapping (`-p 8080:80`)          |
| “No space left on device”   | `docker system prune`                  |
| “Cannot connect to daemon”  | Restart Docker service                 |
| Permissions denied          | Add user to `docker` group             |
| Build cache issues          | `docker builder prune` or `--no-cache` |

---

## 🧭 **18. Docker Flow Summary**

```text
Dockerfile  →  Build Image
Image       →  Run Container
Container   →  Connected by Network
Data        →  Stored in Volumes
Multiple Containers →  Managed by Docker Compose
CI/CD       →  Automated with GitHub Actions
```

---
