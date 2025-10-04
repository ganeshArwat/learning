# JS-2: OOPS-1 : This, Bind, Call, Apply, Inheritance

## Native objects and host objects

### 1. Native Objects

#### Native objects are objects that are part of the JavaScript language itself, as defined by the ECMAScript specification. These objects are always available, regardless of the environment in which JavaScript is running.

- Examples of Native Objects:

  - Global Objects: Object, Function, Boolean, Number, String, Array, Symbol, BigInt, Date, RegExp
  - Error Objects: Error, TypeError, ReferenceError, SyntaxError, etc.
  - Math and JSON Objects: Math, JSON
  - Typed Arrays and DataView: ArrayBuffer, Uint8Array, Float32Array, etc.
  - Promise and Related Objects: Promise, Map, Set, WeakMap, WeakSet

- Characteristics:

  - Defined in ECMAScript (JavaScript) specification.
  - Available in all JavaScript environments (browser, Node.js, etc.).
  - Can be used directly without depending on the host environment.

### 2. Host objects

#### Host objects are objects provided by the runtime environment (such as a browser or Node.js). They are not part of the JavaScript specification but are made available by the host to enable interaction with its features.

- Examples of Host Objects:

  - In Browsers:

    - window
    - document (part of the DOM)
    - console
    - setTimeout, setInterval
    - fetch, XMLHttpRequest
    - localStorage, sessionStorage
    - navigator, history
    - WebSocket, IndexedDB

  - In Node.js:

    - require
    - process
    - Buffer
    - fs (File System module)
    - http (HTTP module)

## Strict Mode

### What is Strict Mode in JavaScript?

#### Strict Mode is a feature in JavaScript that helps catch common mistakes and prevent certain unsafe actions. It was introduced in ECMAScript 5 (ES5) to make JavaScript code more secure, optimized, and easier to debug.

#### How to Enable Strict Mode?

- You can enable strict mode by adding the directive:
- This must be the first statement in a script or a function.

```js
"use strict";
```

#### Example (Global Strict Mode)

- Here, x is not declared with var, let, or const, so an error is thrown.

```js
"use strict";
x = 10; // ❌ ReferenceError: x is not defined
console.log(x);
```

#### Example (Function-Level Strict Mode)

- Strict mode can be applied inside a function to restrict only that function's scope.

```js
function test() {
  "use strict";
  y = 20; // ❌ ReferenceError: y is not defined
  console.log(y);
}
test();
```

### Why Use Strict Mode?

#### 1. Preventing accidental global variables

- Without strict mode, JavaScript would create myVar as a global variable.
- With strict mode, it throws an error.

```js
"use strict";
myVar = 100; // ❌ ReferenceError: myVar is not defined
```

#### 2. Throwing errors for assignment to read-only properties

```js
"use strict";
Object.defineProperty(this, "PI", { value: 3.14, writable: false });
PI = 3.14159; // ❌ TypeError: Cannot assign to read only property 'PI'
```

#### 3. Preventing deletion of variables and functions

```js
"use strict";
let myVar = 10;
delete myVar; // ❌ SyntaxError: Delete of an unqualified identifier in strict mode.
```

#### 4. Detecting duplicate parameter names

```js
"use strict";
function sum(a, a) {
  // ❌ SyntaxError: Duplicate parameter name not allowed in this context
  return a + a;
}
```

#### 5. Restricting the use of this in functions

```js
"use strict";
function show() {
  console.log(this); // ❌ `this` is `undefined` instead of `window` in strict mode
}
show();
```

## This

### What is this in JavaScript?

#### In JavaScript, this is a special keyword that refers to the execution context of a function. The value of this depends on how and where the function is called.

### Rules for this in JavaScript

- The value of this is determined by the function's execution context. Below are the key rules that govern its behavior:

#### 1. Global Context (this in Global Scope)

- In the browser, this refers to the global window object.
- In Node.js, this refers to global.

#### 2. Function Context (Regular Function)

