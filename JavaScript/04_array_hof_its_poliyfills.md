## How Copy Works in General in js

#### A shallow copy of an object is a copy whose properties share the same references (point to the same underlying values) as those of the source object from which the copy was made. As a result, when you change either the source or the copy, you may also cause the other object to change too. That behavior contrasts with the behavior of a deep copy, in which the source and copy are completely independent.

- shallow copy:
  - shallow copy of an object/Array is a copy whose properties share the same references (point to the same underlying values) as those of the source object from which copied

#### In JavaScript, copying data depends on whether the value is primitive or non-primitive (objects, arrays, functions, etc.).

### Copying Primitives (Pass by Value)

- Primitive values include string, number, boolean, null, undefined, bigint, and symbol.
  When you copy a primitive value, a new independent copy is created.

```js
let a = 10;
let b = a; // Copying the value of 'a' into 'b'

b = 20; // Changing 'b' does not affect 'a'
console.log(a); // 10
console.log(b); // 20
```

### Copying Objects and Arrays (Pass by Reference)

- Non-primitive data types (objects, arrays, functions) are stored in memory and copied by reference.

```js
let obj1 = { name: "Ganesh" };
let obj2 = obj1; // Copying by reference

obj2.name = "Arwat"; // Modifies both 'obj1' and 'obj2'

console.log(obj1.name); // "Arwat"
console.log(obj2.name); // "Arwat"
```

### Ways to Copy Objects & Arrays

#### 1️⃣ Shallow Copy (1-Level Deep)

- A shallow copy means that only the first level is copied, but nested objects still share references.
- Using Object.assign()

```js
let obj1 = { name: "Ganesh", details: { age: 23 } };
let obj2 = Object.assign({}, obj1);

obj2.name = "Arwat"; // Only 'obj2' changes
obj2.details.age = 25; // Modifies 'obj1' too because 'details' is a reference

console.log(obj1); // { name: "Ganesh", details: { age: 25 } }
console.log(obj2); // { name: "Arwat", details: { age: 25 } }
```

- Using Spread Operator {...}

```js
let obj1 = { name: "Ganesh", details: { age: 23 } };
let obj2 = { ...obj1 };

obj2.details.age = 25; // Nested object is still a reference

console.log(obj1.details.age); // 25
console.log(obj2.details.age); // 25
```

- 🛑 Problem: Nested objects are still copied by reference.

#### 2️⃣ Deep Copy (Fully Independent)

- A deep copy means that all levels of an object are copied, creating a fully independent object.
- Using JSON.parse(JSON.stringify(obj))

```js
let obj1 = { name: "Ganesh", details: { age: 23 } };
let obj2 = JSON.parse(JSON.stringify(obj1));

obj2.details.age = 25; // Does not affect 'obj1'

console.log(obj1.details.age); // 23
console.log(obj2.details.age); // 25
```

- 🛑 Limitations: This does not work with functions, undefined, symbols, or Date.

- Using structuredClone() (Modern Approach)

```js
let obj1 = { name: "Ganesh", details: { age: 23 } };
let obj2 = structuredClone(obj1);

obj2.details.age = 25;

console.log(obj1.details.age); // 23
console.log(obj2.details.age); // 25
```

- Best deep copy method (works with most data types).

- Using Lodash (\_.cloneDeep)

```js
const _ = require("lodash"); // Install lodash via npm
let obj1 = { name: "Ganesh", details: { age: 23 } };
let obj2 = _.cloneDeep(obj1);
```

#### Copying Arrays

- Arrays behave similarly to objects.

- Shallow Copy
  - Using Spread Operator [...]
  - Using Array.prototype.slice()
  - Using Array.from()

```js
let arr1 = [1, 2, [3, 4]];
let arr2 = [...arr1];

arr2[2][0] = 99; // Modifies both arrays!

console.log(arr1); // [1, 2, [99, 4]]
console.log(arr2); // [1, 2, [99, 4]]
```

- 🛑 Problem: Nested arrays are still references.

- Deep Copy
  - Using JSON.parse(JSON.stringify(arr))
  - Using structuredClone(arr)
  - Using "\_.cloneDeep(arr)"

```js
let arr1 = [1, 2, [3, 4]];
let arr2 = JSON.parse(JSON.stringify(arr1));

arr2[2][0] = 99; // Does NOT modify 'arr1'

console.log(arr1); // [1, 2, [3, 4]]
console.log(arr2); // [1, 2, [99, 4]]
```

## Deep Copy PollyFill

