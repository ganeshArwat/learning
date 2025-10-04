## SPREAD REST DEFAULT

### The spread operator (...) in JavaScript is used to expand elements of an array, object, or iterable into individual elements. It is commonly used for copying, merging, or passing values efficiently.

#### 1. Spread Operator with Arrays

- Copy an array:

```js
const arr1 = [1, 2, 3];
const arr2 = [...arr1]; // Creates a new array copy
console.log(arr2); // [1, 2, 3]
```

- Merge arrays:

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const merged = [...arr1, ...arr2];
console.log(merged); // [1, 2, 3, 4, 5, 6]
```

- Adding element to an array

```js
const numbers = [1, 2, 3];
const newNumbers = [0, ...numbers, 4];
console.log(newNumbers); // [0, 1, 2, 3, 4]
```

- spread operator : partial deep copy till level 1.

```js
let arr = [1, 2, [3, 4], 5, 6];
// [value,value,ref,value,value]

// // spread copies value  from one array another array for the first level
let arr2 = [...arr]; // partial deep copy till level 1.
arr2.pop();
arr2.push(100);
arr2[2][0] = 500;
// arr2 = 300;
console.log("actual array", arr); // actual array [ 1, 2, [ 500, 4 ], 5, 6 ]
console.log("modified array", arr2); // modified array [ 1, 2, [ 500, 4 ], 5, 100 ]
```

#### 2. Spread Operator with Objects

- Copying an Object

```js
const obj1 = { name: "Ganesh", age: 23 };
const obj2 = { ...obj1 }; // Creates a shallow copy
console.log(obj2); // { name: "Ganesh", age: 23 }
```

- Merging Objects

```js
const obj1 = { name: "Ganesh" };
const obj2 = { age: 23 };
const mergedObj = { ...obj1, ...obj2 };
console.log(mergedObj); // { name: "Ganesh", age: 23 }
```

- Overriding Properties

```js
const obj1 = { name: "Ganesh", age: 23 };
const obj2 = { age: 25, city: "Mumbai" };
const updatedObj = { ...obj1, ...obj2 };
console.log(updatedObj); // { name: "Ganesh", age: 25, city: "Mumbai" }
```

#### 3. Spread Operator with Function Arguments

- Passing Array Elements as Arguments

```js
function sum(a, b, c) {
  return a + b + c;
}
const numbers = [1, 2, 3];
console.log(sum(...numbers)); // 6
```

## Rest Operator

### The Rest Operator (...) in JavaScript is used to collect multiple values into an array. It is commonly used in function parameters and array/object destructuring.

#### 1. Rest Operator in Function Parameters

- The rest operator gathers multiple arguments into an array.

```js
function sum(...numbers) {
  return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4, 5)); // 15
```

#### 2. Rest Operator in Array Destructuring

- You can use the rest operator to collect the remaining elements in an array.

```js
const [first, second, ...rest] = [10, 20, 30, 40, 50];

console.log(first); // 10
console.log(second); // 20
console.log(rest); // [30, 40, 50]
```

#### 3. Rest Operator in Object Destructuring

- It can be used to extract some properties while collecting the remaining ones into an object.

```js
const person = { name: "Ganesh", age: 23, city: "Mumbai", country: "India" };
const { name, ...details } = person;

console.log(name); // "Ganesh"
console.log(details); // { age: 23, city: "Mumbai", country: "India" }
```

## Rest Operator vs Spread Operator

### Purpose

- Rest
  - Collects elements into an array/object
- Spread
  - Expands an array/object into individual elements

### Usage

- Rest
  - Function parameters, destructuring
- Spread
  - Function arguments, copying/merging arrays/objects

### Example

- Rest
  - function sum(...nums) {}
- Spread
  - const newArr = [...arr1, ...arr2]

## CALL BY VALUE AND REFERENCE

### 1. Call by Value (Primitive Data Types)

#### When primitive data types (e.g., Number, String, Boolean, Undefined, Null, Symbol, BigInt) are passed to a function, their actual values are copied and passed. Any modification inside the function does not affect the original variable.

```js
function changeValue(x) {
  x = 20; // Modifying the copy
  console.log("Inside function:", x); // 20
}

let a = 10;
changeValue(a);
console.log("Outside function:", a); // 10 (unchanged)
```

```js
// Call By value.
function modifier2([...a], [...b]) {
  console.log("13", a, b); // 13 [ 4, 7, 9 ] [ 3, 6, 8 ]
  a[0] = 10;
  b[1] = 20;
  console.log("16", a, b); // 16 [ 10, 7, 9 ] [ 3, 20, 8 ]
}

