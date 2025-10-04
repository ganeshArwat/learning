## JS-1: Js Code Execution, let var and const

- Js Code Execution Components

  - 1. Memory Heap
  - 2. Call Stack – Executes synchronous code.
  - 3. Web APIs – Handles setTimeout, fetch, event listeners, etc.
  - 4. Microtask Queue – Handles Promises and MutationObserver.
  - 5. Callback Queue (Task Queue) – Handles setTimeout, setInterval, and events.
  - 6. Event Loop – Coordinates execution of all queues.
  - 7. Animation Frame Queue – Handles requestAnimationFrame animations.
  - 8. Rendering Engine – Repaints the UI at 60 FPS (ideally, ~16.67ms per frame).

- Execution Context in JavaScript

  - 1. Global Execution Context (GEC)
  - 2. Function Execution Context (FEC)
  - 3. Eval Execution Context (Rarely Used)

- Execution Context Phases

  - 1. Creation Phase (Memory Allocation)
  - 2. Execution Phase (Code Execution)
  - 3. Execution Context & Call Stack

- JavaScript Execution Flow.

  - 1. Global Execution Context (GEC) is Created
  - 2. Execution Context Creation (For Every Function Call)
  - 3. Synchronous Code Execution
  - 4. Asynchronous Code Handling
  - 5. Event Loop Execution

- JavaScript Execution Order (Including Animations)

  - 1. Call Stack Execution (Runs synchronous code)
  - 2. Microtask Queue Execution (e.g., Promise.then, queueMicrotask)
  - 3. Animation Frame Queue Execution (e.g., requestAnimationFrame)
  - 4. Callback Queue Execution (e.g., setTimeout, setInterval, fetch callbacks)

- Types of Scope in JavaScript

  - 1. Global Scope
  - 2. Function Scope
  - 3. Block Scope
  - 4. Lexical Scope (Closure Scope)
  - 5. Module Scope

- Showdowing

  - Example of Shadowing
  - Block Scope Shadowing
  - With var (Block Scope)
  - With var (Function Scope)
  - Illegal Shadowing

- Hoisting

  - Example of Hoisting with var
  - Hoisting with let and const
  - Hoisting with Function Declarations
  - Hoisting with Function Expressions

- Temporal Dead Zone (TDZ) in JavaScript

- Primitives and Non Primitives

- Var, Let, and Const

- Array

  - Why are Arrays Objects in JavaScript?
  - [Important: why typeof null is object?]

- why typeof null is object

## JS-2: OOPS-1 : This, Bind, Call, Apply, Inheritance

### Native objects and host objects

- 1. Native Objects
- 2. Host objects

### Strict Mode

- What is Strict Mode in JavaScript?
- How to Enable Strict Mode?
- Why Use Strict Mode?
  - 1. Preventing accidental global variables
  - 2. Throwing errors for assignment to read-only properties
  - 3. Preventing deletion of variables and function
  - 4. Detecting duplicate parameter names
  - 5. Restricting the use of this in functions

### This

- What is this in JavaScript?
- Rules for this in JavaScript
  - 1. Global Context (this in Global Scope)
  - 2. Function Context (Regular Function)
  - 3. Object Method (this in an Object)
  - 4. Constructor Functions (new Keyword)
  - 5. Arrow Functions (this in Arrow Functions)
  - 6. this in Event Listeners
  - 7. Explicit Binding (call, apply, bind)
  - 8. this in setTimeout and setInterval

### Chaining

- What is Chaining in JavaScript?
- Example 1: Method Chaining (String)
- Example 2: Chaining with Arrays
- Example 3: Chaining with jQuery (if using jQuery)
- Example 4: Chaining in Custom Objects (Returning this)

### Prototypal Inheritance

- What is Prototypal Inheritance in JavaScript?
- How Prototypal Inheritance Works
- Example 1: Basic Prototypal Inheritance
- Example 2: Adding Properties to Prototype
- Prototype Chain
- Example 3: Extending Inheritance
- ES6 Classes and Prototypal Inheritance

---

## JS-3: Polyfills of call,bind ,apply & deep copy-shallow copy

### SPREAD REST DEFAULT

#### Spread Operator

- 1. Spread Operator with Arrays
  - Copy an array
  - Merge arrays:
  - Adding element to an array
  - spread operator : partial deep copy till level 1.
- 2. Spread Operator with Objects
  - Copying an Object
  - Merging Objects
  - Overriding Properties
- 3. Spread Operator with Function Arguments
  - Passing Array Elements as Arguments

#### Rest Operator

- 1. Rest Operator in Function Parameters
- 2. Rest Operator in Array Destructuring
- 3. Rest Operator in Object Destructuring

