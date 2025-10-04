## 🔹 `useState` – Managing State in Functional Components

### 🔧 What it does:

`useState` lets you add **state** to functional components.

### ✅ Syntax:

```jsx
const [state, setState] = useState(initialValue);
```

### 🧪 Example:

```jsx
import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}
```

---

## 🔹 `useEffect` – Handling Side Effects

### 🔧 What it does:

`useEffect` lets you **perform side effects** (data fetching, DOM manipulation, subscriptions) in functional components.

### ✅ Basic Usage:

```jsx
useEffect(() => {
  // side-effect code
}, [dependencies]);
```

### 📦 Common Use Cases:

- Fetching data
- Setting up event listeners
- Updating the DOM
- Cleanup logic on unmount

### 🧪 Example 1: Run once on mount

```jsx
useEffect(() => {
  console.log("Mounted!");
}, []);
```

### 🧪 Example 2: Run when `count` changes

```jsx
useEffect(() => {
  console.log(`Count changed to: ${count}`);
}, [count]);
```

### 🧪 Example 3: Cleanup on unmount

```jsx
useEffect(() => {
  const timer = setInterval(() => console.log("Tick"), 1000);
  return () => clearInterval(timer); // cleanup
}, []);
```

---

### ⚠️ Common Gotchas

- `useEffect` **runs after every render** by default, unless dependencies are specified.
- Be careful with **infinite loops** (e.g., updating state inside `useEffect` without dependencies).

---

## 🎯 What is a _Side Effect_ in React?

In React (and in programming in general), a **side effect** is any action that affects something **outside the scope of the current function** — things that aren't purely related to rendering UI.

---

### 🔄 In Simple Terms:

If a function:

- fetches data
- sets a timer
- subscribes to an event
- manipulates the DOM manually
- logs something to the console
- reads/writes to localStorage
- updates a global variable

That’s a **side effect**.

---

### 📦 React Example:

When a component renders, it should be **pure** — meaning, given the same inputs (props/state), it should return the same output (JSX).

However, we often need to:

- Fetch user data from an API ✅
- Set a timer ✅
- Listen to scroll or resize events ✅

These don’t belong in the render function directly — instead, they belong in the `useEffect()` hook.

---

### ✅ Why React separates them:

- Keeps rendering **pure and predictable**
- Lets React control when and how side effects run (after render)
- Ensures proper cleanup of side effects (like removing timers or event listeners)

---

### 📌 Example of a Side Effect in React:

```jsx
useEffect(() => {
  // Side effect: API call
  fetch("https://api.example.com/data")
    .then((response) => response.json())
    .then((data) => setData(data));
}, []);
```

Here, the data fetch is a **side effect** — it talks to an external server.

---

## 📏 Rules of Hooks – When and How Hooks Should Be Used

Hooks are powerful, but they come with **strict rules** to keep behavior predictable and avoid bugs. Let's break them down:

---

### ✅ Rule 1: **Only call hooks at the top level**

This means:

- **Do NOT call hooks inside** loops, conditions, or nested functions.

❌ Bad:

```jsx
if (userLoggedIn) {
  useEffect(() => {
    /* ... */
  }, []);
}
```

✅ Good:

```jsx
useEffect(() => {
  if (userLoggedIn) {
    // your logic here
  }
}, [userLoggedIn]);
```

Why? Because React relies on the **order** of hooks to track state and effects properly. If the order changes (like in a loop or condition), React will misbehave.

---

### ✅ Rule 2: **Only call hooks from React functions**

- ✅ Call hooks **inside functional components**
- ✅ Or call hooks inside **custom hooks**
- ❌ Never call them in regular JS functions or class components

❌ Bad:

```js
function doSomething() {
  useState(); // ❌ invalid
}
```

✅ Good:

```jsx
function MyComponent() {
  const [count, setCount] = useState(0); // ✅ valid
}
```

---

### ✅ Rule 3: **Custom Hooks must start with `use`**

This is just a naming convention, but React uses this to **detect custom hooks**.

```js
function useMyCustomHook() {
  // valid
}
```

---

### ⚙️ ESLint Can Help!

React provides an ESLint plugin (`eslint-plugin-react-hooks`) that enforces these rules. It catches most violations automatically.