```js
function superCloneEffective(input) {
  // Base case or edge cases.
  if (!Array.isArray(input) && typeof input !== "object") {
    // Function or either primitive data type.
    return input;
  }

  // Create a new container on the basis of type whether it is a array or object.
  let clone = Array.isArray(input) ? [] : {};

  // Copy all the key and values.
  for (let key in input) {
    const value = input[key];
    clone[key] = superCloneEffective(value);
  }

  // return object after completion.
  return clone;
}

// Testcases.
let person = {
  firstName: "John",
  lastName: "Doe",
  address: {
    street: "North 1st street",
    city: "San Jose",
    state: "CA",
    country: "USA",
  },
  friends: ["Steve", "Nikola", "Ray", { name: "Jai", lastName: "Roy" }],
  sayHi: function () {
    console.log("Hi Class!");
  },
};

let superDeeplyClonedObj = superCloneEffective(person);

superDeeplyClonedObj.lastName = "Odinson";
superDeeplyClonedObj.address.street = "south 1st street";

console.log("person", person);
console.log("superCopiedObject", superDeeplyClonedObj);

superDeeplyClonedObj.sayHi();
```

## Flatten an Array

```js
let input = [[[[[1]]]], 2];

// Array contains only Integers.
function flatten(srcArr) {
  let newArr = [];
  for (element of srcArr) {
    if (Array.isArray(element)) {
      let flatteredArrayUsingRecursion = flatten(element);
      // for(ele of flatteredArrayUsingRecursion){
      //     newArr.push(ele);
      // }

      newArr.push(...flatteredArrayUsingRecursion);
    } else {
      newArr.push(element);
    }
  }

  return newArr;
}

let flattenedArr = flatten(input);
console.log("flattenedArr: ", flattenedArr);
```

## Array

### 1️⃣ Creating an Array

```js
let arr = [10, 20, 30, 40, 50]; // Numeric array
let names = ["Ganesh", "Arwat"]; // String array
let mixed = [1, "hello", true]; // Mixed types
```

### 2️⃣ Important Array Methods

- let arr = [10, 20, 30, 40, 50];

#### Adding & Removing Elements

- push()

  - Adds element at the end
  - arr.push(60); → [10,20,30,40,50,60]

- pop()

  - Removes last element
  - arr.pop(); → [10,20,30,40]

- unshift()

  - Adds element at the start
  - arr.unshift(5); → [5,10,20,30,40,50]

- shift()

  - Removes first element
  - arr.shift(); → [20,30,40,50]

#### Accessing & Finding Elements

- indexOf()

  - Finds index of element
  - arr.indexOf(30); → 2

- includes()

  - Checks if value exists
  - arr.includes(40); → true

- find()

  - Returns first matching element
  - arr.find(x => x > 25); → 30

- findIndex()

  - Returns index of first match
  - arr.findIndex(x => x > 25); → 2

#### Modifying & Slicing

- slice()

  - Extracts part of an array
  - arr.slice(1, 4); → [20,30,40]

- splice()

  - Adds/removes elements
  - arr.splice(2, 1, 100); → [10,20,100,40,50]

- concat()

  - Merges arrays
  - arr.concat([60, 70]); → [10,20,30,40,50,60,70]

- join()

  - Converts array to string
  - arr.join('-'); → "10-20-30-40-50"

- join()

  - Converts array to string
  - arr.join('-'); → "10-20-30-40-50"

- split()

  - Converts String to Array
  - let arr = "10-20-30-40-50"
  - arr.split('-'); → [10,20,30,40,50]

#### Iteration & Transformation

- forEach()

  - Loops through array
  - arr.forEach(x => console.log(x));

- map()

  - Transforms array
  - arr.map(x => x \* 2); → [20,40,60,80,100]

- filter()

  - Filters elements
  - arr.filter(x => x > 25); → [30,40,50]

- reduce()

  - Reduces to single value
  - arr.reduce((sum, x) => sum + x, 0); → 150

#### Sorting & Reversing

- sort()

  - Sorts array
  - [30,10,50].sort(); → [10,30,50]

- reverse()

  - Reverses array
  - [10,20,30].reverse(); → [30,20,10]

#### Special Methods

- flat()

  - Flattens nested arrays
  - [[1,2], [3,4]].flat(); → [1,2,3,4]

- fill()

  - Replaces elements
  - [1,2,3].fill(0); → [0,0,0]

- some()

  - Checks if any element matches condition
  - [10,20,30].some(x => x > 25); → true

- every()

  - Checks if all elements match condition
  - [10,20,30].every(x => x > 5); → true

### slice() vs. splice() in JavaScript

#### 1️⃣ slice() – Extracts a Portion of an Array (Without Modifying the Original)

- ✅ Does NOT modify the original array (returns a new array).
- ✅ Extracts elements from a specified range.
- ✅ Works with positive and negative indexes.

- Syntax

```js
array.slice(startIndex, endIndex);
```

- startIndex → Inclusive (starts extracting from here).
- endIndex → Exclusive (stops before this index).

