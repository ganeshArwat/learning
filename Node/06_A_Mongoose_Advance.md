## ✅ **6.1. Schema Validation and Constraints**

### 🔸 What is Schema Validation?

Mongoose allows you to define validation rules directly in your schema to ensure data integrity before it's saved to MongoDB.

### 🔹 Example:

```js
const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true, // field is required
    minlength: 3,
    maxlength: 50,
  },
  email: {
    type: String,
    required: true,
    unique: true, // unique constraint
    match: /.+\@.+\..+/, // regex for email format
  },
  age: {
    type: Number,
    min: 18,
    max: 65,
  },
  createdAt: {
    type: Date,
    default: Date.now, // default value
  },
});

const User = mongoose.model("User", userSchema);
```

---

### 🛠 Common Built-in Validators:

| Validator                 | Description                    |
| ------------------------- | ------------------------------ |
| `required`                | Field must be present          |
| `min` / `max`             | Used for numbers               |
| `minlength` / `maxlength` | For strings                    |
| `enum`                    | Must match one of given values |
| `match`                   | Must match regex               |
| `validate`                | Custom validator function      |

---

### 🔸 Custom Validator:

```js
phone: {
  type: String,
  validate: {
    validator: function(v) {
      return /\d{10}/.test(v); // must be 10 digits
    },
    message: props => `${props.value} is not a valid phone number!`
  }
}
```

---

### 🔹 Error Handling Example:

```js
const newUser = new User({ name: "Al", email: "bademail" });

newUser.save().catch((err) => {
  console.log("Validation Error:", err.message);
});
```

---

### 🔎 Why It Matters:

- Reduces the need for duplicate validation in frontend/backend
- Ensures only valid data enters your DB
- Works well with form validations and APIs

---

## ✅ **6.2. Default Values, Enums, Min/Max**

### 🔸 1. **Default Values**

You can assign default values to fields using the `default` keyword in Mongoose.

#### ✅ Example:

```js
const userSchema = new mongoose.Schema({
  role: {
    type: String,
    default: "user", // sets default if not provided
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});
```

---

### 🔸 2. **Enums**

`enum` is used to restrict a string field to a specific set of values.

#### ✅ Example:

```js
const userSchema = new mongoose.Schema({
  status: {
    type: String,
    enum: ["active", "inactive", "banned"], // only these values allowed
    default: "active",
  },
});
```

- If a value outside this list is passed, Mongoose will throw a validation error.

---

### 🔸 3. **Min/Max (for Numbers)**

Used to enforce numeric range constraints.

#### ✅ Example:

```js
const productSchema = new mongoose.Schema({
  price: {
    type: Number,
    min: 1, // must be at least 1
    max: 10000, // must be at most 10000
  },
  quantity: {
    type: Number,
    default: 0,
  },
});
```

---

### 🔸 4. **MinLength / MaxLength (for Strings)**

These are useful when you want to validate length of text input.

#### ✅ Example:

```js
const commentSchema = new mongoose.Schema({
  content: {
    type: String,
    required: true,
    minlength: 10,
    maxlength: 300,
  },
});
```

---

### 🔍 Real-World Use Case:

| Feature       | Use Case Example                      |
| ------------- | ------------------------------------- |
| Default Value | Assign default role as "user"         |
| Enum          | Restrict status to "active/inactive"  |
| Min/Max       | Prevent unrealistic pricing/quantity  |
| MinLength/Max | Ensure meaningful content in comments |

---

## ✅ **6.3. Schema Methods (Instance Methods)**

### 🔸 What are Schema Methods?

Mongoose allows you to define **custom methods** on documents. These are called **instance methods**, and they can access data of that particular document using `this`.

---

### 🔹 Use Case Examples:

- Hashing passwords
- Generating tokens
- Formatting output
- Custom calculations

---

### ✅ Example: Adding a Greeting Method to User Schema

```js
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
});

// Instance method
userSchema.methods.greet = function () {
  return `Hello, ${this.name}!`;
};

const User = mongoose.model("User", userSchema);

// Using it
const user = new User({ name: "Ganesh", email: "ganesh@example.com" });
console.log(user.greet()); // Output: Hello, Ganesh!
```

