# ⚛️ React Quick Revision Guide with Examples

---

## ✅ Core

### - JSX

```jsx
const element = <h1>Hello, React!</h1>;
```

### - Component

```jsx
function Greet() {
  return <h2>Hello</h2>;
}
```

### - Props

```jsx
function Welcome(props) {
  return <h2>Hi, {props.name}</h2>;
}
<Welcome name="Ganesh" />;
```

### - children Prop

```jsx
function Wrapper({ children }) {
  return <div>{children}</div>;
}
<Wrapper>
  <p>I’m a child!</p>
</Wrapper>;
```

### - States

```jsx
const [count, setCount] = useState(0);
```

### - Fragments

```jsx
<>
  <h1>Title</h1>
  <p>Description</p>
</>
```

---

## 🧩 Component Category

### - Stateful vs Stateless

- **Stateful**: Has internal state.
- **Stateless**: Just props, no state.

### - Functional vs Class

```jsx
// Functional
function Hello() {
  return <p>Hello</p>;
}

// Class
class Hello extends React.Component {
  render() {
    return <p>Hello</p>;
  }
}
```

---

## 🔁 Pass Data from Child → Parent

```jsx
// Parent
const [value, setValue] = useState("");
<Child onChange={setValue} />;

// Child
function Child({ onChange }) {
  return <input onChange={(e) => onChange(e.target.value)} />;
}
```

---

## 🔄 How Rendering Works

- State/props/context changes → Component re-renders.
- Reconciliation → Only necessary DOM updates are made.
- Virtual DOM diffing keeps performance optimal.

### how react perform effective dom

- React performs effective DOM updates using a concept called the Virtual DOM.
- React create a lightweight copy of the actual Dom in memory Called as `Virtual Dom`
- when the props or state of the component change, React do `Reconciliation` using `Diffing algorithm`

### how react handle Reconciliation and how actually update the dom

- Reconciliation is a process where React compares the current virtual DOM with the previous one to identify changes.

1. Render Phase:
   - Step 1: React creates a virtual DOM tree based on the components.
   - Step 2: When state or props change, React re-renders the component and creates a new virtual DOM tree.
2. Defiifng algo:
   - Step 3: React compares the new virtual DOM tree with the previous one.
3. Commit Phase:
   - Step 4: React updates the DOM to reflect the changes.

---

## 🔂 Lifecycle Methods (Class Component)

```jsx
class Demo extends React.Component {
  componentDidMount() {
    console.log("Mounted");
  }
  componentDidUpdate() {
    console.log("Updated");
  }
  componentWillUnmount() {
    console.log("Cleanup");
  }
  render() {
    return <p>Hello</p>;
  }
}
```

---

## 🪝 Hooks

### - `useState()`

```jsx
const [count, setCount] = useState(0);
```

### - `useEffect()`

```jsx
useEffect(() => {
  console.log("mounted/updated");
}, [dependency]);
```

### - `useLayoutEffect()`

```jsx
useLayoutEffect(() => {
  console.log("Runs before paint");
}, []);
```

### - `useRef()`

```jsx
const inputRef = useRef();
<input ref={inputRef} />;
```

### - `useReducer()`

```jsx
function reducer(state, action) {
  if (action.type === "inc") return state + 1;
  return state;
}
const [count, dispatch] = useReducer(reducer, 0);

<button onClick={() => dispatch({ type: "decrement", payload: 1 })}>-</button>;
```

### - `custom hooks`

- Custom hooks are reusable JavaScript functions that start with the word use and let you extract and share logic between multiple components.

```jsx
funtion useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  const increment = () => setCount(c => c + 1);
  const decrement = () => setCount(c => c - 1);
  return { count, increment, decrement };
}
```

---

## 🌐 Routing (React Router v6)

```jsx
import {
  BrowserRouter,
  Routes,
  Route,
  useParams,
  useNavigate,
  useLocation,
  useSearchParams,
} from "react-router-dom";

// Setup
<BrowserRouter>
  <Routes>
    <Route path="/about" element={<About />} />
  </Routes>
</BrowserRouter>;

// useParams
const { id } = useParams();

// useNavigate
const navigate = useNavigate();
navigate("/home");

// useLocation
const location = useLocation();
console.log(location.pathname); // Logs the current path
console.log(location.search); // Logs the query parameters
console.log(location.state); // Logs any passed state

// useSearchParams
const [searchParams] = useSearchParams();
const page = searchParams.get("page");
```