let p = [4, 7, 9];
let q = [3, 6, 8];

console.log("20", p, q); // 20 [ 4, 7, 9 ] [ 3, 6, 8 ]
modifier2(p, q);
console.log("23", p, q); // 23 [ 4, 7, 9 ] [ 3, 6, 8 ]

// ([...a], [...b]) → The spread operator ([...]) creates a shallow copy of both arrays.
// a and b inside the function are new arrays (not references to arr1 and arr2).
// Modifying a or b inside the function does NOT affect the original arrays (arr1 and arr2).
```

### 2. Call by Reference (Objects, Arrays)

#### When non-primitive data types (like Objects and Arrays) are passed to a function, the reference (memory address) of the original data is passed. Modifications inside the function reflect in the original variable.

```js
function modifyObject(obj) {
  obj.name = "Ganesh"; // Modifying the actual object reference
}

let person = { name: "John" };
modifyObject(person);
console.log(person.name); // Ganesh (changed)
```

### Does JavaScript Truly Support Call by Reference?

#### No, JavaScript does not truly support Call by Reference. It only passes references by value. This means:

1. Modifying properties of an object (mutating the reference) affects the original object. ✅
2. Reassigning the reference inside a function does not affect the original object. ❌

```js
function reassign(obj) {
  obj = { name: "New Person" }; // Assigning a new object (this does not affect the original)
}

let person = { name: "John" };
reassign(person);
console.log(person.name); // John (unchanged)
```

## CALL BIND APPLY

### 1. Call

#### The .call() method in JavaScript is used to invoke a function with a specified this value and arguments. However, when working with arrays, call() behaves differently because arrays do not have their own methods that accept this.

- The call() method in JavaScript is used to invoke a function while explicitly setting this and passing arguments one by one.

- Syntax of call()

```js
functionName.call(thisArg, arg1, arg2, ...)
```

- thisArg → The value to be used as this inside the function.
- arg1, arg2, ... → Arguments to be passed to the function.
- If thisArg is null or undefined, JavaScript defaults to the global object (window in browsers, global in Node.js).

```js
const person1 = { name: "Ganesh" };
const person2 = { name: "Govind" };

function greet(message) {
  console.log(`${message}, my name is ${this.name}`);
}

greet.call(person1, "Hello"); // Output: Hello, my name is Ganesh
greet.call(person2, "Hi"); // Output: Hi, my name is Govind
```

```js
const obj1 = {
  name: "Ganesh",
  showName: function () {
    console.log(this.name);
  },
};

const obj2 = { name: "Govind" };

// Use obj1's method for obj2
obj1.showName.call(obj2); // Output: Govind
```

```js
let cap = {
  name: "Steve",
  team: "Cap",

  petersTeam: function (mem1, mem2) {
    console.log(`Hey ${this.name} I am your neighborhood's  
        spiderman and I belong to ${this.team}'s team with members  ${mem1} and ${mem2}`);
  },
};

let ironMan = {
  name: "Tony",
  team: "Iron Man",
};

cap.petersTeam("Umang", "Manisha");
// ironMan.petersTeam("Umang", "Manisha");
cap.petersTeam.call(ironMan, "Umang", "Manisha"); // it will not store the method in ironMan That's why it is called as only once we cant reuse it like bind
```

#### Call: borrow the method only once with defined number of param use petersTeam method -> only once

- ✅ We use call() to execute a function immediately with a different this value.
- ✅ It is not stored for future use, unlike bind().
- ✅ We must pass all arguments explicitly.
- ex.
- myfn = cap.petersTeam.Bind(ironMan);
- myfn("Umang", "Manisha");

### 2. Bind

#### The .bind() method in JavaScript is used to create a new function with a specific this value and preset arguments. Unlike call() and apply(), bind() does not execute the function immediately—instead, it returns a new function that can be invoked later.

- Syntax of bind()

```js
const newFunction = functionName.bind(thisArg, arg1, arg2, ...);
```

- thisArg → The value to be used as this inside the function.
- arg1, arg2, ... → Optional arguments that are permanently set in the new function.
- bind() returns a new function with this bound to thisArg.

```js
const person = {
  name: "Ganesh",
  greet: function () {
    console.log(`Hello, my name is ${this.name}`);
  },
};

const anotherPerson = { name: "Govind" };

// Create a new function with `this` bound to anotherPerson
const greetGovind = person.greet.bind(anotherPerson);

