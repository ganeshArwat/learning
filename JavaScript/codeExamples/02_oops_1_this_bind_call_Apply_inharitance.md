# JS-2: OOPS-1 : This, Bind, Call, Apply, Inheritance

## Assignment

- Q1. JS Lecture 2: A1 - Make Array.last() method

```
Write code that enhances all arrays such that you can call the array.last() method on any array and it will return the last element.
If there are no elements in the array, it should return -1.

Write your solution inside the main() method, the test cases will be evaluated in the backend.

Sample Test Case 1:
Input:
let nums = [1,2,3];
main(); // calling the main function that would contain your solution.
console.log(nums.last());

Output:
3

Explanation: Calling nums.last() should return the last element: 3.

Sample Test Case 2:
Input:
let nums = [];
main();
console.log(nums.last());

Output:
-1

Explanation: Because there are no elements, return -1.
```

```js
function main() {
  Array.prototype.last = function () {
    if (this.length === 0) {
      return -1;
    } else {
      return this[this.length - 1];
    }
  };
}
```

- Q2. Q2. JS Lecture 2: A2 - Bind the Function

```
Implement bind method below
THANOS has snapped the finger, use the bind method in such a way that now iron man should be able to snap the finger again.

Explanation:

1. You are given boilerplate JS code with the following objects:

const thanos = {
    name: "THANOS",
    snap: function () {
        return this.name + " snapped the finger and half of the universe " + (this.name == "THANOS" ? "disappeared" : "came back")
    }
}

const ironman = {
    name: "IRON MAN"
}

console.log(thanos.snap())

2. Notice that ironman object doesn't have a snap method.
3. You need to utilise Javascript binding facility to make a binded function.
4. This function will be a bind of :
    4.1. snap function from thanos object
    4.2. and ironman object

A variable called 'bindedFunction' has been declared in the main function.
You need to update the main function and initialise the bindedFunction, such that the main function returns this bindedFunction.
Test cases will then be evaluated in the backend.
```

```js
const bindedFunction = thanos.snap.bind(ironman);
return bindedFunction;
```

- Q3. Q3. JS Lecture 2 Output? MCQ1

```js
let cap = {
  name: "Steve",
  sayHI: function () {
    console.log("HI from ", this.name);
  },
};

cap.sayHI();
let sayHi = cap.sayHI;
sayHi();
```

```
Output :
HI from  Steve
HI from  undefined
```

- Q4. JS Lecture 2 Output? MCQ2

```js
const cap = {
  name: "Steve",
  sayHI: function () {
    console.log("53 ", this.name);

    const iAmInner = () => {
      console.log("55", this.name);
    };

    iAmInner();
  },
};

cap.sayHI();
```

```
Output :
53  Steve
55 Steve
```

## Additional Question

- Q1. JS Core - Make Apply Polyfill

```
Write a polyfill for the apply method in JavaScript.

You need to complete the function applyPolyfill which takes three inputs:
1. fn - A function on which apply method needs to be polyfilled.
2. context - The value of this to be used when calling the function.
3. args - An array of arguments to be passed to the function.

The function applyPolyfill(fn, context, args), when called, should behave in a similar fashion as the inbuilt Function.prototype.apply() function in JavaScript.
Refrain from using the inbuilt Function.protoype.apply() function in JS, trivial test case would check for that.


Example:

function greet(country) {

return 'Hello, ' + this.name + ' from '+ country;
}

const person = {
name: 'John',
};

const result = applyPolyfill(greet, person, ['India']);
console.log(result);


Output:
Hello, John! from India
```

```js
function applyPolyfill(fn, context, args) {
  // Ensure that the context is an object (null/undefined handled)
  context = context || globalThis;

  // Create a unique temporary property on the context
  const tempFn = Symbol("tempFn");

  // Assign the function to this temporary property
  context[tempFn] = fn;

  // Call the function using the temporary property with the provided arguments
  const result = context[tempFn](...args);

  // Delete the temporary property to avoid pollution of the context
  delete context[tempFn];

  // Return the result
  return result;
}
```

- Q2. JS Lecture 2: H2 - Using call() method

```
Raw Problem

Implement a program that utilises call() method in Javascript to make the provided function work on different objects.

Explanation:
1. You have a main function that takes in 2 parameters:
1.1. obj -> A object with different set of values.
1.2. func -> A simple function that utilises the values from the object provided and returns a string.

2. You need to write a program using call() method, which makes the provided function 'func' use the object 'obj' to generate a string.
3. You then need to catch the returned string in the 'resultString' variable, which is then returned from the main function.

Note:
The value of obj and func will be totally different for all the test cases, so there is no scope of hard coding the problem.

Sample test case:

Input:
let obj = {
name: "bucky",
team: "Team Cap",
};
let func = function () {
return "Hello avengers this is " + this.name + " from " + this.team + " lets fight !";
};

console.log(main(obj, func))

Output:
Hello avengers this is bucky from Team Cap lets fight !
```

```js
function main(obj, func) {
  // Use call() to invoke the function with the provided obj as 'this'
  let resultString = func.call(obj);

  // Return the resultString
  return resultString;
}
```

- Q3. JS Lecture 2 Output? MCQ4

```js
const cap = {
  name: "Steve",
  sayHI: function () {
    console.log("53", this.name);
    function iAmInner() {
      console.log("55", this.name);
    }

    iAmInner();
  },
};

cap.sayHI();
```

```
Output :
53 Steve
55 undefined
```

- Q4. JS Lecture 2 Output? MCQ5

```js
let cap = {
  name: "Steve",
  sayHi: () => {
    console.log("HI from", this.name);
  },
};

cap.sayHi();
let sayHiAdd = cap.sayHi;
sayHiAdd();
```

```
Output :
HI from undefined
HI from undefined

```

- Q5. JS Lecture 2 Output? MCQ6

```js
Function.prototype.myBind = function (obj) {
  obj.fnRef = this;
  return function (...args) {
    obj.fnRef(...args);
  };
};

let abc = {
  name: "Jsbir",
};

let obj = {
  name: "Steve",
  sayHi: function () {
    console.log(this.name, "say's Hi");
    function inner() {
      console.log("insider inner", this.name);
    }
    let boundThisFN = inner.myBind(abc);
    boundThisFN();
  },
};

obj.sayHi();
```

```
Output :
Steve say's Hi
insider inner Jsbir
```
