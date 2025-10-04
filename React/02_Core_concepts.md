# **Section 2: Core Concepts**

---

## ✅ **Fragments (`<>...</>`) – To Avoid Unnecessary Wrapper Divs**

### ❓ Why Fragments?

In React, **every component must return a single parent element**. But sometimes, you don't want to wrap multiple elements in a `<div>`, especially if it:

- **messes up layout**, or
- **adds unwanted DOM nodes**

### ✅ Solution: **React Fragments**

You can use a **Fragment** to group multiple elements **without** adding an extra node to the DOM.

---

### 📘 Basic Syntax

```jsx
function List() {
  return (
    <>
      <li>Item 1</li>
      <li>Item 2</li>
    </>
  );
}
```

This does **not** add an extra parent element to the DOM.

---

### 🧱 Equivalent Full Syntax

```jsx
import React from "react";

function List() {
  return (
    <React.Fragment>
      <li>Item 1</li>
      <li>Item 2</li>
    </React.Fragment>
  );
}
```

> ✅ Use `React.Fragment` when you need to pass keys to fragments (e.g., inside a `.map()`).

---

### 💡 When to Use Fragments

- When returning **multiple sibling elements** from a component
- When you want to avoid **unnecessary `<div>` wrappers**
- In **lists** or **tables** where layout matters

---

### ✅ Example in a Table

```jsx
function TableRow() {
  return (
    <>
      <td>Name</td>
      <td>Age</td>
    </>
  );
}
```

> Without Fragments, this wouldn't work because a table row can't have a `<div>` inside it.

---

Let's continue with **Props and State**:

---

## ✅ **Props and State**

### ⚡ What are **Props**?

**Props** (short for **properties**) are **immutable** inputs passed into a component from a parent component. They allow you to pass data and event handlers to child components.

#### Example: Passing Props

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

function App() {
  return <Welcome name="Ganesh" />;
}
```

- `Welcome` is a **child component** that receives `name` as a prop from the `App` component.
- Props are read-only and cannot be changed by the component receiving them.

---

### ⚡ What is **State**?

**State** refers to a **mutable** object that allows components to manage and control their own data. Unlike props, state is **local** to the component, meaning it cannot be directly accessed or modified by other components.

#### Example: Using State with `useState`

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

- `count` is the **state** variable, and `setCount` is the function to **update** it.
- `useState(0)` initializes `count` to 0.

---

### 🛠 Key Differences Between Props and State

| Feature        | **Props**                                   | **State**                                         |
| -------------- | ------------------------------------------- | ------------------------------------------------- |
| **Mutability** | Immutable (read-only)                       | Mutable (can change over time)                    |
| **Purpose**    | Used to pass data from parent to child      | Used to manage internal data of a component       |
| **Update**     | Cannot be updated by the child component    | Can be updated using `setState()` or `useState()` |
| **Usage**      | Passed down from parent to child components | Used within the component that owns it            |

---

## How to Pass Data from Child to Parent

### 🔁 Steps to Pass Data from Child to Parent in React

1. **Define a function in the parent component** to handle data from the child.
2. **Pass that function as a prop** to the child component.
3. **Call the function from the child**, passing the data as an argument.

---

### ✅ Example

#### `Parent.js`

```jsx
import React, { useState } from 'react';
import Child from './Child';

const Parent = () => {
  const [message, setMessage] = useState('');

  const handleChildData = (data) => {
    setMessage(data); // Update parent's state with data from child
  };

  return (
    <div>
      <h2>Parent Component</h2>
      <p>Message from child: {message}</p>
      <Child onSendData={handleChildData} />
    </div>
  );
};

export default Parent;
```

#### `Child.js`

```jsx
import React from 'react';

const Child = ({ onSendData }) => {
  const sendData = () => {
    onSendData("Hello from Child!");
  };

  return (
    <div>
      <h3>Child Component</h3>
      <button onClick={sendData}>Send Data to Parent</button>
    </div>
  );
};

