# Node.js Fundamentals

## ✅ 1. What is Node.js?

**🔹 Definition:**
Node.js is a **JavaScript runtime** built on Chrome's V8 engine that allows you to run JavaScript **outside the browser**, typically on the server.

**🔹 Key Features:**

* **Asynchronous & Event-Driven:** Non-blocking I/O operations using callbacks and events.
* **Single-threaded** but handles concurrency via the **event loop**.
* Built-in support for **modules** and **package management** (`npm`).
* Perfect for building **fast, scalable network applications** (e.g., APIs, chat apps, streaming servers).

**🔹 Use Cases:**

* RESTful APIs and backend services (e.g., MERN stack)
* Real-time applications (e.g., chat, gaming with WebSockets)
* CLI tools (e.g., npm, webpack)
* Streaming services (e.g., audio/video)
* Server-side rendering (e.g., with frameworks like Next.js)

**🔹 Event-driven architecture:**
Instead of traditional multi-threading, Node.js uses an **event loop** that listens for events (e.g., file read complete, HTTP request) and triggers callback functions. This makes Node.js highly efficient for **I/O-heavy tasks**.

---

## ✅ 2. Installing Node.js and Running JavaScript Files

### 🔹 Installing Node.js:

You can install Node.js from the official website:
👉 [https://nodejs.org](https://nodejs.org)

Choose the **LTS (Long-Term Support)** version for stability.

After installation, verify using your terminal:

```bash
node -v      # To check Node.js version
npm -v       # To check npm (Node Package Manager) version
```

---

### 🔹 Running JavaScript Files with Node.js:

1. **Create a JS file**:
   Example: `app.js`

```js
console.log("Hello from Node.js!");
```

2. **Run the file in terminal**:

```bash
node app.js
```

✅ Output:

```
Hello from Node.js!
```

---

### 🔹 REPL Mode (Read-Eval-Print Loop):

You can also run Node.js interactively:

```bash
node
```

Then type:

```js
> 2 + 2
4
> console.log("Node is running!")
Node is running!
```

Exit REPL by pressing:

```
Ctrl + C twice
```

---

## ✅ 3. Understanding the Event Loop in Node.js

### 🔹 What is the Event Loop?

The **event loop** is the core mechanism in Node.js that handles **asynchronous operations** like file I/O, timers, or HTTP requests — **without blocking** the main thread.

Node.js uses a **single-threaded** event loop to manage multiple concurrent operations efficiently.

---

### 🔹 Key Concept:

Even though Node.js is single-threaded, it can handle **many I/O tasks at once** via the event loop and **callback functions**.

---

### 🔹 How It Works (Phases of the Event Loop):

1. **Timers** → Executes `setTimeout()` and `setInterval()` callbacks.
2. **Pending Callbacks** → Executes I/O callbacks that were deferred.
3. **Idle / Prepare** → Internal phase.
4. **Poll** → Fetches new I/O events; executes I/O callbacks.
5. **Check** → Executes `setImmediate()` callbacks.
6. **Close Callbacks** → Handles things like `socket.on('close')`.

---

### 🔹 Example:

```js
console.log("Start");

setTimeout(() => {
  console.log("Inside setTimeout");
}, 0);

Promise.resolve().then(() => {
  console.log("Inside Promise");
});

console.log("End");
```

**Output:**

```
Start
End
Inside Promise
Inside setTimeout
```

> ✅ Microtasks (Promises) are prioritized over macrotasks (`setTimeout`).

---

### 🔹 Real-Life Analogy:

Imagine a chef (Node.js) taking orders (callbacks). While waiting for one dish (I/O) to cook, the chef takes and prepares other orders. He checks if anything is ready (event loop), and once a dish is done, he serves it (executes callback).

---

## ✅ 4. Global Objects in Node.js

Node.js provides several **global objects** that are accessible in any module — without requiring an `import`.

---

### 🔹 `__dirname`

Represents the **absolute path** of the directory containing the currently executing file.

```js
console.log(__dirname);
```

📌 Output:

```
/Users/ganesh/project-folder
```

---

### 🔹 `__filename`

Represents the **absolute path** of the current file.

```js
console.log(__filename);
```

📌 Output:

```
/Users/ganesh/project-folder/app.js
```

---

### 🔹 `process`

The `process` object provides information and control over the current Node.js process.

**Useful properties and methods:**

```js
console.log(process.pid);           // Process ID
console.log(process.platform);      // e.g., 'win32' or 'linux'
console.log(process.cwd());         // Current working directory
console.log(process.env);           // Environment variables (as an object)
```

**Example: Exit the process manually:**

```js
if (someConditionFails) {
  console.error("Exiting process...");
  process.exit(1); // Exit with failure code
}
```

---

### 🔹 Bonus: `process.argv`

Used to access command-line arguments passed to a Node.js script.

```js
// node script.js hello world
console.log(process.argv);
```

📌 Output:

```
[
  '/usr/local/bin/node',
  '/path/to/script.js',
  'hello',
  'world'
]
```

You can access arguments using `process.argv[2]`, `process.argv[3]`, etc.

---

🧠 Summary:

| Global         | Meaning                             |
| -------------- | ----------------------------------- |
| `__dirname`    | Directory path of the current file  |
| `__filename`   | File path of the current file       |
| `process`      | Info/control of the running process |
| `process.argv` | Command-line args                   |

---

## ✅ 5. `npm`, `npx`, `package.json`, and Scripts

These are essential tools in Node.js for **managing packages** and **project metadata**.

---

### 🔹 `npm` (Node Package Manager)

`npm` is the default package manager for Node.js used to:

* Install packages (dependencies)
* Manage versioning
* Run scripts
* Publish your own packages (if needed)

#### ✅ Commands:

```bash
npm init          # Initialize a new Node.js project (interactive)
npm init -y       # Auto-generate package.json with default values
```

```bash
npm install express         # Install express as a dependency
npm install nodemon --save-dev   # Install as dev dependency
```

```bash
npm uninstall package-name  # Remove a package
```

```bash
npm list         # Show installed packages
npm outdated     # Show outdated packages
npm update       # Update packages
```

---

### 🔹 `npx` (Node Package Execute)

`npx` runs a package without installing it globally.

#### ✅ Example:

```bash
npx create-react-app my-app
```

👉 This runs the `create-react-app` package *without installing it permanently*.

Another use case:

```bash
npx nodemon index.js
```

If `nodemon` is installed locally, `npx` will still find and run it.

---

### 🔹 `package.json`

This file holds **project metadata** and **dependency info**.

#### ✅ Example:

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.2"
  }
}
```

---

### 🔹 Scripts

You can define **custom commands** under `"scripts"` in `package.json`.

```json
"scripts": {
  "start": "node index.js",
  "dev": "nodemon index.js"
}
```

Then run:

```bash
npm run start     # Runs: node index.js
npm run dev       # Runs: nodemon index.js
```

---

✅ Summary:

| Tool           | Purpose                                             |
| -------------- | --------------------------------------------------- |
| `npm`          | Install, manage packages                            |
| `npx`          | Run packages temporarily (no global install needed) |
| `package.json` | Metadata and dependency list                        |
| Scripts        | Define custom commands to simplify workflows        |

---

## ✅ **Synchronous vs Asynchronous Programming in Node.js**

Node.js is built on **non-blocking asynchronous I/O**, which is what makes it fast and scalable.

---

### 🔹 What is Synchronous Code?

* Executes **line-by-line**.
* Each operation **waits** for the previous one to complete.
* **Blocking** in nature.

```js
const fs = require("fs");

