## ✅ **CORS Configuration and Security in Express.js**

---

### 🔹 Quick Recap: What is CORS?

**CORS** (Cross-Origin Resource Sharing) is a browser security feature that **blocks frontend JavaScript from accessing a backend on a different domain or port** unless the backend explicitly allows it.

For example:
Your frontend is at `http://localhost:3000` and backend is at `http://localhost:5000`
Without CORS setup, the browser **blocks the request**.

---

## 🔧 CORS Setup with `cors` Middleware

### 📦 Install:

```bash
npm install cors
```

---

### 🧪 1. **Allow All Origins** (Good for testing, not secure!)

```js
const cors = require("cors");
app.use(cors()); // Allows all domains
```

---

### 🔐 2. **Allow Specific Origin**

```js
app.use(
  cors({
    origin: "http://localhost:3000", // Allow only this
  })
);
```

---

### 🔐 3. **Allow Multiple Origins Dynamically**

```js
const allowedOrigins = ["http://localhost:3000", "https://myapp.com"];

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

### 🔑 4. **Allow Credentials (Cookies / Auth headers)**

If you're using sessions, JWT in cookies, etc. — you'll need to allow **credentials**:

#### ✅ Server-side:

```js
app.use(
  cors({
    origin: "http://localhost:3000",
    credentials: true, // Allow sending cookies
  })
);
```

#### ✅ Client-side:

```js
axios.get("http://localhost:5000/profile", {
  withCredentials: true,
});
```

---

### 🔍 5. **Customizing Allowed Methods & Headers**

```js
app.use(
  cors({
    origin: "http://localhost:3000",
    methods: ["GET", "POST", "PUT", "DELETE"],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);
```

---

### 🛡️ Security Tips

| Tip                                     | Why                               |
| --------------------------------------- | --------------------------------- |
| ✅ Use **specific origins**              | Avoid exposing API to any site    |
| ✅ Enable **credentials** only if needed | Extra security layer              |
| ❌ Avoid `app.use(cors())` in production | Too open                          |
| ✅ Use HTTPS in production               | Prevent man-in-the-middle attacks |

---

### ✅ Summary

| Setting          | Description                         |
| ---------------- | ----------------------------------- |
| `origin`         | Domain(s) allowed to access API     |
| `credentials`    | Allow cookies and auth headers      |
| `methods`        | HTTP methods allowed (GET, POST...) |
| `allowedHeaders` | Headers allowed from frontend       |

---

## ✅ **Global Error Handling in Express.js**

### 🔹 Why Do We Need It?

In a real-world API, we must catch and handle **all types of errors** centrally, such as:

* Missing resources (404)
* Validation failures
* DB failures
* Unexpected server errors

> Instead of repeating `try/catch` everywhere, we can create **one global error handler**.

---

## 🔧 1. Basic Error Handling Middleware

### ✅ Syntax:

An error-handling middleware in Express **must have 4 arguments**:

```js
(err, req, res, next) => { ... }
```

### 🧪 Example:

```js
app.use((err, req, res, next) => {
  console.error("Global Error:", err.stack);

  res.status(err.status || 500).json({
    success: false,
    message: err.message || "Something went wrong!",
  });
});
```

Place this **after all routes**.

---

## 🔧 2. Throwing Custom Errors from Routes

```js
app.get("/error", (req, res, next) => {
  const error = new Error("This is a custom error");
  error.status = 400;
  next(error); // Pass to global handler
});
```

---

## 🧪 3. 404 Not Found Handler (Optional)

Catch unhandled routes:

```js
app.use((req, res, next) => {
  res.status(404).json({
    success: false,
    message: "Route not found",
  });
});
```

---

## 🔧 4. With `async/await` Routes (Avoiding try/catch everywhere)

### 🧠 Tip: Use a wrapper like this:

```js
const asyncHandler = fn => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);
```

Then wrap routes like:

```js
app.get(
  "/users",
  asyncHandler(async (req, res) => {
    const users = await User.find();
    res.json(users);
  })
);
```

This avoids writing `try/catch` in every async route.

---

## ✅ Summary

| Step                                    | Description                              |
| --------------------------------------- | ---------------------------------------- |
| Custom error middleware                 | Catches any error passed via `next(err)` |
| 404 handler                             | For unknown routes                       |
| `asyncHandler` helper                   | Cleaner async/await route errors         |
| Error logging (with `console` / logger) | For debugging and alerting               |

---

## ✅ **Validating Requests in Express.js**

We’ll cover two popular validation libraries:

* 🔸 `express-validator` – Works with middleware functions
* 🔸 `Joi` – Schema-based and standalone validation logic

---

## 🔸 1. `express-validator` – Middleware-Based Validation


### 📦 Install:

```bash
npm install express-validator
```

### ✅ Basic Usage:

```js
const { body, validationResult } = require("express-validator");

app.post(
  "/register",
  [
    body("username").isLength({ min: 3 }).withMessage("Username must be at least 3 characters"),
    body("email").isEmail().withMessage("Invalid email"),
    body("password").isStrongPassword().withMessage("Weak password"),
  ],
  (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    // Proceed with registration
    res.send("User registered successfully!");
  }
);
```

---

### 🔹 Common Validators:

| Validator            | Description                |
| -------------------- | -------------------------- |
| `isEmail()`          | Checks valid email         |
| `isLength({min})`    | Min/Max string length      |
| `notEmpty()`         | Field must not be empty    |
| `isInt()`            | Checks if value is integer |
| `isStrongPassword()` | Ensures strong passwords   |

---

### 🔧 Validation Error Output Format:

```json
{
  "errors": [
    {
      "msg": "Invalid email",
      "param": "email",
      "location": "body"
    }
  ]
}
```

---

## 🔸 2. `Joi` – Schema-Based Validation

### 📦 Install:

```bash
npm install joi
```

### ✅ Basic Usage:

```js
const Joi = require("joi");

const userSchema = Joi.object({
  username: Joi.string().min(3).required(),
  email: Joi.string().email().required(),
  password: Joi.string().min(6).required(),
});

app.post("/register", (req, res) => {
  const { error } = userSchema.validate(req.body);

  if (error) {
    return res.status(400).json({ message: error.details[0].message });
  }

  res.send("User registered with Joi!");
});
```

---

### 🔹 Use Cases for Joi:

* Great for reusable, central schemas (e.g., validation for multiple services)
* You can use `Joi` in services, not just Express middleware

---

## 🆚 express-validator vs Joi

| Feature            | `express-validator`          | `Joi`                       |
| ------------------ | ---------------------------- | --------------------------- |
| Middleware style   | ✅ Built for Express          | ❌ Must wrap manually        |
| Schema-based       | ❌ No                         | ✅ Yes (centralized schemas) |
| Async validations  | ✅ (e.g. check DB uniqueness) | ✅                           |
| TypeScript support | Average                      | ✅ Strong with `zod` too     |

---

## ✅ **File Uploads in Express.js using `multer`**

---

### 🔹 What is `multer`?

`multer` is a middleware for handling `multipart/form-data`, which is **primarily used for uploading files** (images, PDFs, etc.) via forms or APIs.

---

### 📦 Install:

```bash
npm install multer
```

---

## 🧪 1. **Basic Usage – Uploading a Single File**

```js
const express = require("express");
const multer = require("multer");
const app = express();

// Set destination and filename
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "uploads/"); // folder must exist
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + "-" + file.originalname); // unique filename
  },
});

