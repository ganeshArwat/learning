## Object Mutation - Const, Object.preventExtensions, Object.seal, Object.freeze

#### In JavaScript, objects declared with const can still be mutated. However, methods like Object.preventExtensions(), Object.seal(), and Object.freeze() provide different levels of restriction to object mutation. Let’s explore each one.

### 1. const and Object Mutation

- Declaring an object with const does not prevent mutation; it only prevents reassignment.
- const prevents reassignment but allows object mutation.

```js
const person = { name: "Ganesh", age: 23 };

person.age = 24; // ✅ Allowed: modifying a property
person.city = "Mumbai"; // ✅ Allowed: adding a property
delete person.name; // ✅ Allowed: deleting a property

console.log(person); // { age: 24, city: "Mumbai" }
```

- However, reassigning the object is not allowed:

```js
person = { name: "Arjun" }; // ❌ TypeError: Assignment to constant variable.
```

### 2. Object.preventExtensions()

- Prevents adding new properties but allows modifying or deleting existing properties.
  - ❌ New properties: ❌ Not Allowed
  - ✔ Modifications: ✅ Allowed
  - ✔ Deletion of properties: ✅ Allowed

```js
const car = { brand: "Toyota", model: "Corolla" };

Object.preventExtensions(car);

car.model = "Camry"; // ✅ Allowed: modifying existing property
delete car.brand; // ✅ Allowed: deleting property
car.year = 2023; // ❌ Not Allowed: adding new property

console.log(car); // { model: "Camry" }
```

```js
const config = {
  appName: "scaler.com",
  database: {
    host: "127.0.0.1",
    name: "mainDb",
    user: "root",
    pwd: "admin",
  },
  extra: 10,
};

let notExtendableObj = Object.preventExtensions(config); // it will prevent on level 1 only
// notExtendableObj.database = Object.preventExtensions(notExtendableObj.database); // to prevent on level 2

notExtendableObj.tempServer = "127.0.0.18"; // Addition of new key-value pair which is not allowed at first level.
notExtendableObj.database.tempServer = "127.0.0.18"; // Addition of new key-value pair which is not allowed at first level.
notExtendableObj.appName = "interviewbit.com"; // This is allowed.
delete notExtendableObj.extra; // this is allowed as well.

console.log(notExtendableObj);
```

```
output
{
  appName: 'interviewbit.com',
  database: {
    host: '127.0.0.1',
    name: 'mainDb',
    user: 'root',
    pwd: 'admin',
    tempServer: '127.0.0.18'
  }
}
```

### 3. Object.seal()

- Prevents adding or deleting properties but allows modifying existing ones.
  - ❌ New properties: ❌ Not Allowed
  - ✔ Modifications: ✅ Allowed
  - ❌ Deletion of properties: ❌ Not Allowed

```js
const laptop = { brand: "Dell", price: 50000 };

Object.seal(laptop);

laptop.price = 55000; // ✅ Allowed: modifying existing property
delete laptop.brand; // ❌ Not Allowed: deletion
laptop.color = "Black"; // ❌ Not Allowed: adding new property

console.log(laptop); // { brand: "Dell", price: 55000 }
```

```js
const config = {
  appName: "scaler.com",
  database: {
    host: "127.0.0.1",
    name: "mainDb",
    user: "root",
    pwd: "admin",
  },
  extra: 10,
};

let notExtendableObj = Object.seal(config);
// notExtendableObj.database = Object.seal(notExtendableObj.database); // to prevent on level 2

notExtendableObj.tempServer = "127.0.0.18"; // this line will skipped.
notExtendableObj.database.newpwd = "fake"; // this line will skipped.
notExtendableObj.appName = "interviewbit.com"; // this line is allowed.
delete notExtendableObj.extra; // this line will skipped.

console.log(notExtendableObj);
```

```
{
  appName: 'interviewbit.com',
  database: {
    host: '127.0.0.1',
    name: 'mainDb',
    user: 'root',
    pwd: 'admin',
    newpwd: 'fake'
  },
  extra: 10
}
```

### 4. Object.freeze()

- Prevents adding, deleting, and modifying properties, making the object fully immutable.
  - ❌ New properties: ❌ Not Allowed
  - ❌ Modifications: ❌ Not Allowed
  - ❌ Deletion of properties: ❌ Not Allowed

```js
const mobile = { brand: "Samsung", price: 30000 };

Object.freeze(mobile);

mobile.price = 35000; // ❌ Not Allowed: modification
delete mobile.brand; // ❌ Not Allowed: deletion
mobile.color = "Blue"; // ❌ Not Allowed: adding new property

console.log(mobile); // { brand: "Samsung", price: 30000 }
```

