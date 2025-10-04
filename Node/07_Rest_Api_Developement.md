## ✅ 1. **What is REST?**

### 📘 **REST** (Representational State Transfer) is:

A set of architectural principles for designing networked applications.

### 🔑 Key Principles of REST:

* **Stateless**: No session or context stored on server between requests.
* **Client-Server**: Separation of concerns between frontend (client) and backend (server).
* **Uniform Interface**: Use standard HTTP methods (GET, POST, PUT, DELETE).
* **Resource-Based**: Everything is a resource (users, posts, products) and is accessed via URLs.
* **Representation**: Resources are represented in formats like JSON (most common in REST APIs).
* **Cacheable**: Responses can be cached to improve performance.
* **Layered System**: Architecture can have layers (e.g., middleware, gateways) for scalability.

### 🌐 Example REST API:

| HTTP Method | URL         | Action         |
| ----------- | ----------- | -------------- |
| GET         | /users      | Get all users  |
| GET         | /users/\:id | Get user by ID |
| POST        | /users      | Create a user  |
| PUT         | /users/\:id | Update a user  |
| DELETE      | /users/\:id | Delete a user  |

---

## 🔍 **In-Depth REST Principles (with MERN Context)**

### 1. 📦 **Resource-Based Design**

* Resources are **nouns**, not verbs.
* Use **plural nouns** in URLs:
  ✅ `/users` not `/getUsers`

#### Example:

```bash
GET /users           # List all users
POST /users          # Create a new user
GET /users/:id       # Get a single user
PUT /users/:id       # Update user
DELETE /users/:id    # Delete user
```

---

### 2. 🧭 **HTTP Methods = CRUD**

| HTTP Method | CRUD Operation   | Use Case Example    |
| ----------- | ---------------- | ------------------- |
| GET         | Read             | `GET /posts`        |
| POST        | Create           | `POST /posts`       |
| PUT         | Update (Replace) | `PUT /posts/:id`    |
| PATCH       | Update (Partial) | `PATCH /posts/:id`  |
| DELETE      | Delete           | `DELETE /posts/:id` |

---

### 3. 🧠 **Statelessness**

Each API request must contain **all necessary information** (e.g., token, ID) to process it.
No session is stored between requests.

#### Example:

Frontend sends the token every time:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

### 4. 📄 **Representations (Usually JSON)**

* Resources can be sent as JSON, XML, or HTML.
* In modern REST APIs, **JSON** is the standard.

#### Example JSON Response:

```json
{
  "id": "123",
  "name": "Ganesh",
  "email": "ganesh@example.com"
}
```

---

### 5. ⚙️ **Uniform Interface**

Designing a predictable, standardized interface.

#### Includes:

* **Resource-based URIs**
* **Standard HTTP methods**
* **Consistent response format**
* **Hypermedia as the engine of application state (HATEOAS)** *(optional, advanced)*

---

### 6. 🧱 **Layered System**

Middleware layers like:

* **Auth middleware**
* **Logger**
* **Rate limiter**
* **Database interaction layer**

#### Example:

```js
app.use(authMiddleware); // layer
app.use("/api/users", userRoutes);
```

---

### 7. 🚀 **Cacheable**

Use HTTP headers for caching:

```http
Cache-Control: public, max-age=3600
```

Allows browsers or proxies to cache results.

---

### 8. 🧪 Real-life Example (MERN Stack)

You build a REST API for a blog system:

**Mongoose Model:**

```js
const Post = mongoose.model("Post", {
  title: String,
  content: String,
  author: mongoose.Types.ObjectId
});
```

**Express Route Example:**

```js
app.get("/api/posts/:id", async (req, res) => {
  const post = await Post.findById(req.params.id);
  if (!post) return res.status(404).json({ error: "Post not found" });
  res.json(post);
});
```

---

## ✅ 2. **Best Practices in REST API Development**

Following best practices ensures your API is clean, scalable, secure, and easy to use.

---

### 🔧 **1. Use Consistent Naming Conventions**

* Use **plural nouns** for resource names:
  ✅ `/users`, `/products`, `/orders`

* Avoid verbs in URL:
  ❌ `/getUsers`
  ✅ `GET /users`

---

### 🚦 **2. Use HTTP Methods Properly**