---

### 🔐 Example: Compare Password (used in login)

```js
const bcrypt = require("bcrypt");

const userSchema = new mongoose.Schema({
  email: String,
  password: String,
});

// Add method to compare passwords
userSchema.methods.comparePassword = async function (inputPassword) {
  return await bcrypt.compare(inputPassword, this.password);
};
```

---

### 🧠 Key Points:

| Feature              | Description                                    |
| -------------------- | ---------------------------------------------- |
| `this` inside method | Refers to the current document                 |
| Where to define      | On `schema.methods` object                     |
| Use cases            | Per-document logic (e.g., formatting, hashing) |

---

### 🔍 When to Use:

Use **instance methods** when the logic **depends on a single document** and is reusable — like formatting, comparison, or value generation.

---

## ✅ **6.4. Middleware / Hooks: `pre`, `post`**

### 🔸 What is Mongoose Middleware?

Middleware (also called **hooks**) are functions that are **executed automatically before or after** a specific operation like `save`, `remove`, `update`, etc.

They help you:

- Hash passwords before saving
- Log changes
- Set timestamps
- Modify queries

---

### 🔹 Types of Middleware:

| Hook Type | Triggered On         | Description                           |
| --------- | -------------------- | ------------------------------------- |
| `pre`     | Before the operation | Can modify data before it’s saved     |
| `post`    | After the operation  | Used for logging, notifications, etc. |

---

### ✅ Example: Hash Password Before Save

```js
const bcrypt = require("bcrypt");

userSchema.pre("save", async function (next) {
  if (!this.isModified("password")) return next(); // skip if not modified

  this.password = await bcrypt.hash(this.password, 10);
  next();
});
```

> `this` refers to the document that is about to be saved.

---

### ✅ Example: Log After Saving

```js
userSchema.post("save", function (doc) {
  console.log(`User ${doc.email} was saved.`);
});
```

---

### ✅ Example: Pre `findOne` Hook – Add filter

```js
userSchema.pre("findOne", function () {
  this.where({ deleted: false }); // apply filter
});
```

---

### 🔍 Common Middleware Operations:

| Operation     | Hook Examples                                 |
| ------------- | --------------------------------------------- |
| Document save | `pre('save')`, `post('save')`                 |
| Query hooks   | `pre('find')`, `pre('findOne')`               |
| Update hooks  | `pre('updateOne')`, `pre('findOneAndUpdate')` |

> Note: In **query middleware**, `this` refers to the query, not the document.

---

### 🧠 When to Use Middleware:

- Automatically hash passwords
- Add timestamps
- Soft delete filter
- Audit logs
- Normalize data before saving

---

## ✅ **6.5. Virtuals and Populating References**

---

### 🔸 Part 1: **Virtuals**

Virtuals are **properties not stored in MongoDB**, but **computed dynamically** from other data in the document.

---

### ✅ Example: `fullName` Virtual

```js
const userSchema = new mongoose.Schema({
  firstName: String,
  lastName: String,
});

userSchema.virtual("fullName").get(function () {
  return `${this.firstName} ${this.lastName}`;
});

const User = mongoose.model("User", userSchema);

const user = new User({ firstName: "Ganesh", lastName: "Arwat" });
console.log(user.fullName); // Ganesh Arwat
```

---

### 🔸 Use Case Ideas:

| Virtual Field   | Based On                     |
| --------------- | ---------------------------- |
| `fullName`      | `firstName + lastName`       |
| `isAdult`       | `age >= 18`                  |
| `formattedDate` | `createdAt` formatted string |

---

### ⚠️ Note:

- Virtuals are **not saved** to the database.
- To use them in JSON responses:

```js
userSchema.set("toJSON", { virtuals: true });
userSchema.set("toObject", { virtuals: true });
```

---

### 🔸 Part 2: **Populating References**

#### 📌 What is `populate`?

In MongoDB, relationships are **not joined automatically** like in SQL.
Mongoose lets you **link documents via ObjectIds** and use `.populate()` to fetch related data.

---

### ✅ Example: One-to-Many (User → Posts)

