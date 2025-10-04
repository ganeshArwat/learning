### ✅ **5.1 What is Mongoose? Why use it?**

#### ✅ What is Mongoose?

Mongoose is an **Object Data Modeling (ODM)** library for MongoDB and Node.js. It provides a **schema-based solution** to model your application data.

#### ✅ Why use Mongoose?

* **Schema definition**: Enforces structure and data types for MongoDB documents.
* **Built-in validation**: Validates input before saving to DB.
* **Middleware (Hooks)**: Run functions before/after certain operations (e.g., `pre('save')`).
* **Query helpers**: Built-in methods like `.find()`, `.findById()`, etc.
* **Relationships**: Reference other documents using `ref`.
* **Lean queries & population**: Optimize data and join-like functionality.

🔸 MongoDB is schema-less, so Mongoose adds a layer of safety and structure.

---

### ✅ **5.2 Connecting MongoDB with Mongoose**

To connect MongoDB with Mongoose in a Node.js project:

---

### ✅ **1. Install Mongoose**

Use npm:

```bash
npm install mongoose
```

---

### ✅ **2. Import and Connect**

```js
const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    await mongoose.connect('mongodb://localhost:27017/yourDBName', {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });
    console.log("MongoDB Connected ✅");
  } catch (error) {
    console.error("Connection failed ❌", error);
    process.exit(1); // Stop server if DB fails
  }
};

module.exports = connectDB;
```

> 📝 In real apps, you can use `.env` to store the connection string:

```env
MONGO_URI=mongodb://localhost:27017/yourDBName
```

Then use:

```js
mongoose.connect(process.env.MONGO_URI, {...})
```

---

### ✅ **3. Call it in Main File (e.g., app.js or index.js)**

```js
const express = require('express');
const connectDB = require('./config/db'); // your DB file

const app = express();

connectDB(); // Connect to MongoDB

app.listen(5000, () => {
  console.log("Server is running on port 5000");
});
```

---

Now your Node.js app is connected to MongoDB through Mongoose 🚀

---

### ✅ **5.3 Creating Schemas and Models**

In Mongoose, **Schemas** define the structure of your documents, and **Models** are used to interact with the MongoDB collections.

---

### ✅ **1. Creating a Schema**

```js
const mongoose = require('mongoose');

// Define schema
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  age: {
    type: Number,
    min: 0
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});
```

---

### ✅ **2. Creating a Model**

```js
// Create model
const User = mongoose.model('User', userSchema);

// Export the model
module.exports = User;
```

> 💡 The first argument (`'User'`) becomes the **collection name** in lowercase and plural form (e.g., `users`).

---

### ✅ **3. Using the Model**

In another file (e.g., controller or route):

```js
const User = require('../models/User');

// Create a new user
const newUser = new User({
  name: 'Ganesh',
  age: 23,
  email: 'ganesh@example.com'
});

await newUser.save();
```

---

Schemas + Models = Controlled, consistent data 💡

---

### ✅ **5.4 Schema Types and Options**

Mongoose provides various data types and schema options to define how each field should behave.

---

### ✅ **1. Common Schema Types**

| Type       | Example                                |
| ---------- | -------------------------------------- |
| `String`   | `type: String`                         |
| `Number`   | `type: Number`                         |
| `Boolean`  | `type: Boolean`                        |
| `Date`     | `type: Date`                           |
| `Buffer`   | `type: Buffer`                         |
| `ObjectId` | `type: mongoose.Schema.Types.ObjectId` |
| `Array`    | `type: [String]`                       |
| `Mixed`    | `type: mongoose.Schema.Types.Mixed`    |

---

### ✅ **2. Options You Can Use in Schema Fields**

Here are common options for field validation and behavior:

| Option       | Description                              |
| ------------ | ---------------------------------------- |
| `required`   | Makes the field mandatory                |
| `default`    | Sets a default value                     |
| `unique`     | Enforces unique values in the collection |
| `enum`       | Restricts field to specific values       |
| `min`, `max` | Sets min/max for numbers or dates        |
| `trim`       | Trims whitespace from strings            |
| `lowercase`  | Converts strings to lowercase            |
| `match`      | Regex pattern match for strings          |

---

### ✅ **Example**

```js
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  age: {
    type: Number,
    min: 1,
    max: 120
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    match: /.+\@.+\..+/
  },
  hobbies: {
    type: [String],
    default: []
  },
  joinedAt: {
    type: Date,
    default: Date.now
  }
});
```

---

Schemas give MongoDB documents a **structured shape** and **auto-validation**, which is very useful in large apps.

---

### ✅ **5.5 CRUD Operations with Mongoose**

Here’s how you can perform **Create**, **Read**, **Update**, and **Delete** using Mongoose.

Assume you have this model:

```js
const User = require('../models/User');
```

---

### ✅ 1. **Create** a Document

