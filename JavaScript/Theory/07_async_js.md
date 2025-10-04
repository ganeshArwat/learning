## Synchronous vs Asynchronous JavaScript

### Synchronous vs Asynchronous JavaScript

#### JavaScript operates in a single-threaded environment, meaning it executes code line by line in a sequence. However, to handle time-consuming tasks like fetching data from an API or reading a file, JavaScript provides asynchronous programming to avoid blocking execution.

### 1️⃣ Synchronous JavaScript (Sync)

- Code executes sequentially from top to bottom.
- Each operation blocks the next until it completes.
- If a task takes a long time (e.g., fetching data), it halts execution.

```js
console.log("Step 1");
console.log("Step 2");
console.log("Step 3");

// Output:
// Step 1,
// Step 2,
// Step 3
```

### 2️⃣ Asynchronous JavaScript (Async)

- Code does not block execution; instead, tasks can run in the background.
- JavaScript handles async operations using:
  - Callbacks
  - Promises
  - Async/Await
- Useful for API calls, file reading, setTimeout, setInterval, database queries, etc.

```js
console.log("Step 1");

setTimeout(() => {
  console.log("Step 2 (delayed)");
}, 2000);

console.log("Step 3");
```

```
Step 1
Step 3
Step 2 (delayed)
```

- setTimeout() executes after 2 seconds, but Step 3 executes immediately because JavaScript doesn’t wait for setTimeout() to finish.

```js
let a = true;
console.log("Before: ", a);

setTimeout(() => {
  a = false;
  console.log("I will broke the while loop: ", a);
}, 1000);

// wait for 2sec in series operation.
// let timeFuture = Date.now() + 2000;
// while(Date.now() < timeFuture){}
console.log("After: ", a);

// This is a infinite loop, Which never ends because series operation have higher periority as per the event loop.
while (a) {
  console.log("while");
}
```

```js
console.log("Before");
const cb2 = () => {
  console.log("set timeout 1");
  let timeInfuture = Date.now() + 5000;

  console.log("Before while loop: ", Date.now());

  // Wait for 5 sec.
  while (Date.now() < timeInfuture) {}

  console.log("After while loop: ", Date.now());
};

const cb1 = () => {
  console.log("hello");
  console.log("After cb2: ", Date.now());
};

console.log("Start Time: ", Date.now());
setTimeout(cb2, 1000);

setTimeout(cb1, 2000);

console.log("After");
```

```
Before
Start Time:  1741935640197
After
set timeout 1
Before while loop:  1741935641202
After while loop:  1741935646202
hello
After cb2:  1741935646203
```

## How async Code Execution works in js

- JavaScript uses the Event Loop and Web APIs to manage async operations.

1. Call Stack → Executes synchronous code first.
2. Web APIs → Sends async tasks (e.g., setTimeout(), fetch()) to the browser's background.
3. Callback Queue / Microtask Queue (faster than Callback Queue used for promises) → Stores completed async tasks.
4. Event Loop → Pushes tasks from the queue back to the Call Stack when it’s empty.

### 🔹 Deep Dive into Event Loop Components

#### 1️⃣ Call Stack (Execution Context)

- Executes synchronous JavaScript code.
- If an operation is async (setTimeout, fetch), it delegates it to the browser’s Web APIs.

#### 2️⃣ Web APIs

- Handles async tasks (e.g., setTimeout, fetch, DOM events).
- Once done, it moves the callback to the Callback Queue.

#### 3️⃣ Callback Queue (Macrotask Queue)

- Stores timers (setTimeout), event listeners, and DOM events.
- The Event Loop moves tasks to the Call Stack once it's empty.

#### 4️⃣ Microtask Queue

- Stores Promises (.then() & async/await) and MutationObservers.
- Executes before the Callback Queue.

#### 🔹 Execution Priority Order

- 1️⃣ Synchronous Code (Call Stack first).
- 2️⃣ Microtasks (Promise .then(), async/await).
- 3️⃣ Macrotasks (setTimeout, setInterval, I/O tasks).

#### 🔹 Example: Microtasks vs Macrotasks

```js
console.log("Start");

setTimeout(() => console.log("setTimeout"), 0);

Promise.resolve().then(() => console.log("Promise 1"));
Promise.resolve().then(() => console.log("Promise 2"));

console.log("End");
```

