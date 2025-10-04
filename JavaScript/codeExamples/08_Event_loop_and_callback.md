# JS-8: Event loop and Callback

## Assignment

- Q1. JS Core - Custom setInterval

```
You are given a coding assignment where your task is to implement a custom mySetInterval function using the built-in setTimeout function in JavaScript. The mySetInterval function should allow you to repeatedly execute a callback function at a specified time interval until a given end time is reached.

You need to complete the main function, which has the following signature:

function main(intervalTime, endTime, message, arr) {
    // Write Code Here
}

The main function takes four parameters:

  intervalTime (integer): The time interval, in milliseconds, at which the callback function should be executed.
  endTime (integer): The time, in milliseconds, when the interval execution should stop.
  message (string): The message to be appended to the array arr during each execution of the callback function.
  arr (array): An array where the messages from the callback function will be stored.

Your task is to implement the mySetInterval function and use it within the main function.

The mySetInterval function should have the following signature:

function mySetInterval(callback, time) {
    // Write Code Here
}

The mySetInterval function takes two parameters:

  callback (function): The callback function to be executed repeatedly at the specified time interval.
  time (integer): The time interval, in milliseconds, at which the callback function should be executed.
Inside the mySetInterval function, you need to implement the logic to execute the callback function repeatedly at the specified time interval until explicitly stopped.

Please note that:
  Don't make changes to the boilerplate code.
  Use of in-built setInterval function is prohibited.
```

```js
function main(intervalTime, endTime, message, arr) {
  // Write Code Here ==============================
  function mySetInterval(callback, time) {
    let currTime = 0;
    if (currTime >= endTime) return;
    let repeat = () =>
      setTimeout(() => {
        callback();
        currTime = currTime + intervalTime;
        if (currTime <= endTime) repeat();
      }, intervalTime);

    repeat();
  }

  // Don't make any changes to below code X=X=X=X=X=X=X=X=X=X=X=X=X
  let i = mySetInterval(function () {
    arr.push(message);
  }, intervalTime);
  // X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X=X
}
```

- Q2. JS Lecture 7 MCQ: Which component?

```
Which component handles the execution of asynchronous code/callbacks
```

```
Output :
Event loop
```

- Q3. JS Lecture 7 MCQ: Async Programming

```
What is the main idea behind asynchronous programming in JavaScript?
```

```
Output :
To handle long-running tasks without blocking the main thread.
```

- Q4. JS Lecture 7 MCQ: setTimeout output

```js
console.log("1");

setTimeout(function () {
  console.log("2");
});

console.log("3");
```

```
Output :
1
3
2
```

- Q5. JS Lecture 7 MCQ: setTimeout Closure

```js
for (var i = 0; i < 3; i++) {
  setTimeout(function log() {
    console.log(i); // What is logged?
  }, 1000);
}
```

```
Output :
3
3
3
```

## Additional Question

- Q1. Lecture 7: H1 - Two Files in Series

```
Complete the function twoSeries(file1, file2, ansArray),
which takes in two file names as file1 and file2 and ansArray

Write the code such that:
1. Both the files are serially read using the fetchByCb(fileName, callback)
2. Add the content of both files in the ansArray.
3. At the end of the contents, the ansArray should hold string "All files have been read"

Example:

Input:
let ansArray = [];
twoSeries('FILE 1', 'FILE 2', ansArray)';

Output:
ansArray = ['content : FILE 1', 'content : FILE 2', 'All files have been read']
```

```js
function twoSeries(file1, file2, ansArray) {
  const fetchFiles = (idx, files) => {
    if (idx >= files.length) {
      ansArray.push("All files have been read");
      return;
    }

    fetchByCb(files[idx], (data) => {
      ansArray.push(data);
      fetchFiles(idx + 1, files);
    });
  };

  fetchFiles(0, [file1, file2]);
}
```

- Q2. Lecture 7: H2 - n Files in Series

```
**Raw Problem**
Complete the function nSerialReader(idx, files, ansArray),
which takes:
1. idx => current index, which is initially 0
2. files => an array of strings, which are file names
3. ansArray => an empty array , in which the contents should be pushed

Write the code such that:
1. All the elements in files array are serially read using the fetchByCb(fileName, callback)
2. Add the content of each file in the ansArray.
3. For every file prepend it with "content->"

Example:

Input:
let ansArray = [];
let files = ['file1.txt', 'file2.txt', 'file3.txt']
serialReader(0, files, ansArray)

Output:
ansArray = ['content -> content of file1.txt', 'content -> content of file2.txt', 'content -> content of file3.txt']
```

```js
function nSerialReader(idx, files, ansArray) {
  if (idx >= files.length) return;

  fetchByCb(files[idx], (content) => {
    ansArray.push(`content -> ${content}`);
    nSerialReader(idx + 1, files, ansArray);
  });

  return ansArray;
}
```

- Q3. JS Lecture 7 MCQ: While Loop Output

```js
let a = true;
console.log("Before");
setTimeout(() => {
  a = false;
  console.log("I broke the while loop");
}, 1000);
console.log("After");

while (a) {}
```

```
Output :
Before
After
infinite while loop
```

- Q4. JS Lecture 7 MCQ: Before After

```js
console.log("Before");

const cb2 = () => {
  console.log("set timeout 1");
  while (1) {}
};
const cb1 = () => console.log("hello");
setTimeout(cb2, 1000);

setTimeout(cb1, 2000);

console.log("After");
```

```
Output :
Before
After
set timeout 1
```
