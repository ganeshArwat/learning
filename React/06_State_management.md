## 🔼 Lifting State vs 📦 Context API

### 🔼 **Lifting State Up**

#### 🔹 What is it?

"Lifting state up" means **moving shared state to the closest common ancestor** of two or more components that need to access it.

#### 🔹 Why use it?

To **share state between sibling components** or manage data in a parent so children can update or read it via props.

#### 🧩 Example:

```jsx
function Parent() {
  const [count, setCount] = useState(0);

  return (
    <>
      <ChildA count={count} />
      <ChildB setCount={setCount} />
    </>
  );
}

function ChildA({ count }) {
  return <p>Count is {count}</p>;
}

function ChildB({ setCount }) {
  return <button onClick={() => setCount((c) => c + 1)}>Increment</button>;
}
```

✅ **Good for small apps or when only a few components share state.**

---

### 📦 **Context API**

#### 🔹 What is it?

Context API provides a way to **pass data deeply** through the component tree **without passing props manually at every level**.

#### 🔹 Why use it?

When many components (especially deeply nested ones) need access to **the same global state**, like **theme**, **user auth**, or **language settings**.

---

#### 🧩 Basic Context API Flow:

```jsx
// 1. Create Context
const ThemeContext = React.createContext();

// 2. Provide Context
function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}

// 3. Consume Context
function Toolbar() {
  return <ThemedButton />;
}

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button className={theme}>Click Me</button>;
}
```

✅ **Great for avoiding "prop drilling"**.
❌ **Avoid storing rapidly changing or large state here** (use Redux, Zustand, etc. for that).

---

### ⚖️ When to Use What?

| Use Case                             | Use Lifting State | Use Context API        |
| ------------------------------------ | ----------------- | ---------------------- |
| Share state between 2-3 siblings     | ✅                | ❌                     |
| Deeply nested components need access | ❌                | ✅                     |
| Global themes, auth, language        | ❌                | ✅                     |
| Performance-critical updates         | ⚠️ (not ideal)    | ⚠️ (needs memoization) |

---

## ✅ Combine `createContext` + `Provider` in One File

### 🗂️ Example: `ThemeContext.js`

```jsx
import React, { createContext, useState } from "react";

// 1. Create Context
const ThemeContext = createContext();

// 2. Create Provider Component
const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState("light");

  const toggleTheme = () =>
    setTheme((prev) => (prev === "light" ? "dark" : "light"));

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

// 3. Export both Context and Provider
export { ThemeContext, ThemeProvider };
```

---

### 📦 Usage in App

```jsx
// App.js
import { ThemeProvider } from "./ThemeContext";
import Home from "./Home";

function App() {
  return (
    <ThemeProvider>
      <Home />
    </ThemeProvider>
  );
}
```

### 🎯 Usage with `useContext`

```jsx
// Home.js
import { useContext } from "react";
import { ThemeContext } from "./ThemeContext";

function Home() {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <>
      <h1>Current Theme: {theme}</h1>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </>
  );
}
```

---

### 💡 Benefits

- Centralized and clean structure
- Easy to maintain
- Promotes reuse and modular code
- Scales better in large apps

---

## 🧠 **Redux** – (Optional, Best for Large Apps)

Redux is a **predictable state container** for JavaScript apps. It's commonly used in React for **global state management**, especially in **large-scale applications**.

---

### 🔹 Why Use Redux?

- Global state accessible from **any component**
- Centralized store = easier **debugging & testing**
- Excellent tools: **Redux DevTools**, middleware (like Redux Thunk)
- Works well for complex apps with **shared state, caching, async logic**

---

### 🏗️ Redux Core Concepts

| Concept      | Description                                       |
| ------------ | ------------------------------------------------- |
| **Store**    | Holds the entire state of the application         |
| **Action**   | A plain object describing **what happened**       |
| **Reducer**  | A function that **updates state** based on action |
| **Dispatch** | Triggers the reducer via an action                |
| **Selector** | Reads data from the state                         |

---

### 📦 Basic Redux Example (with React)

Let’s build a simple counter.

#### Step 1: Install Redux Toolkit & React-Redux

```bash
npm install @reduxjs/toolkit react-redux
```

---

#### Step 2: Create `store.js`

```js
// store.js
import { configureStore, createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
  },
});

export const { increment, decrement } = counterSlice.actions;

const store = configureStore({
  reducer: {
    counter: counterSlice.reducer,
  },
});

export default store;
```

---

#### Step 3: Wrap App with `Provider`

```jsx
// index.js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { Provider } from "react-redux";
import store from "./store";

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);
```

