## Js oops

### JavaScript supports Object-Oriented Programming (OOP) using prototypes and ES6 classes. OOP in JavaScript is based on four key principles:

### 1. Creating Objects in JavaScript

#### Using Object Literals

- Simple but not reusable for multiple objects.

```js
const person = {
  name: "Ganesh",
  age: 23,
  greet: function () {
    console.log(`Hello, my name is ${this.name}.`);
  },
};

person.greet(); // Output: Hello, my name is Ganesh.
```

#### 2. Constructor Functions

- Uses the new keyword to create an instance.
- Every instance gets its own copy of greet(), which is not memory-efficient.

```js
function Person(name, age) {
  this.name = name;
  this.age = age;

  this.greet = function () {
    console.log(`Hello, I'm ${this.name}.`);
  };
}

const person1 = new Person("Ganesh", 23);
person1.greet(); // Output: Hello, I'm Ganesh.
```

#### 3. Prototypes (Better Memory Management)

- greet is added to Person.prototype, so all instances share one function, reducing memory usage.

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

// Adding method to prototype
Person.prototype.greet = function () {
  console.log(`Hi, I'm ${this.name}.`);
};

const person1 = new Person("Ganesh", 23);
const person2 = new Person("Cne", 25);

person1.greet(); // Output: Hi, I'm Ganesh.
person2.greet(); // Output: Hi, I'm Cne.
```

#### 4. ES6 Classes (Syntactic Sugar for Prototypes)

- Internally works like prototypes.
- Cleaner, modern syntax.

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, I'm ${this.name}.`);
  }
}

const person1 = new Person("Ganesh", 23);
person1.greet(); // Output: Hello, I'm Ganesh.
```

### 5. Inheritance (Extending a Class)

- extends is used for inheritance.
- super() calls the parent class constructor.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Calls Animal's constructor
    this.breed = breed;
  }

  speak() {
    console.log(`${this.name} barks.`);
  }
}

const dog = new Dog("Bruno", "Labrador");
dog.speak(); // Output: Bruno barks.
```

### 6. Encapsulation (Private & Public Properties)

```js
class BankAccount {
  #balance; // Private property

  constructor(owner, balance) {
    this.owner = owner;
    this.#balance = balance;
  }

  deposit(amount) {
    this.#balance += amount;
    console.log(`Deposited: ${amount}, New Balance: ${this.#balance}`);
  }

  getBalance() {
    return this.#balance;
  }
}

const account = new BankAccount("Ganesh", 1000);
account.deposit(500); // Output: Deposited: 500, New Balance: 1500
console.log(account.getBalance()); // Output: 1500
// console.log(account.#balance); // Error: Private field '#balance' must be declared in an enclosing class
```

### 7. Polymorphism (Method Overriding)

- Circle overrides the area method from Shape.

```js
class Shape {
  area() {
    return "Area method not implemented.";
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }

  area() {
    return Math.PI * this.radius * this.radius;
  }
}

const shape = new Shape();
const circle = new Circle(5);

console.log(shape.area()); // Output: Area method not implemented.
console.log(circle.area()); // Output: 78.53981633974483
```

### 8. Static Methods (Class-Level Methods)

- static methods belong to the class and cannot be called on instances.

```js
class MathUtils {
  static add(a, b) {
    return a + b;
  }
}

console.log(MathUtils.add(5, 3)); // Output: 8
// new MathUtils().add(5, 3); // Error: Static method cannot be called on an instance
```

## Inbuilt object works

### 1. JavaScript’s Inbuilt Object Hierarchy

- JavaScript has three core built-in objects:

1. Array → extends from Array (class) → extends from Object
2. Function → extends from Function (class) → extends from Object
3. Object → The base prototype for everything

- This means:

  - Arrays are special objects (Array extends Object).
  - Functions are also objects (Function extends Object).
  - Regular objects inherit from Object.

```js
let arr = [1, 2, 3];
console.log(arr instanceof Array); // true
console.log(arr instanceof Object); // true

function test() {}
console.log(test instanceof Function); // true
console.log(test instanceof Object); // true
```

### 2. How Primitive Types Work

JavaScript has primitive data types, but they behave like objects temporarily when you access properties/methods.

Hierarchy of Primitive Types

| Primitive | Temporary Parent (Wrapper Object) | Final Parent         |
| :-------- | :-------------------------------- | :------------------- |
| number    | Number                            | Object               |
| string    | String                            | Object               |
| boolean   | Boolean                           | Object               |
| null      | (No parent)                       | (No object wrapping) |
| undefined | (No parent)                       | (No object wrapping) |

- null and undefined do not have any wrapper objects.

### 3. Autoboxing: Temporary Conversion of Primitives

#### What is Autoboxing?

- When you access a method or property on a primitive, JavaScript temporarily converts it into an object (its wrapper class).
- This temporary conversion is called Autoboxing.
- After the method/property is applied, the wrapper object is discarded, and a primitive is returned.

```js
let str = "hello";
console.log(str.toUpperCase()); // Output: "HELLO"

