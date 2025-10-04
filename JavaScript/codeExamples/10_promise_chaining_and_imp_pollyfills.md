# JS-10: Promise chaining and Imp polyfills

## Assignment

- Q1. Js Lecture 1 MCQ: Object

```js
function resolveAfterNSeconds(n, x) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(x);
    }, n);
  });
}

(function () {
  let a = resolveAfterNSeconds(1000, 1);
  a.then(async function (x) {
    let y = await resolveAfterNSeconds(2000, 2);
    let z = await resolveAfterNSeconds(1000, 3);
    let p = resolveAfterNSeconds(2000, 4);
    let q = resolveAfterNSeconds(1000, 5);
    console.log(x + y + z + (await p) + (await q));
  });
})();
```

```
Output :
15 after 6 seconds
```

- Q2. JS Lecture 9 MCQ: aa Promises

```js
const createPromise = () => Promise.resolve(1);

function func1() {
  createPromise().then(console.log);
  console.log(2);
}

async function func2() {
  await createPromise();
  console.log(3);
}

console.log(4);
func1();
func2();
```

```
Output :
4
2
1
3
```

- Q3. JS Lecture 9 MCQ: Error Handling

```
Which of the following statement is correct

1. try ,catch is synchronous in nature

2. try ,catch does not work on syntatic errors

3. type error , range error occur at runtime

4. all of the above
```

```
Output :
4. all of the above
```

- Q4. JS Lecture 9: H1 - Two Files in Series using await

```
Using async await complete the function twoSeries(file1, file2, ansArray),
which takes in two file names as file1 and file2 and ansArray

Write the code such that:
1. Both the files are serially read using the fetchByPromise(fileName)
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
async function twoSeries(file1, file2, ansArray) {
  //write your code here =========================================
  // Read file1 serially
  const content1 = await fetchByPromise(file1);
  ansArray.push(content1);

  // Read file2 serially
  const content2 = await fetchByPromise(file2);
  ansArray.push(content2);

  // Add final string after reading both files
  ansArray.push("All files have been read");
}
```

## Additional Question

- Q1. JS Lecture 9 MCQ: Spread rest

```
Which of the following correctly describes the behavior of the spread (…) and rest (…) operators in JavaScript?

1. The spread operator is used to merge multiple elements into an array, while the rest operator is used to split an array into multiple elements.

2. The spread operator is used to split an array into multiple elements, while the rest operator is used to merge multiple elements into an array.

3. Both the spread and rest operators are used to merge multiple elements into an array.

4. Both the spread and rest operators are used to split an array into multiple elements.
```

```
Output :
2. The spread operator is used to split an array into multiple elements, while the rest operator is used to merge multiple elements into an array.
```

- Q2. JS Lecture 9: H2 - N Files in Series using await

```
Using async await complete the function nSeries(fileArray, ansArray),
that takes in fileArray and ansArray, in which
fileArray is an array of file names.

Write the code such that:
1. All the files in the fileArray are serially read using the fetchByPromise(fileName)
2. Add the content of both files in the ansArray.
3. At the end of the contents, the ansArray should hold string "All files have been read"

Example:

let ansArray = [];
let fileArray = ["FILE 1", "FILE 2"];
nSeries(fileArray, ansArray);

Output:
ansArray = ['content : FILE 1', 'content : FILE 2', 'All files have been read']
```

```js
async function nSeries(fileArray, ansArray) {
  for (const file of fileArray) {
    const content = await fetchByPromise(file);
    ansArray.push(content);
  }
  ansArray.push("All files have been read");
}
```