const upload = multer({ storage });

// Endpoint to upload a file
app.post("/upload", upload.single("file"), (req, res) => {
  res.json({
    message: "File uploaded successfully!",
    file: req.file,
  });
});
```

#### 🧾 Form Field Example:

```html
<input type="file" name="file" />
```

---

## 🧪 2. **Uploading Multiple Files**

```js
app.post("/multi", upload.array("photos", 5), (req, res) => {
  res.json({
    message: "Multiple files uploaded!",
    files: req.files,
  });
});
```

---

## 🛡️ 3. **File Type and Size Validation**

```js
const fileFilter = (req, file, cb) => {
  if (file.mimetype.startsWith("image/")) {
    cb(null, true);
  } else {
    cb(new Error("Only image files are allowed!"), false);
  }
};

const uploadWithFilter = multer({
  storage,
  limits: { fileSize: 2 * 1024 * 1024 }, // 2 MB
  fileFilter,
});
```

---

## 🧠 4. **Access Uploaded Files**

* Access file info: `req.file` or `req.files`
* You can move, rename, or store metadata in a database
* Uploads are saved in the `uploads/` directory by default (you can change this to S3 or other services)

---

## 📦 Folder Setup Tip:

Make sure the folder (e.g. `uploads/`) exists before running the server or use:

```js
import fs from "fs";
if (!fs.existsSync("uploads")) fs.mkdirSync("uploads");
```

---

### ✅ Summary

| Feature            | Example                       |
| ------------------ | ----------------------------- |
| Single file upload | `upload.single("file")`       |
| Multiple files     | `upload.array("photos", 5)`   |
| Custom file names  | With `multer.diskStorage()`   |
| Type & size check  | `fileFilter`, `limits` option |

---

## ✅ **Logging in Express with `winston` or `pino`**

Logging is critical for:

* Debugging issues
* Monitoring your application
* Keeping audit trails for security & performance

---

## 🔸 Option 1: `winston` – Feature-rich Logger

---

### 📦 Install:

```bash
npm install winston
```

---

### ✅ Basic Setup:

```js
const winston = require("winston");