### Rest Operator vs Spread Operator

- Purpose
- Usage
- Example

### CALL BY VALUE AND REFERENCE

- 1. Call by Value (Primitive Data Types)
- 2. Call by Reference (Objects, Arrays)
- Does JavaScript Truly Support Call by Reference?
  - 1. Modifying properties of an object (mutating the reference) affects the original object. ✅
  - 2. Reassigning the reference inside a function does not affect the original object. ❌

### CALL BIND APPLY

- 1. Call
- 2. Bind
- 3. Apply()

### POLYFILL OF CALL BIND APPLY

- PollyFill of Call
- PollyFill of Apply
- PollyFill of Bind

---

## Js-4: Array Hof and its polyfills

### How Copy Works in General in js

- Copying Primitives (Pass by Value)
- Copying Objects and Arrays (Pass by Reference)

### Ways to Copy Objects

- 1️⃣ Shallow Copy (1-Level Deep)

  - Using Object.assign()
  - Using Spread Operator {…}

- 2️⃣ Deep Copy (Fully Independent)
  - Using JSON.parse(JSON.stringify(obj))
  - Using structuredClone() (Modern Approach)
  - Using Lodash (\_.cloneDeep)

### Ways to Copy Arrays

- 1️⃣ Shallow Copy (1-Level Deep)

  - Using Spread Operator […]
  - Using Array.prototype.slice()
  - Using Array.from()

- 2️⃣ Deep Copy (Fully Independent)

  - Using JSON.parse(JSON.stringify(arr))
  - Using structuredClone(arr)
  - Using “\_.cloneDeep(arr)”

### Deep Copy PollyFill

### Flatten an Array

### Array

- 1️⃣ Creating an Array
- 2️⃣ Important Array

  - Adding & Removing Elements
    - push()
    - pop()
    - unshift()
    - shift()
  - Accessing & Finding Elements
    - indexOf()
    - includes()
    - find()
    - findIndex()
  - Modifying & Slicing
    - slice()
    - splice()
    - concat()
    - join()
    - split()
  - Iteration & Transformation
    - forEach()
    - map()
    - filter()
    - reduce()
  - Sorting & Reversing
    - sort()
    - reverse()
  - Special Methods
    - flat()
    - fill()
    - some()
    - every()

- slice() vs. splice() in JavaScript
  - array.slice(startIndex, endIndex);
  - array.splice(startIndex, deleteCount, item1, item2, ...);

### IIFE (Immediately Invoked Function Expression)

- 1️⃣ Basic Syntax of IIFE
- 2️⃣ Named vs. Anonymous IIFE
- 3️⃣ Arrow Function IIFE
- 4️⃣ IIFE with Parameters
- 5️⃣ IIFE Returning a Value
- 6️⃣ Using IIFE to Create a Private Scop
- 7️⃣ IIFE with async / await
- 8️⃣ IIFE with Multiple Functions

### Higher Order Function (HOF)

- 1️⃣ Why Use Higher-Order Functions?
- 2️⃣ Example: Higher-Order Function Taking a Function as an Argument
- 3️⃣ Example: Higher-Order Function Returning a Function

---

## Js-5: Closures

### Lexical Scope

- 1️⃣ What is Lexical Scope?
- 2️⃣ Example of Lexical Scope
- 3️⃣ Lexical Scope with Multiple Levels
- 4️⃣ Lexical Scope and Closures
- 5️⃣ Scope Chain (How JavaScript Searches for Variables)
- 6️⃣ Common Mistake: Trying to Access Variables from an Inner Scope

### Closure

- 1️⃣ What is a Closure?
- 2️⃣ Basic Example of a Closure
- 3️⃣ Real-World Example: Counter with Closures
- 4️⃣ Closures in Event Listeners
- 5️⃣ Closures with setTimeout
- 6️⃣ Private Variables Using Closures
- 7️⃣ Closures in Loops - Common Mistake

### Currying

- 1️⃣ What is Currying?
- 2️⃣ How Currying Works?
- 3️⃣ Why Use Currying?
- 4️⃣ Convert a Normal Function to Curried Function
- 5️⃣ Real-World Example: Filtering Data

### Curry Vs Closure

### Application Closures

---

## Js-6: OOP

### OOP

- 1. Creating Objects in JavaScript
- 2. Constructor Functions
- 3. Prototypes (Better Memory Management)
- 4. ES6 Classes (Syntactic Sugar for Prototypes)
- 5. Inheritance (Extending a Class)
- 6. Encapsulation (Private & Public Properties)
- 7. Polymorphism (Method Overriding)
- 8. Static Methods (Class-Level Methods)

### Inbuilt object works

