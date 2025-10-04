# JS-4: Array , HOFs and it's Polyfills

## Assignment

- Q1. JS Core - Make Reduce Polyfill

```
Write a polyfill of 'reduce'

You need to complete the function reduce, which receives 2 inputs:
1. 'arr'
1.1. An array of numbers
2. 'reducer'
2.1. A function that does some mathematical operation on 2 input numbers and returns the resultant.
2.2. reducer(num1, num2) returns a resultant.

The function reduce(arr, reducer), when called, should behave in a similar fashion as the inbuilt Array.prototype.reduce() function in JavaScript.
Refrain from using the inbuilt Array.prototype.reduce() function in JS, a trivial test case would check for that.

Input :
arr = [2, 3, 4, 5]
reducer = fn(a,b){ return a+b }

reduce(arr, reducer)

Output :
14

Input :
arr = [2, 3, 4]
reducer = fn(a,b){ return a-b }

reduce(arr, reducer)

Output :
-5
```

```js
function reduce(arr, reducer) {
  // Edge case: if the array is empty, return undefined
  if (arr.length === 0) return undefined;

  // Initialize the accumulator with the first element of the array
  let accumulator = arr[0];

  // Iterate through the array starting from the second element
  for (let i = 1; i < arr.length; i++) {
    // Apply the reducer function to the accumulator and current element
    accumulator = reducer(accumulator, arr[i]);
  }

  // Return the final reduced value
  return accumulator;
}
```

- Q2. JS Core - The number function

```
Write a function 'number' which accepts three inputs two numbers x, y and a function (fn).
The number function applies a function (fn) to x and y and returns the result.

Input :
3, 4, sum

Output :
7

Note that you have been provided with sum, mult, diff functions in the boilerplate. Corresponding to the following output:
number(3,4,sum); 7
number(3,4,mult); 12
number(3,4,diff); -1
```

```js
function number(x, y, fn) {
  return fn(x, y);
}
```

- Q3. JS Core - Sort with Helper

```
You are given an array of objects representing books in a library.
Each object contains details such as the author, title, and library ID of a book.
Your task is to write a program that sorts the array in alphabetical order based on the book titles.

Example
Input
[
  { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254 },
  { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264 },
  { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245 }
]

Output
[
  { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245 },
  { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254 },
  { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264 }
]
Note: The sortLibrary function takes the library array as input.

Example usage:

const library = [
  { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254 },
  { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264 },
  { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245 }
];

const sortedLibrary = sortLibrary(library);
console.log(sortedLibrary);
```

```js
function sortLibrary(library) {
  // Use the Array.prototype.sort() method to sort the library array by title
  library.sort((a, b) => {
    // Compare titles in a case-insensitive manner
    return a.title.localeCompare(b.title);
  });
  return library;
}
```

- Q4. JS Lecture 4 MCQ: Output for this?

```js
var result = (function () {
  var name = "John";
  return "Hello, " + name + "!";
})();
console.log(result);
```

```
Output :
"Hello, John!"
```

- Q5. JS Lecture 4 MCQ: What is HOF

```
Which of the following statements accurately describes the concept of Higher Order Functions in JavaScript?
```

```
Output :
Higher Order Functions are functions that take other functions as arguments or return functions as their results.
```

## Additional Question

- Q1. JS Core - Make Map Polyfill

```
Write a polyfill of 'map'

You need to complete the function reduce, which receives 2 inputs:
1. 'arr'
1.1. An array of numbers
2. 'callback'
2.1. A function that takes a number as input, performs some mathematical operation on that number and returns the end value.
2.2. callback(num) returns a new number.
2.3. For each element of the input arr, you need to store the returned number in the answer. (mapped array)

The function map(arr, callback), when called, should behave in similar fashion as inbuilt Array.prototype.map() function in JavaScript.
Refrain from using the inbuilt Array.protoype.map() function in JS, trivial test case would check for that.


Example 1:
arr = [1, 2, 3, 4, 5];
callback = fn(num) => num * num;

Output:
[1, 4, 9, 16, 25]

Example 2:
arr = [1, 2, 3, 4, 5];
callback = fn(num) => num * 2;

Output:
[2, 4, 6, 8, 10]
```

```js
function map(arr, callback) {
  // Create a new array to hold the results
  const result = [];

  // Iterate through each element in the input array
  for (let i = 0; i < arr.length; i++) {
    // Apply the callback function to each element and push the result to the result array
    result.push(callback(arr[i], i, arr));
  }

  // Return the new array with the transformed elements
  return result;
}
```

- Q2. JS Core - Make Filter Polyfill

```
Write a polyfill of 'filter'

You need to complete the function reduce, which receives 2 inputs:
1. 'arr'
1.1. An array of numbers
2. 'callback'
2.1. A function that does takes a number as input and returns a true or false value in return.
2.2. callback(num) returns a boolean.
2.3. For each element of the array, if returned boolean is:
2.3.1. True: The element will be in the filtered array.
2.3.2. False: The element will not be in the filtered array.

The function filter(arr, callback), when called, should behave in similar fashion as inbuilt Array.prototype.filter() function in JavaScript.
Refrain from using the inbuilt Array.protoype.filter() function in JS, trivial test case would check for that.


Example 1:
arr = [1, 2, 3, 4, 5];
callback = fn(num) => num % 2 === 0;

Output:
[2, 4]

Example 2:
arr = [1, 2, 3, 4, 5];
callback = fn(num) => num < 4;

Output:
[1, 2, 3]
```

```js
function filter(arr, callback) {
  // Create a new array to hold the filtered elements
  const result = [];

  // Iterate through each element in the input array
  for (let i = 0; i < arr.length; i++) {
    // Apply the callback function to each element and check if it's true
    if (callback(arr[i], i, arr)) {
      // If the callback returns true, include the element in the result array
      result.push(arr[i]);
    }
  }

  // Return the new array with the filtered elements
  return result;
}
```

- Q3. JS Lecture 4 MCQ: logging a function

```js
console.log(getResult());
var getResult = function () {
  return "Hello World";
};
```

```
Output :
TypeError: getResult is not a function

In JavaScript, hoisting moves variable and function declarations to the top of their scope before execution. However, only declarations are hoisted, not initializations.

Solution:
console.log(getResult());

function getResult() {
  return "Hello World";
}

```

- Q4. JS Lecture 4 MCQ: MultiplyBy2

```js
var x = 5;
function multiplyByTwo() {
  x *= 2;
}
multiplyByTwo();
console.log(x);
```

```
Output :
10
```

- Q5. JS Lecture 4 MCQ: Map and Filter

```js
const result = [1, 2, 3, 4, 5]
  .map((num) => num * 2)
  .filter((num) => num % 3 === 0);

console.log(result);
```

```
Output :
[6]
```