| HTTP Method | Description    |
| ----------- | -------------- |
| GET         | Read           |
| POST        | Create         |
| PUT         | Full Update    |
| PATCH       | Partial Update |
| DELETE      | Delete         |

Example:

```http
PUT /users/123      # Replaces the whole user
PATCH /users/123    # Updates only provided fields
```

---

### 🧾 **3. Use Proper HTTP Status Codes**

| Code | Meaning                                   |
| ---- | ----------------------------------------- |
| 200  | OK                                        |
| 201  | Created                                   |
| 204  | No Content (Success but no response body) |
| 400  | Bad Request                               |
| 401  | Unauthorized                              |
| 403  | Forbidden                                 |
| 404  | Not Found                                 |
| 500  | Server Error                              |

---

### 🛡️ **4. Use Middleware for Common Tasks**

* **Authentication**: JWT or session
* **Validation**: `express-validator` or `Joi`
* **Logging**: `morgan`, `winston`
* **Rate limiting**: `express-rate-limit`

---

### 🔐 **5. Don’t Expose Sensitive Data**

* Avoid returning password, token, or internal IDs in responses.
* Use `.select("-password")` in Mongoose to exclude sensitive fields.

---

### 📁 **6. Organize Your Project Structure**

Use **MVC-style structure**:

```
/controllers
/models
/routes
/middlewares
```

Example:

```bash
routes/userRoutes.js
controllers/userController.js
models/User.js
middlewares/authMiddleware.js
```

---

### 📤 **7. Return Consistent JSON Responses**

Structure all responses with a consistent format:

```json
{
  "success": true,
  "message": "User fetched successfully",
  "data": {
    "id": "123",
    "name": "Ganesh"
  }
}
```

---

### 🔄 **8. Version Your APIs**

Use versioning in URL:

```bash
/api/v1/users
/api/v2/users
```

This ensures backward compatibility.

---

### ⚙️ **9. Use `.env` for Configs**

Keep secrets and configs in `.env`:

```bash
PORT=5000
MONGO_URI=mongodb://localhost:27017/blogapp
JWT_SECRET=mysecretkey
```

---

### 🧪 **10. Always Test Your API**

Use tools like:

* [Postman](https://www.postman.com/)
* [Thunder Client (VS Code Extension)](https://www.thunderclient.com/)
* [Insomnia](https://insomnia.rest/)

---

## ✅ 3. **Structuring Routes and Controllers in a REST API**

A clean structure keeps your project **maintainable**, **scalable**, and **easy to debug**.

---

### 📁 **Folder Structure Example**

```
project/
│
├── controllers/
│   └── userController.js
│
├── routes/
│   └── userRoutes.js
│
├── models/
│   └── User.js
│
├── middlewares/
│   └── authMiddleware.js
│
├── app.js
└── server.js
```

---

## 🧩 1. **Controller Functions**

Controllers handle **business logic**.

📄 `controllers/userController.js`

```js
const User = require("../models/User");

const getAllUsers = async (req, res) => {
  const users = await User.find();
  res.status(200).json({ success: true, data: users });
};

const createUser = async (req, res) => {
  const user = await User.create(req.body);
  res.status(201).json({ success: true, data: user });
};

module.exports = { getAllUsers, createUser };
```

---

## 🛣️ 2. **Route Files**

Routes connect **HTTP methods & paths** to controller functions.

📄 `routes/userRoutes.js`

```js
const express = require("express");
const { getAllUsers, createUser } = require("../controllers/userController");

const router = express.Router();

router.get("/", getAllUsers);
router.post("/", createUser);

module.exports = router;
```

---

## 🧵 3. **Connecting Routes in App**

📄 `app.js`

```js
const express = require("express");
const userRoutes = require("./routes/userRoutes");

const app = express();

// Middleware to parse JSON
app.use(express.json());

// Mount the route
app.use("/api/users", userRoutes);

module.exports = app;
```

📄 `server.js`

```js
const app = require("./app");

app.listen(5000, () => {
  console.log("Server running on http://localhost:5000");
});
```

---

### ✅ This results in working REST endpoints:

* `GET /api/users` → Get all users
* `POST /api/users` → Create a user

---

## ✅ 4. **CRUD API for a Resource (Full Example)**

We'll build a **complete REST API** for a sample resource — `User`.

---

### 🧾 **User Schema (Mongoose Model)**

📄 `models/User.js`

```js
const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
  },
  age: {
    type: Number,
    default: 18,
  },
}, { timestamps: true });

module.exports = mongoose.model("User", userSchema);
```

---

### 🔧 **Controller with Full CRUD**

📄 `controllers/userController.js`

```js
const User = require("../models/User");

// Create
const createUser = async (req, res) => {
  const user = await User.create(req.body);
  res.status(201).json({ success: true, data: user });
};

// Read all
const getAllUsers = async (req, res) => {
  const users = await User.find();
  res.status(200).json({ success: true, data: users });
};

// Read one
const getUserById = async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) return res.status(404).json({ success: false, message: "User not found" });
  res.status(200).json({ success: true, data: user });
};

// Update
const updateUser = async (req, res) => {
  const user = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
  if (!user) return res.status(404).json({ success: false, message: "User not found" });
  res.status(200).json({ success: true, data: user });
};

// Delete
const deleteUser = async (req, res) => {
  const user = await User.findByIdAndDelete(req.params.id);
  if (!user) return res.status(404).json({ success: false, message: "User not found" });
  res.status(200).json({ success: true, message: "User deleted successfully" });
};

module.exports = {
  createUser,
  getAllUsers,
  getUserById,
  updateUser,
  deleteUser,
};
```

---

### 🔌 **Route Setup**

📄 `routes/userRoutes.js`

```js
const express = require("express");
const {
  createUser,
  getAllUsers,
  getUserById,
  updateUser,
  deleteUser,
} = require("../controllers/userController");

const router = express.Router();

router.route("/")
  .get(getAllUsers)
  .post(createUser);

router.route("/:id")
  .get(getUserById)
  .put(updateUser)
  .delete(deleteUser);

module.exports = router;
```

---

### 🚀 **Endpoint Summary**

| Method | Route            | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/api/users`     | Get all users     |
| POST   | `/api/users`     | Create new user   |
| GET    | `/api/users/:id` | Get user by ID    |
| PUT    | `/api/users/:id` | Update user by ID |
| DELETE | `/api/users/:id` | Delete user by ID |

---

## ✅ 5. **Using Postman or Thunder Client for Testing REST APIs**

Testing your API is critical to ensure it behaves correctly. Tools like **Postman** and **Thunder Client** make it easy.

---

## 🧪 What Are These Tools?

| Tool               | Platform          | Key Features                            |
| ------------------ | ----------------- | --------------------------------------- |
| **Postman**        | Desktop/Web App   | Full testing suite, powerful automation |
| **Thunder Client** | VS Code Extension | Lightweight, easy for quick tests       |

---

## 🚀 Steps to Test Your API

### 1. 🔧 Start Your Server

Ensure your Express server is running on a port, e.g.:

```bash
Server running on http://localhost:5000
```

---

### 2. 🌐 Test Endpoints

Let’s assume your API base is: `http://localhost:5000/api/users`

---

### 📌 1. **GET All Users**

* Method: `GET`
* URL: `http://localhost:5000/api/users`
* Click **Send**
* ✅ Response: List of users

---

### 📌 2. **POST (Create User)**

* Method: `POST`
* URL: `http://localhost:5000/api/users`
* Select **Body → raw → JSON**

```json
{
  "name": "Ganesh",
  "email": "ganesh@example.com",
  "age": 23
}
```

* ✅ Response: Newly created user

---

### 📌 3. **GET Single User**

* Method: `GET`
* URL: `http://localhost:5000/api/users/<user_id>`

---

### 📌 4. **PUT (Update User)**

* Method: `PUT`
* URL: `http://localhost:5000/api/users/<user_id>`
* Body:

```json
{
  "name": "Ganesh Arwat Updated"
}
```

---

### 📌 5. **DELETE User**

* Method: `DELETE`
* URL: `http://localhost:5000/api/users/<user_id>`

---

## 🎯 Tips for Postman/Thunder Client

### 🔁 Collections (Postman)

* Save requests to a **collection** to reuse later.
* Great for organizing testing per project.

### ✅ Environment Variables

* Set `{{base_url}} = http://localhost:5000`
* Use `{{base_url}}/api/users` in requests

---

## ⚙️ Thunder Client Setup in VS Code

1. Install extension: **Thunder Client**
2. Click Thunder icon in sidebar
3. Create a new request → Set method & URL
4. Choose `Body → JSON` for POST/PUT
5. Click **Send**

---

## ✅ 6. **Request Validation and Error Handling in REST APIs**

Ensuring that incoming data is **valid**, and handling errors properly, makes your API secure and reliable.

---

## 🛂 1. **Why Validation Matters**

Without validation:

* You can get incorrect or missing data in DB.
* It opens security risks (e.g. NoSQL injections).
* Your API becomes unpredictable.

---

## 🧰 2. **Tools for Validation**

### ✅ Option 1: [`express-validator`](https://express-validator.github.io/)

* Built for Express.js
* Validates and sanitizes incoming request data

```bash
npm install express-validator
```

---

### ✅ Option 2: `Joi` (powerful schema-based validation)

```bash
npm install joi
```

We'll use `express-validator` now since it's commonly used and very clean for beginners.

---

## ✨ Example with `express-validator`

📄 `routes/userRoutes.js`

```js
const express = require("express");
const { body } = require("express-validator");
const {
  createUser
} = require("../controllers/userController");

const router = express.Router();

router.post(
  "/",
  [
    body("name").notEmpty().withMessage("Name is required"),
    body("email").isEmail().withMessage("Valid email required"),
    body("age").optional().isInt({ min: 0 }).withMessage("Age must be a positive number")
  ],
  createUser
);

module.exports = router;
```

---

📄 `controllers/userController.js`

```js
const { validationResult } = require("express-validator");
const User = require("../models/User");

const createUser = async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ success: false, errors: errors.array() });
  }

  const user = await User.create(req.body);
  res.status(201).json({ success: true, data: user });
};
```

---

## ⚠️ 3. **Centralized Error Handling (Middleware)**

You can create a global error handler:

📄 `middlewares/errorMiddleware.js`

```js
const errorHandler = (err, req, res, next) => {
  console.error(err.stack);
  res.status(err.statusCode || 500).json({
    success: false,
    message: err.message || "Server Error",
  });
};

module.exports = errorHandler;
```

📄 `app.js`

```js
const errorHandler = require("./middlewares/errorMiddleware");

// after all routes
app.use(errorHandler);
```

---

## 🧪 Example Error JSON Response

```json
{
  "success": false,
  "errors": [
    {
      "msg": "Name is required",
      "param": "name",
      "location": "body"
    }
  ]
}
```

---

### ✅ Summary:

* Use `express-validator` to validate inputs.
* Always check `validationResult`.
* Use middleware to catch unexpected errors.
* Never expose full error stack to users in production.

---

## ✅ 7. **Pagination and Filtering in REST APIs**

Pagination and filtering are essential for performance and usability, especially when your database has many records.

---

## 🔍 Why Use Pagination?

* Limits the number of results per request.
* Prevents overloading the server and client.
* Improves user experience by breaking results into chunks (pages).

---

## 🗃️ 1. **Basic Pagination Implementation**

### 📄 Example: `GET /api/users?page=2&limit=5`

```js
const getAllUsers = async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;

  const skip = (page - 1) * limit;

  const users = await User.find().skip(skip).limit(limit);
  const totalUsers = await User.countDocuments();

  res.status(200).json({
    success: true,
    page,
    totalPages: Math.ceil(totalUsers / limit),
    data: users
  });
};
```

---

## 🧠 2. **Filtering**

Allow users to filter by query params.

### 📄 Example: `GET /api/users?age=23`

```js
const getAllUsers = async (req, res) => {
  const queryObject = {};

  if (req.query.age) {
    queryObject.age = req.query.age;
  }

  const users = await User.find(queryObject);
  res.json({ success: true, data: users });
};
```

---

## 🔄 Combine Pagination + Filtering

```js
const getAllUsers = async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const skip = (page - 1) * limit;

  const queryObject = {};
  if (req.query.age) queryObject.age = req.query.age;
  if (req.query.name) queryObject.name = new RegExp(req.query.name, "i");

  const total = await User.countDocuments(queryObject);
  const users = await User.find(queryObject).skip(skip).limit(limit);

  res.status(200).json({
    success: true,
    total,
    page,
    totalPages: Math.ceil(total / limit),
    data: users,
  });
};
```

---

## 📦 Sample Request URLs

* `GET /api/users?page=1&limit=5` — Paginate users
* `GET /api/users?age=23` — Filter by age
* `GET /api/users?page=2&limit=3&name=ganesh` — Paginate + Filter by name

---

## 🛠️ Bonus: Sorting

```js
const users = await User.find(queryObject)
  .sort({ age: -1 })    // sort by age DESC
  .skip(skip)
  .limit(limit);
```

---

### ✅ Summary:

* Use `skip()` and `limit()` in Mongoose for pagination.
* Accept filters through query params.
* Return metadata like `totalPages` and `page` in response.

---

## ✅ 8. **Nesting Routes: `/users/:id/posts`**

Nesting routes helps represent **relationships between resources**, such as:

* A **User** has many **Posts**
* A **Product** has many **Reviews**
* A **Course** has many **Lessons**

---

## 🧠 Example Use Case:

A user can create multiple posts.
So you create a nested route:

```
GET /users/:userId/posts → Get all posts for a user  
POST /users/:userId/posts → Create a post for a user
```

---

## 📁 Folder Structure

```
/models/User.js
/models/Post.js
/controllers/postController.js
/routes/postRoutes.js
```

---

## 📄 1. Mongoose Models (Relation using user ID)

📄 `models/Post.js`

```js
const mongoose = require("mongoose");

const postSchema = new mongoose.Schema({
  title: String,
  content: String,
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User", // ref to User model
    required: true
  }
}, { timestamps: true });

module.exports = mongoose.model("Post", postSchema);
```

---

## 📄 2. Nested Routes in Express

📄 `routes/postRoutes.js`

```js
const express = require("express");
const {
  createPostForUser,
  getPostsByUser
} = require("../controllers/postController");

const router = express.Router({ mergeParams: true });

router.route("/")
  .get(getPostsByUser)
  .post(createPostForUser);

module.exports = router;
```

📄 `routes/userRoutes.js`

```js
const express = require("express");
const { getAllUsers, createUser } = require("../controllers/userController");
const postRoutes = require("./postRoutes");

const router = express.Router();

router.route("/")
  .get(getAllUsers)
  .post(createUser);

// Nested route: /users/:userId/posts
router.use("/:userId/posts", postRoutes);

module.exports = router;
```

---

## 📄 3. Controllers for Posts

📄 `controllers/postController.js`

```js
const Post = require("../models/Post");

const getPostsByUser = async (req, res) => {
  const posts = await Post.find({ user: req.params.userId });
  res.status(200).json({ success: true, data: posts });
};

const createPostForUser = async (req, res) => {
  const post = await Post.create({
    ...req.body,
    user: req.params.userId
  });
  res.status(201).json({ success: true, data: post });
};

module.exports = { getPostsByUser, createPostForUser };
```

---

## 🚀 Example API Calls

* `GET /api/users/123/posts` → Get all posts by user 123
* `POST /api/users/123/posts` → Create a post for user 123

  ```json
  {
    "title": "Hello World",
    "content": "This is my first post"
  }
  ```

---

## 🧠 Key Points

* Use `mergeParams: true` in `Router()` to access parent params.
* Design reflects the relationship between resources.
* You can extend this pattern to more deeply nested routes (e.g., `/users/:id/posts/:postId/comments`).

---

Perfect, Ganesh! Let's move on to:

---

## ✅ 9. **API Versioning: `/api/v1/`**

API versioning helps you **manage changes** to your API **without breaking existing clients**. It's an essential practice for building maintainable and scalable backends.

---

## 🔎 Why Version Your API?

* ✅ Safely introduce breaking changes
* ✅ Support multiple versions (v1, v2) at once
* ✅ Let clients upgrade when they’re ready

---

## 🚀 Versioning Styles

| Style             | Example                               | Comment                          |
| ----------------- | ------------------------------------- | -------------------------------- |
| URI Versioning    | `/api/v1/users`                       | ✅ Most common and clear          |
| Header Versioning | `Accept: application/vnd.api.v1+json` | 🔁 Less common, harder to debug  |
| Query Param       | `/api/users?version=1`                | ❌ Not recommended for versioning |

👉 In REST, **URI versioning** is the standard and preferred.

---

## 📁 Folder Setup Example (v1)

```
/routes/
  /v1/
    userRoutes.js
    postRoutes.js
/controllers/
  userController.js
  postController.js
/app.js
/server.js
```

---

## 📄 Example `app.js`

```js
const express = require("express");
const userRoutesV1 = require("./routes/v1/userRoutes");
const postRoutesV1 = require("./routes/v1/postRoutes");

const app = express();
app.use(express.json());

// API versioned routing
app.use("/api/v1/users", userRoutesV1);
app.use("/api/v1/posts", postRoutesV1);

module.exports = app;
```

---

## ✅ How It Works

| Request              | Action              |
| -------------------- | ------------------- |
| `GET /api/v1/users`  | Uses v1 user routes |
| `POST /api/v1/posts` | Uses v1 post routes |

Later, when you want to change the logic or response format:

📁 `/routes/v2/userRoutes.js`
📁 `/controllers/v2/userController.js`

```js
app.use("/api/v2/users", userRoutesV2);
```

Clients using `/v1` won’t be affected!

---

## 🧠 Best Practices

* Always **start with `/api/v1/`** even if you only have one version
* Keep version folders organized: `/routes/v1/`, `/controllers/v1/`
* Maintain old versions until all clients migrate
* Document what changed in v2, v3, etc.

---

👉 **API versioning isn’t only about changing the URL — it’s about separating the entire behavior of your API, including business logic, controllers, schemas, and even responses.**

---

## ✅ So how to separate **business logic** between versions?

Here’s how you can do it **properly** in a scalable way:

---

### 🧱 Folder Structure for Multi-Version Support

```
/controllers/
  /v1/
    userController.js
  /v2/
    userController.js

/routes/
  /v1/
    userRoutes.js
  /v2/
    userRoutes.js

/models/
  User.js   # Shared or versioned if needed

/services/
  /v1/
    userService.js
  /v2/
    userService.js
```

---

### 🧠 Example Use Case

Let’s say in:

* **v1**: You return `name` and `email` of a user.
* **v2**: You return `name`, `email`, and calculated `isAdult` based on age.

---

### 📄 v1 Controller

📁 `controllers/v1/userController.js`

```js
const User = require("../../models/User");

const getUser = async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json({ name: user.name, email: user.email });
};

module.exports = { getUser };
```

---

### 📄 v2 Controller

📁 `controllers/v2/userController.js`

```js
const User = require("../../models/User");

const getUser = async (req, res) => {
  const user = await User.findById(req.params.id);
  const isAdult = user.age >= 18;

  res.json({
    name: user.name,
    email: user.email,
    isAdult,
  });
};

module.exports = { getUser };
```

---

### 📄 Routes Setup

📁 `routes/v1/userRoutes.js`

```js
const express = require("express");
const { getUser } = require("../../controllers/v1/userController");
const router = express.Router();

router.get("/:id", getUser);
module.exports = router;
```

📁 `routes/v2/userRoutes.js`

```js
const express = require("express");
const { getUser } = require("../../controllers/v2/userController");
const router = express.Router();

router.get("/:id", getUser);
module.exports = router;
```

---

### 📄 app.js

```js
const userRoutesV1 = require("./routes/v1/userRoutes");
const userRoutesV2 = require("./routes/v2/userRoutes");

app.use("/api/v1/users", userRoutesV1);
app.use("/api/v2/users", userRoutesV2);
```

---

## 🎯 Result:

| Version | Route               | Returns                    |
| ------- | ------------------- | -------------------------- |
| v1      | `/api/v1/users/123` | `{ name, email }`          |
| v2      | `/api/v2/users/123` | `{ name, email, isAdult }` |

---

## ✅ Final Tip: Decouple Logic Further

If you expect more business logic differences:

* Use separate **services** (`/services/v1/userService.js`)
* Or use a **version-aware factory/service loader**

---

## ✅ 10. **HTTP Status Codes in REST APIs**

HTTP status codes tell the client what **happened** when they made a request. Using them **correctly** makes your API predictable and easy to debug.

---

## 🧾 Status Code Categories

| Code Range | Meaning                         |
| ---------- | ------------------------------- |
| 1xx        | Informational (rarely used)     |
| 2xx        | ✅ Success                       |
| 3xx        | Redirects (rarely used in APIs) |
| 4xx        | ❌ Client Error                  |
| 5xx        | 🚨 Server Error                 |

---

## 🚀 Most Common Status Codes for REST APIs

### ✅ **2xx – Success**

| Code | Meaning    | When to Use                            |
| ---- | ---------- | -------------------------------------- |
| 200  | OK         | Successful GET or PUT request          |
| 201  | Created    | Successful POST (new resource created) |
| 204  | No Content | Successful DELETE (no body returned)   |

---

### ❌ **4xx – Client Errors**

| Code | Meaning      | When to Use                                     |
| ---- | ------------ | ----------------------------------------------- |
| 400  | Bad Request  | Invalid input, missing fields, validation fails |
| 401  | Unauthorized | Missing or invalid authentication               |
| 403  | Forbidden    | Authenticated but not allowed (e.g., roles)     |
| 404  | Not Found    | Resource doesn't exist                          |
| 409  | Conflict     | Duplicate resource (e.g., email already taken)  |

---

### 🚨 **5xx – Server Errors**

| Code | Meaning               | When to Use                                      |
| ---- | --------------------- | ------------------------------------------------ |
| 500  | Internal Server Error | Unexpected error on your server                  |
| 502  | Bad Gateway           | Server acting as a proxy got an invalid response |

---

## 🛠️ Example in Express

```js
const getUserById = async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) {
      return res.status(404).json({ success: false, message: "User not found" });
    }
    res.status(200).json({ success: true, data: user });
  } catch (error) {
    res.status(500).json({ success: false, message: "Server error" });
  }
};
```

---

## ✅ Best Practices

* Don’t always return `200` — be specific.
* Match the status code to what actually happened.
* Use `201 Created` for successful POSTs.
* Use `204 No Content` for successful DELETEs with no return body.
* Never expose full error stacks in production (mask `500` errors).

---

## 🎯 Quick Summary Table

| Method | Success Code | Error Code Examples   |
| ------ | ------------ | --------------------- |
| GET    | 200          | 404 (Not Found)       |
| POST   | 201          | 400 (Validation), 409 |
| PUT    | 200/204      | 400, 404              |
| DELETE | 204          | 404                   |

---

## ✅ 11. **Rate Limiting & Throttling in Express with `express-rate-limit`**

Rate limiting protects your API from abuse, brute-force attacks, or spam by limiting the number of requests a client (usually by IP) can make in a certain time.

---

## 🔐 Why Use Rate Limiting?

* 🛡️ Prevents DDoS attacks and brute-force login attempts
* 🚫 Blocks bots or scrapers from spamming endpoints
* 💰 Saves backend compute and bandwidth costs

---

## 🧰 Tool: `express-rate-limit`

### 📦 Install it:

```bash
npm install express-rate-limit
```

---

## ⚙️ Basic Setup

📄 `app.js`

```js
const rateLimit = require("express-rate-limit");

// Limit each IP to 100 requests per 15 minutes
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests
  message: {
    success: false,
    message: "Too many requests, please try again later.",
  }
});

// Apply to all requests
app.use(limiter);
```

---

## 🛠️ Apply to Specific Routes Only

You can also limit sensitive routes like login or signup:

📄 `routes/authRoutes.js`

```js
const express = require("express");
const rateLimit = require("express-rate-limit");
const { loginUser } = require("../controllers/authController");

const router = express.Router();

// Limit login attempts: 5 per 15 minutes
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  message: {
    success: false,
    message: "Too many login attempts. Try again later.",
  },
});

router.post("/login", loginLimiter, loginUser);

module.exports = router;
```

---

## ⚡ Optional: Customize Headers & Handler

```js
const limiter = rateLimit({
  windowMs: 10 * 60 * 1000,
  max: 50,
  standardHeaders: true, // Return `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
  handler: (req, res, next) => {
    res.status(429).json({
      success: false,
      message: "Rate limit exceeded. Slow down!",
    });
  },
});
```

---

## ✅ Best Practices

* Always apply global rate limits to public APIs.
* Use stricter limits on **sensitive routes** (login, registration, password reset).
* Combine with:

  * IP blacklisting
  * CAPTCHA (e.g. after several failed attempts)
  * API key usage (for public APIs)

---