const logger = winston.createLogger({
  level: "info", // levels: error, warn, info, http, verbose, debug, silly
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json() // or format.simple()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: "logs/error.log", level: "error" }),
    new winston.transports.File({ filename: "logs/combined.log" }),
  ],
});
```

---

### 🧪 Using `logger` in Express:

```js
app.use((req, res, next) => {
  logger.info(`${req.method} ${req.url}`);
  next();
});

// In error handler
app.use((err, req, res, next) => {
  logger.error(err.message);
  res.status(500).send("Something broke!");
});
```

---

### ✅ Advanced Features:

* Different log levels (error, warn, info…)
* Save logs to multiple files
* Use `winston-daily-rotate-file` to rotate logs daily
* Support for custom transports like cloud logging (e.g. AWS CloudWatch, Loggly)

---

## 🔸 Option 2: `pino` – Super Fast Logger

---

### 📦 Install:

```bash
npm install pino
```

### ✅ Basic Usage:

```js
const pino = require("pino");
const logger = pino({ level: "info" });

logger.info("Server started");
logger.error("Something went wrong");
```

---

### 🔧 With Express Middleware:

```bash
npm install pino-http
```

```js
const pino = require("pino-http")();

app.use(pino); // Logs HTTP req/res

app.get("/", (req, res) => {
  req.log.info("Handling GET /");
  res.send("Pino logging active!");
});
```

---

### ✅ pino vs winston

| Feature     | `winston`                        | `pino`                          |
| ----------- | -------------------------------- | ------------------------------- |
| Performance | Slower but flexible              | 🚀 Super fast                   |
| Format      | Highly customizable (JSON, text) | JSON only (by default)          |
| Use case    | Full-featured enterprise logs    | High-performance logs           |
| Middleware  | Custom or manual setup           | Built-in `pino-http` middleware |

---

## ✅ Summary

| Use Case                 | Recommended Logger |
| ------------------------ | ------------------ |
| Feature-rich logging     | `winston`          |
| High-performance logging | `pino`             |
| Production-ready logs    | Both are great     |

---

## ✅ **Debugging in Express.js using the `debug` package**

---

### 🔹 What is `debug`?

The `debug` package is a **lightweight logging utility** that lets you control console output via **namespaces** — perfect for enabling or disabling debug logs **without deleting them**.

---

### 📦 Install:

```bash
npm install debug
```

---

### ✅ Basic Setup in Your App

```js
// myapp.js
const debug = require("debug")("app"); // Namespace = "app"

debug("This is a debug message");
```

---

### 🧪 Run with Debugging Enabled

Run your app with this env variable:

**Windows (CMD/PowerShell):**

```bash
set DEBUG=app && node myapp.js
```

**Linux/macOS (bash):**

```bash
DEBUG=app node myapp.js
```

✅ You'll see:

```
app This is a debug message +0ms
```

❌ Without `DEBUG=app`, nothing will be printed!

---

## 🧠 Best Practice: Use Namespaces

Use different namespaces for different parts of your app:

```js
const debugStartup = require("debug")("app:startup");
const debugDB = require("debug")("app:db");

debugStartup("Starting the app...");
debugDB("Connecting to the database...");
```

Then selectively enable:

```bash
DEBUG=app:startup node index.js
# or
DEBUG=app:* node index.js
```

---

## 📦 Real-World Usage in Express

```js
const express = require("express");
const debug = require("debug")("app:route");
const app = express();

app.get("/", (req, res) => {
  debug("GET / route accessed");
  res.send("Hello, Debug!");
});
```

You can leave debug logs throughout your app and only enable them during development or when troubleshooting.

---

## ✅ Summary

| Feature                 | Description                                |
| ----------------------- | ------------------------------------------ |
| Lightweight logging     | Controlled by env variable `DEBUG`         |
| Namespaces              | Organize logs (e.g. `app:db`, `app:route`) |
| Toggle without deleting | Don't remove `console.log`s — just disable |
| Best for development    | Not meant for production logging           |

---