- 1. JavaScript’s Inbuilt Object Hierarchy
- 2. How Primitive Types Work
- 3. Autoboxing: Temporary Conversion of Primitives

### Object create

- 1. Creating an Object using new Object()
     let obj1 = new Object();
- 2. Creating an Object using Object.create(null)
- 3. Creating an Object with Prototypal Inheritance

### hasOwnProperty

### for in loop

### Types of for Loops

- 1️⃣ Traditional for loop
- 2️⃣ for...in loop
- 3️⃣ for...of loop (ES6)
- 4️⃣ forEach method (for arrays)

---

## Js-7: Async Js

### Synchronous vs Asynchronous JavaScript

- 1️⃣ Synchronous JavaScript (Sync)
- 2️⃣ Asynchronous JavaScript (Async)

### How async Code Execution works in js

### Callbacks

### Parallel Vs Serial

### ⏳ JavaScript Timers (setTimeout, setInterval, clearTimeout, clearInterval)

---

## Js-8: Intro to Promises

### heart attack code / callback hell / Pyramid of doom

### Inversion of Control (IoC) in JavaScript

### 🚨 Why is IoC a Drawback in Callbacks?

### Promises

### How Promises Solve the Inversion of Control Problem?

---

## Js-9: Async Await And Error Handling

### Async Await

- Why async/await?
- Converting a Promise to async/await
- Understanding async and await
- Handling Multiple Async Calls
- Running Multiple Promises in Parallel
- Handling Errors with try/catch

### JavaScript Event Loop & Async Generators

- 1. JavaScript Event Loop (How JS Handles Async Code)
- 2. Microtasks vs. Macrotasks (Execution Order)
- 3. Async Generators (Yielding Async Data)

### Set Timeout

### Polyfills of Set Interval

### 1. Types of Errors in JavaScript

### Error handling

---

## Js-10-11: Promise all any race

### 1. Promise.all()

### 2. Promise.any() (ES2021)

### 3. Promise.race()

### 4. Promise.allSettled()

### Promise Polyfill

### Promise.all Polyfill

### Promise.race Polyfill

---

## Js-12: Week Map/set objects

### Object Mutation - Const, Object.preventExtensions, Object.seal, Object.freeze

- 1. const and Object Mutation
- 2. Object.preventExtensions()
- 3. Object.seal()
- 4. Object.freeze()

### Deep Prevention, Sealing and Freezing

- Deep Prevent Extensions
- Deep Seal
- Deep Freeze

### Symbol

- 1. Creating Symbols
- 2. Using Symbols as Object Keys
- 3. Shared Symbols with Symbol.for()
- 4. Symbols in Class Properties

### Bigint

- 1. Why BigInt?
- 2. Creating a BigInt
- 3. Operations with BigInt
- 4. Mixing BigInt and Number
- 5. Comparisons with BigInt
- 6. BigInt in JSON

### Map

- 1. Creating a Map
- 2. Adding, Getting & Deleting Values
- 3. Iterating Over a Map

### Set

- 1. Creating a Set
- 2. Adding, Getting & Deleting Values
- 3. Iterating Over a Set

### Week Reference

- Strong Reference vs. Weak Reference

  - 1️⃣ Strong Reference (Normal Variables in JavaScript)
  - 2️⃣ Weak Reference (Using WeakMap or WeakSet)

- Why Do We Need Weak References?

- WeakMap

- WeakSet

- When to Use WeakMap and WeakSet?

---

## Js-13: Es6 Extra Features

### Modules in Es6

- 1️⃣ Exporting and Importing Modules
  - Named Export
  - Default Export
- 2️⃣ Exporting & Importing Everything (\*)
- 3️⃣ Mixing Named and Default Exports

### Ternary Operator (? :) in JavaScript

- Basic Ternary
- Nesting Ternary Operators

### Short Circuiting and Logical Operators

- Short-Circuiting with && (AND)
- Short-Circuiting with || (OR)
- Short-Circuiting with ?? (Nullish Coalescing)

### Optional Chaining

- What is Optional Chaining?
- Accessing Nested Properties
- Calling Methods Safely
- Accessing Array Elements
- Using with ?.[] for Dynamic Keys
- Combining with Nullish Coalescing (??)

### Destructuring in JavaScript

- 1️⃣ Array Destructuring

  - Basic Example
  - Skipping Elements
  - Using Rest Operator (...)
  - Swapping Values
  - Default Values

- 2️⃣ Object Destructuring

  - Basic Example
  - Renaming Variables
  - Default Values
  - Nested Object Destructuring

- 3️⃣ Function Parameter Destructuring

  - Destructuring an Object in a Function
  - Destructuring an Array in a Function
