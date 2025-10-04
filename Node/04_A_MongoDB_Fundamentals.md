## ✅ **4.1 What is NoSQL? Why MongoDB?**

### 🔹 What is NoSQL?

**NoSQL** stands for **“Not Only SQL”**. It refers to **non-relational databases** that store data in a format other than traditional tabular (rows and columns).

There are 4 main types of NoSQL databases:

1. **Document-based** (e.g., MongoDB)
2. **Key-Value Stores** (e.g., Redis)
3. **Column-based** (e.g., Cassandra)
4. **Graph-based** (e.g., Neo4j)

---

### 🔹 Why MongoDB?

MongoDB is the most popular **document-oriented** NoSQL database. Here's why developers love it:

| Feature                         | Description                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- |
| 🔸 **Schema-less**              | No need to define the schema strictly; documents in a collection can have different structures. |
| 🔸 **JSON-like format**         | Stores data in **BSON** (Binary JSON) format. Easy to read and write.                           |
| 🔸 **High performance**         | Great for large-scale applications.                                                             |
| 🔸 **Scalability**              | Easy to scale horizontally with replica sets and sharding.                                      |
| 🔸 **Integration with Node.js** | Very smooth using libraries like **Mongoose**.                                                  |

---

### 🧠 Real-Life Example:

Relational DB (SQL):

```sql
SELECT * FROM users WHERE name = 'Ganesh';
```

NoSQL (MongoDB):

```js
db.users.find({ name: "Ganesh" });
```

---

## ✅ **4.1.1 NoSQL vs SQL (Relational vs Non-Relational Databases)**

| Feature                | **SQL (Relational DB)**                                     | **NoSQL (Non-Relational DB)**                                                |
| ---------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 🔸 **Data Model**      | Structured (tables with rows & columns)                     | Semi-structured or unstructured (JSON, key-value, graph, etc.)               |
| 🔸 **Schema**          | Fixed schema (predefined structure)                         | Schema-less or dynamic                                                       |
| 🔸 **Storage Unit**    | Tables                                                      | Collections (contain documents)                                              |
| 🔸 **Query Language**  | SQL (Structured Query Language)                             | Custom queries (like MongoDB Query Language)                                 |
| 🔸 **Joins**           | Supports complex joins between tables                       | Doesn’t support joins natively (use **embedding** or **manual referencing**) |
| 🔸 **Scalability**     | Vertically scalable (stronger server)                       | Horizontally scalable (add more servers)                                     |
| 🔸 **ACID Compliance** | Strong ACID (Atomicity, Consistency, Isolation, Durability) | BASE (Basically Available, Soft state, Eventually consistent)                |
| 🔸 **Best For**        | Complex transactions, strict consistency (e.g., banking)    | Fast access, flexible data, large-scale apps (e.g., social media, chat apps) |

---

## 🔧 Example Comparison

### SQL Table:

```sql
Table: Users
➕----➕--------➕-------➕
| id | name   | age   |
➕----➕--------➕-------➕
| 1  | Ganesh | 23    |
```

### MongoDB Document:

```js
{
  _id: ObjectId("..."),
  name: "Ganesh",
  age: 23
}
```

---

## 🧠 Use Cases

| Use Case                                         | Recommended        |
| ------------------------------------------------ | ------------------ |
| Banking, ERPs, HR systems                        | ✅ SQL             |
| Real-time analytics, IoT apps, social media apps | ✅ NoSQL (MongoDB) |
| You need dynamic schema and fast iteration       | ✅ NoSQL           |
| You need normalized data and relationships       | ✅ SQL             |

---

## 🎯 In MERN Stack?

- MERN uses **MongoDB** because:

  - JSON format flows naturally from **frontend → backend → DB**.
  - Flexible schema fits well with fast-paced development.
  - Scales easily with microservices or serverless architectures.

---

## ✅ **4.2 Documents vs Collections**

### 🔹 **What is a Document?**

In MongoDB, a **document** is the basic unit of data.
It is a JSON-like object (actually stored as BSON = Binary JSON).

Think of a document like a **row** in SQL, but with more flexibility.

### ✅ Example of a MongoDB Document:

```json
{
  "_id": "507f191e810c19729de860ea",
  "name": "Ganesh",
  "age": 23,
  "skills": ["JavaScript", "React", "MongoDB"],
  "isActive": true
}
```

- `"_id"`: A unique identifier automatically created by MongoDB.
- Data types: strings, numbers, arrays, booleans, nested objects, etc.

---

### 🔹 **What is a Collection?**

A **collection** is a group of documents — similar to a **table** in SQL.

But unlike SQL, **documents in a collection don’t need to have the same fields or structure**.