- Execution Flow

  - 1️⃣ "Start" → Prints
  - 2️⃣ setTimeout() → Sent to Web APIs
  - 3️⃣ Promise 1 → Sent to Microtask Queue
  - 4️⃣ Promise 2 → Sent to Microtask Queue
  - 5️⃣ "End" → Prints
  - 6️⃣ Microtasks execute first: "Promise 1" → "Promise 2"
  - 7️⃣ Macrotask (setTimeout) executes last.

- Final Output

```
Start
End
Promise 1
Promise 2
setTimeout
```

## Callbacks

- A callback function is a function that is passed as an argument to another function and is executed later, usually after some operation is completed.

### Why Use Callbacks?

- JavaScript is asynchronous, meaning it executes code line by line but does not always wait for one task to finish before moving to the next. Callbacks allow functions to run after other functions have completed, preventing blocking.

### Example 1: Simple Callback Function

```js
function greet(name, callback) {
  console.log("Hello, " + name);
  callback();
}

function sayGoodbye() {
  console.log("Goodbye!");
}

greet("Ganesh", sayGoodbye);
```

```
Hello, Ganesh
Goodbye!
```

### Example 2: Callback in Asynchronous Code

```js
function fetchData(callback) {
  setTimeout(() => {
    console.log("Data fetched!");
    callback();
  }, 2000);
}

function processData() {
  console.log("Processing data...");
}

fetchData(processData);
```

- Output (after 2 seconds delay):
- Since fetchData uses setTimeout, it simulates an asynchronous operation (like an API call), and processData runs only after fetching is done.

```
Data fetched!
Processing data...
```

### Example 3: Callback with Parameters

```js
function calculate(a, b, callback) {
  let result = callback(a, b);
  console.log("Result:", result);
}

function add(x, y) {
  return x + y;
}

function multiply(x, y) {
  return x * y;
}

calculate(5, 3, add); // Output: Result: 8
calculate(5, 3, multiply); // Output: Result: 15
```

### Problems with Callbacks: Callback Hell

- When multiple nested callbacks are used, the code becomes hard to read and maintain. This is known as callback hell.

```js
function step1(data, callback) {
  setTimeout(() => {
    console.log("Step 1:", data);
    callback("Data from Step 1");
  }, 1000);
}

function step2(data, callback) {
  setTimeout(() => {
    console.log("Step 2:", data);
    callback("Data from Step 2");
  }, 1000);
}

function step3(data, callback) {
  setTimeout(() => {
    console.log("Step 3:", data);
  }, 1000);
}

// Nested callbacks (Callback Hell)
step1("Start", (result1) => {
  step2(result1, (result2) => {
    step3(result2, () => {
      console.log("All steps completed!");
    });
  });
});
```

## Parallel Vs Serial

- When dealing with asynchronous operations, tasks can be executed in parallel or serially (sequentially). Understanding these execution styles is crucial for optimizing performance in JavaScript.

### 1. Serial Execution (One after Another)

- Tasks are executed one at a time, in a sequence.
- Each task waits for the previous one to finish before starting.
- Used when tasks depend on each other or order is important.
- Slower since tasks are completed one after another.

- Example of Serial Execution using Callbacks

```js
function task1(callback) {
  setTimeout(() => {
    console.log("Task 1 completed");
    callback();
  }, 2000);
}

function task2(callback) {
  setTimeout(() => {
    console.log("Task 2 completed");
    callback();
  }, 2000);
}

function task3(callback) {
  setTimeout(() => {
    console.log("Task 3 completed");
  }, 2000);
}

// Serial execution: Each task runs only after the previous one finishes.
task1(() => {
  task2(() => {
    task3();
  });
});
```

- Output (6 seconds total execution time):
- Here, each task waits for the previous one, leading to a total execution time of 6 seconds.

```
Task 1 completed (after 2 sec)
Task 2 completed (after 4 sec)
Task 3 completed (after 6 sec)
```

### 2. Parallel Execution (All at Once)

- Tasks run simultaneously without waiting for each other.
- Faster because all tasks execute at the same time.
- Used when tasks are independent and do not depend on each other.

- Example of Parallel Execution using Promise.all()

