## Call Polyfill

```js
Function.prototype.myCall = function (requiredObject, ...arrayAsArgument) {
  // get your function.
  const functionToBeInvoked = this;

  // copy your function in the requiredObject for temp basis.
  requiredObject.tempFunction = functionToBeInvoked;

  // Call your function.
  requiredObject.tempFunction(...arrayAsArgument);

  // Delete temp method.
  delete requiredObject.tempFunction;
};

// cap.petersTeam.myCall(ironMan, "thor", "loki",);
```

## Apply PolyFill

```js
Function.prototype.myApply = function (requiredObject, arrayAsArgument) {
  // get your function.
  const functionToBeInvoked = this;

  // copy your function in the requiredObject for temp basis.
  requiredObject.tempFunction = functionToBeInvoked;

  // Call your function.
  requiredObject.tempFunction(...arrayAsArgument);

  // Delete temp method.
  delete requiredObject.tempFunction;
};

// let memberssArray = ["thor", "Rajneesh", "loki", "Manisha", "Suraj", "Priyank", "Umang"];
// let memberssArray = ["thor", "loki"];  // Max size of array allowed is 2 because of 2 argument.
// cap.petersTeam.myApply(ironMan, memberssArray);
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

## Bind PolyFill

```js
Function.prototype.myBind = function (requiredObject) {
  // get your function.
  const functionToBeInvoked = this;

  return function (...arrayAsArgument) {
    functionToBeInvoked.call(requiredObject, ...arrayAsArgument);
  };
};

const boundFn2 = cap.petersTeam.myBind(ironMan);
boundFn2("Thor Bansal", "Rajneesh Kumar");
```

## Deep Copy PolyFill

```js
function superCloneEffective(input) {
  // Base case or edge cases.
  if (!Array.isArray(input) && typeof input !== "object") {
    // Function or either primitive data type.
    return input;
  }

  // Create a new container on the basis of type whether it is a array or object.
  let clone = Array.isArray(input) ? [] : {};

  // Copy all the key and values.
  for (let key in input) {
    const value = input[key];
    clone[key] = superCloneEffective(value);
  }

  // return object after completion.
  return clone;
}

// Testcases.
let person = {
  firstName: "John",
  lastName: "Doe",
  address: {
    street: "North 1st street",
    city: "San Jose",
    state: "CA",
    country: "USA",
  },
  friends: ["Steve", "Nikola", "Ray", { name: "Jai", lastName: "Roy" }],
  sayHi: function () {
    console.log("Hi Class!");
  },
};

let superDeeplyClonedObj = superCloneEffective(person);

superDeeplyClonedObj.lastName = "Odinson";
superDeeplyClonedObj.address.street = "south 1st street";

console.log("person", person);
console.log("superCopiedObject", superDeeplyClonedObj);

superDeeplyClonedObj.sayHi();
```

## Flatten an Array

```js
let input = [[[[[1]]]], 2];

// Array contains only Integers.
function flatten(srcArr) {
  let newArr = [];
  for (element of srcArr) {
    if (Array.isArray(element)) {
      let flatteredArrayUsingRecursion = flatten(element);
      // for(ele of flatteredArrayUsingRecursion){
      //     newArr.push(ele);
      // }

      newArr.push(...flatteredArrayUsingRecursion);
    } else {
      newArr.push(element);
    }
  }

  return newArr;
}

