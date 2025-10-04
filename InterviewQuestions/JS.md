Sure Ganesh! Here's a solid list of **JavaScript interview questions with answers**, focused on **React developer roles** like the one you’re targeting at **TCS**. These questions cover **core JS concepts**, **ES6+ features**, and **real-world use cases**.

---

## ✅ **JavaScript Interview Questions and Answers**

### 1. **What are the different data types in JavaScript?**

**Answer:**

* **Primitive**: `string`, `number`, `boolean`, `undefined`, `null`, `symbol`, `bigint`
* **Non-primitive**: `object`, `array`, `function`

---

### 2. **What is the difference between `var`, `let`, and `const`?**

**Answer:**

| Feature       | `var`           | `let`           | `const`         |
| ------------- | --------------- | --------------- | --------------- |
| Scope         | Function        | Block           | Block           |
| Redeclaration | Allowed         | Not allowed     | Not allowed     |
| Reassignment  | Allowed         | Allowed         | ❌ Not allowed   |
| Hoisting      | Yes (undefined) | Yes (TDZ error) | Yes (TDZ error) |

---

### 3. **What is the difference between `==` and `===`?**

**Answer:**

* `==`: Loose equality (type coercion allowed)
* `===`: Strict equality (no type coercion)

```js
0 == '0'   // true
0 === '0'  // false
```

---

### 4. **What is a closure in JavaScript?**

**Answer:**
A closure is a function that **remembers its outer scope** even after the outer function has finished executing.

```js
function outer() {
  let count = 0;
  return function inner() {
    count++;
    return count;
  }
}
const counter = outer();
counter(); // 1
```

---

### 5. **What is the event loop in JavaScript?**

**Answer:**
The event loop handles async operations. It continuously checks the call stack and task queue. If the call stack is empty, it pushes the next task from the queue into the stack.

---

### 6. **Explain `call()`, `apply()` and `bind()` methods.**

**Answer:**

* `call`: Invokes function with specified `this` and arguments (comma separated)
* `apply`: Same as `call`, but arguments as array
* `bind`: Returns a new function with bound `this`

```js
function greet(city) { console.log(this.name + " from " + city); }
greet.call({ name: "Ganesh" }, "Mumbai");
greet.apply({ name: "Ganesh" }, ["Mumbai"]);
const bound = greet.bind({ name: "Ganesh" }, "Mumbai");
bound();
```

---

### 7. **What is hoisting in JavaScript?**

**Answer:**
Hoisting is JavaScript's behavior of moving declarations to the top of the scope before execution.

```js
console.log(a); // undefined
var a = 10;
```

`let` and `const` are hoisted but not initialized, leading to a **ReferenceError**.

---

### 8. **What is the difference between `null` and `undefined`?**

**Answer:**

| Type        | Meaning                            |
| ----------- | ---------------------------------- |
| `null`      | Intentional absence of value       |
| `undefined` | Variable declared but not assigned |

```js
let x; // undefined
let y = null;
```

---

### 9. **What are arrow functions and how are they different?**

**Answer:**
Arrow functions are a shorter syntax for functions, and they do **not bind their own `this`**.

```js
const add = (a, b) => a + b;
```

They are best used for **non-method functions**, **callbacks**, or **map/filter** operations.

---

### 10. **What is a promise?**

**Answer:**
A Promise is an object representing the eventual completion or failure of an async operation.

```js
let promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("done"), 1000);
});
```

Use `.then()` and `.catch()` or `async/await` to handle.

---

### 11. **What is async/await?**

**Answer:**
`async/await` is syntactic sugar over Promises to handle asynchronous code in a more readable way.

```js
async function fetchData() {
  const res = await fetch(url);
  const data = await res.json();
}
```

---

### 12. **What are template literals?**