const data = fs.readFileSync("file.txt", "utf-8");
console.log("File content:", data);
console.log("This line waits for file reading to finish.");
```

⏳ This blocks the program until the file is fully read.

---

### 🔹 What is Asynchronous Code?

* Does **not wait** for the previous task to finish.
* Uses **callbacks**, **promises**, or **async/await**.
* **Non-blocking**.

```js
fs.readFile("file.txt", "utf-8", (err, data) => {
  console.log("File content:", data);
});

console.log("This line runs while file is being read.");
```

✅ Output:

```
This line runs while file is being read.
File content: ...
```

---

## 🧠 Real-World Analogy:

> Imagine you're cooking and your phone rings.
>
> * **Synchronous**: You stop cooking, answer the phone, and only then resume cooking.
> * **Asynchronous**: You give your friend the phone, say "Tell me if it's important," and keep cooking. 😎

---

## 🛠 Node.js is Asynchronous by Default

Many built-in modules like `fs`, `http`, `net`, `stream`, etc., provide **non-blocking async versions**.

```js
fs.writeFile("log.txt", "Hello Node!", (err) => {
  if (err) console.log("Error:", err);
  else console.log("File written successfully.");
});
```

---

## 📌 When to Use Sync vs Async?

| Use Sync         | Use Async                    |
| ---------------- | ---------------------------- |
| During startup   | When handling user requests  |
| One-time configs | File/database/network access |
| CLI tools        | Web servers & APIs           |

---

### ⛔ Avoid Synchronous Code in Servers

```js
// Bad: Blocking I/O
const user = fs.readFileSync("user.json", "utf-8");
```

```js
// Good: Async
fs.readFile("user.json", "utf-8", (err, data) => {
  if (data) {
    console.log("User:", JSON.parse(data));
  }
});
```

---

### ✅ Summary:

| Concept      | Description                   |
| ------------ | ----------------------------- |
| Synchronous  | Blocks execution line by line |
| Asynchronous | Non-blocking, efficient I/O   |
| Node.js      | Favors async for performance  |

---

## ✅ **Streams in Node.js**

> Streams allow **efficient reading/writing of data** in chunks (not all at once).

Perfect for:

* Reading **large files**
* **Video/audio** streaming
* **Network** communication
* **Piping** data between sources

---

### 🔹 Types of Streams

| Stream Type   | Description                                       |
| ------------- | ------------------------------------------------- |
| **Readable**  | Can read data from (e.g. `fs.createReadStream`)   |
| **Writable**  | Can write data to (e.g. `fs.createWriteStream`)   |
| **Duplex**    | Both readable and writable (e.g. TCP sockets)     |
| **Transform** | Duplex + modifies data (e.g. `zlib.createGzip()`) |

---

## 🧪 Basic Example: Read file using a stream

```js
const fs = require("fs");

