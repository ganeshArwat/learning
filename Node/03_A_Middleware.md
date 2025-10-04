### ✅ **1. Router-Level Middleware and Route Modularization**

---


### ✅ **Applying Middleware to a Single Route Method**

Here’s the syntax:

```js
app.get("/example", middlewareFunction, (req, res) => {
  res.send("This route uses a custom middleware");
});
```

Or with multiple middlewares:

```js
app.get("/example", middlewareOne, middlewareTwo, (req, res) => {
  res.send("Handled with multiple middlewares");
});
```

---

### 🔧 Example: Single Route Middleware

```js
const express = require("express");
const app = express();

// Middleware that logs the request time
const logTime = (req, res, next) => {
  console.log("Request received at:", new Date().toISOString());
  next(); // move to the next middleware or route handler
};

app.get("/profile", logTime, (req, res) => {
  res.send("User profile");
});

app.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
```

🔹 Only the `/profile` route will log the timestamp.

---

### 🧠 When to Use Per-Method Middleware?

Use it when:

- Only one or two routes need it (e.g., auth check for `/admin`)
- You want to avoid applying logic unnecessarily to other routes
- You want finer control over execution flow

---

### 🔹 What is Router-Level Middleware?

Router-level middleware is **middleware applied only to specific routers**, not the whole app.

It's useful when you want to:

- Apply middleware to certain routes (like `auth`, `logging`, etc.)
- Keep your code modular and organized

---

### 🔸 Example: Router-Level Middleware

#### 🧱 Step 1: Create a router file

📄 `routes/userRoutes.js`

```js
const express = require("express");
const router = express.Router();

// Router-level middleware
router.use((req, res, next) => {
  console.log("Router-level middleware triggered in /users");
  next();
});

router.get("/", (req, res) => {
  res.send("All users");
});

router.get("/:id", (req, res) => {
  res.send(`User ID: ${req.params.id}`);
});

module.exports = router;
```

---

#### 🧱 Step 2: Mount it in `index.js`

```js
const express = require("express");
const app = express();
const userRoutes = require("./routes/userRoutes");

app.use("/users", userRoutes); // Mounts user router on /users

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
```

Now, when you visit `/users/123`, you’ll get:

- Router middleware log: `Router-level middleware triggered in /users`
- Response: `User ID: 123`

---

### 🔸 Benefits of Route Modularization

✅ Keeps routes organized
✅ Easier to scale large apps
✅ Allows applying route-specific middleware (e.g., auth for `/admin`)

---

Would you like to now continue with:

> ✅ **Built-in, custom, and third-party middleware: `morgan`, `cors`, `helmet`, `express-rate-limit`**?

### 🔍 Summary

| Concept              | Purpose                                          |
| -------------------- | ------------------------------------------------ |
| `express.Router()`   | Creates isolated mini-apps for routes            |
| Router Middleware    | Middleware specific to a route file (not global) |
| Route Modularization | Splits routes into separate files/modules        |

---

## 🔹 **Third-Party Middleware**

These are powerful tools you install via `npm` to enhance your app.

---

## ✅ **1. `morgan` – HTTP Request Logger**

### 🔹 Purpose:

Logs incoming HTTP requests to the console in a structured format — very useful during development and debugging.

### 📦 Install:

```bash
npm install morgan
```

### 🧪 Use:

```js
const express = require("express");
const morgan = require("morgan");
const app = express();

// Log requests in 'dev' format (colored concise output)
app.use(morgan("dev"));

app.get("/", (req, res) => {
  res.send("Hello from Ganesh's backend!");
});

app.listen(3000, () => console.log("Server started"));
```

### 📝 Output:

```
GET / 200 10.123 ms - 28
```

### 📌 Formats:

| Format     | Description                     |
| ---------- | ------------------------------- |
| `dev`      | Concise colored logs            |
| `tiny`     | Very minimal logging            |
| `combined` | Apache-style logging (detailed) |

### 🔐 Use case in production:

Log to a file instead of console:

```js
const fs = require("fs");
const path = require("path");

const accessLogStream = fs.createWriteStream(
  path.join(__dirname, "access.log"),
  { flags: "a" }
);

app.use(morgan("combined", { stream: accessLogStream }));
```

---

## ✅ **2. `cors` – Cross-Origin Resource Sharing**

---

### 🔹 Purpose:

Browsers **block requests to your backend** if the frontend is hosted on a different domain or port — for security reasons.

`cors` middleware **enables or restricts** which frontend origins can communicate with your backend.

---

### 📦 Install:

```bash
npm install cors
```

---

### 🧪 Basic Usage (Allow All Origins)

```js
const cors = require("cors");
app.use(cors()); // Now any frontend can access your API
```

---

### 🔐 Restrict to Specific Origin

```js
app.use(
  cors({
    origin: "http://localhost:3000", // Only allow this origin
  })
);
```

---

### 🧪 With Multiple Origins

