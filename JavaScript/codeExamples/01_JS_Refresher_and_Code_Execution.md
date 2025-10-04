# JS-1: JS Refresher and Code Execution

## Assignment

- Q1, Js Lecture 1 MCQ: Object

```js
let cap = {
  name: "Steve",
  age: 34,
  isAvenger: true,
};

for (let key in cap) {
  console.log(key, " ", cap[key]);
}
```

```
Output :
    name   Steve
    age   34
    isAvenger   true
```

- Q2, Js Lecture 1 MCQ: 4xScope

```js
let a = 2;
{
  let a = 3;
  {
    let a = 4;
    {
      let a = 5;
      console.log(a);
    }
    console.log(a);
  }
  console.log(a);
}
console.log(a);
```

```
Output :
    5
    4
    3
    2
```

- Q3. JS Lecture 1: A1 - Mystery E-commerce  
  You are owner of a mystery e-commerce website.
  The special thing about this e-commerce store is the user can only buy a single item once! and all users have unique names.
  You are given a users database in the form of an objects' Array.
  Complete the function definition of 'updateUsers' function to perform the following tasks:

  1- Create user if does not exist,add orders if any and return users

  2- Create and Initialize order's array if it does not exist and add first order and return users

  3- Add order to existing order's array and return user

```js
Sample Test Case 1:

Input:
updateUsers(
     users,
     {
       name: "Rajneesh",
       age: 34,
       address: {
         local: "22 Alaknanda",
         city: "Dehradun",
         state: "UK",
       },
     },
     "GOT Book Series"
   )

Output:
[
   {
      "name":"Rajneesh",
      "age":34,
      "address":{
         "local":"22 Alaknanda",
         "city":"Dehradun",
         "state":"UK"
      },
      "orders":[
         {
            "id":1,
            "name":"GOT Book Series"
         },
         {
            "id":2,
            "name":"GOT Book Series"
         }
      ]
   },
   {
      "name":"Bhavesh",
      "age":37,
      "address":{
         "local":"48 DT Row",
         "city":"Hyderabad",
         "state":"AP"
      }
   },
   {
      "name":"Jasbir",
      "age":38,
      "address":{
         "local":"196 Lama Bhavan",
         "city":"Gangtok",
         "state":"Sikkim"
      },
      "orders":[
         {
            "id":1,
            "name":"Chair"
         },
         {
            "id":2,
            "name":"PS5"
         }
      ]
   },
   {
      "name":"Rajneesh",
      "age":34,
      "address":{
         "local":"22 Alaknanda",
         "city":"Dehradun",
         "state":"UK"
      },
      "orders":[
         {
            "id":1,
            "name":"GOT Book Series"
         }
      ]
   }
]

Sample Test Case 2:

Input:
updateUsers(users, {
     name: "Ravi",
     age: 24,
     address: {
       local: "25 Iroda",
       city: "Dehradun",
       state: "UK",
     },
   })

Output:
[
   {
      "name":"Rajneesh",
      "age":34,
      "address":{
         "local":"22 Alaknanda",
         "city":"Dehradun",
         "state":"UK"
      },
      "orders":[
         {
            "id":1,
            "name":"GOT Book Series"
         }
      ]
   },
   {
      "name":"Bhavesh",
      "age":37,
      "address":{
         "local":"48 DT Row",
         "city":"Hyderabad",
         "state":"AP"
      }
   },
   {
      "name":"Jasbir",
      "age":38,
      "address":{
         "local":"196 Lama Bhavan",
         "city":"Gangtok",
         "state":"Sikkim"
      },
      "orders":[
         {
            "id":1,
            "name":"Chair"
         },
         {
            "id":2,
            "name":"PS5"
         }
      ]
   },
   {
      "name":"Rajneesh",
      "age":34,
      "address":{
         "local":"22 Alaknanda",
         "city":"Dehradun",
         "state":"UK"
      },
      "orders":[
         {
            "id":1,
            "name":"GOT Book Series"
         }
      ]
   },
   {
      "name":"Ravi",
      "age":24,
      "address":{
         "local":"25 Iroda",
         "city":"Dehradun",
         "state":"UK"
      }
   }
]


Sample Test Case 3:

Input:
updateUsers(users, {
     name: "Ravi",
     age: 24,
     address: {
       local: "25 Iroda",
       city: "Dehradun",
       state: "UK",
     },
   }, "Chair")

Output:
[
   {
      "name":"Rajneesh",
      "age":34,
      "address":{
         "local":"22 Alaknanda",
         "city":"Dehradun",
         "state":"UK"
      },
      "orders":[
         {
            "id":1,
            "name":"GOT Book Series"
         }
      ]
   },
   {
      "name":"Bhavesh",
      "age":37,
      "address":{
         "local":"48 DT Row",
         "city":"Hyderabad",
         "state":"AP"
      }
   },
   {
      "name":"Jasbir",
      "age":38,
      "address":{
         "local":"196 Lama Bhavan",
         "city":"Gangtok",
         "state":"Sikkim"
      },
      "orders":[
         {
            "id":1,
            "name":"Chair"
         },
         {
            "id":2,
            "name":"PS5"
         }
      ]
   },
   {
      "name":"Rajneesh",
      "age":34,
      "address":{
         "local":"22 Alaknanda",
         "city":"Dehradun",
         "state":"UK"
      },
      "orders":[
         {
            "id":1,
            "name":"GOT Book Series"
         }
      ]
   },
   {
      "name":"Ravi",
      "age":24,
      "address":{
         "local":"25 Iroda",
         "city":"Dehradun",
         "state":"UK"
      },
      "orders":[
         {
            "id":1,
            "name":"Chair"
         }
      ]
   }
]
```

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

