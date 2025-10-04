## Lexical Scope

### 1️⃣ What is Lexical Scope?

#### Lexical Scope means that a function's scope is determined by where it is written in the code, not where it is called.

- Inner functions can access variables from their outer functions.
- Outer functions cannot access variables from their inner functions.
- Global variables are accessible anywhere.

### 2️⃣ Example of Lexical Scope

- 🔹 innerFunction() is defined inside outerFunction(), so it inherits the scope of outerFunction().

```js
function outerFunction() {
  let outerVar = "I'm from outerFunction";

  function innerFunction() {
    console.log(outerVar); // ✅ Can access outerVar
  }

  innerFunction();
}

outerFunction();
```

```js
var varName = 10;
function b() {
  console.log("In function b the value of varName: ", varName);
}

function fn(callback) {
  var varName = 20;
  callback(); // 10
  console.log("In function fn the value of varName: ", varName); // 20
}
fn(b);
```

### 3️⃣ Lexical Scope with Multiple Levels

```js
function firstLevel() {
  let a = "First Level";

  function secondLevel() {
    let b = "Second Level";

    function thirdLevel() {
      let c = "Third Level";
      console.log(a); // ✅ Accessing 'a' from firstLevel
      console.log(b); // ✅ Accessing 'b' from secondLevel
      console.log(c); // ✅ Accessing 'c' from thirdLevel
    }

    thirdLevel();
  }

  secondLevel();
}

firstLevel();
```

### 4️⃣ Lexical Scope and Closures

#### Lexical Scope enables closures, which allow inner functions to remember variables from their outer scope even after the outer function has finished executing.

- ✅ The innerFunction() remembers count because of Lexical Scope + Closures.

```js
function outerFunction() {
  let count = 0;

  return function innerFunction() {
    count++;
    console.log("Count:", count);
  };
}

const counter = outerFunction();
counter(); // Count: 1
counter(); // Count: 2
counter(); // Count: 3
```

### 5️⃣ Scope Chain (How JavaScript Searches for Variables)

- When a variable is accessed inside a function, JavaScript searches for it in the following order:

  1. Inside the function itself
  2. Inside its parent function
  3. Inside the global scope

```js
let globalVar = "I'm global";

function firstFunction() {
  let firstVar = "I'm in firstFunction";

  function secondFunction() {
    let secondVar = "I'm in secondFunction";

    console.log(globalVar); // ✅ Found in global scope
    console.log(firstVar); // ✅ Found in firstFunction
    console.log(secondVar); // ✅ Found in secondFunction
  }

  secondFunction();
}

firstFunction();
```

### 6️⃣ Common Mistake: Trying to Access Variables from an Inner Scope

```js
function outerFunction() {
  let secret = "Hidden Message";

  function innerFunction() {
    console.log(secret); // ✅ Allowed
  }

  innerFunction();
}

console.log(secret); // ❌ ERROR! 'secret' is not defined in global scope
```

### 7️⃣ Summary

- ✅ Lexical Scope means functions can access variables from their outer scope.
- ✅ Scope Chain – JavaScript searches for variables from inside → outside.
- ✅ Closures use Lexical Scope to "remember" variables after the outer function has executed.
- ✅ Inner functions can access outer variables, but not the other way around!

## Closure

### 1️⃣ What is a Closure?

#### A closure is when an inner function "remembers" variables from its outer function even after the outer function has finished executing.

- 💡 Closures happen because of Lexical Scope!

### 2️⃣ Basic Example of a Closure

- 🔹 Even though outerFunction() has already finished executing, innerFunction() still remembers the message variable.

```js
function outerFunction() {
  let message = "Hello, Ganesh!";

  function innerFunction() {
    console.log(message); // ✅ Accessing 'message' from outerFunction
  }

  return innerFunction;
}

const closureFunc = outerFunction(); // outerFunction executed
closureFunc(); // Hello, Ganesh // But 'innerFunction' still remembers 'message'!
```

### 3️⃣ Real-World Example: Counter with Closures

- The inner function "remembers" the count variable even after createCounter() has executed.

```js
function createCounter() {
  let count = 0;

  return function () {
    count++;
    console.log("Count:", count);
  };
}

const counter = createCounter(); // Creates a new closure

counter(); // Count: 1
counter(); // Count: 2
counter(); // Count: 3
```

### 4️⃣ Closures in Event Listeners

- Closures are useful in event listeners to store data in memory.

```js
function clickHandler() {
  let clicks = 0;

  return function () {
    clicks++;
    console.log(`Button clicked ${clicks} times`);
  };
}

const button = document.createElement("button");
button.innerText = "Click Me";
document.body.appendChild(button);

const handleClick = clickHandler();
button.addEventListener("click", handleClick);
```

### 5️⃣ Closures with setTimeout

- Closures allow functions to remember variables even when executed later.

- 🔹 setTimeout() delays execution, but the inner function remembers message.

```js
function delayedMessage(message, delay) {
  setTimeout(function () {
    console.log("Message:", message);
  }, delay);
}

delayedMessage("Hello after 3 seconds!", 3000);
```

### 6️⃣ Private Variables Using Closures

- Closures are useful for data encapsulation (private variables).
- Here, balance is private because it is only accessible inside the closure!