---

### Summary:

| Rule                           | Why it matters                    |
| ------------------------------ | --------------------------------- |
| Call hooks only at top level   | Maintain consistent hook order    |
| Call hooks only in React funcs | Prevent misuse                    |
| Name custom hooks with `use`   | Helps React linting and dev tools |

---

## ⚖️ `useEffect` vs `useLayoutEffect` in React

Both hooks are used to perform **side effects**, but the **timing** of their execution is what sets them apart.

---

### 🕒 `useEffect` – Runs **after** the DOM is painted

- It’s **asynchronous**.
- Ideal for **API calls**, **event listeners**, **timers**, and other non-blocking effects.
- It **does not block** the browser's painting of the screen.

🧠 Think of it as: “Do this _after_ the user sees the screen.”

### ✅ Example:

```jsx
useEffect(() => {
  console.log("DOM has been painted");
}, []);
```

---

### ⏱️ `useLayoutEffect` – Runs **before** the DOM is painted

- It’s **synchronous** and runs **after all DOM mutations** but **before painting**.
- Useful when you need to **measure layout** or **synchronously manipulate the DOM**.
- It **blocks rendering** until the code inside finishes.

🧠 Think of it as: “Do this _before_ the user sees the screen.”

### ✅ Example:

```jsx
useLayoutEffect(() => {
  const width = document.getElementById("box").offsetWidth;
  console.log("Box width:", width);
}, []);
```

---

### ⚠️ When to Use Each?

| Use Case                          | Hook              |
| --------------------------------- | ----------------- |
| Fetching data from an API         | `useEffect`       |
| Adding event listeners            | `useEffect`       |
| Animations triggered after paint  | `useEffect`       |
| Measuring DOM dimensions          | `useLayoutEffect` |
| Preventing visual glitches        | `useLayoutEffect` |
| Manually updating scroll position | `useLayoutEffect` |

---

### 🚨 Caution:

Avoid overusing `useLayoutEffect`. Since it blocks painting, it can **hurt performance** if misused. Only use it when **necessary**.

---

## 🔍 `useRef` – Accessing DOM Elements & Persistent Values

### ✅ What is `useRef`?

`useRef` is a hook that returns a **mutable ref object** whose `.current` property persists for the full lifetime of the component.

---

### 🔧 Main Use Cases:

1. **Accessing DOM elements directly**
2. **Storing mutable values** that don't cause re-renders
3. **Keeping previous values** across renders

---

### ✅ Syntax:

```js
const myRef = useRef(initialValue);
```

---

### 📌 1. Accessing DOM Elements:

```jsx
import React, { useRef, useEffect } from "react";

function InputFocus() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus(); // Auto-focus the input field
  }, []);

  return <input ref={inputRef} type="text" />;
}
```

---

### 📌 2. Storing Values Without Triggering Re-renders:

```jsx
function Timer() {
  const countRef = useRef(0);

  useEffect(() => {
    const interval = setInterval(() => {
      countRef.current++;
      console.log(countRef.current); // Logs count but doesn't re-render
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return <h1>Open console to see count</h1>;
}
```

---

### 📌 3. Keeping Previous State:

```jsx
function PreviousValue({ value }) {
  const prevValue = useRef();

  useEffect(() => {
    prevValue.current = value;
  }, [value]);

  return (
    <div>
      <p>Current: {value}</p>
      <p>Previous: {prevValue.current}</p>
    </div>
  );
}
```

---

### ⚠️ Important Notes:

- Updating `.current` does **not cause a re-render**.
- Avoid using it as a full alternative to `useState`, except for storing **non-UI-affecting values**.

---

## ⚙️ `useReducer` – Managing Complex State Logic

### ✅ What is `useReducer`?

`useReducer` is a hook used when you have **more complex state logic** that involves:

* Multiple sub-values
* Conditional updates
* Toggling, incrementing, etc.

It’s a good alternative to `useState` when state updates depend on **previous state** or involve **multiple actions**.

---