```js
function task1() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Task 1 completed");
      resolve();
    }, 2000);
  });
}

function task2() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Task 2 completed");
      resolve();
    }, 2000);
  });
}

function task3() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Task 3 completed");
      resolve();
    }, 2000);
  });
}

// Parallel execution using Promise.all()
Promise.all([task1(), task2(), task3()]).then(() => {
  console.log("All tasks completed in parallel!");
});
```

- Output (2 seconds total execution time):
- Here, all tasks start together and complete in 2 seconds instead of 6!

```
Task 1 completed (after 2 sec)
Task 2 completed (after 2 sec)
Task 3 completed (after 2 sec)
All tasks completed in parallel!
```

### When to Use What?

- ✅ Use Serial Execution if:

  - Tasks depend on each other.
  - Order of execution matters.
  - You are processing data step-by-step (e.g., database transactions).

- ✅ Use Parallel Execution if:

  - Tasks are independent.
  - You want to improve performance.
  - You are making multiple API calls or processing multiple files.

## fs module

### 1️⃣ Synchronous File Read (fs.readFileSync)

- Blocks the execution until the file is fully read.
- Used when you need data before proceeding with other tasks.
- Not recommended for large files in production environments.

```js
const fs = require("fs");

console.log("Start Reading File");

try {
  const data = fs.readFileSync("file.txt", "utf8");
  console.log("File Data:", data);
} catch (err) {
  console.error("Error reading file:", err);
}

console.log("End Reading File");
```

```
Start Reading File
File Data: Hello, this is a file.
End Reading File
```

### 2️⃣ Asynchronous File Read (fs.readFile)

- Non-blocking, execution continues while the file is being read.
- Uses a callback function to handle the file data.
- Recommended for I/O-intensive applications.

```js
const fs = require("fs");

console.log("Start Reading File");

fs.readFile("file.txt", "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }
  console.log("File Data:", data);
});

console.log("End Reading File");
```

```
Start Reading File
End Reading File
File Data: Hello, this is a file.
```

### 3️⃣ Using Promises (fs.promises.readFile)

- Modern alternative to callbacks.
- Works well with async/await.

```js
const fs = require("fs").promises;

async function readFile() {
  console.log("Start Reading File");

  try {
    const data = await fs.readFile("file.txt", "utf8");
    console.log("File Data:", data);
  } catch (err) {
    console.error("Error reading file:", err);
  }

  console.log("End Reading File");
}

readFile();
```

```
Start Reading File
File Data: Hello, this is a file.
End Reading File
```

## ⏳ JavaScript Timers (setTimeout, setInterval, clearTimeout, clearInterval)

#### JavaScript provides timers to execute functions asynchronously after a delay or at regular intervals. These are handled by the event loop in the browser or Node.js.

### 🕒 1️⃣ setTimeout() - Run After a Delay

- Executes a function once after a specified delay.

- 🔹 Syntax

```js
setTimeout(callback, delay);
```

- callback: Function to execute.
- delay: Time in milliseconds (1 sec = 1000 ms).

- Example

```js
console.log("Before setTimeout");

setTimeout(() => {
  console.log("Executed after 2 seconds");
}, 2000); // 2 seconds

console.log("After setTimeout");
```

```
Before setTimeout
After setTimeout
Executed after 2 seconds
```

### 🛑 2️⃣ clearTimeout() - Stop a Timeout

- Cancels a setTimeout before execution.

```js
const timerId = setTimeout(() => {
  console.log("This won't run");
}, 3000);

clearTimeout(timerId); // Cancels setTimeout
console.log("Timeout cleared!");
```

```
Timeout cleared!
```

### 🔄 3️⃣ setInterval() - Run Repeatedly

- Executes a function at fixed intervals.

```js
let count = 0;
const intervalId = setInterval(() => {
  count++;
  console.log(`Interval: ${count}`);
  if (count === 5) clearInterval(intervalId); // Stops after 5 times
}, 1000); // Runs every 1 sec
```

```
Interval: 1
Interval: 2
Interval: 3
Interval: 4
Interval: 5
```

4️⃣ clearInterval() - Stop Repeating

- Cancels a setInterval before it keeps running forever.

```js
const intervalId = setInterval(() => {
  console.log("This will run forever...");
}, 1000);

setTimeout(() => {
  clearInterval(intervalId); // Stops after 3 seconds
  console.log("Interval cleared!");
}, 3000);
```

```
This will run forever...
This will run forever...
This will run forever...
Interval cleared!
```