```js
// Post schema
const postSchema = new mongoose.Schema({
  title: String,
  content: String,
  author: { type: mongoose.Schema.Types.ObjectId, ref: "User" }, // reference
});

// Fetch post with author data
Post.find()
  .populate("author")
  .then((posts) => {
    console.log(posts[0].author.name); // get name from User
  });
```

---

### 🔹 Nested Population:

```js
Post.find().populate({
  path: "author",
  populate: { path: "company" },
});
```

---

### 🔍 Populate vs Embed:

| Strategy    | Use When...                                   |
| ----------- | --------------------------------------------- |
| Embedding   | Data doesn’t change frequently (faster)       |
| Referencing | Separate collections, frequent updates needed |

---

### 🧠 Tips:

- Use `.select()` with `.populate()` to avoid overfetching:

```js
.populate('author', 'name email') // only fetch selected fields
```

---

## ✅ **Mongoose Populate in Detail**

### 🔹 What is `.populate()`?

In MongoDB, documents are stored in collections — and they don’t have joins like SQL.

Mongoose provides `.populate()` to **manually perform joins** by replacing the referenced ObjectId with the **actual document** from another collection.

---

## 🔸 1. Basic One-to-Many Example

### ✅ Use Case: One User → Many Posts

### 🧩 **Schemas:**

```js
// user.model.js
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
});
const User = mongoose.model("User", userSchema);

// post.model.js
const postSchema = new mongoose.Schema({
  title: String,
  content: String,
  author: { type: mongoose.Schema.Types.ObjectId, ref: "User" }, // referencing User
});
const Post = mongoose.model("Post", postSchema);
```

---

### ✅ Saving a post:

```js
const user = await User.create({ name: "Ganesh", email: "ganesh@example.com" });
await Post.create({
  title: "My First Post",
  content: "Hello world",
  author: user._id,
});
```

---

### ✅ Populate author when fetching:

```js
const posts = await Post.find().populate("author");
console.log(posts[0].author.name); // Output: Ganesh
```

---

## 🔸 2. Populate Specific Fields Only

```js
Post.find().populate("author", "name"); // only populate 'name', skip email
```

---

## 🔸 3. Populate with Filters and Options

```js
Post.find().populate({
  path: "author",
  select: "name email",
  match: { email: /@example\.com$/ }, // filter
  options: { sort: { name: 1 } }, // sort authors if needed
});
```

---

## 🔸 4. Populate Nested References (Multi-level)

Imagine a post’s author works in a company. To populate nested data:

```js
UserSchema.add({
  company: { type: mongoose.Schema.Types.ObjectId, ref: "Company" },
});

Post.find().populate({
  path: "author",
  populate: { path: "company", select: "name location" },
});
```

---

## 🔸 5. Populate in Arrays (One-to-Many)

```js
// A user can have many posts
UserSchema.add({
  posts: [{ type: mongoose.Schema.Types.ObjectId, ref: "Post" }],
});

// Populate posts array
User.findById(userId).populate("posts");
```

---

## 🔸 6. Populate in `execPopulate()` (for document instances)

```js
const post = await Post.findOne();
await post.populate("author").execPopulate();
```

---

## 🔸 7. Populate with `lean()` (⚠️ Important)

By default, `.populate()` works on **Mongoose documents**. If you use `.lean()` (to return plain JS objects), it still works, but **virtuals won’t run**, and you can't use methods like `.save()`.

```js
const posts = await Post.find().populate("author").lean();
```

---

## 🔍 Use Cases for `.populate()`:

| Use Case                             | Example          |
| ------------------------------------ | ---------------- |
| Show post with author                | Blog page        |
| List orders with user info           | E-commerce admin |
| Show comments with commenter info    | Social app       |
| Load nested or multi-level relations | Dashboard views  |

---

## 🔸 Performance Note

Too many populates can slow down queries, especially nested ones.

**Alternatives:**

- Use `lean()` for performance (read-only views)
- Consider **denormalizing** frequent info (e.g., store `authorName` directly in `Post`)
- Use **aggregation** for complex queries

---

## ✅ **6.6. Indexes in Mongoose**

### 🔸 What are Indexes?

Indexes in MongoDB are like indexes in books — they **speed up search and query performance**.