```js
const config = {
  appName: "scaler.com",
  database: {
    host: "127.0.0.1",
    name: "mainDb",
    user: "root",
    pwd: "admin",
  },
  extra: 10,
};

let notExtendableObj = Object.freeze(config);
// notExtendableObj.database = Object.freeze(notExtendableObj.database); // to prevent on level 2

notExtendableObj.tempServer = "127.0.0.18"; // this line will skipped.
notExtendableObj.database.newpwd = "fake"; // this line will skipped.
delete notExtendableObj.extra; // this line will skipped.
notExtendableObj.appName = "interviewbit.com"; // this line will skipped.

console.log(notExtendableObj);
```

```
{
  appName: 'scaler.com',
  database: {
    host: '127.0.0.1',
    name: 'mainDb',
    user: 'root',
    pwd: 'admin',
    newpwd: 'fake'
  },
  extra: 10
}
```

## Deep Prevention, Sealing and Freezing

### Deep Prevent Extensions

```js
function deepPreventExtensions(obj) {
  Object.preventExtensions(obj);
  Object.keys(obj).forEach((key) => {
    if (typeof obj[key] === "object" && obj[key] !== null) {
      deepPreventExtensions(obj[key]);
    }
  });
  return obj;
}

const noExtendConfig = deepPreventExtensions(config);
noExtendConfig.database.user = "anotherUser"; // ✅ Allowed (Modification)
noExtendConfig.database.newKey = "value"; // ❌ Not Allowed (Can't add)
delete noExtendConfig.database.pwd; // ✅ Allowed (Can delete)
```

### Deep Seal

```js
function deepSeal(obj) {
  Object.seal(obj);
  Object.keys(obj).forEach((key) => {
    if (typeof obj[key] === "object" && obj[key] !== null) {
      deepSeal(obj[key]);
    }
  });
  return obj;
}

const sealedConfig = deepSeal(config);
sealedConfig.database.user = "newUser"; // ✅ Allowed
sealedConfig.database.newKey = "value"; // ❌ Not Allowed (Can't add)
delete sealedConfig.database.pwd; // ❌ Not Allowed (Can't delete)
```

### Deep Freeze

```js
function deepFreeze(obj) {
  Object.freeze(obj); // Freeze the object itself

  // Recursively freeze properties that are objects
  Object.keys(obj).forEach((key) => {
    if (typeof obj[key] === "object" && obj[key] !== null) {
      deepFreeze(obj[key]);
    }
  });

  return obj;
}

const deepFrozenConfig = deepFreeze(config);

deepFrozenConfig.database.pwd = "newPass"; // ❌ Not Allowed (Now Deep Frozen)
console.log(deepFrozenConfig.database.pwd); // "admin"
```

## Symbol

#### A Symbol is a primitive data type in JavaScript introduced in ES6. It is used to create unique and immutable property keys. Unlike strings, symbols never collide even if they have the same description.

### 1. Creating Symbols

- You can create a Symbol using the Symbol() function.

```js
const sym1 = Symbol();
const sym2 = Symbol();
console.log(sym1 === sym2); // false (Each Symbol is unique)

const sym3 = Symbol("description");
const sym4 = Symbol("description");
console.log(sym3 === sym4); // false
```

### 2. Using Symbols as Object Keys

```js
const ID = Symbol("id");
const user = {
  name: "Ganesh",
  [ID]: 101, // Using Symbol as a key
};

console.log(user); // { name: 'Ganesh', [Symbol(id)]: 101 }
console.log(user[ID]); // 101
```

- Why Use Symbols as Keys?

  - ✔ Avoid property name conflicts
  - ✔ Hide properties from for...in and Object.keys()
  - Symbols do not appear in Object.keys() or for...in loops, but they are retrievable via Object.getOwnPropertySymbols().

```js
console.log(Object.keys(user)); // ['name'] // ID Gets Ignored because it's a Symbol
console.log(Object.getOwnPropertyNames(user)); // ['name']
console.log(Object.getOwnPropertySymbols(user)); // [ Symbol(id) ]
```

### 3. Shared Symbols with Symbol.for()

- Symbols created with Symbol.for() are not unique; they are stored globally.
- Use Symbol.for() when you need a shared Symbol across your application.

```js
const globalSym1 = Symbol.for("shared");
const globalSym2 = Symbol.for("shared");

console.log(globalSym1 === globalSym2); // true (Same reference)
```

- To retrieve the key (description) of a global Symbol:

```js
console.log(Symbol.keyFor(globalSym1)); // "shared"
```

### 4. Symbols in Class Properties

- Symbols are great for private properties in objects.