const readStream = fs.createReadStream("bigfile.txt", {
  encoding: "utf-8",
  highWaterMark: 16 * 1024, // Optional: set chunk size
});

readStream.on("data", (chunk) => {
  console.log("------ NEW CHUNK ------");
  console.log(chunk);
});

readStream.on("end", () => {
  console.log("Finished reading.");
});
```

> 🔁 This reads the file **piece-by-piece**, not all at once, so it uses **less memory**.

---

## ✍️ Writing to a file using `createWriteStream`

```js
const fs = require("fs");

const writeStream = fs.createWriteStream("output.txt");

writeStream.write("Hello, ");
writeStream.write("this is Ganesh writing via stream.\n");

writeStream.end(() => {
  console.log("Writing done!");
});
```

---

## 🔗 Piping Readable → Writable

You can **pipe** one stream into another:

```js
const fs = require("fs");

const readStream = fs.createReadStream("input.txt");
const writeStream = fs.createWriteStream("copy.txt");

readStream.pipe(writeStream);
```

> ✅ This copies the file content efficiently using streams.

---

### 🔥 Real Use Case: Video Streaming Server

```js
const http = require("http");
const fs = require("fs");

http
  .createServer((req, res) => {
    const stream = fs.createReadStream("video.mp4");
    res.writeHead(200, { "Content-Type": "video/mp4" });
    stream.pipe(res);
  })
  .listen(3000, () => {
    console.log("Streaming server running on port 3000");
  });
```

---

## 🧠 Summary

| Feature    | Description                            |
| ---------- | -------------------------------------- |
| `Readable` | Stream for reading (e.g., file input)  |
| `Writable` | Stream for writing (e.g., file output) |
| `.pipe()`  | Connects readable to writable stream   |
| Efficient  | Handles large data in chunks           |

---

## ✅ **Using `nodemon` for Auto-Restart**

### 🔥 Problem:

Every time you make a change in your code, you have to **stop and restart** the Node server manually.

### 💡 Solution:

Use `nodemon`, a utility that **monitors for file changes** and **automatically restarts** your server.

---

### 📦 Step 1: Install nodemon

```bash
npm install -g nodemon
```

> 🔸 `-g` installs it **globally**, so you can use it in any project.

Or install locally (recommended for production projects):

```bash
npm install --save-dev nodemon
```

---

### 🚀 Step 2: Run your app using nodemon

Instead of:

```bash
node server.js
```

Use:

```bash
nodemon server.js
```

Now every time you **save your file**, the server restarts automatically. ✅

---

### ⚙️ Step 3: Add nodemon to `package.json` scripts

```json
"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js"
}
```

Then run:

```bash
npm run dev
```

---

### 🧠 Optional: Create `nodemon.json` for custom config

```json
{
  "watch": ["server.js"],
  "ext": "js,json",
  "ignore": ["data.json"],
  "exec": "node server.js"
}
```

---

## 🧪 Example in Action

1. Start your API with `nodemon server.js`
2. Make a change in your route handler
3. See the terminal — it auto-restarts the server 🎯

---

## ✅ Summary:

| Tool          | What it does                         |
| ------------- | ------------------------------------ |
| `nodemon`     | Auto-restarts your server on changes |
| `npm run dev` | Script to run nodemon easily         |

---

🎉 That’s the **complete Node.js Fundamentals module** from your MERN Backend index:

* ✅ Node intro
* ✅ Event loop
* ✅ Core globals
* ✅ npm, scripts
* ✅ Built-in modules
* ✅ HTTP server
* ✅ REST API
* ✅ Sync vs Async
* ✅ Promises (you knew)
* ✅ Streams
* ✅ nodemon

---