Mongoose allows you to define indexes at the schema level, helping you:

- Search faster
- Enforce uniqueness
- Improve sorting performance

---

### ✅ 1. Declaring Indexes in Schema

```js
const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true, // creates an index automatically
    index: true, // explicitly create index
  },
  age: Number,
});
```

You can also create **compound indexes**:

```js
userSchema.index({ name: 1, age: -1 }); // name ascending, age descending
```

---

### ✅ 2. Types of Indexes

| Index Type   | Syntax                        | Use Case                                  |
| ------------ | ----------------------------- | ----------------------------------------- |
| Single Field | `{ field: 1 }`                | Search, sort on a single field            |
| Compound     | `{ field1: 1, field2: -1 }`   | Queries involving multiple fields         |
| Unique       | `{ field: 1, unique: true }`  | Prevent duplicate entries                 |
| Text Index   | `{ field: "text" }`           | Full-text search on strings               |
| Geospatial   | `{ location: "2dsphere" }`    | Map/Geo queries                           |
| Sparse       | `{ sparse: true }`            | Indexes only documents where field exists |
| Partial      | `{ partialFilterExpression }` | Indexes matching a condition              |

---

### ✅ 3. Creating Indexes with Code

```js
userSchema.index({ email: 1 }, { unique: true });
```

And apply them:

```js
await User.init(); // ensures indexes are created
```

Or manually:

```js
await User.collection.createIndex({ email: 1 });
```

---

### 🔍 Index Use Example

```js
const user = await User.findOne({ email: "ganesh@example.com" });
// ⚡ Fast if email is indexed
```

Without an index on `email`, MongoDB will **scan every document** in the collection = ⏱️ slow.

---

### ⚠️ Caution: Index Bloat

- Too many indexes = slower inserts/updates
- Always index fields used in **search**, **sort**, or **join (populate)**

---

### ✅ Check Indexes

Run this in MongoDB shell or Compass:

```js
db.users.getIndexes();
```

---

## ✅ **6.7. Relationship Types in Mongoose**

MongoDB is non-relational, but with Mongoose, we can **simulate relationships** using **ObjectId references** and `.populate()`.
There are 3 main relationship types:

---

## 🔸 1. One-to-One

### ✅ Use Case: A user has one profile.

#### Schemas:

```js
const userSchema = new mongoose.Schema({
  name: String,
  profile: { type: mongoose.Schema.Types.ObjectId, ref: "Profile" },
});

const profileSchema = new mongoose.Schema({
  bio: String,
  avatar: String,
});
```

#### Usage:

```js
User.findById(id).populate("profile");
```

---

## 🔸 2. One-to-Many

### ✅ Use Case: A user can have many posts.

#### Schemas:

```js
const userSchema = new mongoose.Schema({
  name: String,
});

const postSchema = new mongoose.Schema({
  title: String,
  content: String,
  author: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
});
```

#### Usage:

```js
Post.find().populate("author");
```

#### Alternative: Embed IDs in array (in User):

```js
posts: [{ type: mongoose.Schema.Types.ObjectId, ref: "Post" }];
```

You can then:

```js
User.findById(userId).populate("posts");
```

---

## 🔸 3. Many-to-Many

### ✅ Use Case: Users can join many groups, and groups can have many users.

#### Schemas:

```js
const userSchema = new mongoose.Schema({
  name: String,
  groups: [{ type: mongoose.Schema.Types.ObjectId, ref: "Group" }],
});

const groupSchema = new mongoose.Schema({
  name: String,
  members: [{ type: mongoose.Schema.Types.ObjectId, ref: "User" }],
});
```

#### Usage:

```js
User.find().populate("groups");
Group.find().populate("members");
```

---

## 🔍 When to Embed vs Reference

| Situation                  | Use **Embedding** | Use **Referencing**                  |
| -------------------------- | ----------------- | ------------------------------------ |
| Data changes rarely        | ✅                | ❌                                   |
| Frequent updates           | ❌                | ✅                                   |
| Size is small              | ✅                | ❌                                   |
| Related docs are reused    | ❌                | ✅                                   |
| Performance-sensitive read | ✅                | ❌ unless using `.populate().lean()` |

