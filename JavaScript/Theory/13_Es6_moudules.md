## Modules in Es6

- ES6 introduced modules, which allow you to split your JavaScript code into smaller, reusable files. This improves code organization, maintainability, and reusability.

### 1️⃣ Exporting and Importing Modules

- Modules in JavaScript are handled using export and import.

#### Exporting from a Module

- There are two types of exports:
  - ✅ Named Export
  - ✅ Default Export

#### 📌 Named Export

- Allows exporting multiple values from a file.
- Must be imported with the exact name (use curly braces {}).

- Example: Exporting (mathUtils.js)

```js
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;
export const PI = 3.14159;
```

- Example: Importing

```js
import { add, multiply, PI } from "./mathUtils.js";

console.log(add(5, 3)); // Output: 8
console.log(multiply(4, 2)); // Output: 8
console.log(PI); // Output: 3.14159
```

- ⚠ Note: The import must match the exported name

```js
import { addition } from "./mathUtils.js"; // ❌ Will throw an error (name mismatch)
```

- ✅ You can also rename while importing:

```js
import { add as sum } from "./mathUtils.js";

console.log(sum(10, 5)); // Output: 15
```

#### 📌 Default Export

- Each module can have only one default export.
- You don’t need curly braces {} while importing.

- Example: Exporting Default (greet.js)

```js
const greet = (name) => `Hello, ${name}!`;
export default greet;
```

- Example: Importing

```js
import greet from "./greet.js";
console.log(greet("Ganesh")); // Output: Hello, Ganesh!
```

- ✅ You can rename the default import:

```js
import sayHello from "./greet.js";

console.log(sayHello("Ganesh")); // Output: Hello, Ganesh!
```

### 2️⃣ Exporting & Importing Everything (\*)

- You can import all exports from a module using \*.

- Example: (mathUtils.js)

```js
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;
export const PI = 3.14159;
```

- Import Everything

```js
import * as MathUtils from "./mathUtils.js";

console.log(MathUtils.add(3, 7)); // Output: 10
console.log(MathUtils.PI); // Output: 3.1415
```

### 3️⃣ Mixing Named and Default Exports

- You can combine both named and default exports.

- Example: (math.js)

```js
export const subtract = (a, b) => a - b;
export const divide = (a, b) => a / b;

export default function greet(name) {
  return `Hello, ${name}!`;
}
```

- Example: Importing Both

```js
import greet, { subtract, divide } from "./math.js";

console.log(greet("Ganesh")); // Output: Hello, Ganesh!
console.log(subtract(10, 3)); // Output: 7
console.log(divide(10, 2)); // Output: 5
```

---

## Ternary Operator (? :) in JavaScript 🚀

- The ternary operator is a shorthand for if-else statements. It makes conditional expressions shorter and more readable.
- Syntax

```
condition ? expression_if_true : expression_if_false;
```

🔹 Example 1: Basic Ternary

```js
const age = 18;
const message = age >= 18 ? "You can vote!" : "You cannot vote!";
console.log(message); // Output: You can vote!
```

🔹 Example 3: Nesting Ternary Operators

