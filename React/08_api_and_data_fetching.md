## ✅ 8.1. `fetch()` and `axios`

In React, we commonly use `fetch()` or `axios` to get data from APIs.

---

### 🔹 `fetch()` - Built-in JavaScript Method

#### ✅ Syntax:

```js
fetch(url)
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

#### ✅ React Example using `fetch()`:

```jsx
useEffect(() => {
  const fetchData = async () => {
    try {
      const res = await fetch("https://jsonplaceholder.typicode.com/posts");
      const data = await res.json();
      setPosts(data);
    } catch (err) {
      console.error("Fetch error:", err);
    }
  };
  fetchData();
}, []);
```

---

### 🔹 `axios` - External HTTP Client

#### ✅ Install it:

```bash
npm install axios
```

#### ✅ Syntax:

```js
axios
  .get(url)
  .then((response) => response.data)
  .catch((error) => console.error(error));
```

#### ✅ React Example using `axios`:

```jsx
import axios from "axios";

useEffect(() => {
  const fetchPosts = async () => {
    try {
      const res = await axios.get("https://jsonplaceholder.typicode.com/posts");
      setPosts(res.data);
    } catch (err) {
      console.error("Axios error:", err);
    }
  };

  fetchPosts();
}, []);
```

---

### ✅ Differences Between `fetch()` and `axios`

| Feature              | `fetch()`                       | `axios`                       |
| -------------------- | ------------------------------- | ----------------------------- |
| Built-in             | Yes                             | No (requires installation)    |
| Response             | Needs manual `.json()` parsing  | Auto-parses JSON              |
| Error Handling       | Only rejects on network failure | Rejects on any error response |
| Request Cancellation | No (manual workaround)          | Yes (with cancel tokens)      |
| Interceptors         | No                              | Yes                           |

---

When to use what?

- ✅ Use `axios` for **real-world projects** (better features).
- ✅ Use `fetch()` for **quick demos** or lightweight apps.

---

## ✅ 8.1 (Advanced) — **Axios Request Cancellation** & **Interceptors**

## 🔹 1. Axios Request Cancellation (to avoid memory leaks or race conditions)

Useful when:

* A component unmounts before the request completes.
* You want to cancel previous API calls (like search input changes).

---

### ✅ Example: Request Cancellation using `AbortController`

```jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CancelRequestExample = () => {
  const [posts, setPosts] = useState([]);
  const [cancelled, setCancelled] = useState(false);

  useEffect(() => {
    const controller = new AbortController();

    const fetchData = async () => {
      try {
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
          signal: controller.signal
        });
        setPosts(response.data);
      } catch (error) {
        if (axios.isCancel(error)) {
          setCancelled(true);
          console.log('Request cancelled:', error.message);
        } else {
          console.error('Error:', error);
        }
      }
    };

    fetchData();

    return () => {
      controller.abort(); // cancel the request when component unmounts
    };
  }, []);

  return (
    <div>
      <h2>Request Cancellation Example</h2>
      {cancelled ? (
        <p>Request was cancelled!</p>
      ) : (
        <ul>
          {posts.slice(0, 5).map(post => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CancelRequestExample;
```

---

## 🔹 2. Axios Interceptors

### 👉 Use Cases:

* Automatically attach **auth tokens** to every request.
* Log all requests/responses.
* Handle global errors like 401 Unauthorized.

---

### ✅ Example: Adding an Interceptor

```js
// axiosConfig.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 5000,
});

// Request Interceptor
axiosInstance.interceptors.request.use(
  config => {
    console.log('[Request]', config.url);
    // Add auth token if needed
    config.headers['Authorization'] = 'Bearer my_token';
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Response Interceptor
axiosInstance.interceptors.response.use(
  response => {
    console.log('[Response]', response.status);
    return response;
  },
  error => {
    if (error.response && error.response.status === 401) {
      alert('Unauthorized! Redirecting to login...');
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
```

### ✅ Usage in Component

```jsx
import React, { useEffect, useState } from 'react';
import axiosInstance from './axiosConfig';

const InterceptorExample = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axiosInstance.get('/posts')
      .then(res => setPosts(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Interceptor Example</h2>
      <ul>
        {posts.slice(0, 5).map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default InterceptorExample;
```

---

### 🧠 Summary

| Feature           | Purpose                                         |
| ----------------- | ----------------------------------------------- |
| `AbortController` | Cancel Axios requests (newer method)            |
| `interceptors`    | Add logic before request/response automatically |

---