---

## 🧠 Real-world Examples

| Relationship      | Type         |
| ----------------- | ------------ |
| User ↔ Profile    | One-to-One   |
| User → Posts      | One-to-Many  |
| User ↔ Group      | Many-to-Many |
| Product → Reviews | One-to-Many  |
| Course ↔ Students | Many-to-Many |

---

## ✅ **6.8. Transactions and Session Handling**

---

### 🔸 What is a Transaction?

A **transaction** allows you to **group multiple operations** into a single unit of work — meaning either:

* **All succeed** together, or
* **All fail and rollback** (no partial writes)

✅ Useful for **financial apps, inventory systems, and multi-step updates.**

> ⚠️ Transactions **require MongoDB replica set** (local or Atlas) and MongoDB 4.0+

---

## ✅ Example Use Case: Bank Transfer

Transfer ₹100 from `User A` to `User B`.

---

### 🔹 Setup: Start a Session

```js
const session = await mongoose.startSession();
session.startTransaction();
```

---

### 🔹 Example Code:

```js
try {
  const session = await mongoose.startSession();
  session.startTransaction();

  const opts = { session };

  const userA = await User.findById('A_ID');
  const userB = await User.findById('B_ID');

  if (userA.balance < 100) throw new Error('Insufficient balance');

  userA.balance -= 100;
  userB.balance += 100;

  await userA.save(opts);
  await userB.save(opts);

  await session.commitTransaction(); // ✅ all good
  session.endSession();

  console.log('Transaction success!');
} catch (err) {
  await session.abortTransaction(); // ❌ rollback everything
  session.endSession();
  console.error('Transaction failed:', err);
}
```

---

### 🔹 Where You Might Use Transactions

| Scenario                | Why Use Transactions?                      |
| ----------------------- | ------------------------------------------ |
| E-commerce orders       | Deduct stock, charge payment, create order |
| Bank/accounting systems | Debit from one, credit another             |
| Multi-model updates     | Update two collections in sync             |
| Complex workflows       | All or nothing logic                       |

---

### 🔸 Important Notes

* Use **`{ session }`** in all queries inside the transaction
* If **any** operation fails, call `abortTransaction()` to roll everything back
* Always `endSession()` after `commit` or `abort`

---

### 🔧 Mongoose Model Operations Inside Transaction

```js
await Model.create([doc1, doc2], { session });
await model.save({ session });
await Model.updateOne({}, {}, { session });
```

---

## ✅ **6.9. Lean Queries (`.lean()`)**

---

### 🔸 What is `.lean()` in Mongoose?

`.lean()` tells Mongoose to **skip attaching Mongoose document features** (like getters, setters, methods, and virtuals) and instead return **plain JavaScript objects**.

This makes queries **faster and lighter**, especially when you're just reading data (e.g., for APIs or reports).

---

### 🔍 Why Use `.lean()`?

| Without `.lean()`                | With `.lean()`                   |
| -------------------------------- | -------------------------------- |
| Returns full Mongoose document   | Returns plain JS object          |
| Has `.save()`, virtuals, methods | No virtuals, no document methods |
| More memory and processing       | Better performance               |

---

### ✅ Example:

```js
// Without lean (default)
const user1 = await User.findById(id);
console.log(typeof user1); // object with Mongoose document methods
console.log(user1 instanceof mongoose.Document); // true

// With lean
const user2 = await User.findById(id).lean();
console.log(typeof user2); // plain object
console.log(user2 instanceof mongoose.Document); // false
```

---

### ✅ When to Use `.lean()`

* Read-only API responses
* Performance-critical queries
* Large result sets
* Static pages, dashboards

---

### ⚠️ Warnings

* You can’t use `.save()` on `.lean()` results
* Virtuals won’t work unless explicitly handled
* Middleware, getters/setters, schema methods won’t apply

---

### ✅ Combine with `.populate()` (Yes, it's supported!)

```js
Post.find().populate('author').lean();
```

✅ You get a plain object with populated fields — ideal for frontend consumption.

---

### 🧠 Tip: Use `.lean()` **only** when you don't need document features (e.g., for sending JSON to frontend).

---
