# JS-7: OOPS-2 : Object creation, Freezing objects

## Assignment

- Q1. JS Core - Checking Instance

```
Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class's methods.

There are no constraints on the data types that can be passed to the function. For example, the value or the class could be undefined.

Example 1:

Input: func = () => checkIfInstanceOf(new Date(), Date)
Output: true
Explanation: The object returned by the Date constructor is, by definition, an instance of Date.

Example 2:

Input: func = () => { class Animal {}; class Dog extends Animal {}; return checkIfInstanceOf(new Dog(), Animal); }
Output: true
Explanation:
class Animal {};
class Dog extends Animal {};
checkIfInstance(new Dog(), Animal); // true

Dog is a subclass of Animal. Therefore, a Dog object is an instance of both Dog and Animal.

Example 3:

Input: func = () => checkIfInstanceOf(Date, Date)
Output: false
Explanation: A date constructor cannot logically be an instance of itself.

Example 4:

Input: func = () => checkIfInstanceOf(5, Number)
Output: true
Explanation: 5 is a Number. Note that the "instanceof" keyword would return false. However, it is still considered an instance of Number because it accesses the Number methods. For example "toFixed()"
```

```js
function checkIfInstanceOf(obj, classFunction) {
  return !(!obj || !(obj instanceof classFunction));
}
```

```
Output :

```

- Q2. JS Core - Polyfill Create Object

```
You are tasked with creating a polyfill for the Object.create method in JavaScript. The Object.create method is a built-in function in JavaScript that allows you to create a new object with a specified prototype object.

Your goal is to create a function called myObjectCreate that emulates the functionality of Object.create. The myObjectCreate function should accept a single argument, proto, which represents the prototype object for the new object to be created.

However, there are a few requirements and constraints for your implementation:

1. If the proto argument is null, undefined, or not an object, your function should throw an Error. This is to ensure that the proto argument is a valid object to be used as the prototype.

2. Your implementation should create a new object that inherits from the proto object. This means that any properties or methods defined on the proto object should be accessible by the newly created object.

3. The newly created object should not have any own properties initially. Any properties or methods accessed on the new object that are not defined directly on the object should be looked up in the prototype chain.

Sample Test Case:
To demonstrate the usage of your myObjectCreate function, consider the following example:

// Step 1: Define a prototype object
const personPrototype = {
  greet: function() {
    console.log("Hello, my name is " + this.name + ".");
  }
};

// Step 2: Call myObjectCreate and pass the prototype object
const person = myObjectCreate(personPrototype);

// Step 3: Assign the returned object to a variable

// Step 4: Use the newly created object
person.name = "John";
person.greet(); // Output: Hello, my name is John.

In this example, we first define a personPrototype object that contains a greet method. We then use the myObjectCreate function to create a new object person based on the personPrototype. After assigning a name property to the person object, we call the greet method on the person object, which logs a greeting message with the assigned name.

Your myObjectCreate function should be able to replicate this behavior, allowing the user to create new objects with a specified prototype and access properties and methods defined on the prototype object.
```

```js
function myObjectCreate(proto) {
  if (proto === null || typeof proto !== "object") {
    throw new Error("Invalid prototype object");
  }

  // Create a constructor function that inherits from the given prototype
  function F() {}
  F.prototype = proto;

  // Create a new instance of the constructor function
  const newObj = new F();

  return newObj;
}
```

- Q3. JS Lecture 6 MCQ 1: Output?

```js
function Rabbit(name) {
  this.name = name;
}
Rabbit.prototype.sayHi = function () {
  console.log(this.name);
};
let rabbit = new Rabbit("Rabbit");

rabbit.sayHi();
Rabbit.prototype.sayHi();
Object.getPrototypeOf(rabbit).sayHi();
rabbit.__proto__.sayHi();
```

```
Output :
Rabbit
undefined
undefined
undefined
```

- Q4. JS Lecture 6 MCQ 2: Output?

```js
function A() {}
function B() {}

A.prototype = B.prototype = {};

let a = new A();

console.log(a instanceof B);
```

```
Output :
true
```

- Q5. JS Lecture 6 MCQ 3: Output?

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
}

class Rabbit extends Animal {
  constructor(name) {
    this.name = name;
    this.created = Date.now();
  }
}

let rabbit = new Rabbit("White Rabbit");
console.log(rabbit.name);
```

```
Output :
this.name = name;
ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor

