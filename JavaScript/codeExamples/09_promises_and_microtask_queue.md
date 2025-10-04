# JS-9: Promises and MicroTask Queue

## Assignment

- Q1. JS Lecture 8 MCQ 1: Output?

```js
console.log(1);
setTimeout(function () {
  console.log(3);
});
console.log(4);
setTimeout(function () {
  console.log(2);
});
Promise.resolve().then(function () {
  console.log(5);
});
console.log(6);
```

```
Output :
1
4
6
5
3
2
```

- Q2. JS Lecture 8 MCQ 2: Output?

```js
let p = new Promise(function (resolve, reject) {
  setTimeout(function () {
    reject(new Error("some value"));
  }, 2000);

  resolve("some error");

  setTimeout(function () {
    reject(new Error("some value"));
  }, 2000);

  resolve("some error");

  setTimeout(function () {
    reject(new Error("some value"));
  }, 2000);
});

p.then(null, function (err) {
  console.log(1);
  console.log(err);
});

p.catch(function (err) {
  console.log(2);
  console.log(err);
});

p.finally(function () {
  console.log(1);
});

p.finally(function () {
  console.log(2);
}).then(function (val) {
  console.log(val);
});

p.then(
  function (val) {
    console.log(val);
  },
  function (err) {
    console.log(err);
  }
);
```

```
Output :
1
2
some error
some error
```

- Q3. JS Lecture 8 MCQ 3: Output?

```js
Promise.resolve(1)
  .finally((data) => {
    console.log(data);
    return Promise.reject("error");
  })
  .catch((error) => {
    console.log(error);
    throw "error2";
  })
  .finally((data) => {
    console.log(data);
    return Promise.resolve(2).then(console.log);
  })
  .then(console.log)
  .catch(console.log);
```

```
Output :
undefined
error
undefined
2
error2
```

- Q4. JS Lecture 8 MCQ 4: Output?

```js
const promise1 = Promise.resolve(1);
const promise2 = Promise.resolve(2);
const promise3 = Promise.resolve(3);
const promise4 = Promise.reject(4);

const promiseAll = async () => {
  const group1 = await Promise.all([promise1, promise2]);
  const group2 = await Promise.all([promise3, promise4]);
  return [group1, group2];
};

promiseAll().then(console.log).catch(console.log);
```

```
Output :
4
```

- Q5. JS Lecture 8: Promisify a Function

```
You are tasked with creating a promisify function that can turn any given function into a promisified version of itself. The objective is to convert a function that uses traditional callback-based asynchronous programming into a function that returns a promise.

The promisify function should accept a single argument fn, which is the function to be promisified. The promisified function should have the same behavior as the original function but should return a promise instead of using a callback.

The function fn to be promisified will always have a callback as its last argument. The callback function will have the following signature:

function(result) {}
The promisify function should return a new function that wraps the original function fn. Once you have implemented promisify, you should apply it to the provided function exampleFn and assign the resulting promisified function to a variable called promisified. The promisified function should be invoked with the appropriate arguments and then chained with .then() calls to handle the resolved value of the promise. This is how the function should work:

Example:
function exampleFn(a, b, cb) {
    cb(a + b);
}

const promisified = promisify(exampleFn);
promisified(5, 15).then(res => console.log(res));

Output: 20

```

```js
function promisify(fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      fn(...args, (result, error) => {
        if (error) {
          reject(error);
        } else {
          resolve(result);
        }
      });
    });
  };
}
```

## Additional Question

- Q1. JS Lecture 8 MCQ 5: Output?

```js
setTimeout(() => console.log("timeout"), 0);

Promise.resolve().then(() => console.log("promise"));
```

```
Output :
promise
timeout
```

- Q2. JS Lecture 8 MCQ 6: Output?

```js
const firstPromise = new Promise((res, rej) => {
  setTimeout(res, 500, "one");
});

const secondPromise = new Promise((res, rej) => {
  setTimeout(res, 100, "two");
});
Promise.race([firstPromise, secondPromise]).then((res) => console.log(res));
```

```
Output :
two
```

- Q3. JS Lecture 8 MCQ 7: Output?

```
Why promises are better then cbs ?

It solves problem of inversion of control

microtask task queue has higher priority then cb queue

promises can be resolved or rejected once in the life time after that there

all of the above


```

```
Output :
all of the above
```

- Q4. JS Lecture 8: Two Files in Series by Promise

```
Complete the function twoSeries(file1, file2, ansArray), which takes in two file names as file1 and file2 and ansArray

Write the code such that:

Both the files are serially read using the fetchByPromise(fileName)
Add the content of both files in the ansArray.
At the end of the contents, the ansArray should hold string "All files have been read"
Example:
Input:
let ansArray = [];
twoSeries('FILE 1', 'FILE 2', ansArray)';

Output:
ansArray = ['content : FILE 1', 'content : FILE 2', 'All files have been read']
```

```js
function fetchByPromise(fileName) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      resolve(`content : ${fileName}`);
    }, 100 * Math.random());
  });
}
```
