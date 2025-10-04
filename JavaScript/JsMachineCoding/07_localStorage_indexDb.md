## Cookies

### 🍪 What Are Cookies?

#### Cookies are small pieces of text stored by the browser. They:

- Store data like login info, theme preferences, etc.
- Are sent to the server with every HTTP request.
- Have a max size of ~4KB per cookie.

### ✍️ How to Set a Cookie

- You can set a cookie using JavaScript like this:

```js
document.cookie = "username=ganesh";
```

- ➡️ This will store a cookie named username with value ganesh.

- With Expiration:

```js
document.cookie =
  "username=ganesh; expires=Fri, 05 Apr 2025 12:00:00 UTC; path=/";
```

- expires = When the cookie should expire
- path=/ = Makes it accessible throughout the site

### 📖 How to Read Cookies

```js
console.log(document.cookie);
```

- This returns a string like:

```js
"user=ganesh; theme=dark";
```

- To get a specific cookie:

```js
function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (let cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) return value;
  }
  return null;
}

console.log(getCookie("user")); // "ganesh"
```

### ❌ How to Delete a Cookie

- Set the cookie with a past expiration:

```js
document.cookie = "user=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
```

### 🧪 Test It Yourself in Browser DevTools

- 1. Open DevTools (Right-click → Inspect → Console)
- 2. Paste:

```js
document.cookie = "test=123; expires=Fri, 05 Apr 2025 12:00:00 UTC; path=/";
```

- 3. Then check:

```js
console.log(document.cookie);
```

### 🧰 Useful Cookie Options

- expires
  - Date when cookie expires
- max
  - age Lifetime in seconds
- path
  - Path where the cookie is accessible
- secure
  - Cookie only sent over HTTPS
- SameSite
  - Controls cross-site cookie behavior (Strict, Lax, None)

---

## 💾 LocalStorage & SessionStorage

- Both are part of the Web Storage API and allow you to store key-value data in the browser.

### 🔍 Key Differences

| Feature           | LocalStorage                                    | SessionStorage                                    |
| ----------------- | ----------------------------------------------- | ------------------------------------------------- |
| **Lifetime**      | Permanent (until manually cleared)              | Only for the session (deleted when tab is closed) |
| **Scope**         | Accessible from any tab/window of the same site | Only available in the same tab                    |
| **Storage Limit** | ~5MB                                            | ~5MB                                              |

### ✅ How to Use LocalStorage

- 1️⃣ Storing Data

```js
localStorage.setItem("username", "Ganesh");
```

- 2️⃣ Retrieving Data

```js
let user = localStorage.getItem("username");
console.log(user); // Output: "Ganesh"
```

- 3️⃣ Removing Data

```js
localStorage.removeItem("username");
```

- 4️⃣ Clearing Everything

```js
localStorage.clear();
```

### ✅ How to Use SessionStorage

- Works the same way as LocalStorage, but data is lost when you close the tab.

```js
sessionStorage.setItem("sessionKey", "Hello Session");
console.log(sessionStorage.getItem("sessionKey")); // "Hello Session"
sessionStorage.removeItem("sessionKey");
```

### 🛠️ DevTools Check

- 1. Open DevTools (F12 → Application → Local Storage/Session Storage).
- 2. You can view, edit, and delete stored data.

### 🎯 When to Use What?

| Scenario                                                    | Use            |
| ----------------------------------------------------------- | -------------- |
| Storing user preferences (e.g., theme)                      | LocalStorage   |
| Saving login tokens (⚠️ Not recommended for sensitive data) | LocalStorage   |
| Temporarily storing form data before submission             | SessionStorage |
| Keeping shopping cart items for the entire session          | SessionStorage |

---

## IndexedDB

### 📂 What is IndexedDB?

#### IndexedDB is a low-level, NoSQL database built into the browser. It allows storing large amounts of structured data, unlike LocalStorage (which is limited to 5MB).

- ✅ Key Features:
  - Stores data as key-value pairs
  - Supports indexes for efficient searching
  - Works asynchronously (doesn’t block the UI)
  - Can store complex data like objects and blobs

### 🛠️ How to Use IndexedDB

#### 1️⃣ Opening a Database

```js
let request = indexedDB.open("MyDatabase", 1); // (Name, Version)

request.onsuccess = function (event) {
  let db = event.target.result;
  console.log("Database opened:", db);
};

request.onerror = function (event) {
  console.log("Error opening database", event.target.error);
};
```

- If the database doesn't exist, it gets created.
- The 1 is the version number (useful for schema changes).

#### 2️⃣ Creating an Object Store (Like a Table)

- The first time you create a database, you need to define object stores. This happens inside onupgradeneeded:

```js
request.onupgradeneeded = function (event) {
  let db = event.target.result;

  if (!db.objectStoreNames.contains("users")) {
    let userStore = db.createObjectStore("users", { keyPath: "id" });
    console.log("Object store 'users' created");
  }
};
```

- users is the object store (like a table).
- keyPath: "id" means each object will have a unique id as the primary key.

#### 3️⃣ Adding Data

```js
let db;
request.onsuccess = function (event) {
  db = event.target.result;

  let transaction = db.transaction("users", "readwrite");
  let store = transaction.objectStore("users");

  let user = { id: 1, name: "Ganesh", age: 23 };
  let addRequest = store.add(user);

  addRequest.onsuccess = () => console.log("User added!");
  addRequest.onerror = () => console.log("Error adding user");
};
```

#### 4️⃣ Reading Data

- Get by Id

```js
let transaction = db.transaction("users", "readonly");
let store = transaction.objectStore("users");

let getRequest = store.get(1); // Get user with id=1

getRequest.onsuccess = function () {
  console.log("User:", getRequest.result);
};
```

- Get All Data from an Object Store
  - You can use the .getAll() method to retrieve all records from a specific object store.

```js
let transaction = db.transaction("users", "readonly");
let store = transaction.objectStore("users");

let getAllRequest = store.getAll();

getAllRequest.onsuccess = function () {
  console.log("All users:", getAllRequest.result);
};
```
-  This fetches all records from the "users" store.

#### 5️⃣ Updating Data

```js
let transaction = db.transaction("users", "readwrite");
let store = transaction.objectStore("users");

let updatedUser = { id: 1, name: "Ganesh Arwat", age: 24 };
let updateRequest = store.put(updatedUser);

updateRequest.onsuccess = () => console.log("User updated!");
```

#### 6️⃣ Deleting Data

```js
let transaction = db.transaction("users", "readwrite");
let store = transaction.objectStore("users");

let deleteRequest = store.delete(1);

deleteRequest.onsuccess = () => console.log("User deleted!");
```

#### 🔍 Checking IndexedDB in DevToo

1. Open DevTools (F12) → Application → IndexedDB
2. Expand MyDatabase → users to view stored data
