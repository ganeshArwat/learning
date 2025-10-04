## ✅ **6.10. Aggregation Framework Basics in Mongoose**

---

### 🔸 What is the Aggregation Framework?

The **MongoDB Aggregation Framework** allows you to **process data records** and return computed results — like `GROUP BY`, `JOIN`, `FILTER`, and `SORT` in SQL.

In Mongoose, we use:

```js
Model.aggregate(pipelineArray);
```

---

### ✅ Real-World Use Cases

| Use Case                 | Example                                    |
| ------------------------ | ------------------------------------------ |
| Grouping and counting    | Count posts per user                       |
| Filtering and projecting | Get only active users with selected fields |
| Joining collections      | Lookup authors for posts                   |
| Calculations             | Average price, total sales                 |

---

## 🔧 Basic Aggregation Pipeline Stages

| Stage      | Description                             |
| ---------- | --------------------------------------- |
| `$match`   | Filters documents (like `where`)        |
| `$project` | Selects/reshapes fields                 |
| `$group`   | Groups documents (like `GROUP BY`)      |
| `$sort`    | Sorts documents                         |
| `$limit`   | Limits number of results                |
| `$lookup`  | Performs a join with another collection |
| `$unwind`  | Flattens arrays                         |

---

### ✅ Example: Count Posts per User

```js
Post.aggregate([
  {
    $group: {
      _id: "$author", // group by author id
      totalPosts: { $sum: 1 },
    },
  },
  {
    $sort: { totalPosts: -1 },
  },
]);
```

---

### ✅ Example: Filter + Project Specific Fields

```js
User.aggregate([
  { $match: { status: "active" } },
  { $project: { name: 1, email: 1, _id: 0 } },
]);
```

---

### ✅ Example: Join (Populate-like) using `$lookup`

```js
Post.aggregate([
  {
    $lookup: {
      from: "users", // target collection
      localField: "author", // in Post
      foreignField: "_id", // in User
      as: "authorDetails",
    },
  },
  {
    $unwind: "$authorDetails",
  },
  {
    $project: {
      title: 1,
      "authorDetails.name": 1,
    },
  },
]);
```

> This acts like `.populate()`, but more customizable and powerful.

---

## 🧠 Tips:

- Aggregation is powerful but **can be slower** than `.find()` for simple queries
- It works **outside of Mongoose schema logic** (no validation/methods)
- You can use it with `.exec()` like other Mongoose queries

---

## ✅ **Detailed Guide to Aggregation Framework in Mongoose**

---

### 🔸 What is an Aggregation Pipeline?

A **series of stages** that transform documents.
Each stage takes input from the previous stage, processes it, and passes it to the next stage.

```js
Model.aggregate([
  { stage1 },
  { stage2 },
  ...
]);
```

---

## 🔧 Common Aggregation Stages with Examples

---

### 1️⃣ **`$match`** – Filtering (like `.find()`)

```js
{
  $match: {
    status: "active";
  }
}
```

📌 Filters only documents with `status: 'active'`.

---

### 2️⃣ **`$project`** – Shape the output

```js
{
  $project: {
    name: 1,
    email: 1,
    _id: 0,
    isAdmin: { $eq: ['$role', 'admin'] } // computed field
  }
}
```

📌 Pick specific fields, rename, or compute new ones.

---

### 3️⃣ **`$group`** – Group and Aggregate (like SQL `GROUP BY`)

```js
{
  $group: {
    _id: '$author',
    totalPosts: { $sum: 1 },             // count
    avgLength: { $avg: '$contentLength' } // average
  }
}
```

📌 Groups by `author` and calculates number of posts & average length.

---

### 4️⃣ **`$sort`** – Sorting

```js
{
  $sort: {
    createdAt: -1;
  }
}
```

📌 Sorts results by `createdAt` in descending order.

---

### 5️⃣ **`$limit` and `$skip`** – Pagination

```js
{ $skip: 10 },
{ $limit: 5 }
```

