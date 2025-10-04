### ✅ **1. What is Express.js? Why use it?**

#### 🔹 What is Express.js?

Express.js is a **minimal and flexible Node.js web application framework** that provides a robust set of features to build single-page, multi-page, or hybrid web applications.

#### 🔹 Why use Express.js?

* ✅ **Simplicity & Minimalism**: Easy to set up and start building APIs quickly.
* ✅ **Routing**: Powerful routing mechanism to handle URL requests.
* ✅ **Middleware Support**: Allows processing requests through a chain of functions.
* ✅ **Integration**: Works smoothly with databases like MongoDB via Mongoose.
* ✅ **Community Support**: Widely used with a large ecosystem of plugins.
* ✅ **Performance**: Built on top of Node.js, so it's fast and non-blocking.

---

### ✅ **2. Setting up a Basic Express App**

Here’s how you can create a simple Express server step-by-step.

---

### 📁 Folder Setup

Create a folder for your project:

```bash
mkdir express-basics
cd express-basics
```

Initialize a Node.js project:

```bash
npm init -y
```

Install Express:

```bash
npm install express
```

---

### 📄 Create `index.js` (Entry File)

```js
// index.js

const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

// Root route
app.get("/", (req, res) => {
  res.send("Hello from Express!");
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

---

### ▶ Run the Server

```bash
node index.js
```

You should see:

```
Server is running on http://localhost:3000
```

Open that URL in your browser or use Postman to test it. You’ll get:

```
Hello from Express!
```

---

### ✅ **3. Middleware: `express.json()`, `express.urlencoded()`**

#### 🔹 What is Middleware?

Middleware in Express is a function that has access to the request (`req`), response (`res`), and the `next()` function. It is used to:

* Execute any code
* Modify the request or response object
* End the request-response cycle
* Call the next middleware in the stack

---

### 🔸 `express.json()`

This middleware parses incoming requests with JSON payloads.

```js
app.use(express.json());
```

**Use case:** When you're sending JSON data in a POST or PUT request.

Example:

```js
app.post("/json-data", (req, res) => {
  console.log(req.body); // Parsed JSON object
  res.send("JSON data received");
});
```

---

### 🔸 `express.urlencoded()`

This middleware parses incoming requests with URL-encoded payloads (from HTML forms).

```js
app.use(express.urlencoded({ extended: true }));
```

* `extended: true`: Allows nested objects using the `qs` library.
* `extended: false`: Uses the built-in `querystring` library (basic parsing).

Example:

```js
app.post("/form-data", (req, res) => {
  console.log(req.body); // Parsed form data
  res.send("Form data received");
});
```

---

### 🔍 Summary

| Middleware             | Purpose                               | Used with                |
| ---------------------- | ------------------------------------- | ------------------------ |
| `express.json()`       | Parses JSON bodies                    | APIs using JSON payloads |
| `express.urlencoded()` | Parses URL-encoded bodies (form data) | HTML form submissions    |

---

✅ These are usually placed **before your routes**, like this:

```js
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
```

---

### ✅ **4. HTTP Methods: `GET`, `POST`, `PUT`, `DELETE`**

These HTTP methods are used to **communicate with the server** and perform CRUD operations.

---

### 📌 Basic Usage in Express

Let’s create example routes to demonstrate each method:

```js
const express = require("express");
const app = express();
const PORT = 3000;

app.use(express.json()); // to parse JSON bodies

// GET: Read data
app.get("/users", (req, res) => {
  res.send("Fetching all users");
});

// POST: Create data
app.post("/users", (req, res) => {
  const user = req.body;
  res.send(`User created: ${JSON.stringify(user)}`);
});

// PUT: Update data (full update)
app.put("/users/:id", (req, res) => {
  const userId = req.params.id;
  const updatedUser = req.body;
  res.send(`User with ID ${userId} updated to: ${JSON.stringify(updatedUser)}`);
});