### ✅ Example:

```js
db.users.insertMany([
  { name: "Ganesh", age: 23 },
  { name: "Rahul", age: 25, location: "Mumbai" },
]);
```

- Both are in the `users` collection.
- Different structure? No problem in MongoDB.

---

## 🔁 SQL vs MongoDB Analogy:

| SQL Concept | MongoDB Equivalent     |
| ----------- | ---------------------- |
| Database    | Database               |
| Table       | Collection             |
| Row         | Document               |
| Column      | Field                  |
| Primary Key | `_id` (auto-generated) |

---

## 📘 Real-life Example:

Imagine a `products` collection:

```js
{
  name: "T-Shirt",
  price: 499,
  sizes: ["S", "M", "L"],
  inStock: true
}

{
  name: "Shoes",
  brand: "Nike",
  price: 2999
}
```

- Both are part of the `products` collection.
- The schema is flexible and changes as per need.

---

## ✅ **4.3 MongoDB Installation or Using MongoDB Atlas**

You have **two main ways** to use MongoDB:

---

### 🔹 **Option 1: Install MongoDB Locally**

#### 🔧 Steps:

1. Go to [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
2. Download the **MongoDB Community Server** for your OS.
3. Install it along with **MongoDB Compass** (GUI tool).
4. Add MongoDB to your system’s `PATH` (installer usually handles this).
5. Start the MongoDB server:

   ```bash
   mongod
   ```

6. Open a new terminal and connect to it:

   ```bash
   mongo
   ```

#### ✅ Pros:

- Works offline
- Good for learning and local testing

#### ❌ Cons:

- Needs manual updates and local resources
- Not ideal for team collaboration

---

### 🔹 **Option 2: Use MongoDB Atlas (Cloud-based)**

#### 🧑‍💻 What is Atlas?

MongoDB Atlas is a **cloud database platform** offered by MongoDB Inc.

You can **host, manage, and scale MongoDB databases in the cloud** without installing anything locally.

#### 🌐 Steps to Use MongoDB Atlas:

1. Go to [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Sign up (free tier available)
3. Create a new **Cluster**
4. Choose:

   - Cloud provider (AWS, GCP, or Azure)
   - Region (choose nearby location like Mumbai)

5. Create a **Database User** with a password
6. Add **IP Whitelist** (e.g., `0.0.0.0` for all IPs during dev)
7. Click **Connect > Connect your application**
8. Copy the **Connection String** (e.g., `mongodb➕srv://<username>:<password>@cluster.mongodb.net/myDB`)
9. Use it in your Node.js/Mongoose app like this:

   ```js
   mongoose.connect("your_connection_string_here");
   ```

#### ✅ Pros:

- No local setup
- Easy sharing and collaboration
- Free-tier cluster is enough for learning/dev

#### ❌ Cons:

- Needs internet
- Requires account/login

---

## 🧠 Summary

| Feature  | MongoDB Local   | MongoDB Atlas            |
| -------- | --------------- | ------------------------ |
| Setup    | Needs download  | Browser-based            |
| Storage  | On your machine | On the cloud             |
| Access   | Only local      | Global (if IP allowed)   |
| Best for | Solo devs       | Team/collab & deployment |

---

## ✅ **4.4 CRUD Operations using MongoDB Shell**

CRUD stands for:

- **C** → Create
- **R** → Read
- **U** → Update
- **D** → Delete

These are the basic operations you perform on a database.

We'll use the **MongoDB Shell** (`mongo` or `mongosh`) to perform these operations.

---

## 🔧 Setup: Open Mongo Shell

If you installed MongoDB locally, open your terminal and type:

```bash
mongosh
```

Once inside the shell, select or create a database:

```js
use myDatabase
```

---

## 🔸 1. CREATE → `insertOne()` / `insertMany()`

```js
// Insert one document
db.users.insertOne({
  name: "Ganesh",
  age: 23,
  city: "Mumbai",
});

// Insert many documents
db.users.insertMany([
  { name: "Rahul", age: 25 },
  { name: "Pooja", age: 24 },
]);
```

---

## 🔸 2. READ → `find()` / `findOne()`

```js
// Find all users
db.users.find();

// Find users with age 25
db.users.find({ age: 25 });

// Find one user
db.users.findOne({ name: "Ganesh" });
```

---

## 🔸 3. UPDATE → `updateOne()` / `updateMany()` / `$set`

```js
// Update age of Ganesh
db.users.updateOne({ name: "Ganesh" }, { $set: { age: 24 } });

// Update all users with age 25 to age 26
db.users.updateMany({ age: 25 }, { $set: { age: 26 } });
```

---

## 🔸 4. DELETE → `deleteOne()` / `deleteMany()`

```js
// Delete one user
db.users.deleteOne({ name: "Ganesh" });

// Delete all users with age 26
db.users.deleteMany({ age: 26 });
```

---

## 📘 Bonus Commands:

```js
// Show all databases
show dbs

// Show current database
db

// Show collections in current DB
show collections
```

---

## 🧪 Practice Tip:

Try this mini exercise in your Mongo shell:

1. `use testDB`
2. `db.books.insertMany([{title: "Book A", price: 199}, {title: "Book B", price: 299}])`
3. `db.books.find()`
4. `db.books.updateOne({title: "Book A"}, {$set: {price: 249}})`
5. `db.books.deleteOne({title: "Book B"})`

---

## ✅ **4.5 MongoDB Compass (GUI Tool)**

### 🔹 What is MongoDB Compass?

**MongoDB Compass** is the **official GUI (Graphical User Interface)** for MongoDB.
It helps you **visually explore, query, and manage** your MongoDB databases — without writing shell commands.

---

### ✅ Why Use Compass?

| Feature                       | Benefit                                                |
| ----------------------------- | ------------------------------------------------------ |
| 🔍 Visual DB Browser          | View collections and documents without typing commands |
| 🧩 Schema Analysis            | Automatically analyzes schema structure                |
| 🔧 Visual CRUD                | Easily insert, edit, and delete documents              |
| 📊 Index/Performance Insights | See indexes and slow queries                           |
| 🔎 Built-in Query Builder     | Filter and sort documents visually                     |

---

### 🔧 Installation Steps

1. Go to [https://www.mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass)
2. Download Compass for your OS (Windows/Linux/Mac)
3. Install it just like any app

---

### 🔌 Connecting to MongoDB

#### 👉 Local MongoDB:

- Connection string:

  ```
  mongodb://localhost:27017
  ```

#### 👉 MongoDB Atlas:

- Copy your connection string from Atlas:

  ```
  mongodb➕srv://<username>:<password>@cluster0.mongodb.net/myDB
  ```

- Paste it in Compass under **"New Connection"**

---

### 🖥️ Using MongoDB Compass (UI Overview)

Once connected, you can:

🔸 **See all databases and collections**

🔸 Click any **collection** to:

- View documents
- Apply filters (e.g., `{ name: "Ganesh" }`)
- Add/Edit/Delete documents visually
- View schema summary (field names & types)
- Manage indexes

---

### 🧪 Quick Practice

1. Open Compass
2. Connect to your local or Atlas DB
3. Create a new database:

   - Name: `learningDB`
   - Collection: `students`

4. Insert this document:

   ```json
   {
     "name": "Ganesh",
     "age": 23,
     "course": "MERN Stack"
   }
   ```

5. Explore filtering:
   `{ age: { $gt: 20 } }`

---

## ✅ **4.6 Database Design: Embedding vs Referencing**

When designing a MongoDB schema, especially in MERN applications, you often have to decide:

> Should I **embed** related data inside a document or **reference** it from another document?

---

## 🔹 1. **Embedding**

### 👉 What is it?

Storing related data **within the same document**.

### ✅ Best For:

- One-to-few or one-to-one relationships
- Data that is always fetched together

### ✅ Example: Blog Post with embedded comments

```js
{
  title: "Intro to MERN",
  author: "Ganesh",
  comments: [
    { user: "Pooja", text: "Great post!" },
    { user: "Rahul", text: "Thanks!" }
  ]
}
```

### ✅ Pros:

- Fast reads (no need for multiple queries)
- Easier to update together

### ❌ Cons:

- Document size limit (16MB)
- Redundant data if reused elsewhere

---

## 🔹 2. **Referencing**

### 👉 What is it?

Storing **only the ObjectId** of related documents.

### ✅ Best For:

- One-to-many or many-to-many
- When related data is large or shared across documents

### ✅ Example: Blog Post referencing comments

**Post Document:**

```js
{
  title: "Intro to MERN",
  author: "Ganesh",
  comments: [ObjectId("123"), ObjectId("456")]
}
```

**Comment Document:**

```js
{
  _id: ObjectId("123"),
  user: "Pooja",
  text: "Great post!"
}
```

### ✅ Pros:

- Avoids duplication
- Flexible for large or shared datasets

### ❌ Cons:

- Requires **joins manually** using `populate()` in Mongoose
- Slower reads due to multiple queries

---

## 📊 Summary Table

| Feature            | Embedding              | Referencing               |
| ------------------ | ---------------------- | ------------------------- |
| Relationship       | One-to-few, one-to-one | One-to-many, many-to-many |
| Speed              | Faster reads           | Slower (multiple queries) |
| Flexibility        | Less flexible          | More flexible             |
| Redundancy         | High                   | Low                       |
| Document size risk | Yes                    | No                        |
| Mongoose Support   | Easy to use            | Use `populate()`          |

---

## 🧠 Design Tip for MERN Stack

- Use **embedding** when the child data will always be accessed with the parent.
- Use **referencing** when:

  - Child data is large
  - Shared by many documents
  - Accessed independently

---

## MongoDB Cheetsheet

### Terminology

#### 🔸 **Database**:

- A container for collections. This is the same as a database in SQL and
  usually each project will have its own database full of different collections.

#### 🔸 **Collection**:

- A grouping of documents inside of a database. This is the same as a table in
  SQL and usually each type of data (users, posts, products) will have its own
  collection.

#### 🔸 **Document**:

- A record inside of a collection. This is the same as a row in SQL and usually
  there will be one document per object in the collection. A document is also
  essentially just a JSON object.

#### 🔸 **Field**:

- A key value pair within a document. This is the same as a column in SQL.
  Each document will have some number of fields that contain information
  such as name, address, hobbies, etc. An important difference between SQL
  and MongoDB is that a field can contain values such as JSON objects, and
  arrays instead of just strings, number, booleans, etc.

---

### Basic commands

#### 🔸 `mongosh` :

- Open a connection to your local MongoDB instance. All other commands
  will be run within this mongosh connection.

#### 🔸 `show dbs` :

- Show all databases in the current MongoDB instance

#### 🔸 `use <dbname>` :

```
use myDatabase
```

- Switch to the database provided by dbname
- Switch to myDatabase

#### 🔸 `db` :

- Show current database name

#### 🔸 `cls` :

- Clear the terminal screen

#### 🔸 `show collections` :

- Show all collections in the current database

#### 🔸 `db.dropDatabase()` :

- Delete the current database

#### 🔸 `exit` :

- exit Exit the mongosh session

---

### Create

- Each of these commands is run on a specific collection
- `db.<collectionName>.<command>`

#### ➕ inserOne

- Create a new document inside the specified collection

```js
// Add a new document with the name of Kyle into the users collection
db.users.insertOne({ name: “Kyle” })
```

#### ➕ insertMany

- Create multi new documents inside a specific collection

```js
// Add two new documents with the age of 26 and 20 into the users collection
db.users.insertMany([{ age: 26 }, { age: 20 }]);
```

---

### Read

- Each of these commands is run on a specific collection
- `db.<collectionName>.<command>`

#### ➕ find

- Get All Documents

```js
// Get all documents in the users collection
db.users.find();
```

#### ➕ find(<filterObject>)

- Find all documents that match the filter object

```js
// Get all users with the name Kyle
db.users.find({ name: “Kyle” })

// Get all users whose adress field has a street field with the value 123 Main St
db.users.find({ “address.street”: “123 Main St” })
```

#### ➕ findOne

- The same as find, but only return the first document that matches the filter object

```js
// Get the first user with the name Kyle
db.users.findOne({ name: “Kyle” })
```

#### ➕ countDocuments

- Return the count of the documents that match the filter object passed to it

```js
// Get the number of users with the name Kyle
db.users.countDocuments({ name: “Kyle” })
```

---

### Update

- Each of these commands is run on a specific collection
- `db.<collectionName>.<command>`

#### ➕ updateOne

- Update the first document that matches the filter object with the data passed into the second parameter which is the update object

```js
// Update the first user with an age of 20 to the age of 21
db.users.updateOne({ age: 20 }, { $set: { age: 21 } });
```

#### ➕ updateMany

- Update all documents that matches the filter object with the data passed into the second parameter which is the update object

```js
// Update all users with an age of 12 by adding 3 to their age
db.users.updateMany({ age: 12 }, { $inc: { age: 3 } });
```

#### ➕ replaceOne

- Replace the **first document** that matches the filter with a new object.
- ⚠️ This **overwrites** the entire document (not just specific fields).

```js
// Replace the first user with age 12 with a new object having only age 13
db.users.replaceOne({ age: 12 }, { age: 13 });
```

---

### Delete

- Each of these commands is run on a specific collection
- `db.<collectionName>.<command>`

#### ❌ `deleteOne`

- Delete the **first document** that matches the filter object.

```js
// Delete the first user with an age of 20
db.users.deleteOne({ age: 20 });
```

#### ❌ `deleteMany`

- Delete **all documents** that match the filter object.

```js
// Delete all users with an age of 12
db.users.deleteMany({ age: 12 });
```

---

### 🔎 Complex Filter Object

Any combination of the following operators can be used inside a filter object to create complex queries.

#### 🟢 `$eq`

- Check for **equality**.

```js
// Get all users with the name Kyle
db.users.find({ name: { $eq: "Kyle" } });
```

#### 🔴 `$ne`

- Check for **not equal**.

```js
// Get all users with a name other than Kyle
db.users.find({ name: { $ne: "Kyle" } });
```

#### 🔼 `$gt` / `$gte`

- Check for **greater than** / **greater than or equal to**.

```js
// Get all users with age greater than 12
db.users.find({ age: { $gt: 12 } });

// Get all users with age greater than or equal to 15
db.users.find({ age: { $gte: 15 } });
```

#### 🔽 `$lt` / `$lte`

- Check for **less than** / **less than or equal to**.

```js
// Get all users with age less than 12
db.users.find({ age: { $lt: 12 } });

// Get all users with age less than or equal to 15
db.users.find({ age: { $lte: 15 } });
```

#### 📥 `$in`

- Check if a value is **in** a list of values.

```js
// Get all users with name Kyle or Mike
db.users.find({ name: { $in: ["Kyle", "Mike"] } });
```

#### 📤 `$nin`

- Check if a value is **not in** a list of values.

```js
// Get all users who do NOT have the name Kyle or Mike
db.users.find({ name: { $nin: ["Kyle", "Mike"] } });
```

#### ➕  `$and`

- All conditions must be **true**.

```js
// Get all users with age 12 and name Kyle
db.users.find({ $and: [{ age: 12 }, { name: "Kyle" }] });

// Alternative (simpler syntax)
db.users.find({ age: 12, name: "Kyle" });
```

#### 🔀 `$or`

- At least one condition must be **true**.

```js
// Get all users with name Kyle or age 12
db.users.find({ $or: [{ age: 12 }, { name: "Kyle" }] });
```

#### ❗ `$not`

- **Negate** the condition.

```js
// Get all users whose name is NOT Kyle
db.users.find({ name: { $not: { $eq: "Kyle" } } });
```

#### 🔍 `$exists`

- Check if a field **exists**.

```js
// Get all users that have a 'name' field
db.users.find({ name: { $exists: true } });
```

#### ⚖️ `$expr`

- Compare **fields within the same document**.

```js
// Get all users where balance is greater than debt
db.users.find({ $expr: { $gt: ["$balance", "$debt"] } });
```

---

### 🔧 Complex Update Object

These operators are used inside the **update object** to perform advanced updates. You can combine multiple operators in a single update.

#### 🔁 `$set`

* Set (or update) specific fields without affecting others.

```js
// Update the name of the first user with age 12 to "Hi"
db.users.updateOne(
  { age: 12 },
  { $set: { name: "Hi" } }
)
```

#### ➕  `$inc`

* Increment a field's numeric value.

```js
// Add 2 to the age of the first user with age 12
db.users.updateOne(
  { age: 12 },
  { $inc: { age: 2 } }
)
```

#### 🏷️ `$rename`

* Rename a field in documents.

```js
// Rename the 'age' field to 'years' for all users
db.users.updateMany(
  {},
  { $rename: { age: "years" } }
)
```

#### ❌ `$unset`

* Remove a field from documents.

```js
// Remove the 'age' field from the first user with age 12
db.users.updateOne(
  { age: 12 },
  { $unset: { age: "" } }
)
```

#### ➕  `$push`

* Add a value to an **array** field.

```js
// Add "John" to the friends array for all users
db.users.updateMany(
  {},
  { $push: { friends: "John" } }
)
```

#### ➖ `$pull`

* Remove a value from an **array** field.

```js
// Remove "Mike" from the friends array for all users
db.users.updateMany(
  {},
  { $pull: { friends: "Mike" } }
)
```

---

### 📖 Read Modifiers

These modifiers can be added to the end of any `.find()` query to control how the results are returned.

#### 🔢 `.sort()`

* Sort the results based on one or more fields.

```js
// Get all users sorted by name (A–Z), then by age (Z–A) if names are equal
db.users.find().sort({ name: 1, age: -1 })
```

* `1` for ascending (A–Z, 0–9)
* `-1` for descending (Z–A, 9–0)

#### 🔼 `.limit()`

* Limit the number of returned documents.

```js
// Get only the first 2 users
db.users.find().limit(2)
```

#### ⏭️ `.skip()`

* Skip a specific number of documents.

```js
// Skip the first 4 users
db.users.find().skip(4)
```

* Often used with `.limit()` for **pagination**.

---