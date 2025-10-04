## 1. Promise.all()

- Waits for all promises to resolve.
- If one promise rejects, the whole Promise.all() rejects.
- Returns an array of results (if all promises resolve).
- Use when all tasks must complete successfully.

```js
const p1 = Promise.resolve(10);
const p2 = new Promise((resolve) => setTimeout(() => resolve(20), 1000));
const p3 = Promise.resolve(30);

Promise.all([p1, p2, p3])
  .then((results) => console.log(results)) // ✅ [10, 20, 30]
  .catch((error) => console.log("Error:", error));
```

- If One Fails

```js
const p1 = Promise.resolve(10);
const p2 = new Promise((resolve, reject) =>
  setTimeout(() => reject("Failed!"), 1000)
);
const p3 = Promise.resolve(30);

Promise.all([p1, p2, p3])
  .then((results) => console.log(results))
  .catch((error) => console.log("Error:", error)); // ❌ "Error: Failed!"
```

## 2. Promise.any() (ES2021)

- Resolves when any one promise resolves.
- Ignores rejected promises unless all reject.
- Returns first resolved value.
- Use when you need the first successful result.

```js
const p1 = new Promise((resolve, reject) => setTimeout(reject, 100, "Error 1"));
const p2 = new Promise((resolve) => setTimeout(resolve, 200, "Success 2"));
const p3 = new Promise((resolve) => setTimeout(resolve, 300, "Success 3"));

Promise.any([p1, p2, p3])
  .then((result) => console.log(result)) // ✅ "Success 2" (first resolved)
  .catch((error) => console.log("All failed:", error));
```

- If All Fail

```js
Promise.any([Promise.reject("Error 1"), Promise.reject("Error 2")]).catch(
  (error) => console.log(error.errors)
); // ❌ ["Error 1", "Error 2"]
```

## 3. Promise.race()

- Resolves or rejects as soon as the first promise settles (resolves or rejects).
- Useful when waiting for the fastest response.
- Use when you need the fastest result, whether success or failure.

```js
const p1 = new Promise((resolve) => setTimeout(resolve, 500, "Winner!"));
const p2 = new Promise((resolve) => setTimeout(resolve, 1000, "Loser!"));

Promise.race([p1, p2])
  .then((result) => console.log(result)) // ✅ "Winner!"
  .catch((error) => console.log("Error:", error));
```

- First One Rejects

```js
const p1 = new Promise((_, reject) => setTimeout(reject, 500, "Error!"));
const p2 = new Promise((resolve) => setTimeout(resolve, 1000, "Success"));

Promise.race([p1, p2])
  .then((result) => console.log(result))
  .catch((error) => console.log("Error:", error)); // ❌ "Error!"
```

## Promise.allSettled()

- The Promise.allSettled() method is a Promise combinator that waits for all promises to settle (resolve or reject) and returns an array of results.
- Unlike Promise.all(), it never rejects—it always returns an array of objects with the status (fulfilled or rejected) and corresponding values/errors.

```js
const p1 = Promise.resolve("Success 1"); // ✅ Resolved
const p2 = new Promise((resolve) => setTimeout(resolve, 1000, "Success 2")); // ✅ Resolved after 1 sec
const p3 = Promise.reject("Error 3"); // ❌ Rejected

Promise.allSettled([p1, p2, p3]).then((results) => console.log(results));
```

```
[
  { status: "fulfilled", value: "Success 1" },
  { status: "fulfilled", value: "Success 2" },
  { status: "rejected", reason: "Error 3" }
]
```

## Promise Polyfill

```js
const PENDING = "pending";
const RESOLVED = "resolved";
const REJECTED = "rejected";

// function constructor
function CustomPromise(executorFn) {
  // Add required properties and methods
  let State = PENDING;
  let Value = undefined;
  let scbArr = []; // Success callback's array/queue.
  let fcbArr = []; // Failure callback's array/queue.

  // attach resolve.
  const resolve = (value) => {
    // If result of a promise is already defined in that case we can't revisit the promise.
    if (State !== PENDING) {
      return;
    }

    State = RESOLVED;
    Value = value;

    // Call your all success from scbArr.
    scbArr.forEach((cb) => {
      cb(Value);
    });
  };

  // attach reject.
  const reject = (value) => {
    // If result of a promise is already defined in that case we can't revisit the promise.
    if (State !== PENDING) {
      return;
    }

    State = REJECTED;
    Value = value;

    // Call your all failures from fcbArr.
    fcbArr.forEach((cb) => {
      cb(Value);
    });
  };

  // Most Important: Don't forget to call your executor function.
  executorFn(resolve, reject);

  // Thread `then` with the resolve.
  this.then = function (cb) {
    if (State === RESOLVED) {
      cb(Value);
    } else {
      scbArr.push(cb);
    }
  };

  // Thread `catch` with the reject.
  this.catch = function (cb) {
    if (State === REJECTED) {
      cb(Value);
    } else {
      fcbArr.push(cb);
    }
  };
}

const executorFn = (resolve, reject) => {
  // Cb based fn for resolved state.
  setTimeout(() => {
    resolve("Hey I'm resolved!!!!");
  }, 2000);

  // Cb based fn for rejected state.
  setTimeout(() => {
    reject("Hey I got rejected! with error: .....");
  }, 3000);
};

// ***************** usage of your custom *****************
const myPromise = new CustomPromise(executorFn);

const cb = (data) => {
  console.log(data);
};

myPromise.then(cb);

myPromise.then((data) => {
  console.log("I am the second then");
});

myPromise.then((data) => {
  console.log("I am the third then: ", data);
});

myPromise.catch((err) => {
  console.log("Error: ", err);
});

myPromise.catch((data) => {
  console.log("I am the second catch");
});
```