```js
// Option 1: Using `.save()`
const newUser = new User({ name: "Ganesh", age: 23, email: "ganesh@example.com" });
await newUser.save();

// Option 2: Using `.create()`
await User.create({ name: "Ganesh", age: 23, email: "ganesh@example.com" });
```

---

### ✅ 2. **Read** Documents

```js
// Find all users
const users = await User.find();

// Find one user by email
const user = await User.findOne({ email: "ganesh@example.com" });

// Find by ID
const userById = await User.findById("665abc123def4567890ghi12");
```

---

### ✅ 3. **Update** Documents

```js
// Update one document
await User.updateOne({ email: "ganesh@example.com" }, { $set: { age: 24 } });

// OR: Find and modify directly
const updatedUser = await User.findOneAndUpdate(
  { email: "ganesh@example.com" },
  { age: 25 },
  { new: true } // return the updated document
);
```

---

### ✅ 4. **Delete** Documents

```js
// Delete one
await User.deleteOne({ email: "ganesh@example.com" });

// Delete by ID
await User.findByIdAndDelete("665abc123def4567890ghi12");
```

---

### ✅ Extra Tip:

Always wrap these in try/catch for error handling:

```js
try {
  const user = await User.create({...});
  res.json(user);
} catch (err) {
  console.error(err);
  res.status(500).send("Server Error");
}
```

---

### ✅ **5.6 Mongoose Query Methods**

These are the most commonly used Mongoose methods to query and manipulate data.

---

### ✅ 1. **`.find()`**

Returns **all documents** matching the filter.

```js
const users = await User.find({ age: { $gt: 20 } });
```

* Returns an array.
* You can also chain `.limit()`, `.sort()`, `.select()`, etc.

---

### ✅ 2. **`.findOne()`**

Returns **first matching document**.

```js
const user = await User.findOne({ email: "ganesh@example.com" });
```

* Returns a **single document** or `null`.

---

### ✅ 3. **`.findById()`**

Finds a document by its `_id`.

```js
const user = await User.findById("665abc123def4567890ghi12");
```

* Shortcut for: `findOne({ _id: id })`

---

### ✅ 4. **`.save()`**

Used to **save a new document** or changes to an existing one.

```js
const user = new User({ name: "Ganesh", email: "ganesh@example.com" });
await user.save();
```

* Triggers validation.
* Works on document instances.

---

### ✅ 5. **`.updateOne()`**

Update a single document that matches the filter.

```js
await User.updateOne(
  { email: "ganesh@example.com" },
  { $set: { age: 24 } }
);
```

> ⚠️ Doesn't return the updated document by default.

---

### ✅ 6. **`.deleteOne()`**

Deletes the first matching document.

```js
await User.deleteOne({ email: "ganesh@example.com" });
```

* Returns `{ deletedCount: 1 }` if successful.

---

### ✅ Summary Table

| Method         | Use Case                        |
| -------------- | ------------------------------- |
| `.find()`      | Get multiple docs (array)       |
| `.findOne()`   | Get first matching doc          |
| `.findById()`  | Get doc by `_id`                |
| `.save()`      | Save a document (create/update) |
| `.updateOne()` | Update a single matching doc    |
| `.deleteOne()` | Delete a single matching doc    |

---

### 🔗 **Mongoose Model API (Query Methods Reference)**

