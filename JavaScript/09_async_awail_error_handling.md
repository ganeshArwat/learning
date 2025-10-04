## Async Await

#### async/await is a modern way to handle asynchronous operations in JavaScript, making code cleaner, more readable, and easier to debug.

### Why async/await?

- ✅ Avoids Callback Hell (Pyramid of Doom)
- ✅ Easier to read and write than Promises
- ✅ Error handling is simpler with try/catch
- ✅ Looks like synchronous code but is async

### Converting a Promise to async/await

- Using Promises (Without async/await)

```js
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => resolve("✅ Data Fetched!"), 2000);
  });
}

fetchData()
  .then((data) => console.log(data))
  .catch((error) => console.log("Error:", error));
```

- Using async/await (Cleaner & Easier)

```js
async function getData() {
  try {
    let data = await fetchData(); // Waits for fetchData() to complete
    console.log(data);
  } catch (error) {
    console.log("Error:", error);
  }
}

getData();
```

- ✔ Looks synchronous but runs asynchronously
- ✔ No more .then() and .catch() chaining

### Understanding async and await

#### async -

- Makes a function return a Promise

#### await -

- Pauses execution until the Promise resolves

```js
async function example() {
  return "Hello, async!";
}

example().then(console.log); // Prints: Hello, async!
```

#### await must be inside an async function

- ❌ This will throw an error:

```js
let data = await fetchData(); // ❌ Syntax Error: await is only valid in async functions
```

- ✅ Fix it by using async

```js
async function fetch() {
  let data = await fetchData();
  console.log(data);
}
fetch();
```

### Handling Multiple Async Calls

- Without async/await (Chaining)

```js
function task1() {
  return new Promise((resolve) =>
    setTimeout(() => resolve("Task 1 Done"), 1000)
  );
}
function task2() {
  return new Promise((resolve) =>
    setTimeout(() => resolve("Task 2 Done"), 2000)
  );
}

task1()
  .then((result) => {
    console.log(result);
    return task2();
  })
  .then((result) => console.log(result));
```

- With async/await (Sequential Execution)

```js
async function runTasks() {
  let res1 = await task1();
  console.log(res1);

  let res2 = await task2();
  console.log(res2);
}

runTasks();
```

### Running Multiple Promises in Parallel

- Sequential Execution (Slow)

```js
async function run() {
  let a = await task1(); // Waits 1 sec
  let b = await task2(); // Waits 2 sec
  console.log(a, b);
}

run(); // Takes 3 sec
```

- Parallel Execution with Promise.all()

```js
async function runParallel() {
  let [a, b] = await Promise.all([task1(), task2()]);
  console.log(a, b);
}

runParallel(); // Runs in 2 sec (faster)
```

- ✔ Executes in parallel instead of waiting
- ✔ Improves performance

### Handling Errors with try/catch

- Error Handling with Promises

```js
fetchData()
  .then((data) => console.log(data))
  .catch((error) => console.log("Error:", error));
```

- Error Handling with async/await (Cleaner)

```js
async function getData() {
  try {
    let data = await fetchData();
    console.log(data);
  } catch (error) {
    console.log("Error:", error);
  }
}

getData();
```

## JavaScript Event Loop & Async Generators

- how JavaScript handles asynchronous operations internally

  - 1️⃣ Event Loop – How JavaScript manages async tasks
  - 2️⃣ Microtasks vs. Macrotasks – Execution order of async code
  - 3️⃣ Async Generators – Generating async data step by step

### 1. JavaScript Event Loop (How JS Handles Async Code)

- JavaScript is single-threaded, meaning it executes one task at a time in the Call Stack.
- 👉 But how does it handle async operations?

- 🛠 The Event Loop Steps:
- 1️⃣ Executes synchronous code first
- 2️⃣ Moves async operations (setTimeout, fetch, promises) to the Web APIs
- 3️⃣ After the call stack is empty, the Event Loop checks the task queue
- 4️⃣ It processes Microtask (Promise .then(), async/await) first, then Macrotasks (setTimeout, setInterval, I/O tasks)

### 2. Microtasks vs. Macrotasks (Execution Order)

```js
console.log("1️⃣ Start");

// Microtask (Promises)
Promise.resolve().then(() => console.log("2️⃣ Promise resolved"));

// Macrotask (setTimeout)
setTimeout(() => console.log("3️⃣ setTimeout executed"), 0);

console.log("4️⃣ End");
```

- 🔹 Execution Order:

  - ✅ 1️⃣ "Start" (Synchronous)
  - ✅ 4️⃣ "End" (Synchronous)
  - ✅ 2️⃣ "Promise resolved" (Microtask)
  - ✅ 3️⃣ "setTimeout executed" (Macrotask)