```js
function bankAccount() {
  let balance = 1000;

  return {
    deposit(amount) {
      balance += amount;
      console.log(`Deposited: ${amount}, New Balance: ${balance}`);
    },
    withdraw(amount) {
      if (amount > balance) {
        console.log("Insufficient balance!");
      } else {
        balance -= amount;
        console.log(`Withdrawn: ${amount}, New Balance: ${balance}`);
      }
    },
    getBalance() {
      console.log(`Balance: ${balance}`);
    },
  };
}

const myAccount = bankAccount();
myAccount.deposit(500); // Deposited: 500, New Balance: 1500
myAccount.withdraw(200); // Withdrawn: 200, New Balance: 1300
myAccount.getBalance(); // Balance: 1300
```

### 7️⃣ Closures in Loops - Common Mistake

Be careful when using closures in loops with var!

```js
for (var i = 1; i <= 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 1000);
}
```

- ✅ Expected: 1 2 3
- ❌ Output: 4 4 4

- var is function-scoped, so by the time setTimeout runs, the loop has finished, and i is 4.
- 🔹 Solution: Use let instead of var!

```js
let iamINGEC = 200;
function getFirstName(firstName) {
  console.log("I have got your first Name");
  iamINGEC++;
  return function getLastName(lastName) {
    console.log("I have got Your last Name");
    iamINGEC++;
    return function greeter() {
      console.log(`Hi I am ${firstName} ${lastName}`); // closure
      console.log("Hi GEC", iamINGEC); // Lexical scope
      iamINGEC++;
    };
  };
}

const lastNameRtrn = getFirstName("Rajneesh");
const greeterRtrn = lastNameRtrn("Kumar");
greeterRtrn(); // iamINGEC=201;

greeterRtrn(); // iamINGEC=202
greeterRtrn(); //  iamINGEC=203
console.log("Final Value: ", iamINGEC); // Final iamINGEC = 205
// The variable iamINGEC is not redeclared inside functions, so it refers to the global scope.
```

## Currying

### Currying

#### Currying is a technique in JavaScript where a function takes multiple arguments one at a time instead of all at once.

### 1️⃣ What is Currying?

#### Currying is when you transform a function with multiple arguments into a sequence of nested functions, each taking one argument at a time.

```js
// Example Without Currying:
function add(a, b, c) {
  return a + b + c;
}

console.log(add(2, 3, 5)); // Output: 10

// Same Function with Currying:

function curriedAdd(a) {
  return function (b) {
    return function (c) {
      return a + b + c;
    };
  };
}

console.log(curriedAdd(2)(3)(5)); // Output: 10
```

### 2️⃣ How Currying Works?

- In currying, functions return another function until all arguments are received.

  - curriedAdd(2) returns a function that expects b
  - curriedAdd(2)(3) returns a function that expects c
  - curriedAdd(2)(3)(5) returns the sum 2 + 3 + 5 = 10

### 3️⃣ Why Use Currying?

- ✅ Code Reusability
- ✅ Avoids Repetitive Function Calls
- ✅ Helps in Function Composition (Creating Modular Code)

- Example: Reusability
  - Instead of calling a function with multiple arguments every time, currying allows you to reuse partial functions.
  - Here, double is a partially applied function where a = 2, and it can be reused with different b values.

```js
function multiply(a) {
  return function (b) {
    return a * b;
  };
}

const double = multiply(2); // Partially applied function
console.log(double(5)); // Output: 10
console.log(double(10)); // Output: 20
```

### 4️⃣ Convert a Normal Function to Curried Function

```js
// If you have a normal function like:

function sum(a, b, c) {
  return a + b + c;
}

// You can convert it into a curried function like this:

// const curry = (fn) => {
//   (...args) => {
//     args.lenth >= fn.length ? fn(...args) : (...moreArgs) => curry(fn)(...args, ...moreArgs);
//   }
// }

const curry =
  (fn) =>
  (...args) =>
    args.length >= fn.length
      ? fn(...args)
      : (...moreArgs) => curry(fn)(...args, ...moreArgs);

const curriedSum = curry(sum);
console.log(curriedSum(2)(3)(5)); // Output: 10
console.log(curriedSum(2, 3)(5)); // Output: 10
console.log(curriedSum(2)(3, 5)); // Output: 10
```

```js
function counter(args) {
  let count = 0;
  count++;
  if (args === 0) {
    return count;
  } else {
    return function inner(args) {
      count++;
      if (args === 0) {
        return count;
      } else {
        return inner;
      }
    };
  }
}

// console.log(counter(0)); // print -> 1
// console.log(counter()(0)); // print -> 2
// console.log(counter()()()()(0)); // print -> 5
```

### 5️⃣ Real-World Example: Filtering Data

- Imagine we need to filter a list of students by a specific department.

- Without Currying:

```js
function filterStudents(department, students) {
  return students.filter((student) => student.department === department);
}

const students = [
  { name: "Ganesh", department: "CS" },
  { name: "Raj", department: "IT" },
  { name: "Riya", department: "CS" },
];

console.log(filterStudents("CS", students));
```

- With Currying:

```js
const filterByDepartment = (department) => (students) =>
  students.filter((student) => student.department === department);

const filterCS = filterByDepartment("CS");

console.log(filterCS(students));
```

6️⃣ Conclusion

- Currying breaks down functions into smaller functions.
- It improves reusability, readability, and function composition.
- It allows partial function application for flexibility.

## Curry Vs Closure

## Application Closures
