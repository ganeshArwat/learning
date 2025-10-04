## heart attack code / callback hell / Pyramid of doom

### Callback Hell (a.k.a. "Heart Attack Code" or "Pyramid of Doom") happens when multiple asynchronous operations depend on each other, leading to deeply nested callbacks. This makes code:

- Hard to read
- Difficult to debug
- Tough to maintain

### Example of Callback Hell

- Imagine you need to fetch user data, then fetch orders, then process payments in sequence.

```js
fs.readFile(".././f1.txt", (err, data) => {
  if (err) {
    console.log("Error is: " + err);
  } else {
    console.log("Content is: " + data);
    fs.readFile(".././f2.txt", (err, data) => {
      if (err) {
        console.log("Error is: " + err);
      } else {
        console.log("Content is: " + data);
        fs.readFile(".././f3.txt", (err, data) => {
          if (err) {
            console.log("Error is: " + err);
          } else {
            console.log("Content is: " + data);
            fs.readFile(".././f4.txt", (err, data) => {
              if (err) {
                console.log("Error is: " + err);
              } else {
                console.log("Content is: " + data);
              }
            });
          }
        });
      }
    });
  }
});
```

```js
function fetchUser(userId, callback) {
  setTimeout(() => {
    console.log("User fetched: ", userId);
    callback(userId);
  }, 1000);
}

function fetchOrders(userId, callback) {
  setTimeout(() => {
    console.log("Orders fetched for user:", userId);
    callback(["order1", "order2"]);
  }, 1000);
}

function processPayment(orderId, callback) {
  setTimeout(() => {
    console.log("Payment processed for:", orderId);
    callback();
  }, 1000);
}

// 😵‍💫 Callback Hell (Pyramid of Doom)
fetchUser(101, (userId) => {
  fetchOrders(userId, (orders) => {
    processPayment(orders[0], () => {
      console.log("Payment completed!");
    });
  });
});
```

```
User fetched: 101
Orders fetched for user: 101
Payment processed for: order1
Payment completed!
```

### ✅ Solution 1: Use Named Functions

- Refactor with separate named functions.

```js
function fetchUser(userId, next) {
  setTimeout(() => {
    console.log("User fetched: ", userId);
    next(userId);
  }, 1000);
}

function fetchOrders(userId, next) {
  setTimeout(() => {
    console.log("Orders fetched for user:", userId);
    next(["order1", "order2"]);
  }, 1000);
}

function processPayment(orderId, next) {
  setTimeout(() => {
    console.log("Payment processed for:", orderId);
    next();
  }, 1000);
}

function completeTransaction() {
  console.log("Payment completed!");
}

// Now, calling functions in sequence
fetchUser(101, (userId) =>
  fetchOrders(userId, (orders) =>
    processPayment(orders[0], completeTransaction)
  )
);
```

```js
const list = [".././f4.txt", ".././f3.txt", ".././f2.txt", ".././f1.txt"];

function recursiveWay(list) {
  if (list.length === 0) {
    return;
  }

  fs.readFile(list.pop(), smallCBfunction);
  function smallCBfunction(err, data) {
    if (err) {
      console.log("Error is: " + err);
    } else {
      console.log("Content is: " + data);
      recursiveWay(list);
    }
  }
}

recursiveWay(list);

console.log("After");
```

## 🔄 Inversion of Control (IoC) in JavaScript

### Inversion of Control (IoC) is a design principle where the control flow of a program is transferred from the caller to another entity, like a framework or function. Instead of writing code that dictates the execution flow, we provide instructions (callbacks, dependency injections, etc.) and let another function or system control the execution.

#### 💡 Simple Example (Without IoC)

- You write code that explicitly controls everything:
- Here, you control the entire proc

```js
function fetchData() {
  console.log("Fetching data...");
  console.log("Processing data...");
  console.log("Displaying data...");
}

fetchData();
```

#### ⚡ Example of IoC (With Callbacks)

- In IoC, you hand over control to another function:

```js
function fetchData(callback) {
  console.log("Fetching data...");
  setTimeout(() => {
    console.log("Data fetched!");
    callback(); // Control transferred to callback
  }, 2000);
}

fetchData(() => {
  console.log("Processing data...");
  console.log("Displaying data...");
});
```

- ✔ fetchData() does not dictate what happens next—it delegates control via callback().

#### 🛠️ IoC in Event Listeners

- Another example is event-driven programming:

```js
document.getElementById("btn").addEventListener("click", function () {
  console.log("Button Clicked!");
});
```

- ✔ The browser decides when to call the event handler (not you).

## 🚨 Why is IoC a Drawback in Callbacks?

### 1️⃣ Loss of Control (Hard to Predict Execution)

#### When using callbacks, you hand over control to another function. But this can make it hard to predict when or how your code will run.

```js
function fetchData(callback) {
  setTimeout(() => {
    console.log("Data fetched!");
    callback(); // IoC: Control is given to callback
  }, 2000);
}

fetchData(() => {
  console.log("Processing data...");
});
```

