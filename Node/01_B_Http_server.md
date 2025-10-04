## ✅ **Creating a Basic HTTP Server in Node.js**

This is the **core of backend development** with Node. You’ll understand how servers handle client requests and send responses — without using Express or any framework.

---

### 🔧 Step-by-Step Breakdown

#### 🔹 1. **Import the HTTP module**

```js
const http = require("http");
```

---

#### 🔹 2. **Create the server**

```js
const server = http.createServer((req, res) => {
  // req = Request Object
  // res = Response Object

  res.write("Hello from my first server!");
  res.end(); // Always end the response
});
```

---

#### 🔹 3. **Listen on a port**

```js
server.listen(3000, () => {
  console.log("Server is running at http://localhost:3000");
});
```

---

### 💡 What happens here?

1. The server listens on port **3000**
2. When a browser hits `http://localhost:3000`, the callback fires
3. You respond with `"Hello from my first server!"`

---

## 🔁 Add Route Handling (Basic Routing)

Let’s respond differently based on the path:

```js
const server = http.createServer((req, res) => {
  const url = req.url;

  res.setHeader("Content-Type", "text/plain");

  if (url === "/") {
    res.write("Welcome to the Home Page");
  } else if (url === "/about") {
    res.write("About Us Page");
  } else {
    res.statusCode = 404;
    res.write("404 Not Found");
  }

  res.end();
});
```

---

## 🧠 Add Headers + HTML Response

```js
const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "text/html");

  res.write("<html>");
  res.write("<head><title>My Page</title></head>");
  res.write("<body><h1>Hello from Node.js</h1></body>");
  res.write("</html>");

  res.end();
});
```

---

### 📦 JSON API Response

```js
const server = http.createServer((req, res) => {
  if (req.url === "/api") {
    res.setHeader("Content-Type", "application/json");

    const data = {
      name: "Ganesh",
      course: "MERN Backend",
    };

    res.end(JSON.stringify(data));
  }
});
```

---

### ✅ Best Practice: Always `res.setHeader()` before writing

This avoids issues with content type or malformed responses.

---

### 📁 Summary:

| Step              | What it does                       |
| ----------------- | ---------------------------------- |
| `createServer()`  | Creates the server                 |
| `listen(port)`    | Starts the server                  |
| `req.url`         | Path of the request                |
| `res.write()`     | Sends content to the client        |
| `res.end()`       | Finishes the response              |
| `res.setHeader()` | Sets headers (like `Content-Type`) |

---

## 🔧 **Goal: Create a REST API for Users**

We’ll support the following routes:

| Method | Route        | Description             |
| ------ | ------------ | ----------------------- |
| GET    | `/users`     | Get all users           |
| GET    | `/users/:id` | Get a single user by ID |
| POST   | `/users`     | Add a new user          |
| PUT    | `/users/:id` | Update a user           |
| DELETE | `/users/:id` | Delete a user           |

We’ll keep the data in-memory using a JavaScript array.

---

## 📁 `server.js` – Complete REST API with `http`

```js
const http = require("http");
const { v4: uuidv4 } = require("uuid"); // for generating unique user IDs

const PORT = 3000;
const users = [
  { id: "1", name: "Ganesh" },
  { id: "2", name: "Sarita" },
];

// Helper to parse JSON body
function parseBody(req) {
  return new Promise((resolve) => {
    let body = "";
    req.on("data", (chunk) => (body += chunk));
    req.on("end", () => resolve(JSON.parse(body || "{}")));
  });
}

// Server creation
const server = http.createServer(async (req, res) => {
  const url = req.url;
  const method = req.method;

  // Enable JSON response
  res.setHeader("Content-Type", "application/json");

  // GET /users
  if (url === "/users" && method === "GET") {
    res.writeHead(200);
    return res.end(JSON.stringify(users));
  }

  // GET /users/:id
  if (url.startsWith("/users/") && method === "GET") {
    const id = url.split("/")[2];
    const user = users.find((u) => u.id === id);

    if (!user) {
      res.writeHead(404);
      return res.end(JSON.stringify({ message: "User not found" }));
    }

    res.writeHead(200);
    return res.end(JSON.stringify(user));
  }

  // POST /users
  if (url === "/users" && method === "POST") {
    const body = await parseBody(req);
    const newUser = { id: uuidv4(), name: body.name };

    users.push(newUser);
    res.writeHead(201);
    return res.end(JSON.stringify(newUser));
  }

  // PUT /users/:id
  if (url.startsWith("/users/") && method === "PUT") {
    const id = url.split("/")[2];
    const userIndex = users.findIndex((u) => u.id === id);

    if (userIndex === -1) {
      res.writeHead(404);
      return res.end(JSON.stringify({ message: "User not found" }));
    }

    const body = await parseBody(req);
    users[userIndex].name = body.name;

    res.writeHead(200);
    return res.end(JSON.stringify(users[userIndex]));
  }

  // DELETE /users/:id
  if (url.startsWith("/users/") && method === "DELETE") {
    const id = url.split("/")[2];
    const index = users.findIndex((u) => u.id === id);

    if (index === -1) {
      res.writeHead(404);
      return res.end(JSON.stringify({ message: "User not found" }));
    }

    const deletedUser = users.splice(index, 1)[0];

    res.writeHead(200);
    return res.end(JSON.stringify(deletedUser));
  }

  // If no route matched
  res.writeHead(404);
  res.end(JSON.stringify({ message: "Route not found" }));
});

server.listen(PORT, () => {
  console.log(`🚀 REST API running at http://localhost:${PORT}`);
});
```

---

## 🧪 How to Test the API?

You can use:

* [Postman](https://www.postman.com/)
* `curl` in terminal
* `Thunder Client` VSCode extension

### ✅ Examples:

```bash
GET     http://localhost:3000/users
GET     http://localhost:3000/users/1
POST    http://localhost:3000/users      { "name": "Ravi" }
PUT     http://localhost:3000/users/2    { "name": "Raj" }
DELETE  http://localhost:3000/users/1
```

---

## 📦 Install UUID for ID generation:

```bash
npm init -y
npm install uuid
```

---