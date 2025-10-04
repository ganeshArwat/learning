<!-- error handling middleware -->
# 📝 Express.js Cheat Sheet

## 📦 Setup

```bash
npm init -y
npm install express
```

```js
// app.js
const express = require('express');
const app = express();
const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

---

## 🔧 Middleware

```js
app.use(express.json());           // Parse JSON bodies
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded bodies
app.use(express.static('public')); // Serve static files
```

### Custom Middleware

```js
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});
```

---

## 🌐 Routing

### Basic Routes

```js
app.get('/', (req, res) => res.send('GET Home'));
app.post('/', (req, res) => res.send('POST Home'));
app.put('/', (req, res) => res.send('PUT Home'));
app.delete('/', (req, res) => res.send('DELETE Home'));
```

### Route with Parameters

```js
app.get('/user/:id', (req, res) => {
  res.send(`User ID: ${req.params.id}`);
});
```

### Route Query Strings

```js
app.get('/search', (req, res) => {
  const { q } = req.query;
  res.send(`Search query: ${q}`);
});
```

---

## 📁 Routing in Separate Files

```js
// routes/user.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => res.send('User Home'));
router.get('/:id', (req, res) => res.send(`User ${req.params.id}`));

module.exports = router;

// app.js
const userRoutes = require('./routes/user');
app.use('/user', userRoutes);
```

---

## 📨 Handling Requests & Responses

```js
req.body        // Access POST/PUT body
req.params      // Route params
req.query       // URL query params

res.sendFile(path.join(__dirname, "public", "index.html"));
res.send('Hello')               // Send response
res.json({ msg: 'Hello' })      // Send JSON
res.status(404).send('Not Found') // Status code
```

---

## 🧱 Error Handling

### 404 Handler

```js
app.use((req, res) => {
  res.status(404).send('404 Not Found');
});
```

### Error Middleware

```js
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});


function validateInput(req, res, next) {
  const { username, password, email } = req.body;

  if (!username || !password || !email) {
    return res.status(400).json({ message: "Missing required fields" });
  }

  if (typeof username !== "string" || username.length < 1) {
    return res.status(400).json({ message: "Invalid username" });
  }

  if (typeof password !== "string" || password.length < 6) {
    return res
      .status(400)
      .json({ message: "Password must be at least 6 characters long" });
  }

  if (!validator.isEmail(email)) {
    return res.status(400).json({ message: "Invalid email format" });
  }

  next();
}

app.post("/users", validateInput, async (req, res, next) => {});

app.use((err, req, res, next) => {
  res.status(500).json({ message: err.message });
});

```

---

## 🔐 Environment Variables

```bash
npm install dotenv
```

```js
// app.js
require('dotenv').config();
const PORT = process.env.PORT || 3000;
```

---

## ⚙️ Express with MongoDB (Mongoose)

```bash
npm install mongoose
```

```js
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/mydb')
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error(err));
```

---

## 🧪 Sample CRUD (in memory)

```js
let items = [];

app.get('/items', (req, res) => res.json(items));
app.post('/items', (req, res) => {
  items.push(req.body);
  res.status(201).json({ msg: 'Item added' });
});
```

---

## 🔁 Common Tools

```bash
npm install nodemon --save-dev
```

```json
// package.json
"scripts": {
  "start": "node app.js",
  "dev": "nodemon app.js"
}
```

---

## 🔐 JWT Auth (Basic Example)

```bash
npm install jsonwebtoken
```

```js
const jwt = require('jsonwebtoken');
const token = jwt.sign({ userId: 1 }, 'THIS_IS_MY_KEY', { expiresIn: '1h' });

// Verify
const authHeader = req.headers.authorization;
const token = authHeader.split(" ")[1];

