
## 🔹 **1. `fs` – File System Module**

The `fs` module allows Node.js to interact with the file system: reading, writing, appending, deleting files and directories.

### ✅ Importing the module:

```js
const fs = require("fs");
```

---

### ✨ Commonly Used Methods:

#### ✅ `writeFileSync()`

Writes data to a file **synchronously** (blocks execution).

```js
fs.writeFileSync("test.txt", "Hello Sync");
```

#### ✅ `writeFile()`

Asynchronous version – uses a callback.

```js
fs.writeFile("test_async.txt", "Hello Async", (err) => {
  if (err) console.error(err);
  else console.log("File written!");
});
```

---

#### ✅ `readFileSync()`

Reads file content synchronously.

```js
const data = fs.readFileSync("test.txt", "utf-8");
console.log(data);
```

#### ✅ `readFile()`

Reads file content asynchronously.

```js
fs.readFile("test_async.txt", "utf-8", (err, data) => {
  if (err) console.error(err);
  else console.log(data);
});
```

---

#### ✅ `appendFile()`

Appends data to the end of a file.

```js
fs.appendFileSync("test.txt", "\nAppended line");
```

---

#### ✅ `unlink()`

Deletes a file.

```js
fs.unlink("test.txt", (err) => {
  if (err) console.error(err);
  else console.log("File deleted");
});
```

---

#### ✅ `mkdir()` & `rmdir()`

To create and delete directories:

```js
fs.mkdirSync("new-folder");
fs.rmdirSync("new-folder");
```

---

### 📁 Example: Simple File Logger

```js
const fs = require("fs");
const logMessage = "User logged in at " + new Date().toLocaleString();

fs.appendFile("log.txt", logMessage + "\n", (err) => {
  if (err) console.error("Log write failed");
  else console.log("Log saved");
});
```

---

### 📌 Summary Table:

| Function                  | Type  | Description                 |
| ------------------------- | ----- | --------------------------- |
| `writeFileSync`           | Sync  | Write to a file (overwrite) |
| `writeFile`               | Async | Write to a file             |
| `readFileSync`            | Sync  | Read file content           |
| `readFile`                | Async | Read file content           |
| `appendFile`              | Async | Add content to file         |
| `unlink`                  | Async | Delete a file               |
| `mkdirSync` / `rmdirSync` | Sync  | Create/Delete folders       |

---

## 🔹 **2. `path` – Path Module**

