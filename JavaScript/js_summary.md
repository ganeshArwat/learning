# Questions

- async/await vs promises

# JS-1: JS Refresher and Code Execution

## Js Code Execution

1. Memory Heap
   - Stores variables, functions, and objects.
   - JavaScript uses garbage collection to free up unused memory.
2. Call Stack
   - A LIFO (Last In, First Out) structure that keeps track of function calls.
   - Each function call is pushed onto the stack and popped off when completed.
3. Web Apis
   - Handles asynchronous operations like:
     - setTimeout
     - fetch API (AJAX)
     - DOM manipulation
     - Event Listeners
4. Callback Queue (Task Queue / Message Queue)
   - Stores callback functions (from asynchronous operations) that are ready to be executed.
   - Uses Event Loop to push functions to the Call Stack when it's empty.
5. Microtask Queue
   - Stores Promises and MutationObserver callbacks.
   - Has higher priority than the Callback Queue.
   - Runs before normal callbacks (tasks from the Callback Queue).
6. Event Loop
   - Continuously checks if the Call Stack is empty.
   - Moves tasks from the Microtask Queue first, then from the Callback Queue to the Call Stack.

- Execution Flow:
  1. Call Stack executes synchronous code (main thread).
  2. Async operations go to Web APIs (e.g., setTimeout, fetch).
  3. Once completed, callbacks move to the Callback Queue or Microtask Queue.
  4. Event Loop pushes tasks from Microtask Queue first, then from Callback Queue.
  5. Process repeats until all tasks are executed.

## Execution Context in JavaScript

- An Execution Context (EC) is an environment where JavaScript code is executed. It manages the memory allocation, execution of functions, and handling of variables.

## Types of Execution Context

1. Global Execution Context (GEC)

   - Created when JavaScript starts execution.
   - this in the global context refers to window (browser) or global (Node.js).
   - Stores global variables and functions.

2. Function Execution Context (FEC)

   - Created whenever a function is called.
   - Each function has its own execution context.
   - Maintains local variables and function arguments.

3. Eval Execution Context
   - Created when eval() is used.
   - Not commonly used due to security and performance concerns.

## Execution Context Phases

Each execution context has two main phases:

1. Creation Phase (Memory Allocation)

   - Creates a new execution context.
   - Allocates memory for variables and functions.
   - Variables are set to undefined, and functions are stored as references.
   - this is set based on how the function is called.

2. Execution Phase (Code Execution)
   - Executes the code line by line.
   - Assigns values to variables.
   - Executes function calls and manages the call stack.

## Execution Context & Call Stack

- JavaScript uses a Call Stack to manage execution contexts.
- The Global Execution Context (GEC) is created first and stays until the script finishes.
- When a function is called, a Function Execution Context (FEC) is pushed onto the stack.
- When a function completes, its execution context is popped off the stack.

# JS-2: OOPS-1 : This, Bind, Call, Apply, Inheritance

- Native objects and host objects
- Rules for this
- Behaviour of this
- Prototypal OOPS
- Bind, call and apply
- Prototypal Inheritance
- Arrow Functions
- Execution Context
- Lexical Scope
- Block Scope
- Strict Mode
- Object Prototype
- Method Brrowing
- Memory Management
- Constructor Pattern
- Illegal Shadowing
- Global Execution Context

# JS-3: Polyfills of call,bind ,apply & deep copy-shallow copy

- Shallow Copy
- Deep Copy
- Polyfill
- Call Method
- Apply Method
- Bind Method
- Polyfills of bind, apply and call
- Call by reference and call by value
- Spread Operator
- Rest Operator
- Peak Memory Consumption
- Recursive Stack
- Prototypal Inheritance
- Funtion Prototype

# JS-4: Array , HOFs and it's Polyfills

- How Copy Works in General in js
- Shallow copy
- Shallow copy using Object Assign
- Deep Copy
- Polyfill of Deep Copy
- How to Flatten an Array
- Array and Its use cases
- Function and its use cases

# JS-5: ES6 Classes and Objects

# JS-6: Closure and It's application

- Lexical Scope
- Intro to Closure
- Closure in DevTools
- Nested Closures
- Application of Closure
- var and closure
- let and closure
- Infinite Currying
- Creating Private Variable Using closure
- Creating Memoized function

# JS-7: OOPS-2 : Object creation, Freezing objects

- Creating objects in JS
- Prototypal Inheritance
- Object Descriptors

# JS-8: Event loop and Callback

- Intuition of Async JS
- Async JS with callbacks
- Event loop with callback queue
- Serial and Parallel Execution of Async code

# JS-9: Promises and MicroTask Queue

- Asynchronous Javascript
- Callback Hell
- Inversion of Control
- Promises
- Promises in Javascript
- Consuming Promises
- Chaining Promises
- Callback to promises
- Why promises are better than callback

# JS-10: S-10: Promise chaining and Imp polyfills

- Revision of Promises
- Promise.all
- Create Promise API

# JS-11: Async await & Error handling

- Promises
- Definition of Resolve and Reject in Promises
- Promise methods
- MBE Comms

# JS-12: ES6 DataTypes and Modules

- Modules in JavaScript
- BigInt DataType
- Symbol DataType
- Proxies in JavaScript

# FE Machine coding-1:Intro to the DOM

- Overview of Browser
- DOM API
- Reading Attributes
- CRUD Operations
- Update an attribute
- Event Listeners
- Message-Based Communication

# FE Machine coding-2: Events & Event Handling, Bubbling & capturing

# FE Machine coding-3: Machine coding case studies

# FE Machine coding-4: Browser Perf & Memory leaks

# FE Machine coding-5: HTTP and network Optimization

# FE Machine coding-6:- Typeahead[Intersection Obs, Debouncing, Throttling]

# FE Machine coding-7: - Kanban board-1

# FE Machine coding-8: Kanban board-2