```js
const _secret = Symbol("secretData");

class User {
  constructor(name) {
    this.name = name;
    this[_secret] = "Hidden Value";
  }
}

const u1 = new User("Ganesh");
console.log(u1); // { name: 'Ganesh', [Symbol(secretData)]: 'Hidden Value' }
console.log(u1._secret); // undefined (Can't access directly)
```

## Bigint

#### BigInt is a built-in primitive data type in JavaScript that allows you to work with very large integers beyond the Number.MAX_SAFE_INTEGER (2^53 - 1).

### 1. Why BigInt?

- In JavaScript, numbers are represented as 64-bit floating point values, meaning integers larger than
- 9007199254740991 (2^53 - 1) lose precision:

```js
console.log(9007199254740991 + 1); // ✅ 9007199254740992
console.log(9007199254740991 + 2); // ❌ 9007199254740992 (Precision Loss!)
```

### 2. Creating a BigInt

#### Method 1: Adding n at the end

```js
const bigNum = 9007199254740991n;
console.log(bigNum); // 9007199254740991n
console.log(bigNum + 5n); // 9007199254740996n
```

#### Method 2: Using BigInt() function

```js
const bigNum2 = BigInt(9007199254740991);
console.log(bigNum2); // 9007199254740991n
```

- ✔ Preferred: Use n for literals.
- ✔ BigInt() works but cannot convert decimals:

```js
console.log(BigInt(10.5)); // ❌ Error: Cannot convert a decimal to BigInt
```

### 3. Operations with BigInt

```js
const a = 123456789012345678901234567890n;
const b = 987654321098765432109876543210n;

console.log(a + b); // ✅ Addition
console.log(b - a); // ✅ Subtraction
console.log(a * b); // ✅ Multiplication
console.log(b / a); // ✅ Division (Rounded Down!)
console.log(a % b); // ✅ Modulus
console.log(a ** 2n); // ✅ Exponentiation

// Unlike regular numbers, BigInt does NOT support floating-point values.
console.log(10n / 3n); // ✅ 3n (No decimals in BigInt)
```

### 4. Mixing BigInt and Number

- You cannot mix BigInt and Number in operations.

```js
console.log(10n + 20); // ❌ Error: Cannot mix BigInt and Number
```

- ✔ Convert Number → BigInt:

```js
console.log(10n + BigInt(20)); // ✅ 30n
```

### 5. Comparisons with BigInt

- Comparisons (<, >, <=, >=, ===, !==) work normally between BigInt and Number:

```js
console.log(10n > 5); // ✅ true
console.log(10n == 10); // ✅ true (== allows coercion)
console.log(10n === 10); // ❌ false (Strict type check fails)
```

### 6. BigInt in JSON

- BigInt cannot be serialized in JSON.

```js
const obj = { large: 12345678901234567890n };
console.log(JSON.stringify(obj)); // ❌ Error: BigInt cannot be serialized
```

- ✔ Convert manually before serialization:

```js
const obj = { large: 12345678901234567890n };
console.log(JSON.stringify({ large: obj.large.toString() })); //  '{"large":"12345678901234567890"}'
```

## Map

#### A Map is a built-in JavaScript object that allows key-value pairs, but unlike regular objects, it can have any type of key, including objects, functions, and even NaN.

### 1. Creating a Map

- A Map is created using the new Map() constructor:
  - ✔ Unlike objects ({}), Map maintains the insertion order of keys.
  - ✔ Keys can be any data type (string, number, object, function).

```js
const myMap = new Map();
```

### 2. Adding, Getting & Deleting Values

- Adding values with set()

```js
myMap.set("name", "Ganesh");
myMap.set(1, "One"); // Number as a key
myMap.set(true, "Boolean"); // Boolean as a key
myMap.set({ a: 1 }, "Object Key"); // Object as a key
console.log(myMap);
```

- Getting values with get()

```js
console.log(myMap.get("name")); // "Ganesh"
console.log(myMap.get(1)); // "One"
console.log(myMap.get(true)); // "Boolean"
```

- Checking key existence with has()

```js
console.log(myMap.has("name")); // true
console.log(myMap.has(100)); // false
```

- Deleting a key with delete()

```js
myMap.delete(1);
console.log(myMap.has(1)); // false
```

- Clearing all values with clear()

```js
myMap.clear();
console.log(myMap.size); // 0
```

### 3. Iterating Over a Map

- Using forEach()

```js
myMap.set("a", 1);
myMap.set("b", 2);
myMap.set("c", 3);

myMap.forEach((value, key) => {
  console.log(`${key} = ${value}`);
});
```

- Using for...of

```js
for (let [key, value] of myMap) {
  console.log(`${key} = ${value}`);
}
```

- Getting Keys, Values, and Entries

```js
console.log([...myMap.keys()]); // ["a", "b", "c"]
console.log([...myMap.values()]); // [1, 2, 3]
console.log([...myMap.entries()]); // [["a",1], ["b",2], ["c",3]]
```