greetGovind(); // Output: Hello, my name is Govind
```

#### Partial Application (Pre-setting Arguments)

- With bind(), we can preset arguments, creating a partially applied function:

```js
function multiply(a, b) {
  return a * b;
}

// Create a function that always multiplies by 2
const double = multiply.bind(null, 2);

console.log(double(5)); // Output: 10
console.log(double(10)); // Output: 20
```

#### bind() with Event Listeners

- In event handlers, "this" can refer to the element triggering the event. We can use bind() to ensure this refers to a specific object:

- Without bind(), this inside handleClick would refer to "button", "not user".

```js
const button = document.querySelector("button");

const user = {
  name: "Ganesh",
  handleClick: function () {
    console.log(`Clicked by ${this.name}`);
  },
};

button.addEventListener("click", user.handleClick.bind(user));
```

### 2. Apply()

#### The .apply() method is similar to .call(), but instead of passing arguments individually, it takes them as an array. It immediately invokes the function with a specific this value.

- Syntax of apply()

```js
functionName.apply(thisArg, [arg1, arg2, ...])
```

- thisArg → The object to be used as this inside the function.
- [arg1, arg2, ...] → An array of arguments to pass to the function.

#### 1: Using apply() to Set this

- Here, we borrowed the fullName method and used apply() to call it with user as this.

```js
const person = {
  fullName: function () {
    console.log(`${this.firstName} ${this.lastName}`);
  },
};

const user = { firstName: "Ganesh", lastName: "Arwat" };

// Call `fullName` with `user` as `this`
person.fullName.apply(user);
// Output: Ganesh Arwat
```

#### 2: apply() vs call()

- The only difference between apply() and call() is how arguments are passed:
  - call() → Arguments are passed individually
  - apply() → Arguments are passed as an array
- ✅ Both work the same, but apply() is useful when arguments are in an array.

```js
function greet(city, country) {
  console.log(`Hello, I am ${this.name} from ${city}, ${country}`);
}

const person = { name: "Ganesh" };

// Using call()
greet.call(person, "Mumbai", "India");
// Output: Hello, I am Ganesh from Mumbai, India

// Using apply()
greet.apply(person, ["Mumbai", "India"]);
// Output: Hello, I am Ganesh from Mumbai, India
```

#### 3: Finding the Maximum or Minimum in an Array

- A common use case for apply() is using Math.max and Math.min on arrays:

```js
const numbers = [12, 45, 78, 23, 89];

const maxNumber = Math.max.apply(null, numbers);
console.log(maxNumber); // Output: 89

const minNumber = Math.min.apply(null, numbers);
console.log(minNumber); // Output: 12
```

#### 4: Using apply() with Built-in Methods

- We can also use apply() with array methods like slice() to clone an array:

```js
onst arr = [1, 2, 3, 4, 5];

// Clone array using apply()
const clonedArr = [].slice.apply(arr);
console.log(clonedArr); // Output: [1, 2, 3, 4, 5]
```

## POLYFILL OF CALL BIND APPLY

### PollyFill of Call

```js
Function.prototype.myCall = function (requiredObject, ...arrayAsArgument) {
  // get your function.
  const functionToBeInvoked = this;

  // copy your function in the requiredObject for temp basis.
  requiredObject.tempFunction = functionToBeInvoked;

  // Call your function.
  requiredObject.tempFunction(...arrayAsArgument);

  // Delete temp method.
  delete requiredObject.tempFunction;
};

// cap.petersTeam.myCall(ironMan, "thor", "loki",);
```

### PollyFill of Apply

```js
Function.prototype.myApply = function (requiredObject, arrayAsArgument) {
  // get your function.
  const functionToBeInvoked = this;

  // copy your function in the requiredObject for temp basis.
  requiredObject.tempFunction = functionToBeInvoked;

  // Call your function.
  requiredObject.tempFunction(...arrayAsArgument);

  // Delete temp method.
  delete requiredObject.tempFunction;
};

// let memberssArray = ["thor", "Rajneesh", "loki", "Manisha", "Suraj", "Priyank", "Umang"];
// let memberssArray = ["thor", "loki"];  // Max size of array allowed is 2 because of 2 argument.
// cap.petersTeam.myApply(ironMan, memberssArray);
```

### PollyFill of Bind

```js
Function.prototype.myBind = function (requiredObject) {
  // get your function.
  const functionToBeInvoked = this;

  return function (...arrayAsArgument) {
    functionToBeInvoked.call(requiredObject, ...arrayAsArgument);
  };
};

const boundFn2 = cap.petersTeam.myBind(ironMan);
boundFn2("Thor Bansal", "Rajneesh Kumar");
```