- Microtasks (Promises) always execute before Macrotasks (setTimeout, setInterval).

### 3. Async Generators (Yielding Async Data)

- Normal generators (function\*) yield values step by step.
- Async Generators (async function\*) work similarly but return Promises.

```js
function* normalGenerator() {
  yield "Hello";
  yield "World";
}

const gen = normalGenerator();
console.log(gen.next().value); // "Hello"
console.log(gen.next().value); // "World"
```

- Async Generator (Handles Async Data)

```js
async function* asyncGenerator() {
  yield await new Promise((resolve) =>
    setTimeout(() => resolve("Async Hello"), 1000)
  );
  yield await new Promise((resolve) =>
    setTimeout(() => resolve("Async World"), 1000)
  );
}

(async () => {
  for await (let value of asyncGenerator()) {
    console.log(value);
  }
})();

// Async Hello
// Async World
```

- ✔ Handles async data streaming
- ✔ Great for reading large files, API responses, real-time data

## Set Timeout Polyfill

```js
function customSetTimeout(callback, delay) {
  let start = Date.now(); // Current time

  function checkTime() {
    if (Date.now() - start >= delay) {
      callback(); // Call the function after delay
    } else {
      requestAnimationFrame(checkTime); // Check again
    }
  }

  requestAnimationFrame(checkTime);
}

// Usage:
console.log("Before");
customSetTimeout(() => console.log("Executed after 2 sec"), 2000);
console.log("After");
```

## Polyfills of Set Interval

```js
function mySetInterval(cb, delay) {
  let timerIdObject = {
    flag: true,
  };

  function helperMethod() {
    if (timerIdObject.flag) {
      cb();
      setTimeout(helperMethod, delay);
    }
  }

  setTimeout(helperMethod, delay);
  return timerIdObject;
}

function clearMyInterval(timerIdObject) {
  timerIdObject.flag = false;
}

/*******usage****/
function cb() {
  console.log("I will be called on every interval: " + Date.now());
}

let timerIdObject = mySetInterval(cb, 1000);

function cancelInterval() {
  console.timeEnd();
  console.log("cancelled th cb");
  clearMyInterval(timerIdObject);
}

console.time();
setTimeout(cancelInterval, 5000);

console.log("After");
```

## 1. Types of Errors in JavaScript

### 1️⃣ Syntax Errors (Parsing Errors)

#### Occurs when JavaScript fails to interpret code.

```js
console.log("Hello";  // ❌ Missing closing parenthesis
```

### 2️⃣ Reference Errors

- Occurs when trying to access a variable that is not defined.
- Ensure the variable is declared before use.

```js
console.log(x); // ❌ ReferenceError: x is not defined
```

### 3️⃣ Type Errors

- Occurs when an operation is performed on an incompatible type.
- Ensure correct data types for operations.

```js
let num = 10;
num(); // ❌ TypeError: num is not a function
```

### 4️⃣ Range Errors

- Occurs when a value is outside the allowed range.
- Ensure values are within valid ranges.

```js
let arr = new Array(-5); // ❌ RangeError: Invalid array length
```

## Error handling

### Error Handling Using try...catch

- We use try...catch to gracefully handle errors and prevent program crashes.

```js
try {
  let result = x + 10; // ❌ x is not defined
} catch (error) {
  console.log("An error occurred:", error.message);
}
```

### finally Block (Always Runs)

- finally runs whether an error occurs or not.
- Ensures cleanup (e.g., closing connections)

```js
try {
  let result = 5 / 0; // ❌ Potential division by zero
  console.log(result);
} catch (error) {
  console.log("Error:", error.message);
} finally {
  console.log("Execution completed ✅");
}
```

### Throwing Custom Errors

- You can manually throw errors using throw.

```js
function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero!");
  }
  return a / b;
}

try {
  console.log(divide(10, 0));
} catch (error) {
  console.log("Error:", error.message);
}
```

## Handling Errors in Async Code

```js
console.log("Before");
try {
  setTimeout(() => {
    console.log("set timeout is executed");
    console.log(a);
  }, 1000);
} catch (err) {
  console.log("Ganesh_message_of_error: ", err.message);
  console.log("Ganesh_name_of_error: ", err.name);
}
console.log("After");
```

```
Before
After
set timeout is executed
ReferenceError: a is not defined
```

```js
console.log("Before");
setTimeout(() => {
  try {
    console.log("set timeout is executed");
    console.log(a);
  } catch (err) {
    console.log("Error Handled");
    console.log("message: ", err.message);
    console.log("name of error: ", err.name);
  }
}, 1000);

console.log("After try catch");
```

```
Before
After try catch
set timeout is executed
Error Handled
message:  a is not defined
name of error:  ReferenceError
```