let flattenedArr = flatten(input);
console.log("flattenedArr: ", flattenedArr);
```

## Flatten an Object

```js
function flattenObject(obj, parentKey = "", result = {}) {
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      const newKey = parentKey ? `${parentKey}.${key}` : key;
      if (
        typeof obj[key] === "object" &&
        obj[key] !== null &&
        !Array.isArray(obj[key])
      ) {
        flattenObject(obj[key], newKey, result);
      } else {
        result[newKey] = obj[key];
      }
    }
  }
  return result;
}
```

## Polyfill for reduce

```js
if (!Array.prototype.myReduce) {
  Array.prototype.myReduce = function (callback, initialValue) {
    if (typeof callback !== "function") {
      throw new TypeError(callback + " is not a function");
    }

    const array = this;
    let accumulator = initialValue;
    let startIndex = 0;

    // If no initialValue, use first element as initial and start from index 1
    if (accumulator === undefined) {
      if (array.length === 0) {
        throw new TypeError("Reduce of empty array with no initial value");
      }
      accumulator = array[0];
      startIndex = 1;
    }

    for (let i = startIndex; i < array.length; i++) {
      if (i in array) {
        // Skip empty slots (sparse arrays)
        accumulator = callback(accumulator, array[i], i, array);
      }
    }

    return accumulator;
  };
}
```

## Set Timeout Polyfill

```js
function customSetTimeout(callback, delay) {
  let start = Date.now(); // Current time

  function checkTime() {
    if (Date.now() - start >= delay) {
      callback(); // Call the function after delay
    } else {
      requestAnimationFrame(checkTime); // Check again
    }
  }

  requestAnimationFrame(checkTime);
}

// Usage:
console.log("Before");
customSetTimeout(() => console.log("Executed after 2 sec"), 2000);
console.log("After");
```

## Set Interval Polyfill

```js
function mySetInterval(cb, delay) {
  let timerIdObject = {
    flag: true,
  };

  function helperMethod() {
    if (timerIdObject.flag) {
      cb();
      setTimeout(helperMethod, delay);
    }
  }

  setTimeout(helperMethod, delay);
  return timerIdObject;
}

function clearMyInterval(timerIdObject) {
  timerIdObject.flag = false;
}

/*******usage****/
function cb() {
  console.log("I will be called on every interval: " + Date.now());
}

let timerIdObject = mySetInterval(cb, 1000);

function cancelInterval() {
  console.timeEnd();
  console.log("cancelled th cb");
  clearMyInterval(timerIdObject);
}

console.time();
setTimeout(cancelInterval, 5000);

console.log("After");
```

## Mystery E-commerce

```js
function updateUsers(users, userObject, item) {
  // Check if the user already exists
  let userIndex = users.findIndex((user) => user.name === userObject.name);

  if (userIndex === -1) {
    // User does not exist, create and add them with the new order
    // Initialize orders with the new item
    userObject.orders = [
      {
        id: 1,
        name: item,
      },
    ];
    users.push(userObject);
  } else {
    // User exists, check for orders
    let existingUser = users[userIndex];
    if (!existingUser.orders) {
      // Initialize orders array if it doesn't exist
      existingUser.orders = [
        {
          id: 1,
          name: item,
        },
      ];
    } else {
      // Add item only if it's not already in the orders array
      let itemExists = existingUser.orders.some(
        (order) => order.name === item.name
      );
      if (!itemExists) {
        existingUser.orders.push({
          id: existingUser.orders.length + 1, // Increment the order id based on the length of the orders array
          name: item,
        });
      }
    }
  }

  return users;
}
```

## Decimal to Binary

```js
function ConvertToBinary(dec) {
  return Number(dec).toString(2);
}
```

## Binary to Decimal

```js
function binaryToDecimal(binaryStr) {
  return parseInt(binaryStr, 2);
}
```

## Filter Anagrams

- [nap - pan]

```js
function aclean(arr) {
  // Create a map to store unique anagrams
  let map = new Map();

  arr.forEach((word) => {
    // Convert word to lowercase and sort its letters alphabetically
    let sorted = word.toLowerCase().split("").sort().join("");

    // Only add the word to the map if it is not already present
    if (!map.has(sorted)) {
      map.set(sorted, word);
    }
  });

  // Return an array of the values (the first occurrences of each anagram)
  return Array.from(map.values());
}
```

## Make Array.last() method

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