- When a regular function is called, this refers to the global object (window in browsers or global in Node.js).
- In strict mode ('use strict'), this is undefined.

```js
function show() {
  console.log(this); // In browser: window, In Node.js: global
}
show();

("use strict");
function test() {
  console.log(this); // undefined in strict mode
}
test();
```

#### 3. Object Method (this in an Object)

- When a function is called as a method of an object, this refers to that object.

```js
const obj = {
  name: "Ganesh",
  show: function () {
    console.log(this.name); // "Ganesh"
  },
};
obj.show();
```

#### 4. Constructor Functions (new Keyword)

- When a function is called with new, this refers to the newly created object.

```js
function Person(name) {
  this.name = name;
}
const p = new Person("Ganesh");
console.log(p.name); // "Ganesh"
```

#### 5. Arrow Functions (this in Arrow Functions)

- Arrow functions do not have their own this. Instead, they inherit this from the surrounding (lexical) scope.
- it takes this from outside(nearest scope)

```js
const obj = {
  name: "Ganesh",
  show: function () {
    const arrowFunc = () => console.log(this.name);
    arrowFunc(); // "Ganesh", because arrow function takes `this` from `show`
  },
};
obj.show();
```

#### 6. this in Event Listeners

- In an event handler, this refers to the element that fired the event.

```js
document.getElementById("btn").addEventListener("click", function () {
  console.log(this); // The button element
});
```

#### 7. Explicit Binding (call, apply, bind)

- JavaScript provides methods to explicitly set this:

  - call() – Calls a function with a specified this value and arguments.
  - apply() – Similar to call(), but arguments are passed as an array.
  - bind() – Returns a new function with this permanently set.

```js
function show() {
  console.log(this.name);
}
const obj = { name: "Ganesh" };

show.call(obj); // "Ganesh"
show.apply(obj); // "Ganesh"

const boundFunc = show.bind(obj);
boundFunc(); // "Ganesh"
```

#### 8. this in setTimeout and setInterval

- In regular functions inside setTimeout or setInterval, this refers to the global object (window in browsers).
- Use arrow functions to inherit this from the surrounding scope.

```js
const obj = {
  name: "Ganesh",
  show: function () {
    setTimeout(function () {
      console.log(this.name); // undefined (window in browsers)
    }, 1000);

    setTimeout(() => {
      console.log(this.name); // "Ganesh" (arrow function inherits `this`)
    }, 1000);
  },
};
obj.show();
```

### Summary of Effects of Strict Mode on this

#### Global Scope

- With Strict - window (browser), global (Node.js)
- Without Strict - undefined

#### Regular Function

- With Strict - window (browser), global (Node.js)
- Without Strict - undefined

#### Object Method

- With Strict - The object
- Without Strict - The object (no change)

#### Constructor Function

- With Strict - window if new is missing (dangerous)
- Without Strict - undefined, throwing an error if new is missing (safer)

#### Arrow Function

- With Strict - Inherits this from its lexical scope
- Without Strict - Inherits this from its lexical scope (no change)

#### call(), apply(), bind()

- With Strict - Defaults to window if null or undefined is passed
- Without Strict - this remains undefined

#### setTimeout, setInterval

- With Strict - this is window (browser)
- Without Strict - undethis is undefined

## Chaining

### What is Chaining in JavaScript?

#### Chaining in JavaScript refers to the practice of calling multiple methods on an object in a single statement, improving code readability and efficiency.

#### It works because methods return the object itself (this) or another object, allowing multiple operations to be performed sequentially.

#### Example 1: Method Chaining (String)

```js
let result = "  hello world  "
  .trim() // Removes spaces from both ends
  .toUpperCase() // Converts to uppercase
  .replace("WORLD", "JS"); // Replaces "WORLD" with "JS"

console.log(result); // "HELLO JS"
```

#### Example 2: Chaining with Arrays

