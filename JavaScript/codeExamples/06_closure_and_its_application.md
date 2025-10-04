# JS-6: Closure and It's application

## Assignment

- Q1. JS Core - Flatten an Object

```
You are given an object that contains nested objects. The task is to write a function to flatten the object, bringing all the keys of nested objects to the same level. Flattening means to create new key-value pairs where the keys represent the nested structure using dot notation.

Function Signature:

function flattenObject(obj) => Object

Constraints:
  The input object can have nested objects of arbitrary depth.
  The input object can have various data types as values, including objects, arrays, strings, numbers, etc.

Example:

Input:
const obj = {
  newObj: {
    obj2: {
      obj5: {
        one: 1,
      },
    },
  },
  obj3: {
    obj4: {
      two: 2
    },
  },
};

Output:
{
  'newObj.obj2.obj5.one': 1,
  'obj3.obj4.two': 2,
}
```

```js
function flattenObject(ob) {
  var flatObj = {};

  for (let [key, val] of Object.entries(ob)) {
    if (typeof val === "object" && !Array.isArray(val) && val != null) {
      let ret = flattenObject(val);
      for (let [k, v] of Object.entries(ret)) {
        flatObj[`${key}.${k}`] = v;
      }
    } else {
      flatObj[key] = val;
    }
  }
  return flatObj;
}
```

- Q2. JS Core - Function Currying 1

```
You are tasked with creating a function fn that allows for function chaining and keeps track of the number of function calls made. Each time the function is called, it returns another function, and the count of function calls is incremented. The function chain can be terminated by passing a specific value.

Constraints:
  The function chain can have an arbitrary number of function calls.
  The function chain is terminated by passing the value 0 to the innermost function

Examples:

  Example 1:
  fn()()()()(0)
  Output:
  4

  Example 2:
  fn()()()(0)
  Output:
  3

  Example 3:
  fn()()()()()(0)
  Output:
  5
```

```js
function fn() {
  let count = 1;
  return function innerFn(param) {
    if (param === 0) {
      return count;
    }

    count++;
    return innerFn;
  };
  return innerFn;
}
```

- Q3. JS Lecture 5 MCQ: Lexical

```js
var varName = 10;
function b() {
  console.log(varName);
}
function fn() {
  var varName = 20;
  b();
  console.log(varName);
}
fn();
```

```
Output :
10
20
```

- Q4. JS Lecture 5 MCQ: Closure

```js
function outer() {
  let arrFn = [];
  let i;
  for (i = 0; i < 3; i++) {
    arrFn.push(function fn() {
      console.log(i);
    });
  }
  return arrFn;
}
let arrFn = outer();
arrFn[0]();
arrFn[1]();
arrFn[2]();
```

```
Output :
3
3
3
```

## Additional Question

- Q1. JS Core - Function Currying 2

```
You are required to implement a function f that calculates the product of two numbers, x and y. The function should support two different function call patterns: f(x, y) and f(x)(y).

Constraints:
  The function f should be able to handle positive and negative integer values for x and y.
  The function call patterns f(x, y) and f(x)(y) will only involve numerical inputs.

Example:
f(3, 4);
f(3)(4);

Output:
12
12
```

```js
function f(y, x) {
  return x ? x * y : (x) => x * y;
}
```

- Q2. JS Lecture 5 MCQ: Lexical Scope 2

```js
let a;

console.log(a);

function A() {
  let a = 2;
  console.log(a);

  function C() {
    console.log(a);

    function D() {
      console.log(a);

      a = 2;
    }
    D();
    a = 3;
  }
  C();
}

a = 3;

A();
```

```
Output :
undefined
2
2
2
```

- Q3. JS Lecture 5 MCQ: Lexical Scope 3

```js
let a;

console.log(a);

function B() {
  let a;
  console.log(a);

  function E() {
    a = 6;
    console.log(a);
  }

  a = 2;
  E();
  console.log(a);
}

a = 3;

B();
```

```
Output :
undefined
undefined
6
6
```

- Q4. JS Lecture 5 MCQ: Lexical Scope 4

```js
let a;

console.log(a);

function F() {
  console.log(a);
  a = 3;
}

a = 2;

F();
```

```
Output :
undefined
2
```

- Q5. JS Lecture 5 MCQ: Closure 2

```js
function createCounter(init, delta) {
  function count() {
    init = init + delta;
    return init;
  }
  return count;
}
let c1 = createCounter(10, 5);
let c2 = createCounter(5, 2);

console.log(c1());
console.log(c2());
console.log(c1());
console.log(c2());
```

```
Output :
15
7
20
9
```