// DELETE: Remove data
app.delete("/users/:id", (req, res) => {
  const userId = req.params.id;
  res.send(`User with ID ${userId} deleted`);
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

---

### 🔍 Quick Summary

| Method | Use For            | Express Syntax              |
| ------ | ------------------ | --------------------------- |
| GET    | Read/Retrieve data | `app.get(path, handler)`    |
| POST   | Create data        | `app.post(path, handler)`   |
| PUT    | Update data        | `app.put(path, handler)`    |
| DELETE | Delete data        | `app.delete(path, handler)` |

---

You can test these with:

* **Postman**
* **curl**
* or a front-end client like React

---
Great! Let's continue to the next topic:

---

### ✅ **5. Creating Routes in Express**

#### 🔹 What are Routes?

Routes define **how your application responds to client requests** to specific endpoints using HTTP methods like GET, POST, etc.

---

### 🔸 Basic Route Structure

```js
app.METHOD(PATH, HANDLER);
```

* `METHOD`: HTTP method (e.g., `get`, `post`, `put`, `delete`)
* `PATH`: Route path (e.g., `'/'`, `'/users'`)
* `HANDLER`: Function with `req`, `res` (and optionally `next`)

---

### 🔸 Example: Creating Simple Routes

```js
const express = require("express");
const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send("Home Page");
});

app.get("/about", (req, res) => {
  res.send("About Page");
});

app.post("/contact", (req, res) => {
  res.send("Contact form submitted");
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

---

### 🔸 Organizing Routes in a Separate File

**Step 1:** Create `routes/userRoutes.js`

```js
const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.send("Get all users");
});

router.post("/", (req, res) => {
  res.send("Create a user");
});

module.exports = router;
```

**Step 2:** Use it in `index.js`

```js
const express = require("express");
const app = express();
const userRoutes = require("./routes/userRoutes");

app.use("/users", userRoutes); // Mount the routes

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
```

Now:

* `GET /users` → "Get all users"
* `POST /users` → "Create a user"

---

### ✅ **6. Route Parameters and Query Strings**

These are used to **pass data through the URL**, often for fetching, updating, or filtering resources.

---

## 🔹 Route Parameters (`:param`)

Route parameters are used to capture values from the URL directly.

### 🧪 Example:

```js
app.get("/users/:id", (req, res) => {
  const userId = req.params.id;
  res.send(`User ID is: ${userId}`);
});
```

**URL to test:**

```
http://localhost:3000/users/42
```

**Output:**

```
User ID is: 42
```

You can also use multiple parameters:

```js
app.get("/users/:userId/posts/:postId", (req, res) => {
  const { userId, postId } = req.params;
  res.send(`User: ${userId}, Post: ${postId}`);
});
```

---

## 🔹 Query Strings (`?key=value`)

Query strings are used to send optional key-value pairs in the URL.

### 🧪 Example:

```js
app.get("/search", (req, res) => {
  const { keyword, sort } = req.query;
  res.send(`Searching for: ${keyword}, Sort by: ${sort}`);
});
```

**URL to test:**

```
http://localhost:3000/search?keyword=node&sort=asc
```

**Output:**

```
Searching for: node, Sort by: asc
```

---

### 🔍 Summary

| Feature      | Syntax              | Accessed using  |
| ------------ | ------------------- | --------------- |
| Route Param  | `/users/:id`        | `req.params.id` |
| Query String | `/search?key=value` | `req.query.key` |

---

### ✅ **7. Handling Request and Response Objects**

In Express, `req` and `res` are the two most important objects you’ll use in every route.

---

## 🔹 `req` – The Request Object

This contains **everything sent by the client** (browser, Postman, frontend app, etc.).

### Common Properties:

| Property      | Description                                |
| ------------- | ------------------------------------------ |
| `req.body`    | Data sent in POST/PUT requests (JSON/form) |
| `req.params`  | URL route parameters                       |
| `req.query`   | Query string parameters (`?key=value`)     |
| `req.headers` | Request headers                            |
| `req.method`  | HTTP method (GET, POST, etc.)              |
| `req.url`     | Full URL of the request                    |

### Example:

```js
app.post("/login", (req, res) => {
  console.log(req.body); // { username: 'ganesh', password: '1234' }
  res.send("Login data received");
});
```

---

## 🔹 `res` – The Response Object

This is used to **send data back** to the client.

### Common Methods:

| Method           | Description                          |
| ---------------- | ------------------------------------ |
| `res.send()`     | Sends a response (text or object)    |
| `res.json()`     | Sends a JSON response                |
| `res.status()`   | Sets the status code (e.g. 200, 404) |
| `res.redirect()` | Redirects to another route           |

### Example:

```js
app.get("/profile", (req, res) => {
  res.status(200).json({
    name: "Ganesh",
    age: 23
  });
});
```

---

### ✅ Combined Example

```js
app.post("/register", (req, res) => {
  const { username, email } = req.body;
  res.status(201).send(`User ${username} registered with email ${email}`);
});
```

---

### ✅ **8. Serving Static Files in Express**

#### 🔹 What are Static Files?

Static files are assets like:

* HTML files
* CSS files
* JavaScript files
* Images (e.g. `.jpg`, `.png`)
* Fonts, PDFs, etc.

Express makes it easy to **serve static content** from a folder.

---

### 🔧 How to Serve Static Files

Use `express.static()` middleware.

### 🧪 Example:

#### 📁 Project Structure

```
/public
  ├── index.html
  ├── styles.css
  └── script.js
