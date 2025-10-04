# 📚 5. React Router Topics Overview

## 🚀 Basic Routing in React (using react-router-dom)

### 1. First, install React Router:

```bash
npm install react-router-dom
```

### 2. Basic Setup

-Imagine you have two pages: Home and About.
-You need to set up BrowserRouter, Routes, and Route like this:

```jsx
// App.js

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Home";
import About from "./About";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### ⚡ What’s happening?

- `<BrowserRouter>`: Tells React that we are using client-side routing.
- `<Routes>`: A container for all the `<Route>` elements.
- `<Route path="/" element={<Home />}>`: When the URL is `/`, show `Home`.
- `<Route path="/about" element={<About />}>`: When the URL is `/about`, show `About`.

---

## 🎯 Dynamic Routing in React

#### Dynamic Routing means the URL changes based on dynamic values like an ID, username, slug, etc.

- Example URL:

  - `/user/101`
  - `/user/102`
  - `/product/iphone-15`

- We can capture that dynamic part using :paramName in the route.

### 1. Setup a Dynamic Route

- Here, :userId is a dynamic parameter.

```jsx
// App.js

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Home";
import User from "./User";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/user/:userId" element={<User />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### 2. Create the User Component (Read the userId)

```jsx
// User.js

import { useParams } from "react-router-dom";

function User() {
  const { userId } = useParams(); // 👈 get userId from URL

  return (
    <div>
      <h1>User Page</h1>
      <h2>User ID: {userId}</h2>
    </div>
  );
}

export default User;
```

### ⚡ What’s happening?

- `/user/101` ➔ `userId` will be `101`
- `/user/102` ➔ userId will be `102`
- `useParams()` is used to grab the dynamic part from the URL.

-✅ Dynamic Routing Done!

---

## 📚 3. Nested Routes in React Router

**Nested Routing** means putting routes _inside_ a parent route.  
Example:

- `/dashboard` ➔ Dashboard Home
- `/dashboard/profile` ➔ Profile Page inside Dashboard
- `/dashboard/settings` ➔ Settings Page inside Dashboard

Instead of making separate top-level routes, we nest them.

---

### 1. Setup the Nested Routes

```jsx
// App.js

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Home";
import Dashboard from "./Dashboard";
import Profile from "./Profile";
import Settings from "./Settings";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />

        {/* Parent Route */}
        <Route path="/dashboard" element={<Dashboard />}>
          {/* Nested Routes */}
          <Route path="profile" element={<Profile />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

---

### 2. Create Components

```jsx
// Home.js

function Home() {
  return <h1>Home Page</h1>;
}

export default Home;
```

```jsx
// Dashboard.js

import { Outlet, Link } from "react-router-dom";

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <nav>
        <Link to="profile">Profile</Link> |<Link to="settings">Settings</Link>
      </nav>
      <Outlet /> {/* Nested routes will render here */}
    </div>
  );
}

export default Dashboard;
```

```jsx
// Profile.js

function Profile() {
  return <h2>Profile Page</h2>;
}

export default Profile;
```

```jsx
// Settings.js

function Settings() {
  return <h2>Settings Page</h2>;
}

export default Settings;
```

---

### ⚡ How it works?

- `/dashboard` ➔ shows Dashboard page.
- Inside Dashboard page:
  - Click **Profile** ➔ `/dashboard/profile`
  - Click **Settings** ➔ `/dashboard/settings`
- `<Outlet />` is a placeholder where nested pages are rendered inside the parent (`Dashboard`).

✅ **Nested Routes Done!**

---

# 📚 4. Navigation in React Router

React Router gives two main ways to navigate inside the app without refreshing the page:

| Tag         | Purpose                                             |
| :---------- | :-------------------------------------------------- |
| `<Link>`    | Basic navigation                                    |
| `<NavLink>` | Navigation + _active class_ for styling active link |

---

## 1. Using `<Link>`

✅ Navigate to other pages **without page reload**.

Example:

```jsx
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link> |<Link to="/dashboard">Dashboard</Link>
    </nav>
  );
}