solution:
constructor(name) {
  super()
}
```

## Additional Question

- Q1. JS Core - Polyfill Seal Object

```
You are tasked with creating a polyfill for the Object.seal method in JavaScript. The Object.seal method is a built-in function that seals an object, preventing new properties from being added and marking all existing properties as non-configurable.

Your goal is to create a function called sealPolyfill that emulates the functionality of Object.seal. The sealPolyfill function should be added to the Object.prototype object to make it accessible on all objects.

However, there are a few requirements and constraints for your implementation:

If the Object.seal method is already defined, your polyfill should not override it. You should only provide the polyfill if it doesn't exist.

The polyfill implementation should check if the value on which sealPolyfill is called is a valid object. If it's not an object or is null, a TypeError should be thrown.

The polyfill should iterate over all the properties of the object and mark them as non-configurable using Object.defineProperty. This prevents the properties from being deleted or having their attributes modified.

After sealing all existing properties, the polyfill should call Object.preventExtensions to prevent any new properties from being added to the object. This ensures that the object becomes a sealed object.

The sealed object should be returned by the polyfill function.

Example:
To demonstrate the usage of your sealPolyfill function, consider the following example:

const obj = {
name: 'John',
age: 30
};

console.log(Object.isSealed(obj)); // Output: false

obj.sealPolyfill();

console.log(Object.isSealed(obj)); // Output: true

obj.name = 'Jane'; // Existing property can still be modified
console.log(obj.name); // Output: Jane

obj.gender = 'Female'; // Attempt to add a new property
console.log(obj.gender); // Output: undefined (property was not added)

delete obj.age; // Attempt to delete an existing property
console.log(obj.age); // Output: 30 (property was not deleted)

In this example, we start with an object obj with two properties: name and age. Initially, the object is not sealed, as confirmed by Object.isSealed(obj) returning false.

We then call the sealPolyfill function on the obj object, which seals the object using the polyfill implementation. After sealing, Object.isSealed(obj) returns true.

Once sealed, we can still modify the value of existing properties (obj.name = 'Jane'), but we cannot add new properties (obj.gender = 'Female') as the property addition is prevented. Similarly, attempting to delete an existing property (delete obj.age) does not work, as the property deletion is prevented.

Your sealPolyfill function should be able to replicate this behavior, allowing users to seal objects and prevent the addition of new properties while preserving the existing ones.

```

```js
if (!Object.prototype.sealPolyfill) {
  Object.defineProperty(Object.prototype, "sealPolyfill", {
    value: function () {
      if (typeof this !== "object" || this === null) {
        throw new TypeError("Expected an object");
      }

      Object.preventExtensions(this);

      const keys = Object.getOwnPropertyNames(this);
      for (const key of keys) {
        Object.defineProperty(this, key, { configurable: false });
      }

      return this;
    },
    configurable: true, // !Important else the test cases will fail.
  });
}
```

- Q2. JS Lecture 6 MCQ 4: Output?

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
}

class Rabbit extends Animal {
  constructor(name) {
    super(name);
    this.created = Date.now();
  }
}

let rabbit = new Rabbit("White Rabbit");
console.log(rabbit.name);
```

```
Output :
White Rabbit
```

- Q3. JS Lecture 6 MCQ 5: Output?

```js
let val = 0;

class A {
  set foo(_val) {
    val = _val;
  }

  get foo() {
    return val;
  }
}

class B extends A {}

class C extends A {
  get foo() {
    return val;
  }
}

const b = new B();
console.log(b.foo);
b.foo = 1;
console.log(b.foo);

const c = new C();
console.log(c.foo);
c.foo = 2;
console.log(c.foo);
console.log(b.foo);
```

```
Output :
0
1
1
1
1
```

- Q4. JS Lecture 6 MCQ 6: Output?

```js
let animal = {
  jumps: null,
};

let rabbit = {
  __proto__: animal,
  jumps: true,
};

console.log(rabbit.jumps); // ? (1)

delete rabbit.jumps;

console.log(rabbit.jumps); // ? (2)

delete animal.jumps;

console.log(rabbit.jumps); // ? (3)
```

```
Output :
true
null
undefined
```

- Q5. JS Lecture 6 MCQ 7: Output?

```js
class A {
  a = "a";
}

A.prototype.c = "c";

class B extends A {
  b = "b";
}

const a = new A();
const b = new B();

console.log(a.a);
console.log(a.b);
console.log(a.c);
console.log(b.a);
console.log(b.b);
console.log(b.c);
```

```
Output :
a
undefined
c
a
b
c
```
