## 🔁 React Component Lifecycle: Mounting, Updating, Unmounting

React has **three main phases** in a component's life:

---

### 1️⃣ **Mounting Phase**

This is when a component is being **created and inserted** into the DOM.

**Class Component Methods:**

- `constructor()`
- `static getDerivedStateFromProps()` _(rarely used)_
- `render()`
- `componentDidMount()` ✅

📌 `componentDidMount()` is commonly used to:

- Fetch data from APIs
- Add event listeners
- Set timers

```jsx
class MyComponent extends React.Component {
  componentDidMount() {
    console.log("Component mounted!");
  }

  render() {
    return <h1>Hello!</h1>;
  }
}
```

**Functional Equivalent (with hooks):**

```jsx
useEffect(() => {
  console.log("Mounted!");
}, []);
```

---

### 2️⃣ **Updating Phase**

This happens when:

- Props or state changes
- The component re-renders

**Class Component Methods:**

- `static getDerivedStateFromProps()`
- `shouldComponentUpdate()`
- `render()`
- `getSnapshotBeforeUpdate()`
- `componentDidUpdate(prevProps, prevState)` ✅

📌 `componentDidUpdate()` is used to:

- Respond to prop/state changes
- Run side-effects when a specific prop/state changes

```jsx
componentDidUpdate(prevProps, prevState) {
  if (this.props.count !== prevProps.count) {
    console.log('Count changed!');
  }
}
```

**Functional Equivalent (with hooks):**

```jsx
useEffect(() => {
  console.log("Count changed!");
}, [count]);
```

---

### 3️⃣ **Unmounting Phase**

This is when the component is removed from the DOM.

**Class Component Method:**

- `componentWillUnmount()` ✅

📌 Used to:

- Clean up subscriptions
- Clear timers or listeners

```jsx
componentWillUnmount() {
  console.log('Component will unmount');
}
```

**Functional Equivalent:**

```jsx
useEffect(() => {
  return () => {
    console.log("Cleanup on unmount");
  };
}, []);
```

---
## 🧱 **Error Boundaries in React**

### 🔸 What are Error Boundaries?

Error Boundaries are **React components** that catch JavaScript errors anywhere in their **child component tree**, log those errors, and display a **fallback UI** instead of crashing the entire app.

They catch errors in:

* Rendering
* Lifecycle methods
* Constructors of child components

But they **do NOT** catch:

* Errors in event handlers
* Async code (like setTimeout, promises)
* Server-side rendering
* Errors thrown in the error boundary itself

---

### 🔹 Methods in Class Components

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  // 1. Update state so the next render shows the fallback UI
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  // 2. Log the error
  componentDidCatch(error, info) {
    console.error("Error caught by boundary:", error, info);
  }

  render() {
    if (this.state.hasError) {
      return <h2>Something went wrong.</h2>;
    }
    return this.props.children;
  }
}
```

### 🔸 Usage Example

```jsx
<ErrorBoundary>
  <MyComponent />
</ErrorBoundary>
```

Now if `MyComponent` throws an error during rendering or lifecycle, it won’t break the entire app — just shows the fallback UI.

---

### ✅ In Functional Components?

React does not support hooks-based error boundaries yet. You **must use class components** for error boundaries.

---