index.js
```

#### 📝 `index.js`

```js
const express = require("express");
const app = express();
const PORT = 3000;

// Serve files in the 'public' folder
app.use(express.static("public"));

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

Now you can:

* Access `index.html` via: `http://localhost:3000/index.html`
* Use CSS/JS files in browser directly like:

  * `http://localhost:3000/styles.css`
  * `http://localhost:3000/script.js`

---

### 📌 You can also give a virtual path prefix:

```js
app.use("/static", express.static("public"));
```

Now you'd access `styles.css` like this:

```
http://localhost:3000/static/styles.css
```

---

### ✅ Summary

| Function                   | Use                                      |
| -------------------------- | ---------------------------------------- |
| `express.static('folder')` | Serves files in a folder publicly        |
| Virtual path (`/static`)   | Adds a prefix to static file access URLs |

---

### ✅ **9. Using `dotenv` for Environment Variables**

#### 🔹 What is `dotenv`?

`dotenv` is a Node.js package that **loads environment variables from a `.env` file** into `process.env`.

This is useful to:

* Hide sensitive data (like DB credentials, API keys)
* Use different configs for dev, test, and production

---

### 🧪 Step-by-Step Setup

#### 📦 1. Install `dotenv`

```bash
npm install dotenv
```

---

#### 📄 2. Create a `.env` file in the root of your project

```env
PORT=4000
APP_NAME=MERN Backend
```

> ⚠️ Do **NOT** commit `.env` files to version control – add it to `.gitignore`.

---

#### 📝 3. Load `.env` in your main file (e.g. `index.js`)

```js
require("dotenv").config(); // at the top

const express = require("express");
const app = express();

const PORT = process.env.PORT || 3000;
const APP_NAME = process.env.APP_NAME;

app.get("/", (req, res) => {
  res.send(`Welcome to ${APP_NAME}`);
});

app.listen(PORT, () => {
  console.log(`${APP_NAME} is running on http://localhost:${PORT}`);
});
```

---

### ✅ Summary

| File          | Purpose                           |
| ------------- | --------------------------------- |
| `.env`        | Stores your environment variables |
| `process.env` | Access those variables in code    |
| `dotenv`      | Package to load `.env` values     |

---

### ✅ **10. Basic Error Handling Middleware**

---

### 🔹 What is Error Handling Middleware?

It’s a **special type of middleware** in Express that handles errors in a centralized way.

Unlike regular middleware, it has **four parameters**:

```js
(err, req, res, next)
```

---

### 🧪 Basic Example

```js
const express = require("express");
const app = express();
const PORT = 3000;

// Normal route
app.get("/", (req, res) => {
  res.send("Home Page");
});

// Route with a forced error
app.get("/error", (req, res) => {
  throw new Error("Something went wrong!");
});

// Error-handling middleware (should be after all routes)
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    message: "Internal Server Error",
    error: err.message,
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

---

### 🔹 You can also pass errors using `next(err)`

```js
app.get("/fail", (req, res, next) => {
  const err = new Error("Manual failure triggered");
  next(err); // Passes to the error handler
});
```

---

### ✅ Summary

| Feature          | Description                                       |
| ---------------- | ------------------------------------------------- |
| Error Middleware | Catches any thrown or passed errors               |
| Signature        | `function(err, req, res, next)`                   |
| Use Case         | Centralized error logging and response formatting |

---