---

#### Step 4: Use Redux in Component

```jsx
// Counter.js
import { useSelector, useDispatch } from "react-redux";
import { increment, decrement } from "./store";

function Counter() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <>
      <h2>Count: {count}</h2>
      <button onClick={() => dispatch(increment())}>➕</button>
      <button onClick={() => dispatch(decrement())}>➖</button>
    </>
  );
}
```

---

### ✅ When to Use Redux

Use Redux when:

- You have **shared state** across many components
- You want **time-travel debugging**
- Your app grows too big to manage state via Context or props

---

### ⚠️ Caution

> Redux is **overkill for small/medium apps** – it adds boilerplate and complexity.

---

When you have **multiple slices**, you can combine them easily in the `configureStore` function using an object where each key represents a **slice of state**.

---

## 🧩 Example: Multiple Redux Slices

Let’s say you have:

- `counterSlice` (for count)
- `userSlice` (for user info)

---

### 🔹 Step 1: Create Slices

#### counterSlice.js

```js
import { createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
  },
});

export const { increment, decrement } = counterSlice.actions;
export default counterSlice.reducer;
```

---

#### userSlice.js

```js
import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
  name: "user",
  initialState: { name: "", loggedIn: false },
  reducers: {
    login: (state, action) => {
      state.name = action.payload;
      state.loggedIn = true;
    },
    logout: (state) => {
      state.name = "";
      state.loggedIn = false;
    },
  },
});

export const { login, logout } = userSlice.actions;
export default userSlice.reducer;
```

---

### 🔹 Step 2: Combine in Store

#### store.js

```js
import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./counterSlice";
import userReducer from "./userSlice";

const store = configureStore({
  reducer: {
    counter: counterReducer,
    user: userReducer,
  },
});

export default store;
```

---

### 🔹 Step 3: Access State in Components

#### AnyComponent.js

```jsx
import { useSelector, useDispatch } from "react-redux";
import { increment } from "./counterSlice";
import { login } from "./userSlice";

function AnyComponent() {
  const count = useSelector((state) => state.counter.value);
  const user = useSelector((state) => state.user.name);
  const dispatch = useDispatch();

  return (
    <>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>+</button>

      <p>User: {user}</p>
      <button onClick={() => dispatch(login("Ganesh"))}>Login</button>
    </>
  );
}
```

---

### ✅ Result

Your Redux store now manages **multiple state slices** like this:

```js
{
  counter: { value: 0 },
  user: { name: '', loggedIn: false }
}
```

---

## 🔍 What Is the `name` in a Redux Slice?

### 👉 In `createSlice({ name: 'something', ... })`

- The `name` is used internally by Redux Toolkit.
- It also helps **generate action type strings** like `'counter/increment'`.
- It **does not** affect your store structure directly.

```js
const counterSlice = createSlice({
  name: "counter", // used for debugging and action types
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value++;
    },
  },
});
```

> The `name` will prefix generated action types, e.g., `'counter/increment'`.

---

## 🔍 What Is the Key in the `reducer` Object in `configureStore`?

This **does determine** your state structure in the Redux store.

```js
const store = configureStore({
  reducer: {
    counter: counterReducer,
    user: userReducer,
  },
});
```

In the example above:

- `counter` is the key for `counterReducer`
- `user` is the key for `userReducer`

So your Redux state becomes:

```js
{
  counter: { value: 0 },
  user: { name: '', loggedIn: false }
}
```

---

### 🔁 TL;DR – Relationship Between Name and Store Key

| In Slice (`name`) | In Store (`reducer` key)  | Purpose                                                     |
| ----------------- | ------------------------- | ----------------------------------------------------------- |
| `'counter'`       | `counter: counterReducer` | `name` is for action naming; `counter` key shapes the store |

So you could even do this (though not recommended for clarity):

```js
reducer: {
  countStuff: counterReducer,
}
```

Now your state becomes:

```js
{
  countStuff: {
    value: 0;
  }
}
```

Even if `name: 'counter'` inside the slice.

---

### ✅ Best Practice

Keep `name` and store key **the same** for clarity:

```js
name: "counter";
reducer: {
  counter: counterReducer;
}
```

---

## ✅ Context API vs Redux – Key Differences