// Behind the scenes:
let tempStrObj = new String("hello"); // Autoboxing
console.log(tempStrObj.toUpperCase()); // "HELLO"
tempStrObj = null; // Wrapper object is discarded
```

-🔹 "hello" is a primitive string, but when we use .toUpperCase(), JavaScript temporarily converts it into a String object, applies the method, and then discards the object.

## Object create

### 1. Creating an Object using new Object()

```js
let obj1 = new Object();
obj1.name = "Rajneesh Kumar";
console.log("obj1: ", obj1); // obj1: { name: "Rajneesh Kumar" }
```

### 2. Creating an Object using Object.create(null)

- Object.create(null) creates an empty object with no prototype.
- This means obj2 does not inherit from Object.prototype, so it has no built-in methods like toString(), hasOwnProperty(), etc.

```js
let obj2 = Object.create(null);
obj2.name = "Rajneesh Kumar Yadav";
console.log("obj2: ", obj2); // obj2: { name: "Rajneesh Kumar Yadav" }
```

### 3. Creating an Object with Prototypal Inheritance

- Object.create(obj) creates obj2, which inherits from obj.

- obj2 gets:

  - name = "Rajneesh" (overrides obj.name).
  - lastName = "Kumar" (new property).
  - Prototype properties from obj, including address and sayHi()

```js
let obj = {
  name: "Steve",
  address: {
    state: "Newyork",
    city: "Manhatten",
  },
  sayHi: function () {
    console.log(`${this.name} say's Hi`);
    console.log("object this: ", this);
    return this;
  },
};

let obj2 = Object.create(obj);
obj2.name = "Rajneesh";
obj2.lastName = "Kumar";
console.log("obj2: ", obj2);
console.log(obj2.address); // Inherited from obj
console.log(obj2.sayHi()); // Uses sayHi() from obj
```

## hasOwnProperty

#### The hasOwnProperty() method checks whether an object has a direct property (own property) and does not inherit it from its prototype chain.

```js
object.hasOwnProperty(property);
```

```js
let person = {
  name: "Ganesh",
  age: 23,
};

console.log(person.hasOwnProperty("name")); // true
console.log(person.hasOwnProperty("age")); // true
console.log(person.hasOwnProperty("city")); // false
```

#### Example 2: Filtering Inherited Properties

```js
let parentObj = { parentProp: "I am inherited" };
let childObj = Object.create(parentObj); // childObj inherits from parentObj
childObj.name = "Ganesh";

console.log(childObj.hasOwnProperty("name")); // true (own property)
console.log(childObj.hasOwnProperty("parentProp")); // false (inherited)
```

## for in loop

#### The for...in loop in JavaScript is used to iterate over the enumerable properties of an object. It is mainly used for iterating over the keys of an object.

- Syntax:
  - key → Represents the property name (not value).
  - object → The object whose properties are being iterated over.

```js
for (let key in object) {
  // code to execute
}
```

### 1. Iterating Over Object Properties

```js
let person = {
  name: "Ganesh",
  age: 23,
  city: "Mumbai",
};

for (let key in person) {
  console.log(key, ":", person[key]);
}

// Output:
// name : Ganesh
// age : 23
// city : Mumbai
```

### 2. Skipping Inherited Properties

- If an object inherits properties via prototype, for...in includes those as well. Use hasOwnProperty() to filter them.

```js
let parentObj = { parentProp: "I am inherited" };
let childObj = Object.create(parentObj);
childObj.name = "Ganesh";

for (let key in childObj) {
  if (childObj.hasOwnProperty(key)) {
    console.log(key, ":", childObj[key]);
  }
}

// Output:

// With hasOwnProperty()
// name: Ganesh;

// Without hasOwnProperty(), it would also log
// name : Ganesh
// parentProp : I am inherited
```

## Types of for Loops

### 1️⃣ Traditional for loop

- 🔹 Used when you know the exact number of iterations.
- 🔹 Best for iterating over arrays using an index.

```js
for (let i = 0; i < 5; i++) {
  console.log(i); // 0, 1, 2, 3, 4
}
```

### 2️⃣ for...in loop

- 🔹 Used for iterating over object properties.
- 🔹 It iterates over keys (property names), not values.
- ⚠ Avoid using for...in for arrays, as it iterates over indexes as strings, which can lead to unexpected behavior.

```js
const person = { name: "Ganesh", age: 23, city: "Mumbai" };

for (let key in person) {
  console.log(key, person[key]);
}
// Output:
// name Ganesh
// age 23
// city Mumbai
```

### 3️⃣ for...of loop (ES6)

- 🔹 Used for iterating over iterable objects (arrays, strings, maps, sets).
- 🔹 Returns values, not keys.

```js
const fruits = ["Apple", "Mango", "Banana"];

for (let fruit of fruits) {
  console.log(fruit);
}
// Output:
// Apple
// Mango
// Banana

for (let char of "Ganesh") {
  console.log(char);
}
// Output: G a n e s h
```

### 4️⃣ forEach method (for arrays)

- 🔹 Used for iterating over arrays.
- 🔹 Cannot be broken using break or continue.

```js
const numbers = [10, 20, 30];

numbers.forEach((num, index) => {
  console.log(`Index: ${index}, Value: ${num}`);
});
// Output:
// Index: 0, Value: 10
// Index: 1, Value: 20
// Index: 2, Value: 30
```
