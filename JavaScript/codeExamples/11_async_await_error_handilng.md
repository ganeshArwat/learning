# JS-11: Async await & Error handling

## Assignment

- Q1. JS Lecture 10: MCQ - 1 Generator

```js
function* f(...a) {
  let s = new Set();
  for (x in a) {
    s.add(a[x]);
    yield a[x];
  }
  yield s;
}

let f1 = f(3, 2, 1);

while (true) {
  let yv = f1.next().value;
  if (typeof yv == "object") {
    console.log(yv);
    yv.add(3);
    console.log(yv);
    break;
  }
}
```

```
Output :
actual output
Set(3) { 3, 2, 1 }
Set(3) { 3, 2, 1 }

answer
Set {1,2,3}
Set {1,2,3}
```