## Set

### A Set in JavaScript is a collection of unique values (no duplicates). It is similar to an array, but all values must be distinct.

### 1. Creating a Set

- A Set is created using the new Set() constructor.
- ✔ Unlike arrays, Set automatically removes duplicate values.

```js
const mySet = new Set();
```

### 2. Adding, Checking & Deleting Values

#### Adding values with add()

```js
mySet.add(1);
mySet.add(2);
mySet.add(2); // Duplicate, will not be added
mySet.add("Hello");
mySet.add({ name: "Ganesh" }); // Object key
console.log(mySet); // Set { 1, 2, 'Hello', { name: 'Ganesh' } }
```

#### Checking existence with has()

```js
console.log(mySet.has(1)); // true
console.log(mySet.has(100)); // false
```

#### Deleting a value with delete()

```js
mySet.delete(2);
console.log(mySet.has(2)); // false
```

#### Clearing all values with clear()

```js
mySet.clear();
console.log(mySet.size); // 0
```

### 3. Iterating Over a Set

- Using forEach()

```js
mySet.add("a");
mySet.add("b");
mySet.add("c");

mySet.forEach((value) => {
  console.log(value);
});
```

- Using for...of

```js
for (let value of mySet) {
  console.log(value);
}
```

- Converting Set to Array

```js
const arrayFromSet = [...mySet];
console.log(arrayFromSet); // ['a', 'b', 'c']
```

### 4. Removing Duplicates from an Array

```js
const numbers = [1, 2, 3, 1, 2, 4, 5, 4];
const uniqueNumbers = [...new Set(numbers)];
console.log(uniqueNumbers); // [1, 2, 3, 4, 5]
```

## Week Reference

### A weak reference means an object reference that does not prevent garbage collection. JavaScript provides two special collections for weakly-referenced objects:

- ✅ WeakMap (for key-value pairs)
- ✅ WeakSet (for unique object values)

### Strong Reference vs. Weak Reference

#### 1️⃣ Strong Reference (Normal Variables in JavaScript)

- If an object has a strong reference, it stays in memory until the reference is removed.

```js
let user = { name: "Ganesh" }; // Strong reference
console.log(user.name); // "Ganesh"

user = null; // Now the object is eligible for garbage collection
```

- 👉 As long as user holds a reference, the object { name: "Ganesh" } remains in memory.

#### 2️⃣ Weak Reference (Using WeakMap or WeakSet)

- If an object is stored in a WeakMap or WeakSet, it does not prevent garbage collection.

```js
const weakMap = new WeakMap();
let user = { name: "Ganesh" };

weakMap.set(user, "Some data");

console.log(weakMap.get(user)); // "Some data"

user = null; // The object is now garbage collected
console.log(weakMap.get(user)); // undefined (because it's automatically removed)
```

- 👉 Even though WeakMap stored the object, it was garbage-collected when no strong references remained.

### Why Do We Need Weak References?

1. Prevents Memory Leaks 🚀
   -No need to manually remove objects when they are no longer needed.
2. Better Performance ⏳
   - Automatic cleanup means less memory usage.
3. Useful for Caching & DOM Manipulation 🏗️
   - Weak references are great for caching objects without preventing their deletion.

## WeakMap

### A WeakMap is like a Map, but its keys must be objects, and they are weakly referenced, meaning:

- ✔ Keys do not prevent garbage collection (if no other references exist)
- ✔ No size property (not iterable)

```js
const weakMap = new WeakMap();
let obj = { name: "Ganesh" };

weakMap.set(obj, "Developer");
console.log(weakMap.get(obj)); // "Developer
```

- Key Removed When No Other References Exist

```js
obj = null; // Now { name: "Ganesh" } is garbage collected
console.log(weakMap.get(obj)); // undefined
```

- 🚨 Limitations of WeakMap:
- ❌ No Iteration (forEach, for...of not supported)
- ❌ No size property (because keys can disappear anytime)

## WeakSet

- A WeakSet is similar to Set, but it can only store objects and has weak references.

```js
const weakSet = new WeakSet();
let user = { name: "Ganesh" };

weakSet.add(user);
console.log(weakSet.has(user)); // true
```

- Object Removed When No Other References Exist

```js
user = null; // Garbage collected
console.log(weakSet.has(user)); // false
```

- 🚨 Limitations of WeakSet:
- ❌ No Iteration (forEach, for...of not supported)
- ❌ No size property

## 3. When to Use WeakMap and WeakSet?

- ✅ Caching Data Without Memory Leaks
- ✅ Storing Metadata Without Affecting Garbage Collection
- ✅ Tracking Object Existence Without Preventing Deletion