```js
const allowedOrigins = ["http://localhost:3000", "https://yourapp.com"];

app.use(
  cors({
    origin: function (origin, callback) {
      if (!origin || allowedOrigins.includes(origin)) {
        callback(null, true);
      } else {
        callback(new Error("Not allowed by CORS"));
      }
    },
  })
);
```

---

### 🧠 Common CORS Options

| Option           | Description                                |
| ---------------- | ------------------------------------------ |
| `origin`         | Allowed origin(s)                          |
| `methods`        | Allowed HTTP methods (`GET`, `POST`, etc.) |
| `credentials`    | Allow cookies and auth headers             |
| `allowedHeaders` | Custom headers allowed from frontend       |

### 🔒 Example: Enabling credentials

```js
app.use(
  cors({
    origin: "http://localhost:3000",
    credentials: true,
  })
);
```

Then in your frontend (`fetch`, `axios`, etc.):

```js
axios.get("/api", { withCredentials: true });
```

---

### 🛡️ Security Tip

✅ Use `cors()` with a **specific origin in production**
❌ Avoid using `cors()` without arguments in production (it's too open)

---

## ✅ **3. `helmet` – Security via HTTP Headers**

---

### 🔹 Purpose:

By default, Express apps are vulnerable to **common web attacks** like:

* XSS (Cross-Site Scripting)
* Clickjacking
* MIME-sniffing
* Cache poisoning
* HTTP header leaks

🔐 `helmet` helps secure your app by **setting secure HTTP headers automatically**.

---

### 📦 Install:

```bash
npm install helmet
```

---

### 🧪 Basic Usage:

```js
const helmet = require("helmet");
app.use(helmet()); // Protects app with sensible defaults
```

This line adds 10+ security headers like:

* `X-DNS-Prefetch-Control`
* `X-Frame-Options`
* `Strict-Transport-Security`
* `Content-Security-Policy` (CSP)
* `X-XSS-Protection` (deprecated but added for older browsers)

---

### 🔍 Example of Headers Added

```http
Strict-Transport-Security: max-age=15552000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-DNS-Prefetch-Control: off
```

These headers:

* Prevent the site from being embedded in iframes
* Force HTTPS communication
* Prevent MIME type confusion
* Protect from certain XSS attacks

---

### ⚙️ Customize Helmet

You can use individual protections:

```js
app.use(helmet.frameguard({ action: "deny" })); // Disallow iframes
app.use(helmet.noSniff()); // Prevent MIME sniffing
```

---

### 🔒 Disable Specific Headers (optional)

If you don’t want a specific policy:

```js
app.use(
  helmet({
    contentSecurityPolicy: false, // useful during development
  })
);
```

---

### ✅ Summary

| Feature                     | What it does                              |
| --------------------------- | ----------------------------------------- |
| `helmet()`                  | Enables multiple security headers         |
| `frameguard`, `nosniff`     | Prevents iframe and MIME attacks          |
| `strict-transport-security` | Enforces HTTPS                            |
| `contentSecurityPolicy`     | Limits allowed sources for scripts/images |

---

## ✅ **4. `express-rate-limit` – Prevent Abuse & Brute-Force Attacks**

---

### 🔹 Purpose:

Protects your API from:

* **Too many requests** (DDOS attacks)
* **Brute-force login attempts**
* **Spammy bots hitting your endpoints**

It works by **limiting how many requests** a client (IP) can make in a time window.

---

### 📦 Install:

```bash
npm install express-rate-limit
```

---

### 🧪 Basic Usage:

```js
const rateLimit = require("express-rate-limit");

// Allow max 100 requests per 15 minutes per IP
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,
  message: "Too many requests from this IP, please try again later.",
});

app.use(limiter); // Apply globally
```

---

### 🔒 Use Case: Apply Only to Login

```js
const loginLimiter = rateLimit({
  windowMs: 10 * 60 * 1000, // 10 minutes
  max: 5, // Max 5 login attempts per 10 minutes
  message: "Too many login attempts. Try again after 10 minutes.",
});

app.post("/login", loginLimiter, (req, res) => {
  // login logic here
});
```

---

### 🧠 Options You Can Customize

| Option         | Description                                       |
| -------------- | ------------------------------------------------- |
| `windowMs`     | Time frame for limit (in milliseconds)            |
| `max`          | Max number of requests allowed                    |
| `message`      | Response when limit is exceeded                   |
| `headers`      | Show rate limit info in headers (default: `true`) |
| `keyGenerator` | Function to generate a unique key (default: IP)   |

---

### 📌 Response Headers:

You’ll get headers like:

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1718390400
```

These help clients (like browsers or frontend devs) know how many requests remain.

---

### ✅ Summary

| Feature                   | Benefit                                 |
| ------------------------- | --------------------------------------- |
| Protects routes           | Against abuse & brute-force attacks     |
| Highly customizable       | Per-route, per-IP, or per-user limits   |
| Essential for public APIs | Especially login, signup, contact forms |

---