| Feature / Aspect          | **Context API**                             | **Redux**                                     |
| ------------------------- | ------------------------------------------- | --------------------------------------------- |
| 🔧 **Built-in**           | ✅ Yes (React built-in)                     | ❌ No (requires `redux`, `react-redux`)       |
| 🧠 **Purpose**            | Prop drilling avoidance                     | Global state management                       |
| 🏗️ **Architecture**       | Simple, minimal boilerplate                 | More structured: actions, reducers, store     |
| 🔄 **State Updates**      | Via `useState`, `useReducer`, `useContext`  | Via `dispatch` and `reducers`                 |
| 📦 **Data Sharing**       | Works well for small-medium apps            | Best for large and complex apps               |
| 🧩 **Middleware Support** | ❌ Manual, not built-in                     | ✅ Has built-in middleware (like Redux Thunk) |
| 🚀 **Performance**        | Slower for frequent updates (rerenders all) | More optimized with selectors like `reselect` |
| 🧪 **DevTools**           | ❌ Basic (console logs)                     | ✅ Redux DevTools available                   |
| 🧰 **Boilerplate Code**   | Minimal                                     | More setup: store, actions, reducers, etc.    |
| 📚 **Learning Curve**     | Easy                                        | Moderate to High                              |

---

## 🧠 When to Use What?

### ✅ Use **Context API** when:

- You have **small or medium apps**.
- You only need to pass **simple global data** (like theme, auth, language).
- You want **less boilerplate** and easier setup.

### ✅ Use **Redux** when:

- Your app has **complex state logic** (e.g. filtering, pagination, auth, etc.).
- You need **middleware** (e.g. API calls with Redux Thunk/Saga).
- You want **time-travel debugging** and **predictable state**.

---

## 🔁 Example Use Cases

| Scenario                           | Use Context or Redux? |
| ---------------------------------- | --------------------- |
| Theme switcher (dark/light mode)   | ✅ Context API        |
| Auth state (user login/logout)     | ✅ Context API        |
| Shopping cart with filters, prices | ✅ Redux              |
| Complex form state with validation | ✅ Redux              |
| Language/i18n state                | ✅ Context API        |

---

## 🔄 What is **Redux Thunk**?

### ➕ In short:

**Redux Thunk** allows you to write **async logic** (like fetching data from an API) inside action creators.

---

### 🤔 Why do we need it?

By default, Redux **only supports synchronous actions**.
But in real apps, you often need to:

- fetch data from APIs
- perform async tasks (e.g. `setTimeout`)
- dispatch actions **after** an async operation

That's where **Redux Thunk** comes in.

---

## 🔧 How Redux Thunk Works

Redux Thunk lets action creators **return a function** (instead of an action object).
This function can:

- perform async tasks
- and then `dispatch()` actions manually

---

### 🔁 Without Thunk:

```js
// returns a plain object (SYNC)
{ type: 'FETCH_USER_SUCCESS', payload: user }
```

---

### 🔁 With Thunk:

```js
// returns a function (ASYNC)
(dispatch) => {
  fetch("api/user")
    .then((res) => res.json())
    .then((data) => dispatch({ type: "FETCH_USER_SUCCESS", payload: data }));
};
```

---

## 🚀 How to Use Redux Thunk (Step-by-step)

### 1️⃣ Install it (already included with Redux Toolkit! ✅)

```bash
npm install redux-thunk
```

But **if you use `@reduxjs/toolkit`**, thunk is **enabled by default**. No need to configure it.

---

### 2️⃣ Example: Fetch User from API

#### userSlice.js

```js
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

// Step 1: Create an async thunk
export const fetchUser = createAsyncThunk("user/fetchUser", async () => {
  const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
  return await response.json();
});

const userSlice = createSlice({
  name: "user",
  initialState: {
    user: {},
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.loading = false;
        state.error = "Failed to fetch user";
      });
  },
});

export default userSlice.reducer;
```

---

#### Usage in Component

```js
import { useDispatch, useSelector } from "react-redux";
import { fetchUser } from "./userSlice";

function UserInfo() {
  const dispatch = useDispatch();
  const { user, loading, error } = useSelector((state) => state.user);

  return (
    <>
      <button onClick={() => dispatch(fetchUser())}>Fetch User</button>
      {loading && <p>Loading...</p>}
      {user.name && <p>Name: {user.name}</p>}
      {error && <p>Error: {error}</p>}
    </>
  );
}
```

---

## ✅ Summary

| Feature                  | Redux Thunk |
| ------------------------ | ----------- |
| Handles Async Logic      | ✅          |
| Uses Promises            | ✅          |
| Dispatch manually        | ✅          |
| Built into Redux Toolkit | ✅          |

---

## React Query

### 🔥 Why Use React Query?

Traditional Redux or `useState`/`useEffect` is:

- Manual
- Repetitive
- Hard to cache/update efficiently

👉 **React Query** handles all of this **automatically**:

