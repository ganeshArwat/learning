## ✅ **Core React Questions & Answers**

### 1. **What is React?**

**Answer:**
React is a JavaScript library developed by Facebook for building fast, interactive user interfaces using reusable components. It's based on a **component-driven** architecture and uses a **virtual DOM** for performance optimization.

---

### 2. **What is the Virtual DOM?**

**Answer:**
The Virtual DOM is a lightweight JavaScript representation of the real DOM. React updates the virtual DOM first, compares it with the previous version (diffing), and then updates only the changed parts in the actual DOM (reconciliation), improving performance.

---

### 3. **What are components in React?**

**Answer:**
Components are the building blocks of a React app. They are reusable and come in two types:

- **Functional Components** (using hooks)
- **Class Components** (using lifecycle methods)

---

### 4. **What is JSX?**

**Answer:**
JSX (JavaScript XML) is a syntax extension that allows writing HTML-like code within JavaScript. It gets transpiled to `React.createElement()` calls.

```js
const element = <h1>Hello, React!</h1>;
```

---

### 5. **What is the difference between Props and State?**

**Answer:**

| Props                        | State                           |
| ---------------------------- | ------------------------------- |
| Passed from parent component | Managed within the component    |
| Immutable                    | Mutable                         |
| Read-only                    | Can be updated using `setState` |

---

### 6. **What is `useState` and how do you use it?**

**Answer:**
`useState` is a hook that adds state to functional components.

```js
const [count, setCount] = useState(0);
```

---

### 7. **Explain `useEffect` Hook.**

**Answer:**
`useEffect` is used for side effects like data fetching, DOM manipulation, etc.

```js
useEffect(() => {
  console.log("Component Mounted");
}, []);
```

- The second argument (dependency array) controls when the effect runs.

---

### 8. **What is the difference between controlled and uncontrolled components?**

**Answer:**

- **Controlled**: Form input values are managed by React state.
- **Uncontrolled**: Form input values are managed by the DOM.

---

### 9. **What is React Context API?**

**Answer:**
React Context provides a way to pass data through the component tree without manually passing props at every level. It helps with **props drilling** problems.

---

### 10. **What are keys in React and why are they important?**

**Answer:**
Keys help React identify which items have changed, are added, or removed in a list. They improve rendering performance.

```js
items.map((item) => <li key={item.id}>{item.name}</li>);
```

---

### 11. **What is lifting state up in React?**

**Answer:**
When multiple components need to share state, the state is "lifted up" to their common parent and passed down as props.

---

### 12. **What are React Fragments?**

**Answer:**
Fragments let you group multiple elements without adding extra DOM nodes.

```js
<>
  <h1>Title</h1>
  <p>Description</p>
</>
```

---

### 13. **What is `useMemo` and when would you use it?**

**Answer:**
`useMemo` is used to memoize expensive computations and avoid re-executing them on every render.

```js
const memoizedValue = useMemo(() => computeValue(a, b), [a, b]);
```

---

### 14. **What is `useCallback`?**

**Answer:**
`useCallback` returns a memoized version of a callback function, useful to prevent unnecessary re-renders of child components.

```js
const handleClick = useCallback(() => {
  doSomething();
}, []);
```

---

### 15. **What are Higher-Order Components (HOC)?**

**Answer:**
An HOC is a function that takes a component and returns a new component with additional functionality.

```js
const EnhancedComponent = withLogger(MyComponent);
```

---

### 16. **How do you handle errors in React?**

**Answer:**
By using **Error Boundaries** — special class components that catch JavaScript errors in child components.

---

### 17. **What is React Router and how does it work?**

**Answer:**
React Router is used for client-side routing. It maps URL paths to components using `<Route>` and `<Link>`.

```js
<Route path="/home" element={<Home />} />
```

---

### 18. **How do you optimize performance in React apps?**

**Answer:**

- Use `React.memo`, `useMemo`, and `useCallback`
- Lazy load components with `React.lazy`
- Code splitting
- Avoid unnecessary re-renders

---

### 19. **What is Redux and when would you use it?**

**Answer:**
Redux is a state management library useful in large applications where multiple components need to share and update state in a predictable way using actions and reducers.

---

### 20. **What is the difference between React and Angular/Vue?**

**Answer:**

| Feature      | React      | Angular     | Vue        |
| ------------ | ---------- | ----------- | ---------- |
| Type         | Library    | Framework   | Framework  |
| Language     | JavaScript | TypeScript  | JavaScript |
| Data Binding | One-way    | Two-way     | Two-way    |
| Flexibility  | High       | Opinionated | Moderate   |

---

### 21. **What is Prop Drilling and how can it be avoided?**