## Promise.all Polyfill

```js
Promise.myPromiseAll = function (arrOfPromises) {
  return new Promise(function (resolve, reject) {
    if (!Array.isArray(arrOfPromises)) {
      reject("Expected a array of promises. But recived: ", arrOfPromises);
      return;
    }

    let unResolvedPromisesArrayLength = arrOfPromises.length;
    const resolvedPromisesResults = [];

    if (unResolvedPromisesArrayLength === 0) {
      resolve(resolvedPromisesResults);
    }

    arrOfPromises.forEach(async (promise) => {
      try {
        const value = await promise;
        resolvedPromisesResults.push(value);

        unResolvedPromisesArrayLength--;

        if (unResolvedPromisesArrayLength === 0) {
          resolve(resolvedPromisesResults);
        }
      } catch (err) {
        reject(err);
      }
    });
  });
};

//  when all the promises are resolved
// Test Case 1
const p0 = Promise.resolve(3);
const p1 = 42;
const p2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("foo");
  }, 1000);
});

Promise.myPromiseAll([p0, p1, p2])
  .then(console.log)
  .catch((err) => {
    console.log("promise got rejected with error: " + err);
  });

// Real.
Promise.all([p0, p1, p2])
  .then(console.log)
  .catch((err) => {
    console.log("promise got rejected with error: " + err);
  });

//  when all the promises are rejected
// Test Case 2
const p0_1 = Promise.resolve(3);
const p1_1 = 42;
const p2_1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("foo");
  }, 1000);
});

Promise.myPromiseAny = function (arrOfPromises) {
  return new Promise((resolve, reject) => {
    if (!Array.isArray(arrOfPromises)) {
      return reject(new TypeError("Expected an array of promises."));
    }

    let rejectedCount = 0;
    const errors = [];

    if (arrOfPromises.length === 0) {
      return reject(new AggregateError(errors, "All promises were rejected"));
    }

    arrOfPromises.forEach((promise, index) => {
      Promise.resolve(promise)
        .then(resolve) // As soon as one promise resolves, resolve the whole Promise.any
        .catch((err) => {
          errors[index] = err;
          rejectedCount++;

          // If all promises are rejected, reject with AggregateError
          if (rejectedCount === arrOfPromises.length) {
            reject(new AggregateError(errors, "All promises were rejected"));
          }
        });
    });
  });
};
// Our Method.
Promise.myPromiseAll([p0_1, p1_1, p2_1])
  .then(console.log)
  .catch((err) => {
    console.log("promise got rejected with error: " + err);
  });

// Real
Promise.all([p0_1, p1_1, p2_1])
  .then(console.log)
  .catch((err) => {
    console.log("promise got rejected with error: " + err);
  });
```

## Promise.any Polyfill

```js
Promise.myPromiseAny = function (arrOfPromises) {
  return new Promise((resolve, reject) => {
    if (!Array.isArray(arrOfPromises)) {
      return reject(new TypeError("Expected an array of promises."));
    }

    let rejectedCount = 0;
    const errors = [];

    if (arrOfPromises.length === 0) {
      return reject(new AggregateError(errors, "All promises were rejected"));
    }

    arrOfPromises.forEach((promise, index) => {
      Promise.resolve(promise)
        .then(resolve) // As soon as one promise resolves, resolve the whole Promise.any
        .catch((err) => {
          errors[index] = err;
          rejectedCount++;

          // If all promises are rejected, reject with AggregateError
          if (rejectedCount === arrOfPromises.length) {
            reject(new AggregateError(errors, "All promises were rejected"));
          }
        });
    });
  });
};

// ✅ **Test Cases**
const p1 = Promise.reject("Error 1");
const p2 = Promise.reject("Error 2");
const p3 = new Promise((resolve) => setTimeout(resolve, 1000, "Success 3"));
const p4 = Promise.resolve("Success 4");

// **Case 1: At least one promise resolves**
Promise.myPromiseAny([p1, p2, p3, p4])
  .then(console.log) // Output: "Success 4" (first resolved value)
  .catch(console.error);

// **Case 2: All promises reject**
Promise.myPromiseAny([p1, p2])
  .then(console.log)
  .catch((err) => console.error(err.errors)); // Output: ["Error 1", "Error 2"]
```

## Promise.race Polyfill

```js
Promise.myPromiseRace = function (arrOfPromises) {
  return new Promise((resolve, reject) => {
    if (!Array.isArray(arrOfPromises)) {
      return reject(new TypeError("Expected an array of promises."));
    }

    if (arrOfPromises.length === 0) {
      return; // `Promise.race([])` returns a pending promise, so we do nothing.
    }

    arrOfPromises.forEach((promise) => {
      Promise.resolve(promise)
        .then(resolve) // If any promise resolves, resolve the entire race.
        .catch(reject); // If any promise rejects first, reject the entire race.
    });
  });
};

// ✅ **Test Cases**
const p1 = new Promise((resolve) =>
  setTimeout(resolve, 3000, "Resolved in 3s")
);
const p2 = new Promise((resolve) =>
  setTimeout(resolve, 2000, "Resolved in 2s")
);
const p3 = new Promise((resolve) =>
  setTimeout(resolve, 1000, "Resolved in 1s")
);
const p4 = new Promise((_, reject) =>
  setTimeout(reject, 500, "Rejected in 0.5s")
);

// **Case 1: First promise resolves**
Promise.myPromiseRace([p1, p2, p3])
  .then(console.log) // Output: "Resolved in 1s"
  .catch(console.error);

// **Case 2: First promise rejects**
Promise.myPromiseRace([p1, p2, p3, p4]).then(console.log).catch(console.error); // Output: "Rejected in 0.5s"
```