jwt.verify(token, 'secret', (err, decoded) => {
  if (err) return res.sendStatus(403);
  console.log(decoded);
});
```

---

# 📘 Express + Mongoose Cheat Sheet

## 🔧 Setup

### Step 1: Initialize Project

```bash
npm init -y
npm install express mongoose dotenv
npm install nodemon --save-dev
```

### Step 2: Basic File Structure

```
project/
│
├── app.js
├── .env
├── models/
│   └── User.js
├── routes/
│   └── userRoutes.js
├── controllers/
│   └── userController.js
```

---

## 📁 .env

```env
PORT=5000
MONGO_URI=mongodb://127.0.0.1:27017/myapp
```

---

## 🚀 app.js (Entry Point)

```js
const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();
app.use(express.json());

// Routes
const userRoutes = require('./routes/userRoutes');
app.use('/api/users', userRoutes);

// DB Connection
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

---

## 🧱 models/User.js

```js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  age: {
    type: Number,
    default: 0
  }
}, { timestamps: true });

module.exports = mongoose.model('User', userSchema);
```

---

## 🧠 controllers/userController.js

```js
const User = require('../models/User');

// GET all users
exports.getUsers = async (req, res) => {
  const users = await User.find();
  res.json(users);
};

// POST new user
exports.createUser = async (req, res) => {
  const user = new User(req.body);
  await user.save();
  res.status(201).json(user);
};

// GET user by ID
exports.getUserById = async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
};

// PUT update user
exports.updateUser = async (req, res) => {
  const user = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(user);
};

// DELETE user
exports.deleteUser = async (req, res) => {
  await User.findByIdAndDelete(req.params.id);
  res.json({ message: 'User deleted' });
};
```

---

## 🔁 routes/userRoutes.js

```js
const express = require('express');
const router = express.Router();
const {
  getUsers,
  createUser,
  getUserById,
  updateUser,
  deleteUser
} = require('../controllers/userController');

router.get('/', getUsers);
router.post('/', createUser);
router.get('/:id', getUserById);
router.put('/:id', updateUser);
router.delete('/:id', deleteUser);

module.exports = router;
```

---

## 🧪 Test with Postman or cURL

| Method | URL              | Body (JSON)                                         | Description     |
| ------ | ---------------- | --------------------------------------------------- | --------------- |
| GET    | `/api/users`     | —                                                   | Get all users   |
| POST   | `/api/users`     | `{ "name": "Ganesh", "email": "ganesh@email.com" }` | Create user     |
| GET    | `/api/users/:id` | —                                                   | Get single user |
| PUT    | `/api/users/:id` | `{ "name": "Updated" }`                             | Update user     |
| DELETE | `/api/users/:id` | —                                                   | Delete user     |

---

## 📦 package.json Scripts

```json
"scripts": {
  "start": "node app.js",
  "dev": "nodemon app.js"
}
```

---

## ✅ Summary of Mongoose Methods

| Function                    | Purpose               |
| --------------------------- | --------------------- |
| `Model.find()`              | Fetch all documents   |
| `Model.findById(id)`        | Find document by ID   |
| `Model.create(data)`        | Insert new document   |
| `Model.findByIdAndUpdate()` | Update document by ID |
| `Model.findByIdAndDelete()` | Delete document by ID |
| `Model.deleteMany()`        | Delete multiple docs  |

---

# ✅ Express + Mongoose + Middleware Hooks Cheat Sheet


## 🧱 models/User.js (With `pre` and `post` Hooks)

```js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  age: {
    type: Number,
    default: 0
  }
}, { timestamps: true });

/* ✅ Pre-save Hook */
userSchema.pre('save', function (next) {
  console.log('🔄 Before saving user:', this.name);
  next();
});

/* ✅ Post-save Hook */
userSchema.post('save', function (doc, next) {
  console.log('✅ User saved:', doc.name);
  next();
});

/* ✅ Pre-find Hook */
userSchema.pre(/^find/, function (next) {
  console.log('🔍 Before find query:', this.getQuery());
  next();
});

/* ✅ Post-find Hook */
userSchema.post('find', function (docs, next) {
  console.log(`✅ Found ${docs.length} users`);
  next();
});

/* ✅ Pre-remove Hook */
userSchema.pre('remove', function (next) {
  console.log('⛔ Before removing user:', this.name);
  next();
});

/* ✅ Post-remove Hook */
userSchema.post('remove', function (doc, next) {
  console.log('✅ User removed:', doc.name);
  next();
});

module.exports = mongoose.model('User', userSchema);
```