export default Child;
```

---

### 🔎 What's Happening?

* `Parent` has a function `handleChildData` that updates state.
* `Parent` passes `handleChildData` to `Child` as `onSendData`.
* `Child` calls `onSendData()` with the message.
* `Parent` receives it and updates its state.

---

### ✅ **Derived State**

Sometimes, a component's state depends on its **props** or other external variables. This is called **derived state**.

#### Example:

```jsx
function UserGreeting(props) {
  const [greeting, setGreeting] = useState("");

  useEffect(() => {
    if (props.isLoggedIn) {
      setGreeting("Welcome back!");
    } else {
      setGreeting("Please log in.");
    }
  }, [props.isLoggedIn]);

  return <h1>{greeting}</h1>;
}
```

Here, the state `greeting` is derived from the `isLoggedIn` prop.

---

### ✅ **children Prop**

React provides a special prop called `children`, which allows components to pass down elements to be rendered.

#### Example:

```jsx
function Box({ children }) {
  return <div className="box">{children}</div>;
}

function App() {
  return (
    <Box>
      <h1>Hello World!</h1>
    </Box>
  );
}
```

Here, the `Box` component renders whatever is passed as **children** between its opening and closing tags.

---

Let's move on to **Component Categories**:

---

## ✅ **Component Categories**

React components can be categorized into different types based on their structure and how they handle data and behavior. Understanding these categories will help you organize and design your React application more effectively.

### 1️⃣ **Presentational Components** (Also called Dumb Components)

- These components are responsible only for **displaying UI** and **rendering data**.
- They don’t handle any logic or manage state; instead, they receive data through **props**.
- They're often **stateless** (before the introduction of hooks).
- Their main job is to render the UI and pass user interactions (like clicks) back to container components via **callback functions**.

#### Example:

```jsx
function Button({ label, onClick }) {
  return <button onClick={onClick}>{label}</button>;
}
```

Here, the `Button` component is purely presentational. It receives a label and a click handler through props and renders the UI accordingly.

---

### 2️⃣ **Container Components** (Also called Smart Components)

- These components manage **state**, **logic**, and **behavior**.
- They are usually responsible for **handling user input**, **fetching data**, and **passing data** down to presentational components.
- They may or may not pass data as props to other components.

#### Example:

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>Count: {count}</h1>
      <Button label="Increment" onClick={() => setCount(count + 1)} />
    </div>
  );
}
```

Here, `Counter` is a **container** component because it manages the state (`count`) and passes it to the `Button` component.

---

### 3️⃣ **Stateful Components** vs **Stateless Components**

While **stateful components** manage their internal state (using `useState` or class component state), **stateless components** are more focused on rendering based on props.

However, with the advent of **Hooks** (like `useState` and `useEffect`), even functional components can manage state, making the distinction less rigid.

---

### 4️⃣ **Functional Components** vs **Class Components**

- **Functional components** (with hooks) are **preferred** due to their simplicity and less boilerplate.
- **Class components** are generally **legacy** but still supported in React. They allow the use of lifecycle methods like `componentDidMount`.

### 💡 Best Practice: Use **Functional Components** whenever possible. They're simpler, more concise, and support hooks, which are the future of React.

---

### 📊 Summary of Component Categories

| Component Type     | Key Characteristics                                                 |
| ------------------ | ------------------------------------------------------------------- |
| **Presentational** | Only UI, receives props, no state, renders based on data            |
| **Container**      | Handles state and logic, may pass data to presentational components |
| **Stateful**       | Manages internal state                                              |
| **Stateless**      | Doesn’t manage state, only renders based on props                   |
| **Functional**     | Simple, with hooks, no lifecycle methods, preferred in modern React |
| **Class**          | Legacy, with lifecycle methods, used less in modern React           |

---

Let's continue with **Component Composition**:

---

## ✅ **Component Composition**

In React, **component composition** refers to the concept of building complex UIs by combining smaller, reusable components. It allows you to create a **modular structure** where components are **nested** and **arranged** to form more complex UIs. This is the foundation of React's declarative approach.

### 🔑 Key Principle: **"Composition over Inheritance"**

React encourages **composition** (putting components together) instead of using **inheritance** (subclassing components), which is common in traditional OOP. Composition is more flexible and allows for greater reusability and maintainability.

---

### 🧱 **How Composition Works**