- 💡 Here, fetchData() decides when to call callback(), not you.

- ❌ Problem: You don’t have control over when the callback executes, which can cause unexpected behaviors.

## Promises

### A Promise is an object in JavaScript that represents the eventual completion (or failure) of an asynchronous operation.

### 🔹 Why Use Promises?

- ✅ Avoid Callback Hell (No Pyramid of Doom)
- ✅ Better Error Handling using .catch()
- ✅ Improves Readability compared to callbacks

### Creating a Promise

- A Promise takes a function with resolve and reject arguments.
- ✔ resolve(value) – If successful, it runs .then(value)
- ✔ reject(error) – If failed, it runs .catch(error)

```js
const myPromise = new Promise((resolve, reject) => {
  let success = true;

  setTimeout(() => {
    if (success) {
      resolve("✅ Promise resolved!");
    } else {
      reject("❌ Promise rejected!");
    }
  }, 2000);
});
```

### Using a Promise

#### You can use .then() and .catch() to handle success and errors.

```js
myPromise
  .then((message) => {
    console.log("Success:", message);
  })
  .catch((error) => {
    console.log("Error:", error);
  });
```

### Promise States

- A Promise can be in one of 3 states:

#### Pending - Initial state (waiting for result)

#### Fulfilled - resolve() was called

#### Rejected - reject() was called

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Done!");
  }, 3000);
});

console.log(promise); // Logs: Promise { <pending> }
```

### Chaining Promises

You can chain multiple .then() calls to avoid nesting.

```js
new Promise((resolve) => {
  setTimeout(() => resolve(10), 1000);
})
  .then((num) => {
    console.log(num); // 10
    return num * 2;
  })
  .then((num) => {
    console.log(num); // 20
    return num * 3;
  })
  .then((num) => {
    console.log(num); // 60
  })
  .catch((error) => {
    console.log("Error:", error);
  });
```

```js
fs.promises
  .readFile("./f1.txt")
  .then(function (data) {
    console.log("My Content is: " + data);
    return fs.promises.readFile("./f2.txt");
  })
  .then(function (data) {
    console.log("My Content is: " + data);
    return fs.promises.readFile("./f13.txt");
  })
  .then(function (data) {
    console.log("My Content is: " + data);
    return fs.promises.readFile("./f4.txt");
  })
  .then(function (data) {
    console.log("My Content is: " + data);
  })
  .catch((err) => {
    console.log("ohh! I hit by error: " + err);
  });
```

### Handling Errors with .catch()

- If an error occurs at any stage, it goes to .catch().

```js
new Promise((resolve, reject) => {
  setTimeout(() => reject("❌ Error occurred!"), 2000);
})
  .then((data) => {
    console.log("Success:", data);
  })
  .catch((error) => {
    console.log("Caught:", error);
  });
```

### Using finally()

finally() always runs, whether the promise is resolved or rejected.

```js
myPromise
  .then((msg) => console.log("Success:", msg))
  .catch((err) => console.log("Error:", err))
  .finally(() => console.log("Operation Completed!"));
```

### Promise.all() – Run Multiple Promises in Parallel

- Promise.all() waits for all promises to complete before resolving.
- ✔ Faster execution since both tasks run simultaneously
- ❌ Fails if any promise is rejected

```js
const p1 = new Promise((resolve) => setTimeout(() => resolve("Task 1"), 2000));
const p2 = new Promise((resolve) => setTimeout(() => resolve("Task 2"), 1000));

Promise.all([p1, p2])
  .then((results) => console.log("All Done:", results))
  .catch((error) => console.log("Error:", error));
```

### 🔹 Promise.race() – Get the First Completed Promise

- Returns the first resolved/rejected promise.

```js
Promise.race([p1, p2]).then((result) => console.log("First Done:", result));
```

## 🚀 How Promises Solve the Inversion of Control Problem?

#### Inversion of Control (IoC) happens when we pass a callback function to another function, giving up control over when and how it gets executed. This can lead to callback hell, unpredictable execution, and difficult error handling.

#### 💡 Promises solve IoC by giving control back to the caller instead of the function handling the async operation.

### 🔴 Problem: IoC in Callbacks

- In callbacks, the async function decides when to call your function, leading to loss of control.
- ❌ Problem:
  - The caller doesn't control when callback() runs.
  - The function (fetchData) decides when to call it.

```js
function fetchData(callback) {
  setTimeout(() => {
    console.log("Fetched Data");
    callback(); // IoC: fetchData controls when callback runs
  }, 2000);
}

fetchData(() => {
  console.log("Processing Data...");
});
```

### ✅ Solution: Promises Restore Control

- With Promises, the caller decides what to do after the async task is complete.

- ✔ fetchData() doesn’t call our function directly
- ✔ The caller decides what happens next using .then()

```js
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Fetched Data");
      resolve(); // Resolving the promise
    }, 2000);
  });
}

fetchData().then(() => {
  console.log("Processing Data...");
});
```