| Feature               | React Query |
| --------------------- | ----------- |
| API Data Fetching     | ✅          |
| Caching               | ✅          |
| Automatic Refetching  | ✅          |
| Pagination / Infinite | ✅          |
| Background Syncing    | ✅          |
| Request Deduplication | ✅          |
| Optimistic Updates    | ✅          |

---

## 🚀 Step-by-Step Setup

### 1️⃣ Install React Query

```bash
npm install @tanstack/react-query
```

---

### 2️⃣ Set Up the Query Client

In your main file (e.g. `main.jsx` or `index.js`):

```js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById("root")).render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>
);
```

---

### 3️⃣ Use `useQuery` for Fetching Data

#### 📄 Example: Fetch Users

```js
import { useQuery } from "@tanstack/react-query";

const fetchUsers = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  return res.json();
};

function Users() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["users"],
    queryFn: fetchUsers,
  });

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <ul>
      {data.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

---

## 🧠 Key Concepts

### 🔹 `queryKey`

- Unique ID for the query
- Used for caching, refetching, and updates

```js
queryKey: ["users"];
```

### 🔹 `queryFn`

- Async function that fetches your data

```js
queryFn: fetchUsers;
```

---

## 🔄 `useMutation` for POST, PUT, DELETE

For actions that **change data** (e.g. create, update, delete), use `useMutation`.

Example:

```js
import { useMutation } from "@tanstack/react-query";

const addUser = async (newUser) => {
  const res = await fetch("/api/users", {
    method: "POST",
    body: JSON.stringify(newUser),
    headers: { "Content-Type": "application/json" },
  });
  return res.json();
};

const { mutate } = useMutation({ mutationFn: addUser });

<button onClick={() => mutate({ name: "Ganesh" })}>Add User</button>;
```

---

## ✅ Advantages Over Redux for Async

| Feature                           | Redux + Thunk | React Query |
| --------------------------------- | ------------- | ----------- |
| Manual reducers / types           | ✅ Yes        | ❌ No       |
| Auto-caching & background refresh | ❌ No         | ✅ Yes      |
| Pagination, retry, stale data     | ❌ Manual     | ✅ Built-in |
| DevTools                          | ❌ Basic      | ✅ Amazing! |

---

## 🚫 Why NOT to Overuse Redux (Especially for Beginners)

Many beginners fall into the trap of using Redux **for everything**, even when it's **unnecessary**, which leads to:

---

### ❌ 1. **Unnecessary Complexity**

Redux involves:

- Setting up actions
- Creating reducers
- Managing boilerplate
- Connecting components

👉 For small local state (like a form input or modal toggle), it's **overkill**.

✅ Use `useState` or `useReducer` for simple local state instead.

---

### ❌ 2. **Global Overuse**

Some devs store **every piece of UI state** (like `isModalOpen`, `searchQuery`, etc.) in Redux.

> That's like using a nuclear bomb to swat a fly.

✅ **Local UI state** should stay **local** unless it’s shared across unrelated components.

---

### ❌ 3. **Poor Async Handling**

Beginners often:

- Write custom async logic
- Manage loading/error states manually
- Forget cleanup

✅ **React Query** (or SWR, etc.) handles async data, caching, retries, etc., **automatically**.

---

### ❌ 4. **Mixing Server & Client State**

Many developers mix:

- API data (server state)
- UI state (client state)

In the same Redux store.

This can lead to a **bloated, unmanageable state tree**.

✅ Use **React Query** or **RTK Query** for API data
✅ Use Redux only for **app-wide client state**

---

### ❌ 5. **Boilerplate Explosion**

Without Redux Toolkit, you write:

- Action types
- Action creators
- Reducers

Which becomes painful and redundant for simple things.

✅ Use `createSlice` from Redux Toolkit — or just use `useContext` + `useReducer` for smaller apps.

---

## 🧠 When to Use Redux (The Right Way)

Use Redux when:
✅ You have **complex app-wide state** (e.g., user auth, cart, settings)
✅ Many **unrelated components** need access to shared state
✅ You want **strict control** over state structure
✅ You have **multiple slices** of client-side logic

---

## ✅ Redux Alternatives for Beginners

| Task                           | Better Alternative        |
| ------------------------------ | ------------------------- |
| Simple UI state (modal, input) | `useState` / `useReducer` |
| Sharing small global state     | `useContext`              |
| Async API data (fetching)      | React Query / RTK Query   |
| Local-only app logic           | Zustand / Jotai / Recoil  |

---

## ⚔️ Redux vs Context API: When to Use What?

| Feature             | **Context API**                          | **Redux (Toolkit)**                    |
| ------------------- | ---------------------------------------- | -------------------------------------- |
| ✅ Use Case         | Small to medium shared state             | Complex global state with many updates |
| 🔄 State Updates    | Infrequent                               | Frequent and complex                   |
| 🔁 Re-renders       | Can cause unnecessary re-renders         | Optimized via selectors/memoization    |
| 🔌 Async Support    | Manual (via `useEffect`)                 | Built-in via middleware like Thunk     |
| 📦 Setup Complexity | Very simple                              | More setup (slices, actions, reducers) |
| ⚡ Performance      | Not ideal for large, fast-changing state | Optimized for performance              |
| 🧠 Learning Curve   | Easy                                     | Steeper for beginners                  |

---

## ✅ Use **Context API** When:

- You only need to share **simple global state** (like theme, auth status, language)
- The state doesn't change often
- You want minimal setup
- Your app is small or mid-size

**Examples:**

- User authentication status
- Theme (light/dark)
- Language (i18n)
- Toast or modal toggles

---

## ✅ Use **Redux** When:

- You have **complex global state** used across many components
- The state updates **frequently**
- You need **middleware** (e.g., `redux-thunk`) for API handling
- You need **time-travel debugging**, dev tools, etc.
- You are building a **large-scale** app with multiple team members

**Examples:**

- E-commerce cart management
- Role-based permission management
- Complex form states
- Application settings spanning multiple pages

---

## 💡 Pro Tip: Combine Them Smartly

Use **Context API** for:

> App-level UI state (theme, auth, toggles)

Use **Redux** for:

> Business logic & data-heavy state (cart, notifications, filters, dashboards)

---

## 🧠 Zustand – The Minimalist Global Store

> “Bear necessities” 🐻 for global state

### 🔹 Key Features:

- Simple API (no boilerplate)
- Built-in support for middleware, selectors, and persistence
- Works with React out of the box

### 📦 Install:

```bash
npm install zustand
```

### 🧪 Example:

```js
// store.js
import { create } from "zustand";