```js
let numbers = [1, 2, 3, 4, 5];

let result = numbers
  .map((num) => num * 2) // [2, 4, 6, 8, 10]
  .filter((num) => num > 5) // [6, 8, 10]
  .reduce((sum, num) => sum + num, 0); // 6 + 8 + 10 = 24

console.log(result); // 24
```

#### Example 3: Chaining with jQuery (if using jQuery)

```js
$("#myDiv").css("color", "blue").slideUp(1000).slideDown(1000);
```

#### Example 4: Chaining in Custom Objects (Returning this)

- To enable chaining in custom objects, methods should return this (the object itself).

```js
class Calculator {
  constructor(value = 0) {
    this.value = value;
  }

  add(num) {
    this.value += num;
    return this; // Enables chaining
  }

  subtract(num) {
    this.value -= num;
    return this;
  }

  multiply(num) {
    this.value *= num;
    return this;
  }

  getResult() {
    return this.value;
  }
}

let result = new Calculator(10).add(5).subtract(3).multiply(2).getResult();

console.log(result); // (10 + 5 - 3) * 2 = 24
```

## Prototypal Inheritance

### What is Prototypal Inheritance in JavaScript?

#### Prototypal Inheritance is a mechanism in JavaScript where objects inherit properties and methods from other objects via a special object called prototype. This allows for code reuse without needing class-based inheritance.

### How Prototypal Inheritance Works

#### Every JavaScript object has an internal link to another object, called its prototype. When a property or method is accessed on an object, JavaScript first checks if it exists on the object itself. If not, it looks up the prototype chain until it finds the property or reaches the end (null).

#### Example 1: Basic Prototypal Inheritance

- Here, child does not have its own greet() method, so JavaScript looks up the prototype chain and finds greet() in parent.

```js
let parent = {
  greet: function () {
    console.log("Hello from parent!");
  },
};

let child = Object.create(parent); // child inherits from parent

child.greet(); // "Hello from parent!"
```

#### Example 2: Adding Properties to Prototype

- The Person constructor function defines the name property.
- The sayHello method is added to Person.prototype, so all instances (john, jane) share the same method instead of duplicating it.

```js
function Person(name) {
  this.name = name;
}

Person.prototype.sayHello = function () {
  console.log("Hello, my name is " + this.name);
};

let john = new Person("John");
john.sayHello(); // "Hello, my name is John"

let jane = new Person("Jane");
jane.sayHello(); // "Hello, my name is Jane"
```

```js
Array.prototype.sum = function () {
  let sum = 0;
  for (let i = 0; i < this.length; i++) {
    sum = sum + this[i];
  }
  console.log(sum);
};

// usecase of this and prototype
arr1.sum();
arr2.sum();
console.log(arr1);
console.log(arr2);
```

#### Prototype Chain

- If an object doesn’t have a property, JavaScript looks for it in its prototype, then its prototype’s prototype, and so on, until null is reached.

```js
console.log(john.__proto__ === Person.prototype); // true
console.log(Person.prototype.__proto__ === Object.prototype); // true
console.log(Object.prototype.__proto__ === null); // true
```

#### Example 3: Extending Inheritance

```js
function Animal(name) {
  this.name = name;
}

Animal.prototype.makeSound = function () {
  console.log(this.name + " makes a sound.");
};

function Dog(name, breed) {
  Animal.call(this, name); // Call parent constructor
  this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype); // Inherit from Animal
Dog.prototype.constructor = Dog; // Reset constructor reference

Dog.prototype.bark = function () {
  console.log(this.name + " barks!");
};

let dog = new Dog("Buddy", "Labrador");
dog.makeSound(); // "Buddy makes a sound."
dog.bark(); // "Buddy barks!"
```

#### ES6 Classes and Prototypal Inheritance

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  makeSound() {
    console.log(this.name + " makes a sound.");
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Call parent constructor
    this.breed = breed;
  }

  bark() {
    console.log(this.name + " barks!");
  }
}

let dog = new Dog("Buddy", "Labrador");
dog.makeSound(); // "Buddy makes a sound."
dog.bark(); // "Buddy barks!"
```
