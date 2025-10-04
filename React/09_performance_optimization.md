## **Why Re-renders Occur in React**

Re-renders in React happen **whenever a component's state or props change**. React uses these changes to update the UI efficiently. Here's a breakdown of why and when re-renders occur:

---

### ✅ **Main Causes of Re-renders in React:**

1. **State Changes (`useState`, `this.setState`)**

   - If you call a state setter like `setCount(newValue)`, React will re-render the component.

2. **Props Change**

   - If the parent component passes new props to a child, the child will re-render.

3. **Context Changes**

   - If you're using `useContext`, and the context value changes, every component that consumes the context re-renders.

4. **Force Update**

   - Calling `forceUpdate()` in class components or updating a dummy state can force a re-render.

5. **Redux Store / Zustand / Recoil Updates**

   - If you're using a state management library, changes to the state slices you're subscribed to can trigger re-renders.

---

### 🔁 **What Doesn't Cause Re-renders:**

- Directly mutating state without using `setState`/`setX` won't trigger re-renders.
- Changing variables outside of state/props won't trigger re-renders unless they're linked to state.

---

### ⚡ Tip: How to Avoid Unnecessary Re-renders

- Use `React.memo` to prevent re-renders if props haven't changed.
- Use `useCallback` and `useMemo` to memoize functions and values.
- Avoid creating new objects/functions inside render if not needed.

---

## **Tools for Performance Optimization in React**

### 🔧 **React Developer Tools (Extension)**

Available for **Chrome**, **Firefox**, and **Edge**.

#### ✅ What It Offers:

- **Components Tab**

  - Inspect component hierarchy
  - View current **props**, **state**, and **context**
  - See hooks like `useState`, `useEffect`, `useRef` values live

- **Profiler Tab** _(for React 16.5+)_

  - Visualize **what components re-rendered**, when, and why
  - View **render timings** and **component flame graphs**
  - Diagnose **unnecessary re-renders**

---

### 🔥 How to Use the Profiler Tool:

1. Go to your app in the browser (with the extension installed).
2. Open **DevTools** → **Profiler** tab.
3. Click **“Record”**, interact with your app, then click **“Stop”**.
4. You’ll see:

   - **Commit tree** (which components re-rendered)
   - **Why each component rendered**
   - Render time for each component
   - Flamegraph and ranked view

---

### 📈 Example Use Case:

You notice your app is lagging when typing in an input.
Using **Profiler**, you might discover:

- A parent component re-renders every keystroke.
- A deeply nested child re-renders unnecessarily.
- Fix: Apply `React.memo()` or lift state.

---

## **🧠 `React.memo` — What It Is and How It Works**

`React.memo` is a **higher-order component** used to **optimize functional components** by **preventing unnecessary re-renders**.

---

### ✅ **What It Does**

When you wrap a component with `React.memo`, React will:

- **Compare the previous props with the new props**
- If the props haven't changed, it **skips re-rendering** the component

---

### 🧾 **Syntax**

```jsx
const MyComponent = React.memo((props) => {
  // component code
});
```

You can also provide a **custom comparison function**:

```jsx
const MyComponent = React.memo(
  (props) => {
    // component code
  },
  (prevProps, nextProps) => {
    // return true if props are equal => no re-render
    // return false if props changed => re-render
  }
);
```

---

### 🎯 **When to Use `React.memo`**

Use it when:

- Your component re-renders frequently with **the same props**
- Your component is **pure** (doesn't rely on external state)
- You want to optimize **performance**

---

### ❗ Caveats

- Works **only on props** — if internal state changes, re-render still happens.
- Not useful if:

  - The component is always re-rendered with new props.
  - The rendering is cheap (minimal JSX or no performance issue).

- Be careful of **reference props** (like arrays, objects, functions) — they often create new references even if data is the same. Use `useCallback` and `useMemo` to help with this.

---

### 🔍 Example

```jsx
const Child = React.memo(({ value }) => {
  console.log("Child rendered");
  return <div>{value}</div>;
});

const Parent = () => {
  const [count, setCount] = useState(0);
  return (
    <>
      <button onClick={() => setCount((c) => c + 1)}>Increment</button>
      <Child value="Hello" />
    </>
  );
};
```

➡️ Clicking the button updates `count`, but `Child` **won't re-render** because its props haven't changed.

---

## **📦 Code Splitting and Lazy Loading in React**

### 🚀 **1. What is Code Splitting?**

**Code Splitting** is the practice of **splitting your JavaScript bundle** into smaller chunks that can be **loaded on demand**, instead of delivering one large file at once.

🔹 **Why?**
It **reduces initial load time**, improves performance, and makes your app feel faster.

---

### 💤 **2. What is Lazy Loading?**

**Lazy Loading** means **loading components only when they’re needed**, like when a user navigates to a route that requires it.

It’s React’s way of **doing code splitting at the component level**.

---

### ⚙️ **How to Implement in React**

React provides built-in support using:

#### ✅ `React.lazy()`

Used to dynamically import components.

#### ✅ `Suspense`

Used to wrap lazy components and show fallback UI (e.g., a loader) while loading.

---

### 🔨 **Example: Lazy Load a Component**

```jsx
import React, { Suspense } from "react";

const LazyComponent = React.lazy(() => import("./LazyComponent"));

function App() {
  return (
    <div>
      <h1>Main App</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
    </div>
  );
}
```

---

### 🧭 **Use with React Router (Route-level Code Splitting)**

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Suspense, lazy } from "react";

