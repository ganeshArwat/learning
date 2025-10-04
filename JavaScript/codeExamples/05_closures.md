# JS-5: ES6 Classes and Objects

## Assignment

- Q1. JS_This_Constructo

```
When using constructor functions (invoked with the new keyword), this refers to the newly created object. Constructor functions allow you to set up shared properties and methods across multiple instances. However, if you accidentally call a constructor function without the new keyword, this will not refer to the new object and could cause unexpected behavior.

Practice Question: Implement a Fix for the Misused Constructor Function You are given a constructor function Person that is supposed to create a new Person object with name and age properties. However, if the Person constructor is called without the new keyword, it does not correctly initialize the properties because this is not set to a new object.

Your task is to fix the Person constructor so that it works correctly with or without the new keyword. If the new keyword is not used, the constructor should automatically call itself with new to avoid incorrect behavior.
```

```js
function Person(name, age) {
  if (!(this instanceof Person)) {
    return new Person(name, age);
  }

  this.name = name;
  this.age = age;
}

// Create a new Person object correctly
const john = new Person("John", 30);
console.log(john.name, john.age); // Output: 'John', 30

// Bug: Calling without `new` does not create a new Person object
const jane = Person("Jane", 25);
console.log(jane.name, jane.age); // Output: Error or `undefined`, `undefined`
```

- Q2. JS_Navigating_deep_properties_safely

```
In JavaScript, accessing deeply nested properties in a large object can sometimes be tricky. If some of the intermediate properties are not present, you could easily end up with an error that breaks your code.

Consider the following objects:
const carol = {
  details: {
    personal: { firstName: "Carol", lastName: "Smith" },
    age: 25,
    city: "New York",
  },
};

const dave = {
  details: {
    age: 30,
    city: "San Francisco",
  },
};

function getFirstName(user) {
  return user.details.personal.firstName;
}

When calling getFirstName(carol), it works as expected. However, calling getFirstName(dave) will result in an error because the personal property doesn't exist in dave.details.

Problem Statement

Write a function named get that takes an object and a path to a property, and safely returns the value at that path. If the resolved value is undefined, the function should return an optional defaultValue. This function will help avoid errors when accessing deeply nested properties.

get(object, path, [defaultValue]);

object: The object to query.

path: The path of the property to get. It can be a string with . as the separator between fields, or an array of path strings.

defaultValue: Optional parameter. The value returned if the resolved value is undefined.

get(carol, "details.personal.firstName"); // 'Carol'
get(carol, "details.city"); // 'New York'
get(dave, "details.personal.firstName"); // undefined
get({ a: [{ b: { c: 42 } }] }, "a.0.b.c"); // 42
```

```js
function get(objectParam, pathParam, defaultValue) {
  // TODO: Convert path to an array if it's a string
  // TODO: Initialize index, length, and reference to the object
  // TODO: Traverse the object step-by-step
  // TODO: Determine the final value and return

  // Convert path to an array if it's a string
  const pathArray = Array.isArray(pathParam) ? pathParam : pathParam.split(".");

  // Traverse the object step-by-step
  let result = objectParam;
  for (const key of pathArray) {
    if (result && typeof result === "object" && key in result) {
      result = result[key];
    } else {
      return defaultValue;
    }
  }

  // Return the resolved value or defaultValue
  return result;
}
```