---

## 📡 Data Fetching

### - `fetch`

```jsx
useEffect(() => {
  fetch("https://api.example.com/data")
    .then((res) => res.json())
    .then((data) => console.log(data));
}, []);
```

### - `axios`

```jsx
import axios from "axios";

useEffect(() => {
  axios
    .get("https://api.example.com/data")
    .then((res) => console.log(res.data));
}, []);

// Request Interceptor
axiosInstance.interceptors.request.use(
  (config) => {
    console.log("[Request]", config.url);
    // Add auth token if needed
    config.headers["Authorization"] = "Bearer my_token";
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Request Cancellation
const controller = new AbortController();
const response = await axios.get("https://jsonplaceholder.typicode.com/posts", {
  signal: controller.signal,
});

if (true) {
  setCancelled(true);
  console.log("Request cancelled:", error.message);
}
```

---

## 📦 State Management

### - Context API

```jsx
const MyContext = React.createContext();
<MyContext.Provider value={data}>
  <Child />
</MyContext.Provider>;
const value = useContext(MyContext);
```

### - Redux (Conceptual)

1. Create Slice: Use createSlice to define userSlice with initial state and a login reducer.
2. Configure Store: Use configureStore to register the user reducer in the Redux store.
3. Wrap App: Wrap your <App /> with <Provider store={store}> in index.js.
4. Use in Component: Use useSelector to access state and useDispatch to trigger login("Ganesh").

#### 1. Create Slice

```jsx
// ✅ src/redux/userSlice.js
import { createSlice } from "@reduxjs/toolkit";

const configObj = {
  name: "user",
  initialState: { name: "", loggedIn: false },
  reducers: {
    login: (state, action) => {
      state.name = action.payload;
      state.loggedIn = true;
    },
  },
};

const userSlice = createSlice(configObj);

export const { login } = userSlice.actions;
export default userSlice.reducer;
```

#### 2. configure Store

```js
// ✅ src/redux/store.js
import { configureStore } from "@reduxjs/toolkit";
import userReducer from "./userSlice";

const store = configureStore({
  reducer: {
    user: userReducer,
    // user2: userReducer, // if using the same reducer twice
  },
});

export default store;
```

#### 3. wrap app in the store provider

```jsx
// ✅ src/index.js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { Provider } from "react-redux";
import store from "./redux/store";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
```

#### 4. use the data in the app

```jsx
// ✅ src/App.js
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { login } from "./redux/userSlice";

const App = () => {
  const user = useSelector((state) => state.user.name);
  const dispatch = useDispatch();

  return (
    <div style={{ padding: "20px" }}>
      <h1>Redux Toolkit Example</h1>
      <p>User: {user || "Not Logged In"}</p>
      <button onClick={() => dispatch(login("Ganesh"))}>Login</button>
    </div>
  );
};

export default App;
```

---

### - Redux Thunk

```js
function fetchData() {
  return async (dispatch) => {
    const res = await fetch("/api");
    const data = await res.json();
    dispatch({ type: "SET_DATA", payload: data });
  };
}
```

### - Context API vs Redux

| Context API          | Redux                          |
| -------------------- | ------------------------------ |
| Built-in             | External library               |
| Best for light state | Best for large-scale apps      |
| No middleware        | Supports middleware like thunk |

---

## 🚀 Performance Optimization

### - `useMemo()`

- Memoize the expensive calculation

```jsx
function ExpensiveComponent({ number }) {
  const expensiveResult = useMemo(() => {
    console.log("Calculating...");
    let result = 0;
    for (let i = 0; i < 100000000; i++) {
      result += number;
    }
    return result;
  }, [number]);

  return <div>Result: {expensiveResult}</div>;
}
```

### - `useCallback()`

- Memoizes function references to prevent unnecessary re-renders

```jsx
function Button({ onClick, label }) {
  console.log("Button rendered:", label);
  return <button onClick={onClick}>{label}</button>;
}

function App() {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount((c) => c + 1);
  }, []);

  return (
    <div>
      <p>Count: {count}</p>
      <Button onClick={increment} label="Increment" />
    </div>
  );
}
```

### - `React.memo`

- Memoizes entire components to avoid re-rendering if props don't change

```jsx
const Button = React.memo(function Button({ onClick, label }) {
  console.log("Rendering Button:", label);
  return <button onClick={onClick}>{label}</button>;
});
```

---