You can **combine multiple components** within a parent component to build a more complex UI.

#### Example:

```jsx
function Header() {
  return <h1>Welcome to My App</h1>;
}

function Footer() {
  return <footer>© 2025 My App</footer>;
}

function Layout() {
  return (
    <div>
      <Header />
      <main>Content goes here</main>
      <Footer />
    </div>
  );
}
```

In the `Layout` component, we’re **composing** `Header` and `Footer` as child components.

---

### 🧩 **Props as a Way to Customize Composition**

You can **pass props** into child components to customize their behavior and make them more reusable.

#### Example: Customizable Card Component

```jsx
function Card({ title, content }) {
  return (
    <div className="card">
      <h2>{title}</h2>
      <p>{content}</p>
    </div>
  );
}

function App() {
  return (
    <div>
      <Card title="React Basics" content="Learn the fundamentals of React." />
      <Card
        title="Advanced React"
        content="Explore advanced topics like hooks and state management."
      />
    </div>
  );
}
```

Here, the `Card` component is reused with different data passed through props, showcasing the flexibility of **composition**.

---

### 🔁 **Children as a Way to Nest Components**

You can use the special `children` prop to **pass nested components** from a parent component to a child.

#### Example: Parent with Nested Components

```jsx
function Box({ children }) {
  return <div className="box">{children}</div>;
}

function App() {
  return (
    <Box>
      <h1>Hello, World!</h1>
      <p>This is inside a box.</p>
    </Box>
  );
}
```

Here, `Box` is a **container** that accepts any nested content (via `children`) and renders it inside a `<div>`.

---

### 💡 **Benefits of Component Composition**

- **Reusability**: Break down complex UIs into small, reusable pieces.
- **Flexibility**: Customize components by passing different props.
- **Readability**: Maintain a clear structure and separate concerns.
- **Maintainability**: Easy to modify and extend without touching other parts of the code.

---

### 📊 Summary of Component Composition

| Concept           | Example                                                          |
| ----------------- | ---------------------------------------------------------------- |
| **Parent-Child**  | A parent component renders multiple child components.            |
| **Props**         | Pass data to children to customize their behavior.               |
| **Children Prop** | Pass nested components to parent components.                     |
| **Reusability**   | Use the same component in different places with different props. |

---

Let's dive into **How Rerendering Works** in React:

---

## ✅ **How Rerendering Works**

Understanding how **rerendering** works in React is crucial for optimizing performance and managing state efficiently. In React, a **rerender** happens when a component's **state** or **props** change, triggering a re-evaluation of the component’s output.

### 🌀 **When Does Rerendering Occur?**

React will rerender a component in the following scenarios:

1. **State Change**: When a component’s local state changes (via `useState` or `setState`), React will trigger a rerender for that component.

   Example:

   ```jsx
   const [count, setCount] = useState(0);

   const increment = () => setCount(count + 1);

   return <button onClick={increment}>{count}</button>;
   ```

2. **Props Change**: If the **props** passed to a component change, React will rerender that component.

   Example:

   ```jsx
   function Parent() {
     const [message, setMessage] = useState("Hello, World!");
     return <Child message={message} />;
   }

   function Child({ message }) {
     return <div>{message}</div>;
   }
   ```

3. **Context Change**: If a component is consuming context (via `useContext`), and the context value changes, the component will rerender.