📌 Skip first 10 docs and limit to next 5 — for pagination.

---

### 6️⃣ **`$lookup`** – Join/Reference (like SQL JOIN)

```js
{
  $lookup: {
    from: 'users',             // target collection (must be in lowercase)
    localField: 'author',      // Post.author
    foreignField: '_id',       // User._id
    as: 'authorInfo'
  }
}
```

📌 Joins `Post` with `User` collection using ObjectId.

---

### 7️⃣ **`$unwind`** – Flatten Arrays

```js
{
  $unwind: "$authorInfo";
}
```

📌 Converts an array (`authorInfo`) into multiple documents.

---

### 8️⃣ **`$addFields`** – Add computed fields

```js
{
  $addFields: {
    isPublished: {
      $eq: ["$status", "published"];
    }
  }
}
```

📌 Adds a new field based on logic.

---

## 🧪 Real-Life Example: Posts with Author Info

```js
Post.aggregate([
  { $match: { status: "published" } },
  {
    $lookup: {
      from: "users",
      localField: "author",
      foreignField: "_id",
      as: "authorInfo",
    },
  },
  { $unwind: "$authorInfo" },
  {
    $project: {
      title: 1,
      content: 1,
      "authorInfo.name": 1,
      "authorInfo.email": 1,
    },
  },
]);
```

---

## 🧠 Pro Tips

| Tip                             | Why It Matters                              |
| ------------------------------- | ------------------------------------------- |
| Use indexes with `$match` early | Improves performance                        |
| Avoid unnecessary `$unwind`     | It duplicates docs, can increase load       |
| Use `.exec()` for chaining      | Makes your pipeline work like other queries |
| Don't overuse `$lookup`         | Expensive on large datasets                 |

---

## 📊 Use Cases

| Use Case                  | Stages You’ll Use               |
| ------------------------- | ------------------------------- |
| Total orders per user     | `$group`, `$lookup`, `$project` |
| Active users in last week | `$match`, `$sort`, `$limit`     |
| Dashboard charts          | `$group`, `$project`, `$sort`   |
| Search with relevance     | `$match`, `$project`, `$text`   |

---

## ✅ **6.11. Discriminators (Schema Inheritance) in Mongoose**

---

### 🔸 What Are Discriminators?

**Discriminators** in Mongoose let you create **sub-models** (child schemas) based on a **base model**, allowing schema inheritance.

✅ Ideal when:

- You have a **shared base structure** (like a `User` model)
- But want to define **specialized schemas** (like `Admin`, `Customer`)

---

### ✅ Real-World Example

Let’s say you have a `User` model, but want to differentiate between:

- **Admin users**
- **Customer users**

Both have `name` and `email`, but Admins also have `accessLevel`, while Customers have `membershipType`.

---

## 🔧 Step-by-Step: Discriminator Example

### 1️⃣ Base Schema

```js
const mongoose = require("mongoose");

const baseOptions = {
  discriminatorKey: "__type", // adds __type field in documents
  collection: "users", // all discriminators share same collection
};

const userSchema = new mongoose.Schema(
  {
    name: String,
    email: String,
  },
  baseOptions
);

const User = mongoose.model("User", userSchema);
```

---

### 2️⃣ Admin Schema

```js
const Admin = User.discriminator(
  "Admin",
  new mongoose.Schema({
    accessLevel: Number,
  })
);
```

---

### 3️⃣ Customer Schema

```js
const Customer = User.discriminator(
  "Customer",
  new mongoose.Schema({
    membershipType: String,
  })
);
```

---

### 4️⃣ Creating Documents

```js
const admin = await Admin.create({
  name: "Ganesh",
  email: "g@a.com",
  accessLevel: 5,
});
const customer = await Customer.create({
  name: "Ravi",
  email: "r@b.com",
  membershipType: "Gold",
});
```

➡️ Both are saved in the **same `users` collection**, but with a special `__type` field.

---

### 5️⃣ Querying Documents