const Home = lazy(() => import("./pages/Home"));
const About = lazy(() => import("./pages/About"));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading Page...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

---

### 📦 Bonus: Webpack & Vite Do Code Splitting

When you use tools like **Webpack**, **Vite**, or **Create React App**, they automatically split code based on dynamic `import()` statements.

---

### 📉 Benefits

- Faster initial load
- Better user experience
- Optimized bundle size

---

## **useMemo and useCallback**

let's clarify **`useMemo`** and **`useCallback`** in React. They're powerful hooks for **performance optimization**, especially when working with **expensive computations** or **referential equality** (like avoiding unnecessary re-renders or re-creations of functions/objects).

---

## 🔁 `useMemo` vs `useCallback`

| Feature       | `useMemo`                                  | `useCallback`                              |
| ------------- | ------------------------------------------ | ------------------------------------------ |
| Purpose       | Memoize a **value** (object, number, etc.) | Memoize a **function**                     |
| Syntax        | `useMemo(() => computeValue, [deps])`      | `useCallback(() => fn, [deps])`            |
| Returns       | **Result** of the function                 | **Function** itself                        |
| Used to avoid | Recomputing expensive calculations         | Recreating functions that cause re-renders |

---

## 📦 `useMemo` Example — Avoid Recomputing Expensive Value

```jsx
const expensiveCalculation = (num) => {
  console.log("Calculating...");
  return num * 1000; // Imagine this is CPU-heavy
};

function App({ num }) {
  const result = useMemo(() => expensiveCalculation(num), [num]);

  return <div>Result: {result}</div>;
}
```

> Without `useMemo`, the calculation runs **on every render**. With it, it only recalculates when `num` changes.

---

## 🔁 `useCallback` Example — Avoid Recreating Function

```jsx
const Child = React.memo(({ onClick }) => {
  console.log("Child rendered");
  return <button onClick={onClick}>Click me</button>;
});

function Parent() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log("Clicked");
  }, []);

  return (
    <>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <Child onClick={handleClick} />
    </>
  );
}
```

> Without `useCallback`, `handleClick` is a **new function on every render**, causing `Child` to re-render even if props didn't change. With `useCallback`, it stays the **same reference** until deps change.

---

## ⚠️ When _Not_ to Use Them

- Don’t use them **blindly** — they add complexity and a small overhead.
- Only use when:

  - You notice **unnecessary re-renders**
  - You’re passing **functions/objects** to memoized children (`React.memo`)
  - You have **heavy computations**

---

## **🧊 What is **Virtualization** in React?**

**Virtualization** is a performance optimization technique where **only the visible part of a large list or grid is rendered**, and off-screen items are **not mounted in the DOM** until needed.

---

### 💡 Why Use Virtualization?

Rendering hundreds or thousands of items at once in React (or any UI framework) can:

- **Slow down performance**
- Cause **jank** or **lag**
- Increase **memory usage**

Virtualization solves this by:

- Rendering only what's visible
- Unmounting DOM nodes that are out of view

---

### 📦 Popular Libraries for Virtualization

| Library             | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `react-window`      | Lightweight and fast, great for simple use cases     |
| `react-virtual`     | Very performant, flexible, headless (no styles)      |
| `react-virtualized` | Feature-rich but heavier (older than `react-window`) |

---

### 📂 Example: Using `react-window`

```bash
npm install react-window
```

```jsx
import { FixedSizeList as List } from "react-window";

const MyList = () => (
  <List height={400} itemCount={1000} itemSize={35} width={300}>
    {({ index, style }) => <div style={style}>Item #{index}</div>}
  </List>
);
```

🔍 What happens here:

- Even though there are **1000 items**, only the ones **visible in the 400px container** are rendered.
- As the user scrolls, `react-window` dynamically renders the next set of items.

---

### 🧠 Use Cases

- Infinite scroll
- Chat apps
- Large data tables
- File explorers

---

### ⚠️ Gotchas

- Virtualization doesn't work well with items of **dynamic height** (unless using special techniques).
- SEO engines won’t see off-screen items — not ideal for **crawlable content**.
- Scrolling to an item programmatically requires knowing size estimates.

---