4. **Force Update**: You can manually trigger a rerender using `forceUpdate()` (although it's rarely needed).

---

### 🧠 **Should Component Always Rerender?**

React tries to minimize the number of rerenders by using **virtual DOM** diffing and comparison algorithms. However, it still rerenders a component when there’s a change in state or props. This can sometimes cause unnecessary rerenders, which may affect performance, especially in large applications.

#### React's **Reconciliation Algorithm**:

React uses a process called **reconciliation** to update the **DOM** efficiently:

- **Virtual DOM**: React maintains a virtual DOM (an in-memory representation of the real DOM).
- **Diffing**: React compares the current virtual DOM with the previous one to find differences.
- **Efficient Updates**: After determining the differences, React updates the actual DOM only where changes are necessary.

This process is **fast** because it avoids re-rendering the entire UI and only updates the **minimal number of elements** that have changed.

---

### 🕹️ **How to Prevent Unnecessary Rerenders?**

You can optimize rerendering and avoid unnecessary updates with several techniques:

1. **React.memo** (for functional components):

   - If props haven’t changed, React will skip rerendering the component.

   ```jsx
   const MemoizedComponent = React.memo(function MyComponent({ prop1, prop2 }) {
     return (
       <div>
         {prop1} {prop2}
       </div>
     );
   });
   ```

2. **PureComponent** (for class components):

   - React automatically implements a shallow comparison of props and state to avoid rerendering unless props or state change.

   ```jsx
   class MyComponent extends React.PureComponent {
     render() {
       return <div>{this.props.value}</div>;
     }
   }
   ```

3. **useMemo and useCallback** (for memoizing functions and values):

   - **`useMemo`** caches a value so it doesn’t need to be recomputed on every render.
   - **`useCallback`** memoizes a function so it doesn’t get recreated on every render.

   Example:

   ```jsx
   const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
   const memoizedCallback = useCallback(() => {
     console.log(a, b);
   }, [a, b]);
   ```

4. **shouldComponentUpdate** (for class components):

   - Override `shouldComponentUpdate()` to prevent unnecessary rerenders based on custom conditions.

   ```jsx
   class MyComponent extends React.Component {
     shouldComponentUpdate(nextProps, nextState) {
       return nextProps.someProp !== this.props.someProp;
     }
     render() {
       return <div>{this.props.someProp}</div>;
     }
   }
   ```

---

### 🚀 **Performance Considerations**

- **Avoid unnecessary state updates**: If the state doesn't change, don’t call `setState`.
- **Key Prop in Lists**: Make sure each item in lists has a **unique key** to help React identify and re-render only the changed items in the list.
- **Lazy Loading**: For large components or routes, use **lazy loading** to load components only when they are needed.

---

### 📊 Summary of Rerendering

| Scenario                  | Rerender Triggered?                               |
| ------------------------- | ------------------------------------------------- |
| **State Change**          | Yes                                               |
| **Props Change**          | Yes                                               |
| **Context Change**        | Yes                                               |
| **Force Update**          | Yes (manual)                                      |
| **Unchanged Props/State** | No (Optimized via `React.memo` / `PureComponent`) |

---

Let's move on to **How Diffing Works** in React:

---

## ✅ **How Diffing Works**

React uses an efficient **diffing algorithm** to minimize the number of changes made to the real DOM, which helps to improve performance and responsiveness. This process is part of the **reconciliation** phase in React’s rendering process.

### 🧩 **Virtual DOM and Diffing**

React maintains a **Virtual DOM** (a lightweight, in-memory representation of the real DOM). When there is a change in the application (like a state or props change), React updates the virtual DOM and compares it to the previous virtual DOM to find differences (also called “diffs”).

#### Key Points:

- **Virtual DOM**: A fast, in-memory representation of the real DOM.
- **Diffing**: React compares the current virtual DOM with the previous one to identify changes.
- **Minimal Updates**: React applies only the changes that are necessary to the real DOM.

This process is **faster** because updating the virtual DOM is much quicker than updating the real DOM. React then uses this comparison to make the **minimal set of updates** to the real DOM.

---

### 🔄 **The Diffing Algorithm (Reconciliation)**

React’s diffing algorithm can be summarized in a few key steps:

1. **Initial Render**: On the initial render, React creates a virtual DOM tree based on the components.
2. **State or Props Change**: When state or props change, React re-renders the component and creates a new virtual DOM tree.

3. **Tree Comparison**: React compares the new virtual DOM tree with the previous tree using the diffing algorithm. This comparison checks for differences between the nodes.

4. **Minimal Updates**: Based on the comparison, React identifies the **minimum set of changes** needed in the real DOM (e.g., adding, removing, or updating elements).

5. **Batching Updates**: React batches updates and applies them efficiently in a single pass to avoid multiple DOM manipulations.

---

### 🔍 **How React Diffing Optimizes Updates**

React’s diffing algorithm optimizes updates by making some **assumptions** based on the structure of the component tree and how components are used:

#### 1. **Component Tree Structure**:

- **Same Component Type**: When comparing nodes, React assumes that elements of the same type are similar. It compares the component’s props, children, and state.

Example:

```jsx
<Button label="Click Me" /> // React compares this Button to the previous one
```

#### 2. **Key Prop for Lists**:

- When rendering lists of elements, React uses the **key prop** to optimize the diffing process. The key helps React identify which items have changed, been added, or removed.
- This prevents React from re-rendering all list items and instead only updates the ones that have changed.

Example:

```jsx
const list = ["React", "Vue", "Angular"];

return (
  <ul>
    {list.map((item, index) => (
      <li key={index}>{item}</li>
    ))}
  </ul>
);
```

#### 3. **Reordering Elements**:

- React will attempt to **reorder** the elements in a list when keys are provided. Without keys, React may unnecessarily re-render all the items.

#### 4. **Children Prop**:

- For components that use `children`, React compares the children recursively to detect changes.

---

### 🏗️ **Optimizing React’s Diffing Algorithm**

While React’s diffing algorithm is quite efficient, there are some practices you can follow to further optimize the performance:

1. **Use Keys in Lists**: Always provide a unique `key` prop for list items to help React efficiently track and update items.

2. **Avoid Changing Component Types**: When possible, avoid dynamically switching between completely different types of components. React optimizes the rendering of the same type of component.

3. **Keep Component Trees Stable**: Keep the structure of your component tree as consistent as possible between renders. Avoid creating new objects or arrays as props unnecessarily.

4. **Avoid Re-rendering Unnecessary Components**: Use **React.memo**, **shouldComponentUpdate**, or **PureComponent** to prevent unnecessary re-renders of components that haven’t changed.

---

### 📊 Summary of Diffing Process

| Step                   | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| **Virtual DOM**        | An in-memory copy of the real DOM used for comparison.             |
| **State/Props Change** | React updates the virtual DOM when state or props change.          |
| **Diffing**            | React compares the new virtual DOM with the previous one.          |
| **Minimal Updates**    | Only necessary changes are applied to the real DOM.                |
| **Keys in Lists**      | Keys help React identify elements in a list for efficient updates. |

---

### ✅ 1. **Conditional Rendering**

- Showing different UI based on conditions.
- Techniques:

  - `if/else` statements
  - Ternary (`? :`) operator
  - Logical `&&` operator

- Example:

  ```jsx
  {
    isLoggedIn ? <LogoutButton /> : <LoginButton />;
  }
  ```

---

### ✅ 2. **Lists and Keys**

- Rendering lists of components using `.map()`
- Each child in a list should have a unique `"key"` prop.

```jsx
const todos = ["Buy milk", "Do laundry"];
const list = todos.map((item, index) => <li key={index}>{item}</li>);
```

---

### ✅ 3. **Keys in Lists – Why They Matter**

- Helps React identify which items changed, added, or removed.
- **Avoid using indexes** as keys if list items are dynamic.
- Improves performance during re-renders.

---

### ✅ 4. **Event Handling**

- React uses camelCase: `onClick`, `onChange`, etc.
- You pass a function reference, not a function call.

```jsx
<button onClick={handleClick}>Click me</button>
```

---

### ✅ 5. **Forms and Controlled Components**

- Form inputs that are tied to React state.
- Example:

  ```jsx
  const [name, setName] = useState("");
  <input value={name} onChange={(e) => setName(e.target.value)} />;
  ```

---

### ✅ 6. **Events in React**

- Synthetic events = consistent across browsers.
- Event pooling (React batches and reuses events for performance).
- Can access native event via `event.nativeEvent`.

---

### ✅ 7. **Lifting State Up**

- Move state to the closest common ancestor to share data between components.
- Example:

  ```jsx
  <TemperatureInput
    scale="celsius"
    temperature={celsius}
    onTemperatureChange={handleCelsiusChange}
  />
  ```

---

### ✅ 8. **Portals**

- Render children into a DOM node **outside** the parent component hierarchy.
- Use case: Modals, tooltips, dropdowns.

```jsx
ReactDOM.createPortal(child, document.getElementById("modal-root"));
```

---