```js
let arr = [10, 20, 30, 40, 50];

let newArr = arr.slice(1, 4); // Extracts elements from index 1 to 3
console.log(newArr); // [20, 30, 40]
console.log(arr); // [10, 20, 30, 40, 50] (Original remains unchanged)

let arr = [10, 20, 30, 40, 50];
console.log(arr.slice(-3)); // [30, 40, 50] (Extracts last 3 elements)
```

#### 2️⃣ splice() – Modifies the Original Array (Adds/Removes Elements)

- ❌ Modifies the original array (does not return a new array).
- ✅ Can remove, replace, or add elements at any position.

```js
array.splice(startIndex, deleteCount, item1, item2, ...);
```

- startIndex → Position where changes begin.
- deleteCount → Number of elements to remove.
- item1, item2, ... → Elements to insert (optional).

- Removing Elements

```js
let arr = [10, 20, 30, 40, 50];

arr.splice(1, 2); // Removes 2 elements starting from index 1
console.log(arr); // [10, 40, 50] (Modified)
```

- Replacing Elements

```js
let arr = [10, 20, 30, 40, 50];

arr.splice(2, 1, 99); // Replaces 30 with 99
console.log(arr); // [10, 20, 99, 40, 50]
```

- Adding Elements

```js
let arr = [10, 20, 30, 40, 50];

arr.splice(2, 0, 99, 100); // Inserts 99 and 100 at index 2
console.log(arr); // [10, 20, 99, 100, 30, 40, 50]
```

## IIFE (Immediately Invoked Function Expression)

#### An IIFE (Immediately Invoked Function Expression) is a function that is executed immediately after its creation. It is useful for avoiding variable pollution in the global scope and executing code right away.

### 1️⃣ Basic Syntax of IIFE

```js
(function () {
  console.log("IIFE executed!");
})();
```

- The function is wrapped in parentheses (function() { ... }), making it an expression.
- The trailing () immediately invokes the function.

### 2️⃣ Named vs. Anonymous IIFE

- 🔹 Anonymous IIFE

```js
(function () {
  console.log("Anonymous IIFE");
})();
```

- 🔹 Named IIFE
- The name myIIFE is only accessible inside the function, not in the global scope.

```js
(function myIIFE() {
  console.log("Named IIFE");
})();
```

#### 3️⃣ Arrow Function IIFE

```js
(() => {
  console.log("Arrow Function IIFE");
})();
```

#### 4️⃣ IIFE with Parameters

```js
(function (name) {
  console.log("Hello, " + name);
})("Ganesh");
```

#### 5️⃣ IIFE Returning a Value

```js
let result = (function () {
  return "Returned from IIFE";
})();
console.log(result); // Returned from IIFE
```

#### 6️⃣ Using IIFE to Create a Private Scop

- Avoid polluting the global scope
- ✔️ The variable count is not accessible globally.

```js
let counter = (function () {
  let count = 0; // Private variable

  return {
    increment: function () {
      count++;
    },
    getCount: function () {
      return count;
    },
  };
})();

counter.increment();
console.log(counter.getCount()); // 1
```

#### 7️⃣ IIFE with async / await

- ✔️ Used in asynchronous operations without polluting the global scope.

```js
(async function () {
  let data = await fetch("https://jsonplaceholder.typicode.com/todos/1").then(
    (response) => response.json()
  );
  console.log(data);
})();
```

#### 8️⃣ IIFE with Multiple Functions

```js
(function () {
  function greet() {
    console.log("Hello, Ganesh!");
  }
  function farewell() {
    console.log("Goodbye, Ganesh!");
  }

  greet();
  farewell();
})();
```

## Higher Order Function (HOF)

#### A Higher-Order Function (HOF) is a function that either takes another function as an argument or returns a function as its output.

#### 1️⃣ Why Use Higher-Order Functions?

- ✅ Code Reusability – Avoid repetition.
- ✅ Modularity – Break code into smaller, reusable parts.
- ✅ Functional Programming – Helps write clean, declarative code.

#### 2️⃣ Example: Higher-Order Function Taking a Function as an Argument

- 🔹 Here, operate() is a higher-order function because it takes another function (add or multiply) as an argument.

```js
function operate(a, b, operation) {
  return operation(a, b); // Calling the passed function
}

function add(x, y) {
  return x + y;
}

function multiply(x, y) {
  return x * y;
}

console.log(operate(5, 3, add)); // 8
console.log(operate(5, 3, multiply)); // 15
```

#### 3️⃣ Example: Higher-Order Function Returning a Function

- 🔹 greeting() returns a function, making it a higher-order function.

```js
function greeting(message) {
  return function (name) {
    console.log(message + ", " + name + "!");
  };
}

const sayHello = greeting("Hello");
sayHello("Ganesh"); // Hello, Ganesh!
sayHello("Arwat"); // Hello, Arwat!
```