```
Output :

```

- Q4. Js Lecture 1 MCQ: Hoisting is real

```js
function real() {
  console.log("I am real. Always Run me");
}

function real() {
  console.log("No I am real one");
}
real();
function real() {
  console.log("you Both are wasted");
}
```

```
Output :
    you Both are wasted"
```

- Q5. Js Lecture 1 MCQ: Let and Scope

```js
let a = 10;
console.log("line number 2", a);
function fn() {
  console.log("line number 4", a);
  let a = 20;
  a++;
  cosole.log("line number 7", a);

  if (a) {
    let a = 30;
    a++;
    console.log("line number 11", a);
  }

  console.log("line number 13", a);
}
fn();
console.log("line number 16", a);
```

```
Output :
line number 2 10
ReferenceError: Cannot access 'a' before initialization

```

## Additional Question

- Q1. Js Lecture 1 MCQ: Invincible Strings

```js
let a = "this only works if and only if";
let b = a.slice(a.indexOf("only"));
let c = b.lastIndexOf("only");

b[c] = "i";
console.log(a);
console.log(b);
```

```
Output :
this only works if and only if
only works if and only if

b[c] = "i"; will not work becase the string is immutable
```

- Q2. JS Lecture 1: H1 - Decimal to Binary

```
Complete the function ConvertToBinary(dec), which takes a decimal number and returns its binary.

Sample Test Case 1:

Input:
45

Output:
101101
```

```js
function ConvertToBinary(dec) {
  return Number(dec).toString(2);
}
```

```
Output :

```

- Q2 - B. JS Lecture 1: H1 - Binary to Decimal

```
Complete the function binaryToDecimal(binary), which takes a binary number text and returns its Decimal.

Sample Test Case 1:

Input:
1010

Output:
10
```

```js
function binaryToDecimal(binaryStr) {
    return parseInt(binaryStr, 2);
}
```

- Q3. JS Lecture 1 MCQ: var scope

```js
var a = 10;
console.log("line number 2", a);
function fn() {
  console.log("line number 4", a);
  var a = 20;
  a++;
  console.log("line number 7", a);
  if (a) {
    var a = 30;
    a++;
    console.log("line number 11", a);
  }
  console.log("line number 13", a);
}

fn();
console.log("line number 16", a);
```

```
Output :
line number 2 10
line number 4 undefined
line number 7 21
line number 11 31
line number 13 31
line number 16 10
```

- Q4. JS Lecture 1: H2 - Filter Anagrams

```
Write a function aclean(arr) that returns an array cleaned from anagrams. Keep the first occurrence of the anagram

Anagrams are words that have the same number of the same letters but in a different order.

For instance: nap - pan ear - are - era cheaters - hectares - teachers

Sample Test Case 1:
Input:
["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

Output:
['nap', 'teachers', 'ear']

```

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