### 🔧 Syntax:

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
```

* `reducer`: a function that takes `state` and `action`, and returns new state
* `dispatch`: a function used to trigger updates

---

### 📌 Example: Counter

```jsx
import React, { useReducer } from 'react';

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
    </>
  );
}
```

---

### 🧠 When to use `useReducer`?

| Scenario                                 | Use          |
| ---------------------------------------- | ------------ |
| Simple state (e.g., toggle, input value) | `useState`   |
| Complex state logic                      | `useReducer` |
| Multiple related states                  | `useReducer` |
| You want Redux-like structure            | `useReducer` |

---

### ⚠️ Tip:

You can also combine `useReducer` with `useContext` for **global state** management in small apps (like a mini Redux).

---

## In React, `memo`, `useMemo`, and `useCallback` are performance optimization tools used to **avoid unnecessary re-renders** or **recomputations** in functional components. Here's a clear explanation of each:

### 🧠 1. `React.memo`

#### Purpose:

Prevents a **functional component** from re-rendering unless its **props change**.

#### Syntax:

```jsx
const MyComponent = React.memo((props) => {
  // render logic
});
```

#### Example:

```jsx
const Child = React.memo(({ name }) => {
  console.log("Child rendered");
  return <div>{name}</div>;
});
```

#### Use when:

* The component renders the same output given the same props.
* Props are primitive or shallowly equal.

---

### 🧠 2. `useMemo`

#### Purpose:

Memoizes the **result of a computation**, so it’s not recalculated unless dependencies change.

#### Syntax:

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

#### Example:

```jsx
const expensiveValue = useMemo(() => {
  return slowFunction(num);
}, [num]);
```

#### Use when:

* You have a computationally expensive calculation.
* The result is reused in rendering.

---

### 🧠 3. `useCallback`

#### Purpose:

Returns a **memoized version of a callback function**, so the function identity doesn't change unless dependencies change.

#### Syntax:

```jsx
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

#### Example:

```jsx
const handleClick = useCallback(() => {
  console.log("Clicked");
}, []);
```

#### Use when:

* You pass callbacks to child components (especially memoized ones).
* You want to avoid unnecessary re-renders due to function reference changes.

---

### Quick Summary:

| Feature       | Prevents                | Used With                | When to Use                       |
| ------------- | ----------------------- | ------------------------ | --------------------------------- |
| `React.memo`  | Re-render of component  | Functional Components    | Props don’t change                |
| `useMemo`     | Re-execution of code    | Expensive Calculations   | Dependencies unchanged            |
| `useCallback` | Re-creation of function | Event Handlers/Callbacks | Prevent function identity changes |

---

## 🔧 Custom Hooks in React

#### ✅ What is a Custom Hook?

A **custom hook** is a JavaScript function whose name starts with `use` and allows you to **reuse stateful logic** across multiple components.

It lets you **extract component logic** into reusable functions while still using React hooks like `useState`, `useEffect`, etc.

---

### 🛠️ Syntax of a Custom Hook

```jsx
function useCustomHook() {
  const [state, setState] = useState(initialValue);

  // custom logic here

  return [state, setState]; // or an object
}
```

---

### ✨ Example: `useCounter` Custom Hook

```jsx
// useCounter.js
import { useState } from 'react';

function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);

  const increment = () => setCount((c) => c + 1);
  const decrement = () => setCount((c) => c - 1);
  const reset = () => setCount(initialValue);

  return { count, increment, decrement, reset };
}

export default useCounter;
```

Then in a component:

```jsx
import useCounter from './useCounter';

function CounterComponent() {
  const { count, increment, decrement, reset } = useCounter(10);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>➕</button>
      <button onClick={decrement}>➖</button>
      <button onClick={reset}>🔄</button>
    </div>
  );
}
```

---

### 🔍 When to Create Custom Hooks

Create a custom hook when:

* You **reuse the same logic** (e.g., timers, API calls, form handling).
* You want to **clean up** a component by moving logic out.
* You're using **multiple hooks** together for a single feature.

---

### 📦 Examples of Common Custom Hooks

| Hook Name         | Purpose                             |
| ----------------- | ----------------------------------- |
| `useFetch`        | Handles API calls                   |
| `useForm`         | Manages form state and validation   |
| `useDebounce`     | Delays value updates (e.g., search) |
| `useLocalStorage` | Syncs state with localStorage       |
| `useToggle`       | Boolean toggle state handler        |

---