**Answer:**
Prop Drilling is the process of passing data from parent to child to grandchild, even if intermediate components don't need it.

**Avoid it by:**

- Using **Context API**
- Using **state management libraries** like Redux or Zustand

---

### 22. **How do you conditionally render elements in React?**

**Answer:**
Using:

- Ternary operator:

  ```js
  {
    isLoggedIn ? <Dashboard /> : <Login />;
  }
  ```

- Logical AND:

  ```js
  {
    isAdmin && <AdminPanel />;
  }
  ```

---

### 23. **What is the difference between `useEffect` and `useLayoutEffect`?**

**Answer:**

| `useEffect`               | `useLayoutEffect`                 |
| ------------------------- | --------------------------------- |
| Runs after paint/render   | Runs before the paint             |
| Doesn't block UI painting | Can block UI if long-running      |
| Commonly used             | Use when DOM needs to be measured |

---

### 24. **What is React.lazy and Suspense?**

**Answer:**
Used for **code-splitting** and **lazy loading** components:

```js
const LazyComponent = React.lazy(() => import("./MyComponent"));
<Suspense fallback={<Loader />}>
  <LazyComponent />
</Suspense>;
```

---

### 25. **What are controlled components?**

**Answer:**
In controlled components, form inputs like `<input>` are controlled by React state.

```js
<input value={value} onChange={(e) => setValue(e.target.value)} />
```

---

### 26. **What is reconciliation in React?**

**Answer:**
Reconciliation is React's process of comparing the new virtual DOM with the previous one and updating only the changed parts in the real DOM efficiently.

---

### 27. **What is the difference between `React.memo` and `useMemo`?**

**Answer:**

- `React.memo`: Memoizes **components** to prevent unnecessary re-renders.
- `useMemo`: Memoizes **values** or **computed results** inside components.

---

### 28. **How to handle forms in React?**

**Answer:**

- Controlled form with state:

```js
const [name, setName] = useState("");
<form onSubmit={handleSubmit}>
  <input value={name} onChange={(e) => setName(e.target.value)} />
</form>;
```

- You can also use libraries like **Formik** or **React Hook Form**.

---

### 29. **How do you handle side effects in React?**

**Answer:**
Using `useEffect`, for things like:

- Fetching data
- Subscribing to events
- Manually modifying the DOM

---

### 30. **What is the difference between mounting, updating, and unmounting in React?**

**Answer:**

- **Mounting**: Component is being inserted into the DOM
- **Updating**: Component is being re-rendered due to state/props change
- **Unmounting**: Component is removed from the DOM

---

### 31. **Can you explain how React updates the DOM?**

**Answer:**

1. React renders virtual DOM.
2. Compares it with the previous virtual DOM (diffing).
3. Calculates minimal number of changes (patch).
4. Updates only necessary real DOM parts.

---

### 32. **Why should we avoid using index as key in lists?**

**Answer:**
Using `index` as key can lead to bugs in reordering or deleting list items. It breaks identity and affects React’s optimization.

---

### 33. **How do you prevent re-renders in React?**

**Answer:**

- Use `React.memo` for components
- Use `useMemo` for values
- Use `useCallback` for functions
- Avoid unnecessary state updates

---

### 34. **What is the purpose of `useRef`?**

**Answer:**

- To access a **DOM node**
- To store a **mutable value** that doesn't trigger re-render

```js
const inputRef = useRef();
inputRef.current.focus();
```

---

### 35. **What is React Portals?**

**Answer:**
React Portals allow you to render children into a DOM node that exists outside the DOM hierarchy of the parent component.

```js
ReactDOM.createPortal(child, document.getElementById("modal-root"));
```

---

### 36. **How do you fetch data in React?**

**Answer:**
Using `fetch` or `axios` inside `useEffect`.

```js
useEffect(() => {
  fetch("https://api.example.com/data")
    .then((res) => res.json())
    .then((data) => setData(data));
}, []);
```

---

### 37. **How do you share state between components?**

**Answer:**

- Lift state up to the **common parent**
- Use **Context API**
- Use **Redux or Zustand**

---

### 38. **What is an event handler in React?**

**Answer:**
A function that handles user interactions like click, input, submit.

```js
<button onClick={handleClick}>Click</button>
```

---

### 39. **What are the lifecycle methods in class components?**

**Answer:**

- `componentDidMount`
- `componentDidUpdate`
- `componentWillUnmount`

In functional components, they are handled via `useEffect`.

---

### 40. **Explain Redux in one minute.**

**Answer:**
Redux is a predictable state container for JavaScript apps. It uses:

- A **single source of truth** (store)
- **Actions** to describe what happened
- **Reducers** to update the state

---