- (Ternaries inside ternaries – but don't overuse them for readability)

```js
const num = 0;
const result = num > 0 ? "Positive" : num < 0 ? "Negative" : "Zero";
console.log(result); // Output: Zero
```

---

## Short Circuiting and Logical Operators

- JavaScript provides logical operators (&&, ||, ??) that short-circuit expressions, meaning they stop evaluating as soon as the result is determined.

### && (AND)

- Returns first falsy value or last truthy

### ?? (Nullish Coalescing)

- Returns first defined (non-null) value

### 1️⃣ Short-Circuiting with && (AND)

- If the first value is falsy, the second value is never evaluated.
- Returns the first falsy value or the last truthy value.

```js
console.log(false && "Hello"); // Output: false
console.log(0 && "World"); // Output: 0
console.log(1 && "Hello"); // Output: Hello (last truthy value)
```

- ✅ Use case: Conditional execution

```js
const isLoggedIn = true;
isLoggedIn && console.log("Welcome back!"); // Output: Welcome back!
```

### 2️⃣ Short-Circuiting with || (OR)

- If the first value is truthy, the second value is never evaluated.
- Returns the first truthy value or the last falsy value.

```js
console.log(true || "Hello"); // Output: true
console.log(0 || "World"); // Output: World
console.log("" || false || "Ganesh"); // Output: Ganesh
```

- ✅ Use case: Setting Default Values

```js
const username = "" || "Guest";
console.log(username); // Output: Guest
```

### 3️⃣ Short-Circuiting with ?? (Nullish Coalescing)

- Returns the first defined (non-null, non-undefined) value.
- Works like || but ignores falsey values like 0 or "".

```js
console.log(null ?? "Default"); // Output: Default
console.log(undefined ?? "Guest"); // Output: Guest
console.log(0 ?? 100); // Output: 0 (Unlike `||`, it keeps 0)
console.log("" ?? "Hello"); // Output: "" (Unlike `||`, it keeps empty string)
```

- ✅ Use case: Handling null or undefined values

```js
const user = null;
const displayName = user ?? "Anonymous";
console.log(displayName); // Output: Anonymous
```

---

## Optional Chaining (?.)

### 🔹 What is Optional Chaining?

- Optional chaining (?.) prevents errors when accessing deeply nested properties that might not exist. Instead of throwing an error, it returns undefined if any part of the chain is null or undefined.

- 🔹 Syntax

```js
object?.property; // Returns undefined if object is null/undefined
object?.method(); // Calls method only if it exists
object?.[expression]; // Access dynamic keys safely
```

### 1️⃣ Accessing Nested Properties

- 🔴 Without Optional Chaining (Error if user.profile is undefined)

```js
const user = { name: "Ganesh" };
console.log(user.profile.bio); // ❌ TypeError: Cannot read properties of undefined
```

- 🟢 With Optional Chaining (Safe)

```js
console.log(user.profile?.bio); // ✅ Output: undefined (No error!)
```

### 2️⃣ Calling Methods Safely

- 🔴 Without Optional Chaining (Error if method doesn't exist)

```js
const user = {};
console.log(user.getName()); // ❌ TypeError: user.getName is not a function
```

- 🟢 With Optional Chaining

```js
console.log(user.getName?.()); // ✅ Output: undefined (No error!)
```

### 3️⃣ Accessing Array Elements

- 🔴 Without Optional Chaining (Error if users is undefined)

```js
const data = {};
console.log(data.users[0].name); // ❌ TypeError: Cannot read properties of undefined
```

- 🟢 With Optional Chaining

```js
console.log(data.users?.[0]?.name); // ✅ Output: undefined (No error!)
```

### 4️⃣ Using with ?.[] for Dynamic Keys

- 🔴 Without Optional Chaining

```js
const user = { details: { age: 23 } };
console.log(user.details["address"].city); // ❌ TypeError: Cannot read properties of undefined
```

- 🟢 With Optional Chaining

```js
console.log(user.details?.["address"]?.city); // ✅ Output: undefined (No error!)
```

### 5️⃣ Combining with Nullish Coalescing (??)

- To set default values when accessing optional properties:

```js
const user = { name: "Ganesh" };
const country = user.address?.country ?? "India";
console.log(country); // ✅ Output: India
```

---

## Destructuring in JavaScript

- Destructuring in JavaScript allows you to extract values from arrays or objects and assign them to variables in a cleaner way. It helps avoid repetitive code and makes working with data structures more efficient.

### 1️⃣ Array Destructuring

- Extracts values from arrays and assigns them to variables.

- 🔹 Basic Example

```js
const numbers = [10, 20, 30];

const [a, b, c] = numbers; // Assign values to variables

console.log(a); // 10
console.log(b); // 20
console.log(c); // 30
```

- 🔹 Skipping Elements

```js
const nums = [1, 2, 3, 4, 5];

const [first, , third] = nums; // Skipping second value
console.log(first); // 1
console.log(third); // 3
```

- 🔹 Using Rest Operator (...)

```js
const colors = ["Red", "Blue", "Green", "Yellow"];

const [firstColor, ...remainingColors] = colors;

console.log(firstColor); // "Red"
console.log(remainingColors); // ["Blue", "Green", "Yellow"]
```

- 🔹 Swapping Values

```js
let x = 5,
  y = 10;
[x, y] = [y, x];

console.log(x); // 10
console.log(y); // 5
```

- 🔹 Default Values

```js
const names = ["Ganesh"];

const [firstName, lastName = "Unknown"] = names;

console.log(firstName); // "Ganesh"
console.log(lastName); // "Unknown" (default value used)
```

### 2️⃣ Object Destructuring

- Extracts properties from objects and assigns them to variables.

- 🔹 Basic Example

```js
const user = {
  name: "Ganesh",
  age: 23,
  country: "India",
};

const { name, age, country } = user;

console.log(name); // "Ganesh"
console.log(age); // 23
console.log(country); // "India"
```

- 🔹 Renaming Variables

```js
const person = { firstName: "John", lastName: "Doe" };

const { firstName: fName, lastName: lName } = person;

console.log(fName); // "John"
console.log(lName); // "Doe"
```

- 🔹 Default Values

```js
const userInfo = { name: "Ganesh" };

const { name, age = 25 } = userInfo;

console.log(name); // "Ganesh"
console.log(age); // 25 (default value)
```

- 🔹 Nested Object Destructuring

```js
const student = {
  name: "Amit",
  details: {
    age: 22,
    grade: "A",
  },
};

const {
  name,
  details: { age, grade },
} = student;

console.log(name); // "Amit"
console.log(age); // 22
console.log(grade); // "A"
```

### 3️⃣ Function Parameter Destructuring

- You can destructure objects or arrays inside function parameters

- 🔹 Destructuring an Object in a Function

```js
function greet({ name, age }) {
  console.log(`Hello, ${name}. You are ${age} years old.`);
}

const person = { name: "Ganesh", age: 23 };
greet(person); // "Hello, Ganesh. You are 23 years old."
```

- 🔹 Destructuring an Array in a Function

```js
function getCoordinates([x, y]) {
  console.log(`X: ${x}, Y: ${y}`);
}

getCoordinates([10, 20]); // "X: 10, Y: 20"
```