📘 [https://mongoosejs.com/docs/api/model.html](https://mongoosejs.com/docs/api/model.html)

---

### ✅ **5.7 Model Methods and Statics**

In Mongoose, you can add **custom methods** to your models using:

* `schema.methods` → **Instance methods**
* `schema.statics` → **Static methods** (class-level)

---

### ✅ 1. **Instance Methods** (`schema.methods`)

These are called on **individual documents**.

```js
const userSchema = new mongoose.Schema({
  name: String,
  email: String
});

// Define instance method
userSchema.methods.sayHello = function () {
  return `Hi, I am ${this.name}`;
};

const User = mongoose.model('User', userSchema);

// Usage
const user = await User.findOne();
console.log(user.sayHello()); // "Hi, I am Ganesh"
```

---

### ✅ 2. **Static Methods** (`schema.statics`)

These are called directly on the **model**.

```js
// Define static method
userSchema.statics.findByEmail = function (email) {
  return this.findOne({ email });
};

const User = mongoose.model('User', userSchema);

// Usage
const user = await User.findByEmail("ganesh@example.com");
```

---

### ✅ Why Use These?

| Method Type     | Used When You Want To...                     |
| --------------- | -------------------------------------------- |
| Instance Method | Add logic that operates on a single document |
| Static Method   | Add logic for querying/filtering documents   |

---

### ✅ Use Cases

* `instance method`: `user.isAdult()`, `user.generateToken()`
* `static method`: `User.findByRole('admin')`, `User.findActiveUsers()`

---

### ✅ **5.8 Timestamps and Versioning in Mongoose**

Mongoose gives you built-in support for:

* **Timestamps** → Automatically track `createdAt` and `updatedAt`
* **Versioning** → Tracks changes to documents via `__v`

---

### ✅ 1. **Timestamps**

To enable timestamps in your schema:

```js
const userSchema = new mongoose.Schema({
  name: String,
  email: String
}, {
  timestamps: true
});
```

🔹 Now every document will automatically have:

```js
{
  createdAt: "2025-06-21T11:30:00.000Z",
  updatedAt: "2025-06-21T11:35:00.000Z"
}
```

Mongoose updates `updatedAt` every time you `save()` or `update()` the document.

---

### ✅ 2. **Versioning with `__v`**

Mongoose adds a `__v` field to every document by default:

```json
{
  "_id": "665f123abc...",
  "name": "Ganesh",
  "__v": 0
}
```

This field is used for **internal version control** to detect conflicting updates during concurrent operations.

---

### ✅ How to Disable Versioning

If you want to turn it off:

```js
const userSchema = new mongoose.Schema({ name: String }, {
  versionKey: false
});
```

---

### ✅ Summary

| Feature      | Option              | Purpose                         |
| ------------ | ------------------- | ------------------------------- |
| `timestamps` | `timestamps: true`  | Adds `createdAt`, `updatedAt`   |
| `versioning` | `versionKey: false` | Removes the `__v` version field |

---

### ✅ **5.9 `.select()`, `.sort()`, `.create()` vs `.save()`**

These are useful Mongoose methods to control **data selection, ordering**, and **document creation**.

---

### ✅ 1. **`.select()`** – Include or exclude fields

```js
const user = await User.findOne().select("name email");
```

* Returns only `name` and `email`.
* To **exclude** fields, use `-` (minus sign):

```js
const user = await User.findOne().select("-__v -password");
```

---

### ✅ 2. **`.sort()`** – Sort query results

```js
const users = await User.find().sort({ age: 1 }); // ascending
const usersDesc = await User.find().sort({ age: -1 }); // descending
```

You can sort by any field, even multiple:

```js
.sort({ age: 1, name: -1 })
```

---

### ✅ 3. **`.create()` vs `.save()`**

| Feature        | `.create()`           | `.save()`                                 |
| -------------- | --------------------- | ----------------------------------------- |
| Type           | **Model method**      | **Document instance method**              |
| Use Case       | Quick one-line insert | You want to work with a doc before saving |
| Validation     | Yes                   | Yes                                       |
| Triggers Hooks | Yes                   | Yes                                       |

#### Example: `.create()`

```js
await User.create({
  name: "Ganesh",
  email: "ganesh@example.com",
  age: 23
});
```

#### Example: `.save()`

```js
const user = new User({ name: "Ganesh", email: "ganesh@example.com" });
// Do more with user...
await user.save();
```

---

### ✅ Summary

* Use `.select()` to filter returned fields.
* Use `.sort()` to order results.
* Use `.create()` when inserting directly.
* Use `.save()` when you want to build or modify a document step-by-step.

---

### ✅ **5.10 Error Handling with Async/Await in Mongoose**

When working with Mongoose + async/await, proper **error handling** is critical to avoid app crashes and to give meaningful feedback to users.

---

### ✅ 1. **Basic try-catch pattern**

```js
const createUser = async (req, res) => {
  try {
    const user = await User.create(req.body);
    res.status(201).json(user);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Something went wrong" });
  }
};
```

---

### ✅ 2. **Handling Validation Errors**

Mongoose automatically throws **ValidationError** if schema validation fails.

```js
try {
  await User.create({ email: "invalid" }); // email required in schema
} catch (err) {
  if (err.name === "ValidationError") {
    return res.status(400).json({ message: err.message });
  }
}
```

---

### ✅ 3. **Handling Duplicate Key Errors (e.g., unique email)**

MongoDB returns `error code 11000` for duplicate keys (like unique email):

```js
try {
  await User.create({ email: "ganesh@example.com" }); // already exists
} catch (err) {
  if (err.code === 11000) {
    return res.status(400).json({ message: "Email already exists" });
  }
}
```

---

### ✅ 4. **Optional: Create a Reusable Error Handler Middleware**

```js
// middleware/errorHandler.js
module.exports = (err, req, res, next) => {
  console.error(err);

  if (err.name === "ValidationError") {
    return res.status(400).json({ message: err.message });
  }

  if (err.code === 11000) {
    return res.status(400).json({ message: "Duplicate key error" });
  }

  res.status(500).json({ message: "Server Error" });
};
```

Then in your `app.js`:

```js
const errorHandler = require('./middleware/errorHandler');
app.use(errorHandler);
```

---

### ✅ Summary

* Always wrap Mongoose queries in `try-catch`
* Check `err.name` for validation errors
* Check `err.code === 11000` for duplicate key errors
* Use centralized middleware for cleaner error handling

---