export default Navbar;
```

- Clicking **Home** will go to `/`.
- Clicking **Dashboard** will go to `/dashboard`.

**No page reload happens. It’s SPA (Single Page Application) behavior.** 🌟

---

## 2. Using `<NavLink>`

✅ Same as `<Link>`, but it **automatically adds an active class** to the link when you're on that page. Useful for styling.

Example:

```jsx
import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <NavLink
        to="/"
        style={({ isActive }) => ({
          fontWeight: isActive ? "bold" : "normal",
          color: isActive ? "red" : "black",
        })}
      >
        Home
      </NavLink>{" "}
      |
      <NavLink
        to="/dashboard"
        style={({ isActive }) => ({
          fontWeight: isActive ? "bold" : "normal",
          color: isActive ? "red" : "black",
        })}
      >
        Dashboard
      </NavLink>
    </nav>
  );
}

export default Navbar;
```

- When you're on `/`, Home will be **bold red**.
- When you're on `/dashboard`, Dashboard will be **bold red**.
- `isActive` automatically tells which link is currently active.

---

### ⚡ Quick Comparison:

| Feature                 | `<Link>` | `<NavLink>` |
| :---------------------- | :------- | :---------- |
| Navigation              | ✅       | ✅          |
| Auto Active Class       | ❌       | ✅          |
| Styling Based on Active | ❌       | ✅          |

---

# 🎯 5. React Router Important Hooks

React Router provides some special hooks to make routing more powerful:

| Hook                | Purpose                    |
| :------------------ | :------------------------- |
| `useParams()`       | Get dynamic URL parameters |
| `useNavigate()`     | Navigate programmatically  |
| `useSearchParams()` | Get Query Params           |
| `useLocation()`     | Get current URL info       |

---

## 1. `useParams()`

✅ **To get dynamic parts from the URL.**

Example:

```jsx
import { useParams } from "react-router-dom";

function User() {
  const { userId } = useParams();

  return <h1>User ID is {userId}</h1>;
}
```

Suppose URL = `/user/55`, then `userId = 55`.

---

## 2. `useNavigate()`

✅ **To navigate programmatically without `<Link>`.**

Example:

```jsx
import { useNavigate } from "react-router-dom";

function Contact() {
  const navigate = useNavigate();

  function handleSubmit() {
    // after submit, go to home
    navigate("/");
  }

  return (
    <div>
      <h1>Contact Page</h1>
      <button onClick={handleSubmit}>Submit and Go Home</button>
    </div>
  );
}
```

- `navigate("/")` ➔ goes to home.
- `navigate("/dashboard")` ➔ goes to dashboard.
- `navigate(-1)` ➔ goes **back** (like browser back button).
- `navigate(1)` ➔ goes **forward**.

---

## 3. `useSearchParams()`

#### 1. **Import the hook**

```js
import { useSearchParams } from "react-router-dom";
```

#### 2. **Use it in your component**

```jsx
import React from "react";
import { useSearchParams } from "react-router-dom";

const MyComponent = () => {
  const [searchParams] = useSearchParams();

  const userId = searchParams.get("user");
  const token = searchParams.get("token");

  return (
    <div>
      <h2>Query Parameters</h2>
      <p>User ID: {userId}</p>
      <p>Token: {token}</p>
    </div>
  );
};

export default MyComponent;
```

---

### 🌐 Example URL

```
http://localhost:3000/dashboard?user=123&token=abc456
```

- `user` → `"123"`
- `token` → `"abc456"`

### 🧠 Notes

- `useSearchParams()` returns a `URLSearchParams` object.
- You can also **set** query parameters using the same hook (for navigation).
- React Router **v5 and earlier** uses different methods like `useLocation`.

---

## 4. `useLocation()`

✅ **To get the current URL info.**

Example:

```jsx
import { useLocation } from "react-router-dom";

function CurrentPage() {
  const location = useLocation();

  return (
    <div>
      <h1>Current URL Path: {location.pathname}</h1>
    </div>
  );
}

const useQuery = () => new URLSearchParams(useLocation().search);

// In your component
const query = useQuery();
const user = query.get("user");
```

If you are on `/about`, `location.pathname = "/about"`.

---

# 🔥 Summary Cheat Sheet:

| Hook                | Usage                                    |
| :------------------ | :--------------------------------------- |
| `useParams()`       | Read values like `:id`, `:slug` from URL |
| `useNavigate()`     | Go to another page with code             |
| `useSearchParams()` | Read query params                        |
| `useLocation()`     | Read current URL, query params, etc      |

---