---

## 📚 Common Mongoose Middleware Hooks

| Hook Type                      | When It Runs               | Example Use Cases            |
| ------------------------------ | -------------------------- | ---------------------------- |
| `pre('save')`                  | Before saving a document   | Hash password, validate data |
| `post('save')`                 | After saving a document    | Logging, notifications       |
| `pre('find')` / `pre(/^find/)` | Before find queries        | Filtering inactive records   |
| `post('find')`                 | After querying documents   | Logging, transform results   |
| `pre('remove')`                | Before document is removed | Cleanup references           |
| `post('remove')`               | After document removal     | Logging, alerts              |

---

## ✅ Reminder: To Trigger `remove` Middleware

```js
const user = await User.findById(id);
await user.remove(); // Not findByIdAndDelete
```

`findByIdAndDelete()` bypasses document middleware (`pre/post remove`). To use hooks, fetch the doc and call `remove()` manually.

---

## Using Cookies

```js
const cookieParser = require("cookie-parser");
app.use(cookieParser());

app.get("/visit", (req, res) => {
  // Implementation for visit counting
  const visit_count = req.cookies.visitCount;
  if(visit_count) {
      res.cookie('visitCount', parseInt(visit_count) + 1);
      res.send(`This is your visit number ${parseInt(visit_count) + 1}`);
  } else {
      res.cookie('visitCount', `1`);
      res.send(`This is your visit number 1`);
  }
});
```

---

## Using bcrypt

```js
const bcrypt = require("bcrypt");

const password = "mySecret123";

// 🔐 Hash the password
const salt = await bcrypt.genSalt(12);
const hashedPassword = await bcrypt.hash(password, salt);

console.log("Hashed Password:", hashedPassword);

// ✅ Verify the password (later during login)
const isMatch = await bcrypt.compare("mySecret123", hashedPassword);

if (isMatch) {
  console.log("✔️ Password matched!");
} else {
  console.log("❌ Invalid password.");
}
```

---

## RateLimiting

```js
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  // Configure the rate limiting middleware
  windowMs: 15 * 60 * 1000, // 15 minutes in milliseconds
  max: 100, // Limit each IP to 100 requests per windowMs
  message: "Too many requests from this IP, please try again after 15 minutes", // Custom message
  statusCode: 429, // HTTP status code for too many requests
  headers: true, // Send rate limit info in the headers
});

// Apply the rate limiting middleware to all requests
app.use(limiter);
```

---

## Stripe Payment gatway

```
1. of the following is required to integrate Stripe with Node.js Express?
- Stripe API key

2. In a Node.js Express application, where should you store your Stripe API key?
- In a configuration file

3. Which Stripe API method is used to create a payment intent?
- stripe.paymentIntent.create()

4. What is the purpose of a PaymentIntent in the context of Stripe?
- To process a payment

5. Which Stripe API method is used to confirm a PaymentIntent?
- stripe.paymentIntent.confirm()

6. What is the purpose of the stripe object in a React component that integrates with Stripe?
- To interact with the Stripe API

7. Which Stripe API method is used to handle the client-side payment flow in a React component?
- stripe.handleCardPayment()

8. In a React component, what is the purpose of the Elements component from @stripe/react-stripe-js?
- To render payment form elements

9. Which of the following is NOT a valid event type in the context of Stripe webhooks?
- payment_intent.processing
```