const useStore = create((set) => ({
  count: 0,
  increase: () => set((state) => ({ count: state.count + 1 })),
}));

export default useStore;
```

```jsx
// App.jsx
import useStore from "./store";

function Counter() {
  const { count, increase } = useStore();
  return (
    <div>
      <p>{count}</p>
      <button onClick={increase}>+1</button>
    </div>
  );
}
```

---

## 🧠 Jotai – Atomic State Management

> Think of state as **atoms** — minimal and reactive

### 🔹 Key Features:

- Each piece of state is an **atom**
- Reactivity like Recoil, but simpler
- Works with async and derived atoms easily

### 📦 Install:

```bash
npm install jotai
```

### 🧪 Example:

```js
// atoms.js
import { atom } from "jotai";

export const countAtom = atom(0);
```

```jsx
// Counter.jsx
import { useAtom } from "jotai";
import { countAtom } from "./atoms";

function Counter() {
  const [count, setCount] = useAtom(countAtom);
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount((c) => c + 1)}>+1</button>
    </div>
  );
}
```

---

## 🧠 Recoil – Facebook’s Atomic State Library

> Designed to scale with large apps, like Facebook

### 🔹 Key Features:

- Similar to Jotai (atoms/selectors)
- Great for large apps with complex interdependent state
- Integrates with React Suspense (for async)

### 📦 Install:

```bash
npm install recoil
```

### 🧪 Example:

```js
// atoms.js
import { atom } from "recoil";

export const countAtom = atom({
  key: "count",
  default: 0,
});
```

```jsx
// App.jsx
import { useRecoilState, RecoilRoot } from "recoil";
import { countAtom } from "./atoms";

function Counter() {
  const [count, setCount] = useRecoilState(countAtom);
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount((c) => c + 1)}>+1</button>
    </div>
  );
}

export default function App() {
  return (
    <RecoilRoot>
      <Counter />
    </RecoilRoot>
  );
}
```

---

## ⚔️ Which One to Choose?

| Feature               | Zustand       | Jotai       | Recoil           |
| --------------------- | ------------- | ----------- | ---------------- |
| Boilerplate           | 🚫 None       | 🚫 None     | Moderate         |
| Async Support         | ✅ Middleware | ✅ Built-in | ✅ With Suspense |
| Re-render performance | ✅ Great      | ✅ Great    | ✅ Optimized     |
| Ecosystem size        | Medium        | Smaller     | Larger           |
| Learning curve        | Low           | Low         | Medium           |

---