**Answer:**
They are backtick `` ` `` strings that support multi-line and expression interpolation.

```js
const name = "Ganesh";
console.log(`Hello, ${name}!`);
```

---

### 13. **What is destructuring in JavaScript?**

**Answer:**
A syntax to unpack values from arrays or properties from objects.

```js
const [a, b] = [1, 2];
const { name, age } = { name: "Ganesh", age: 23 };
```

---

### 14. **What are spread and rest operators?**

**Answer:**

* **Spread (`...`)**: Expands an array/object

```js
const nums = [1, 2, 3];
const copy = [...nums];
```

* **Rest (`...`)**: Gathers remaining elements

```js
function sum(...args) { return args.reduce((a,b) => a+b); }
```

---

### 15. **What is the difference between synchronous and asynchronous code?**

**Answer:**

* **Synchronous**: Code runs in sequence (blocking)
* **Asynchronous**: Code runs in background, allows other tasks to execute (non-blocking)

---

### 16. **Explain the concept of lexical scope.**

**Answer:**
A variable’s scope is determined by its position in the source code. Inner functions have access to variables declared in their outer scope.

---

### 17. **What are pure functions?**

**Answer:**

* Given the same input, always returns the same output.
* No side effects.

```js
function add(a, b) {
  return a + b;
}
```

---

### 18. **What is a higher-order function?**

**Answer:**
A function that either:

* Takes another function as an argument
* Returns a function

```js
function greet(msg) {
  return function(name) {
    return `${msg}, ${name}`;
  };
}
```

---

### 19. **What is the difference between shallow copy and deep copy?**

**Answer:**

* **Shallow copy**: Copies only top-level properties
* **Deep copy**: Copies nested objects/arrays fully

```js
const shallow = [...arr]; // shallow
const deep = JSON.parse(JSON.stringify(obj)); // deep
```

---

### 20. **What is the difference between `map()`, `filter()` and `forEach()`?**

**Answer:**

| Method      | Purpose                       | Returns            |
| ----------- | ----------------------------- | ------------------ |
| `map()`     | Transform each element        | New array          |
| `filter()`  | Keep elements matching a rule | New filtered array |
| `forEach()` | Run logic for each item       | `undefined`        |

---

### 21. **What is the difference between `setTimeout` and `setInterval`?**

**Answer:**

* `setTimeout(fn, ms)` → runs **once** after delay.
* `setInterval(fn, ms)` → runs **repeatedly** every delay.

```js
setTimeout(() => console.log("Once"), 1000);
setInterval(() => console.log("Repeat"), 1000);
```

---

### 22. **What is the Temporal Dead Zone (TDZ)?**

**Answer:**
It's the time between variable hoisting and initialization for `let` and `const`. Accessing variables in TDZ throws a **ReferenceError**.

```js
console.log(x); // ❌ ReferenceError
let x = 10;
```

---

### 23. **What is the difference between `Object.freeze()` and `Object.seal()`?**

**Answer:**

* `freeze()`: Prevents adding, removing, or modifying properties.
* `seal()`: Prevents adding/removing, but allows modification.

---

### 24. **What are falsy values in JavaScript?**

**Answer:**
Values considered `false` in boolean context:
`false`, `0`, `""`, `null`, `undefined`, `NaN`

---

### 25. **What is function currying?**

**Answer:**
Transforming a function that takes multiple arguments into a sequence of functions taking one argument at a time.

```js
function add(a) {
  return function(b) {
    return a + b;
  };
}
add(2)(3); // 5
```

---

### 26. **What is debouncing and throttling?**

**Answer:**

* **Debouncing**: Wait for inactivity before running a function (e.g. typing).
* **Throttling**: Limit function execution to once every interval (e.g. scroll).

---

### 27. **What is the `this` keyword in JavaScript?**

**Answer:**
`this` refers to the context in which a function is called.

* In a method: `this` is the object
* Alone in strict mode: `undefined`
* In event handlers: refers to element
* In arrow functions: `this` is **lexically inherited**

---

### 28. **What are the differences between `Array.map()` and `Array.reduce()`?**

**Answer:**

* `map()`: Returns a new array by transforming each element.
* `reduce()`: Reduces array to a single value using an accumulator.

```js
[1,2,3].map(x => x * 2); // [2,4,6]
[1,2,3].reduce((acc, val) => acc + val, 0); // 6
```

---

### 29. **What is memory leak in JS and how can it happen?**

**Answer:**
Memory leak is unused memory that is not released. Causes include:

* Global variables
* Forgotten timers/intervals
* Detached DOM nodes still referenced
* Closures retaining large scope

---

### 30. **Explain event delegation in JavaScript.**

**Answer:**
Instead of adding listeners to multiple children, delegate one listener to a parent and use `event.target` to act accordingly.

```js
document.getElementById("list").addEventListener("click", function(e) {
  if (e.target.tagName === "LI") {
    console.log("List item clicked:", e.target.textContent);
  }
});
```

---

### 31. **What is the difference between deep copy and shallow copy of an object?**

**Answer:**

* **Shallow copy** copies only top-level references.
* **Deep copy** recursively copies all nested levels.

```js
let deep = JSON.parse(JSON.stringify(obj)); // not perfect but common
```

---

### 32. **How are JavaScript arrays different from objects?**

**Answer:**

* Arrays are ordered collections with index-based access.
* Objects are unordered key-value pairs.

But arrays are actually specialized objects.

---

### 33. **What are IIFE (Immediately Invoked Function Expressions)?**

**Answer:**
Functions that run immediately when defined.

```js
(function() {
  console.log("IIFE executed");
})();
```

Used to create isolated scopes.

---

### 34. **What is the difference between synchronous and asynchronous programming in JS?**

**Answer:**

* **Synchronous**: One operation at a time (blocking)
* **Asynchronous**: Runs in background, uses Promises/async-await (non-blocking)

---

### 35. **Explain optional chaining and nullish coalescing.**

**Answer:**

```js
// Optional chaining
let name = user?.details?.name;

// Nullish coalescing
let result = value ?? "default"; // only uses default if null or undefined
```

---

### 36. **What is destructuring and give an example with nested object?**

**Answer:**

```js
const user = { name: "Ganesh", address: { city: "Mumbai" } };
const { address: { city } } = user;
console.log(city); // Mumbai
```

---

### 37. **Explain JavaScript event bubbling and capturing.**

**Answer:**

* **Bubbling**: Events propagate from child to parent.
* **Capturing**: Events propagate from parent to child.

Use `{ capture: true }` in event listener to capture.

---

### 38. **What are Generators in JavaScript?**

**Answer:**
Special functions that can pause execution using `yield`.

```js
function* gen() {
  yield 1;
  yield 2;
}
const g = gen();
g.next(); // {value: 1, done: false}
```

---

### 39. **Explain the difference between mutable and immutable data types.**

**Answer:**

* **Mutable**: Can be changed after creation (arrays, objects)
* **Immutable**: Cannot be changed (primitive types like string, number)

---

### 40. **What is prototype and prototypal inheritance?**

**Answer:**
Every object in JS has an internal `[[Prototype]]`. When accessing a property, JavaScript looks up the prototype chain if not found directly.

```js
const parent = { greet: () => "Hello" };
const child = Object.create(parent);
console.log(child.greet()); // "Hello"
```

---