The `path` module provides utilities for working with **file and directory paths** in a **cross-platform** way (Windows uses `\`, Unix uses `/`).

### ✅ Import the module:

```js
const path = require("path");
```

---

### ✨ Commonly Used Methods:

#### ✅ `path.basename(path)`

Returns the **file name** from a full path.

```js
console.log(path.basename("/users/ganesh/app.js")); // app.js
```

---

#### ✅ `path.dirname(path)`

Returns the **directory name** from a full path.

```js
console.log(path.dirname("/users/ganesh/app.js")); // /users/ganesh
```

---

#### ✅ `path.extname(path)`

Returns the **file extension**.

```js
console.log(path.extname("index.html")); // .html
```

---

#### ✅ `path.join([...paths])`

Joins multiple segments into one **normalized path**.

```js
const fullPath = path.join(__dirname, "views", "index.html");
console.log(fullPath);
// Output: /Users/ganesh/project/views/index.html
```

> ✅ Automatically handles slashes `/` and backslashes `\`

---

#### ✅ `path.resolve([...paths])`

Resolves a full **absolute path** from right to left.

```js
console.log(path.resolve("folder", "subfolder", "file.txt"));
// Output: /current/working/directory/folder/subfolder/file.txt
```

---

#### ✅ `path.parse(path)`

Returns an object with detailed info about the path.

```js
console.log(path.parse("/users/ganesh/app.js"));
```

📌 Output:

```js
{
  root: '/',
  dir: '/users/ganesh',
  base: 'app.js',
  ext: '.js',
  name: 'app'
}
```

---

### ✅ Real Use Case:

When building servers or reading files dynamically, you should always use `path.join()` or `path.resolve()` to construct paths — this prevents OS-specific path bugs.

```js
const fs = require("fs");
const filePath = path.join(__dirname, "data", "hello.txt");

fs.writeFileSync(filePath, "Hello from path module!");
```

---

### 🧠 Summary Table:

| Method       | Description                                |
| ------------ | ------------------------------------------ |
| `basename()` | Get the file name                          |
| `dirname()`  | Get the directory name                     |
| `extname()`  | Get the file extension                     |
| `join()`     | Join path segments cleanly                 |
| `resolve()`  | Resolve absolute path                      |
| `parse()`    | Breaks a path into parts (dir, base, etc.) |

---

## 🔹 **3. `os` – Operating System Module**

The `os` module provides information about the operating system: CPU details, memory usage, platform, user info, etc.

It’s especially useful for writing **platform-aware scripts**, diagnostics, or system monitoring tools.

### ✅ Import the module:

```js
const os = require("os");
```

---

### ✨ Commonly Used Methods:

#### ✅ `os.platform()`

Returns the platform:

```js
console.log(os.platform()); // e.g., 'win32', 'linux', 'darwin'
```

---

#### ✅ `os.arch()`

Returns the CPU architecture:

```js
console.log(os.arch()); // e.g., 'x64'
```

---

#### ✅ `os.cpus()`

Returns information about each CPU core.

```js
console.log(os.cpus().length); // number of CPU cores
console.log(os.cpus()[0]);     // detailed info of one core
```

---

#### ✅ `os.totalmem()` & `os.freemem()`

Memory in **bytes**:

```js
console.log("Total Memory:", os.totalmem());
console.log("Free Memory:", os.freemem());
```

✅ You can convert it to MB or GB for readability:

```js
console.log((os.freemem() / (1024 * 1024)).toFixed(2) + " MB");
```

---

#### ✅ `os.homedir()`

Returns the user's home directory:

```js
console.log(os.homedir());
```

---

#### ✅ `os.hostname()`

Returns the hostname of the machine:

```js
console.log(os.hostname());
```

---

#### ✅ `os.type()` & `os.version()`

OS type and version:

```js
console.log(os.type());     // e.g., 'Linux', 'Windows_NT'
console.log(os.version());  // OS version
```

---

#### ✅ `os.uptime()`

System uptime in seconds:

```js
console.log("Uptime:", os.uptime(), "seconds");
```

---

### 📁 Example: Simple System Info Script

```js
const os = require("os");

console.log("System Info:");
console.log("Platform:", os.platform());
console.log("Architecture:", os.arch());
console.log("CPU Cores:", os.cpus().length);
console.log("Total Memory:", (os.totalmem() / 1024 / 1024).toFixed(2), "MB");
console.log("Free Memory:", (os.freemem() / 1024 / 1024).toFixed(2), "MB");
console.log("Uptime:", os.uptime(), "seconds");
```

---

### 🧠 Summary Table:

| Method       | Description                      |
| ------------ | -------------------------------- |
| `platform()` | OS platform (e.g., win32, linux) |
| `arch()`     | CPU architecture                 |
| `cpus()`     | Info about CPU cores             |
| `totalmem()` | Total system memory              |
| `freemem()`  | Free memory available            |
| `homedir()`  | User's home directory            |
| `uptime()`   | System uptime in seconds         |
| `hostname()` | Name of the device               |

---

## 🔹 **4. `http` – HTTP Module**

The `http` module allows you to **create an HTTP server** in Node.js, which can handle requests and send responses.

This module is the foundation of many web frameworks (like Express), and it's great to understand how it works under the hood.

---

### ✅ Import the module:

```js
const http = require("http");
```

---

### ✅ Create a Basic Server

```js
const http = require("http");

const server = http.createServer((req, res) => {
  res.write("Hello from Node.js Server!");
  res.end(); // Ends the response
});

server.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
```

---

### ✨ Request & Response Objects

#### `req` = Incoming Request

Contains info like:

* `req.url`: the requested URL path
* `req.method`: HTTP method (GET, POST, etc.)
* `req.headers`: headers object

#### `res` = Outgoing Response

You use it to send data to the client:

* `res.write()`: write a response
* `res.end()`: end the response
* `res.setHeader()`: set headers like content-type

---

### ✅ Send HTML Response

```js
const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "text/html");
  res.write("<h1>Welcome to My Server</h1>");
  res.end();
});
```

---

### ✅ Route Handling Example

```js
const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.write("Home Page");
  } else if (req.url === "/about") {
    res.write("About Page");
  } else {
    res.write("404 Not Found");
  }
  res.end();
});
```

---

### ✅ Sending JSON Response

```js
const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "application/json");
  const user = { name: "Ganesh", age: 23 };
  res.end(JSON.stringify(user));
});
```

---

### 📁 Tip: Auto-reload server using `nodemon`

Instead of manually restarting your server every time:

```bash
npx nodemon index.js
```

---

### 🧠 Summary Table:

| Feature             | Description                      |
| ------------------- | -------------------------------- |
| `http.createServer` | Creates a new HTTP server        |
| `req.url`           | Requested path                   |
| `req.method`        | HTTP method                      |
| `res.write()`       | Writes response                  |
| `res.end()`         | Ends response                    |
| `res.setHeader()`   | Sets headers (like Content-Type) |

---

## 🔹 **5. `events` – Events Module**

The `events` module provides a way to handle **custom asynchronous events**.
Node.js itself uses this heavily (like HTTP servers, Streams, etc.).

At the heart of this module is the **`EventEmitter`** class.

---

### ✅ Step 1: Import and Create an Event Emitter

```js
const EventEmitter = require("events");
const emitter = new EventEmitter();
```

---

### ✅ Step 2: Listen for Events using `.on()`

```js
emitter.on("greet", (name) => {
  console.log(`Hello, ${name}`);
});
```

---

### ✅ Step 3: Emit Events using `.emit()`

```js
emitter.emit("greet", "Ganesh");
// Output: Hello, Ganesh
```

---

### ✨ More Useful Methods:

#### ✅ `.once()`

Executes the listener **only once**:

```js
emitter.once("login", () => {
  console.log("User logged in");
});

emitter.emit("login"); // Will trigger
emitter.emit("login"); // Will NOT trigger
```

---

#### ✅ `.removeListener()` / `.off()`

Removes a listener:

```js
const sayHi = () => console.log("Hi!");
emitter.on("hi", sayHi);

emitter.removeListener("hi", sayHi); // OR emitter.off("hi", sayHi);
```

---

### 📁 Real-world Use Case: Custom Logger

```js
const EventEmitter = require("events");

class Logger extends EventEmitter {
  log(message) {
    console.log("LOG:", message);
    this.emit("logged", { message, time: new Date() });
  }
}

const logger = new Logger();

logger.on("logged", (data) => {
  console.log("Event received:", data);
});

logger.log("User created!");
```

---

### 🧠 Summary Table:

| Method               | Description                          |
| -------------------- | ------------------------------------ |
| `.on(event, cb)`     | Register a listener                  |
| `.emit(event, data)` | Emit (trigger) an event              |
| `.once()`            | Register a listener to run only once |
| `.removeListener()`  | Remove a listener                    |

---

Node.js is **event-driven at its core** — this module teaches you how the event loop interacts with custom logic 🔄

---
