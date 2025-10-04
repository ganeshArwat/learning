# JavaScript Memory Leaks: Causes & Prevention 🚀

#### A memory leak occurs when memory that is no longer needed is not released, leading to high memory usage and performance issues. In JavaScript, memory is managed automatically with Garbage Collection (GC), but certain coding patterns prevent GC from freeing memory, causing memory leaks.

## 🚨 Common Causes of Memory Leaks

### 1️⃣ Unused Global Variables & Timers

#### 🔹 Issue: Variables declared globally persist in memory.

```js
function createLeak() {
  globalVar = "I am a leak!"; // Unintended global variable
}
createLeak();
```

#### ✅ Fix: Use let, const, or var inside functions.

```js
function createLeak() {
  let localVar = "No Leak!";
}
```

### 2️⃣ Forgotten Timers & Intervals

#### 🔹 Issue: setInterval() keeps running even if elements are removed.

```js
function startTimer() {
  setInterval(() => {
    console.log("Running...");
  }, 1000);
}
startTimer(); // Never stops!
```

#### ✅ Fix: Use clearInterval().

```js
let timer = setInterval(() => console.log("Running..."), 1000);

setTimeout(() => {
  clearInterval(timer);
  console.log("Timer stopped!");
}, 5000);
```

### 3️⃣ Event Listeners Not Removed

#### 🔹 Issue: Event listeners stay in memory even if elements are removed.

```js
document.getElementById("btn").addEventListener("click", function () {
  console.log("Clicked!");
});
```

#### ✅ Fix: Use .removeEventListener().

```js
const button = document.getElementById("btn");
function handleClick() {
  console.log("Clicked!");
}
button.addEventListener("click", handleClick);

// Later when button is removed
button.removeEventListener("click", handleClick);
```

### 4️⃣ Closures Holding References

#### 🔹 Issue: A closure keeps an unused variable in memory.

```js
function outer() {
  let bigData = new Array(1000000).fill("Leak"); // Large array

  return function inner() {
    console.log(bigData[0]); // Keeps `bigData` in memory
  };
}
const leakyFunction = outer();
```

#### ✅ Fix: Nullify unused references.

```js
let leakyFunction = outer();
leakyFunction = null; // Allows garbage collection
```

### 5️⃣ Detached DOM Elements

#### 🔹 Issue: DOM elements removed from the page but still referenced in JavaScript.

```js
let div = document.getElementById("myDiv");
document.body.removeChild(div); // Still in memory
```

#### ✅ Fix: Set references to null

```js
div = null;
```
