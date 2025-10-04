# JS-3: Polyfills of call,bind ,apply & deep copy-shallow copy

## Assignment

- Q1. JS Core - Make Deep Copy

```
Complete the function 'makeDeepCopy(object)',

such that it returns a deep copy of the object being passed as a parameter.
Below is the definition of a deep copy of an object, to understand the problem task.

Deep Copy:
A deep copy of an object is a copy whose properties do not share the same references (point to the same underlying values) as those of the source object from which the copy was made. As a result, when you change either the source or the copy, you can be assured you're not causing the other object to change too

Note:
A simple object would be provided to you,
and the returned object from the function you write would be evaluated in the backend to ensure its a deep copy.

Example:
let ingredients_list = { dish: "noodles", recipe: { list: ["eggs", "flour", "water"] } };

If a change is being made to the list array of the deep copy of the above object 'ingredients_list',
it should not cause any change to the list elements of the original object.
```

```js
function makeDeepCopy(object) {
  // Base case or edge cases.
  if (typeof object !== "object" && !Array.isArray(object)) {
    return object;
  }

  // Create a new container on the basis of type whether it is a array or object.
  let objcopy = typeof object == "object" ? {} : [];

  // Copy all the key and values.
  for (let key in object) {
    objcopy[key] = makeDeepCopy(object[key]);
  }

  // return object after completion.
  return objcopy;
}
```

- Q2. JS Core - Make Bind Polyfill

```
Write a polyfill for the bind method in JavaScript.

You need to create a polyfill for the bind method, which allows you to set the context (the value of this) for a function and optionally preset some initial arguments.

You should implement a function customBind on the Function.prototype object. This function should accept a single argument obj, which represents the context (the value of this) to be used when calling the function.

When the customBind method is called on a function, it should return a new function that, when invoked, executes the original function with the specified context (obj) and any additional arguments passed to the bound function.

Your task is to complete the implementation of the customBind function.

Example:
function greet() {
return 'Hello, ' + this.name + '!';
}

const person = {
name: 'John',
};

const boundFunction = greet.customBind(person);
const result = boundFunction()
console.log(result);

Output:
Hello, John!
```

```js
Function.prototype.customBind = function (obj) {
  // Store the reference to the original function
  const originalFunction = this;

  // Return a new function
  return function (...args) {
    // Use 'apply' to call the original function with the correct context and arguments
    return originalFunction.apply(obj, args);
  };
};
```

- Q3. JS Lecture 3 MCQ: call by ref 1

```js
function modifier(a, b) {
  a = 10;
  b = 20;
}
let p = [4, 7, 9];
let q = [3, 6, 8];
modifier(p, q);
console.log(p, q);
```

```
Output :
[ 4, 7, 9 ] [ 3, 6, 8 ]
```

- Q4. JS Lecture 3 MCQ: Deep vs Shallow

```
What is the key difference between deep copy and shallow copy
```

```
Output :
Deep copy creates an exact copy of the original object, including all its nested objects, while shallow copy only creates copies of the top-level properties.
```

- Q5. JS Lecture 3 MCQ: Creating Shallow Copy

```
Which of the following methods can be used to create a shallow copy of an object in JavaScript?
```

```
Output :
a spread operator
b Object.assign()
```

## Additional Question

- Q1. JS Core - Make Call Polyfill

```
Write a polyfill for the call method in JavaScript.

You need to create a polyfill for the call method, which allows you to invoke a function with a specified context and any number of arguments.

Your task is to implement a function customCall on the Function.prototype object. This function should accept two or more arguments: obj, which represents the context (the value of this) to be used when calling the function, and ...args, which represents the arguments to be passed to the function.

When the customCall method is called on a function, it should execute the original function with the specified context (obj) and the provided arguments (args).

Your implementation should not rely on the inbuilt call method in JavaScript.

Note: Avoid using the inbuilt call method in JavaScript, as trivial test cases will check for that.



Example:
function greet() {
return 'Hello, ' + this.name + '!';
}

const person = {
name: 'John',
};

const result = greet.customCall(person);
console.log(result);

Output:
Hello, John!
```

```js
Function.prototype.customCall = function (obj) {
  obj.funref = this;
  return obj.funref();
};
```

- Q2. JS Core - Flatten an Array

```
Complete the function 'flatten(array)',

such that it takes an array and returns a single flattened array of values,
regardless of how many nested arrays are in the input array.

Below is an example to further understand the requirement of the question.

Example:

let array = [1,2,3,[4,5],[6,7,8,[9,10,11]]];

console.log(flatten(array));

Output:

[1,2,3,4,5,6,7,8,9,10,11]

```

```js
function flatten(array) {
  let result = [];
  for (let i = 0; i < array.length; i++) {
    if (Array.isArray(array[i])) {
      temp = flatten(array[i]);
      for (let j = 0; j < temp.length; j++) {
        result.push(temp[j]);
      }
    } else {
      result.push(array[i]);
    }
  }

  return result;
}
```

- Q3. JS Lecture 3 MCQ: call by ref 2

```js
function modifier(a, b) {
  a = 10;
  b = 20;

  console.log(a, b);
}

let p = [4, 7, 9];
let q = [3, 6, 8];
modifier(p, q);
```

```
Output :
10 20
```

- Q4. JS Lecture 3 MCQ: call by ref 3

```js
function modifier(a, b) {
  a[0] = 10;
  b[0] = 20;
}

let p = [4, 7, 9];
let q = [3, 6, 8];

modifier(p, q);
console.log(p, q);
```

```
Output :
[10, 7, 9] [20, 6, 8]
```

- Q5. JS Lecture 3 MCQ: Creating Deep Copy

```
Which of the following methods can be used to create a deep copy of an object in JavaScript?
```

```
Output :
JSON.stringify and JSON.parse the object
```