```js
const users = await User.find(); // returns all types
const admins = await Admin.find(); // only Admins
const customers = await Customer.find(); // only Customers
```

---

### 🧠 Benefits of Discriminators

| Benefit                 | Description                         |
| ----------------------- | ----------------------------------- |
| Schema inheritance      | Shared structure with custom fields |
| Polymorphic collections | All types in one collection         |
| Clean separation        | Still query by subtype easily       |

---

### ⚠️ Limitations

- Can’t use discriminators across **multiple collections**
- Can't change discriminator type after creation
- Best for **read-heavy** use cases with clear hierarchy

---

## ✅ **6.12. Mongoose Plugins**

---

### 🔸 What Are Mongoose Plugins?

Mongoose **plugins** are reusable blocks of schema logic that can be shared across multiple models.

They allow you to:

- Add **custom behavior** (methods, hooks, validations)
- Apply **reusable logic** (timestamps, soft deletes, slugs, etc.)
- Keep code DRY and modular

---

### ✅ How to Create a Plugin

A plugin is just a function that takes:

```js
function myPlugin(schema, options) {
  // Add a field
  schema.add({ createdBy: String });

  // Add a method
  schema.methods.getCreatedBy = function () {
    return this.createdBy;
  };
}
```

---

### ✅ How to Use a Plugin

```js
const userSchema = new mongoose.Schema({
  name: String,
});

userSchema.plugin(myPlugin); // ⬅️ apply plugin to schema

const User = mongoose.model("User", userSchema);
```

---

### ✅ Popular Plugin Examples

---

#### 1️⃣ **Timestamps Plugin (built-in)**

```js
const schema = new mongoose.Schema({ name: String }, { timestamps: true });
```

⏰ Adds `createdAt` and `updatedAt` automatically.

---

#### 2️⃣ **Mongoose Slug Plugin**

Automatically generates slugs from fields (e.g., blog titles).

```bash
npm install mongoose-slug-generator
```

```js
const slug = require("mongoose-slug-generator");
mongoose.plugin(slug);

const blogSchema = new mongoose.Schema({
  title: String,
  slug: { type: String, slug: "title", unique: true },
});
```

---

#### 3️⃣ **Soft Delete Plugin (e.g., `mongoose-delete`)**

```bash
npm install mongoose-delete
```

```js
const mongooseDelete = require("mongoose-delete");
schema.plugin(mongooseDelete, { overrideMethods: "all" });
```

Adds `.delete()`, `.restore()`, and hides soft-deleted docs by default.

---

#### 4️⃣ **Custom Plugin Example: Track Updated By**

```js
function trackUpdatedBy(schema) {
  schema.add({ updatedBy: String });

  schema.pre("save", function (next) {
    this.updatedBy = "admin"; // or get from auth context
    next();
  });
}
schema.plugin(trackUpdatedBy);
```

---

### 🧠 Why Use Plugins?

| Reason                    | Benefit                        |
| ------------------------- | ------------------------------ |
| Reusability               | Share across multiple schemas  |
| Separation of concerns    | Keep schemas clean             |
| Third-party functionality | Leverage open-source solutions |

---

## ✅ **6.13. Soft Delete Strategy in Mongoose**

---

### 🔸 What is Soft Delete?

A **soft delete** doesn't remove the document from the database. Instead, it **marks it as deleted** using a flag (e.g., `isDeleted: true`).

✅ Useful when:

- You want to **undo deletion** (restore)
- You need **deletion history or audit trail**
- You want to **prevent data loss**

---

### 🔧 How to Implement Soft Delete Manually

---

### 1️⃣ Add `isDeleted` Field to Schema

```js
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  isDeleted: {
    type: Boolean,
    default: false,
  },
});
```

---

### 2️⃣ Override `find()` Queries to Exclude Deleted

```js
userSchema.pre(/^find/, function (next) {
  this.where({ isDeleted: false });
  next();
});
```

Now, every `find`, `findOne`, `findById` will automatically **exclude soft-deleted records**.

---

### 3️⃣ Create a Soft Delete Method

```js
userSchema.methods.softDelete = function () {
  this.isDeleted = true;
  return this.save();
};
```

---

### 4️⃣ Restore a Soft Deleted Document

```js
userSchema.methods.restore = function () {
  this.isDeleted = false;
  return this.save();
};
```

---

### ✅ Example Usage:

```js
const user = await User.findById(userId);
await user.softDelete(); // marks as deleted

const activeUsers = await User.find(); // soft-deleted user excluded
```

---

## 🛠 OR Use a Plugin: `mongoose-delete`

```bash
npm install mongoose-delete
```

### Usage:

```js
const mongooseDelete = require("mongoose-delete");

userSchema.plugin(mongooseDelete, { deletedAt: true, overrideMethods: "all" });
```

### Now you can:

| Method                         | Description             |
| ------------------------------ | ----------------------- |
| `.delete()`                    | Soft delete             |
| `.restore()`                   | Restore deleted record  |
| `.find()`                      | Excludes deleted docs   |
| `.findWithDeleted()`           | Includes deleted docs   |
| `.countDocumentsWithDeleted()` | Count including deleted |

---

## 🧠 Benefits of Soft Delete

| Advantage               | Why It Matters                     |
| ----------------------- | ---------------------------------- |
| Prevent accidental loss | Easy to restore mistakenly deleted |
| Audit support           | Retain who/when deleted            |
| Analytics & reporting   | Include deleted users/orders       |

---

## ✅ **6.14. Performance Tips in Mongoose**

Performance tuning is critical for scaling your application. Below are the best practices you should know and apply in real-world Mongoose projects.

---

### 🔸 1. Use `.lean()` for Read-Only Queries

```js
User.find().lean();
```

✅ Returns plain JS objects
✅ Skips Mongoose overhead (getters, methods, virtuals)
⚠️ Avoid if you need document methods or middleware.

---

### 🔸 2. Limit `.populate()` Usage

* `.populate()` performs extra queries behind the scenes.
* Use **only when necessary** and **select only required fields**.

```js
Post.find().populate('author', 'name email').lean();
```

✅ Prefer `.lean()` with `.populate()` to reduce memory usage.

---

### 🔸 3. Index Your Queries

Use indexes on frequently searched, filtered, or sorted fields.

```js
userSchema.index({ email: 1 }); // for login or unique email lookups
```

✅ Always index foreign keys used in `.populate()` references.

📌 Check your indexes:

```js
db.collection.getIndexes();
```

---

### 🔸 4. Use Projections to Fetch Only What You Need

```js
User.find({}, 'name email'); // only name & email
```

✅ Reduces payload and improves query speed.

---

### 🔸 5. Avoid Large Document Sizes

* MongoDB has a **16 MB document limit**.
* Keep nested arrays small (e.g., don’t embed thousands of items).
* Prefer referencing when related data grows large.

---

### 🔸 6. Batch Queries or Use Pagination

Use `.limit()` and `.skip()` for paging large datasets.

```js
User.find().skip(20).limit(10);
```

✅ Prevents memory overload on large collections.

---

### 🔸 7. Use Aggregation for Complex Reports (not `.populate()`)

For performance-critical analytics, use `aggregate()` instead of chained `.populate()` and `.map()`.

---

### 🔸 8. Disable `autoIndex` in Production

```js
mongoose.connect(uri, { autoIndex: false });
```

✅ Speeds up app start time and prevents index conflicts.

---

## 🚀 Summary of Performance Tips

| Tip                       | Why Use It                          |
| ------------------------- | ----------------------------------- |
| `.lean()`                 | Fast reads, less memory             |
| Indexes                   | Speed up queries and population     |
| `.select()` / Projections | Minimize returned data              |
| Limit `.populate()`       | Avoid unnecessary joins             |
| Use pagination            | Prevent huge memory loads           |
| Use aggregation wisely    | For optimized complex data handling |

---