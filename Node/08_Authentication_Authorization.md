### 🔰 **1. Authentication vs Authorization**

Let’s start with the **basic difference**:

| Feature        | Authentication                                           | Authorization                                                      |
| -------------- | -------------------------------------------------------- | ------------------------------------------------------------------ |
| **Definition** | Verifying the identity of the user.                      | Determining what actions a user is allowed to perform.             |
| **When?**      | Happens **before** authorization.                        | Happens **after** authentication.                                  |
| **Example**    | Logging in with email/password.                          | Checking if a user is an admin before accessing a protected route. |
| **How?**       | Done using credentials (password, OTP, biometrics, etc.) | Done using roles, permissions, or access levels.                   |
| **Outcome**    | “You are who you say you are.”                           | “You are allowed to do this.”                                      |

---

### 🧠 Real-world Example:

Imagine you're going to a movie theater:

* **Authentication** = Showing your ticket to enter the theater (identity check).
* **Authorization** = Showing your seat number to sit in the right seat (access control).

---

### ✅ Use in Backend Projects

* After a user logs in (authenticated), you’ll attach a **token** (e.g., JWT).
* Then, you’ll use middleware to:

  * Check if the token is valid (authentication).
  * Check if the user has the right **role** to access certain routes (authorization).

---

## ✅ **2. User Registration and Login Endpoints**

This is where authentication begins — by allowing users to **sign up** and **log in**.

---

### 🧾 **Key Endpoints**

#### 🟢 `POST /api/users/register`

Registers a new user.

**Request Body:**

```json
{
  "name": "Ganesh",
  "email": "ganesh@example.com",
  "password": "securePassword123"
}
```

**Typical Flow:**

1. Validate inputs.
2. Check if user already exists.
3. Hash the password using `bcryptjs`.
4. Save user to the database.
5. Optionally return a JWT or success message.

---

#### 🟢 `POST /api/users/login`

Logs in a registered user.

**Request Body:**

```json
{
  "email": "ganesh@example.com",
  "password": "securePassword123"
}
```

**Typical Flow:**

1. Validate inputs.
2. Check if user exists.
3. Compare hashed password using `bcrypt.compare()`.
4. Generate a JWT token.
5. Return token and user info.

---

### 🛠 Sample Code (Express + Mongoose + bcryptjs + JWT)

#### 📁 `controllers/userController.js`

```js
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User'); // Mongoose model

// Registration
exports.register = async (req, res) => {
  const { name, email, password } = req.body;

  const existingUser = await User.findOne({ email });
  if (existingUser) return res.status(400).json({ message: "User already exists" });

  const hashedPassword = await bcrypt.hash(password, 10);

  const newUser = new User({ name, email, password: hashedPassword });
  await newUser.save();

  res.status(201).json({ message: "User registered successfully" });
};

// Login
exports.login = async (req, res) => {
  const { email, password } = req.body;

  const user = await User.findOne({ email });
  if (!user) return res.status(400).json({ message: "Invalid credentials" });

  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) return res.status(400).json({ message: "Invalid credentials" });

  const token = jwt.sign({ id: user._id, role: user.role }, process.env.JWT_SECRET, {
    expiresIn: '1h',
  });

  res.status(200).json({ token, user: { id: user._id, name: user.name, role: user.role } });
};
```

---

### 🔐 Environment Variables Example (`.env`)

```
JWT_SECRET=supersecretkey
```

---

### 🧪 Test using Thunder Client or Postman

* Register first
* Then try logging in using the same credentials
* You should receive a `token` you can use to access protected routes later

---

## ✅ **3. Password Hashing with `bcryptjs`**

### 🔐 Why Hash Passwords?

Passwords should **never be stored in plain text**. If your database gets compromised, plain text passwords expose all your users.

So we **hash** passwords before saving them.

---

### 🔧 What is `bcryptjs`?

`bcryptjs` is a library that helps you:

* **Hash** a password securely.
* **Compare** a plain password with a hashed one during login.

Install it:

```bash
npm install bcryptjs
```

---

### 🔄 Password Hashing Flow

#### 🟢 1. **Hashing Password (on Registration)**

```js
const bcrypt = require('bcryptjs');

const plainPassword = "mySecret123";
const hashedPassword = await bcrypt.hash(plainPassword, 10); // 10 = salt rounds
```

* The higher the number (e.g., 10), the more secure but slower it is.
* It generates a different hash every time even for the same password due to salting.

---

#### 🔵 2. **Comparing Password (on Login)**

```js
const isMatch = await bcrypt.compare(plainPassword, hashedPassword);
if (isMatch) {
  // Password is correct
} else {
  // Invalid password
}
```

---

### 📁 Example Inside a Controller:

```js
// On registration
const hashedPassword = await bcrypt.hash(req.body.password, 10);
const user = new User({ email: req.body.email, password: hashedPassword });
await user.save();

// On login
const user = await User.findOne({ email: req.body.email });
const isMatch = await bcrypt.compare(req.body.password, user.password);
if (!isMatch) return res.status(400).json({ message: "Invalid credentials" });
```

---

### ✅ Summary:

* Always hash passwords before saving.
* Never store plain passwords.
* Use `bcrypt.compare()` for secure login checks.

---

## ✅ **4. JSON Web Token (JWT) Based Authentication**

### 🔐 What is JWT?

JWT (JSON Web Token) is a **token-based** authentication method used to **secure APIs**.

A JWT is a **digitally signed string** that contains **user data**. It’s sent from the server to the client after login, and used in future requests to verify the user.

---

### 🧱 Structure of a JWT

```
<Header>.<Payload>.<Signature>
```

Example:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEyMyIsInJvbGUiOiJhZG1pbiJ9.7xfK...
```

* **Header**: Type of token and signing algorithm (e.g., HS256)
* **Payload**: Data (like `id`, `role`, etc.)
* **Signature**: Hashed secret used to validate the token

---

### 🧪 Why Use JWT?

* Stateless (no need to store sessions)
* Secure (if secret is kept safe)
* Easy to use with headers

---

### 🔧 Setup in Express

#### 1. **Install JWT**

```bash
npm install jsonwebtoken
```

#### 2. **Generate a JWT (on Login)**

```js
const jwt = require('jsonwebtoken');

const token = jwt.sign(
  { id: user._id, role: user.role }, // payload
  process.env.JWT_SECRET,           // secret key
  { expiresIn: '1h' }               // options
);
```

✅ You send this token back to the client.

---

#### 3. **Verify a JWT (on Protected Routes)**

```js
const token = req.headers.authorization?.split(" ")[1];
if (!token) return res.status(401).json({ message: "Access Denied" });

const decoded = jwt.verify(token, process.env.JWT_SECRET);
req.user = decoded; // now req.user has id and role
next();
```

---

### 🛡 Example Middleware: `authMiddleware.js`

```js
const jwt = require("jsonwebtoken");

const auth = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return res.status(401).json({ message: "No token provided" });
  }

  const token = authHeader.split(" ")[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded; // { id, role }
    next();
  } catch (err) {
    res.status(401).json({ message: "Invalid token" });
  }
};

module.exports = auth;
```

---

### 🔐 Add to Route

```js
const auth = require('../middlewares/auth');

router.get("/dashboard", auth, (req, res) => {
  res.json({ message: "Welcome", user: req.user });
});
```

---

### ✅ Summary

| Action       | Method                      |
| ------------ | --------------------------- |
| Generate JWT | `jwt.sign(payload, secret)` |
| Verify JWT   | `jwt.verify(token, secret)` |

---

## ✅ **5. Protecting Routes with Middleware**

After generating a **JWT token** on login, you need to **protect certain routes** so that only authenticated users can access them.

This is where **middleware** comes into play.

---

### 🧠 What is Middleware?

In Express.js, **middleware** is a function that runs **before** the final route handler. It’s perfect for:

* Checking if a JWT token exists and is valid.
* Attaching user data to the `req` object.
* Preventing unauthorized access.

---

### 🔐 Create Authentication Middleware

#### 📁 `middlewares/authMiddleware.js`

```js
const jwt = require("jsonwebtoken");

const authMiddleware = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return res.status(401).json({ message: "Unauthorized: No token provided" });
  }

  const token = authHeader.split(" ")[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded; // Add user info to request
    next(); // Go to the actual route
  } catch (error) {
    return res.status(403).json({ message: "Forbidden: Invalid token" });
  }
};

module.exports = authMiddleware;
```

---

### ✅ Use the Middleware on Protected Routes

#### 📁 `routes/userRoutes.js`

```js
const express = require("express");
const authMiddleware = require("../middlewares/authMiddleware");

const router = express.Router();

router.get("/profile", authMiddleware, (req, res) => {
  res.json({
    message: "Welcome to your profile!",
    user: req.user, // Available because of middleware
  });
});
```

---

### 🛡 Result

| Scenario                              | Outcome            |
| ------------------------------------- | ------------------ |
| Valid token in `Authorization` header | ✅ Access granted   |
| Missing or malformed token            | ❌ 401 Unauthorized |
| Invalid or expired token              | ❌ 403 Forbidden    |

---

### 🧪 Test It

* Use Postman/Thunder Client
* Add this header:

  ```
  Authorization: Bearer <your_token>
  ```

---

### ✅ Summary

* Middleware centralizes token validation.
* Use `req.user` in your route to access authenticated user info.
* You can now protect any route by simply adding `authMiddleware`.

---

## ✅ **6. Role-Based Access Control (RBAC)**

Role-Based Access Control lets you **restrict access to certain routes** based on a user's role (e.g., `admin`, `user`, `moderator`, etc.).

You’ve already added user roles in your JWT payload:

```js
jwt.sign({ id: user._id, role: user.role }, ...);
```

Now, let’s build middleware to restrict routes based on these roles.

---

### 🔐 Step-by-Step: Implementing RBAC

---

### ✅ Step 1: Add a `role` Field in User Schema

```js
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user',
  }
});
```

---

### ✅ Step 2: Add Role in JWT Payload

In the login controller:

```js
const token = jwt.sign(
  { id: user._id, role: user.role },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);
```

---

### ✅ Step 3: Create Role Middleware

#### 📁 `middlewares/authorizeRoles.js`

```js
const authorizeRoles = (...allowedRoles) => {
  return (req, res, next) => {
    if (!req.user || !allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ message: "Access Denied: Insufficient permissions" });
    }
    next();
  };
};

module.exports = authorizeRoles;
```

> It accepts multiple roles like `authorizeRoles('admin', 'moderator')`.

---

### ✅ Step 4: Protect Route with Both Middlewares

```js
const auth = require('../middlewares/authMiddleware');
const authorizeRoles = require('../middlewares/authorizeRoles');

router.get('/admin-only', auth, authorizeRoles('admin'), (req, res) => {
  res.json({ message: "Hello Admin 👑" });
});
```

---

### ✅ Test Flow:

| Role in Token | Route         | Access      |
| ------------- | ------------- | ----------- |
| `admin`       | `/admin-only` | ✅ Allowed   |
| `user`        | `/admin-only` | ❌ Forbidden |

---

### ✅ Summary:

* RBAC gives you **fine-grained control** over your app.
* Middleware like `authorizeRoles` helps keep your code clean.
* Supports multiple roles and scalable access levels.

---

## ✅ **7. Forgot/Reset Password Flow**

This flow allows users to reset their password **securely** in case they forget it. It usually involves:

1. **Sending a password reset link to the user’s email.**
2. **Verifying a secure token.**
3. **Letting the user set a new password.**

---

### 🧠 High-Level Flow

#### 🔁 Forgot Password Flow

1. User sends email → `POST /forgot-password`
2. Server generates a **reset token** and emails it.
3. Token is saved with **expiry** in DB.

#### 🔄 Reset Password Flow

4. User clicks link → lands on a form
5. Form submits new password + token → `POST /reset-password/:token`
6. Server validates token and updates password.

---

## 🔧 Step-by-Step Implementation

### ✅ Step 1: Add Reset Token Fields to User Schema

```js
resetPasswordToken: String,
resetPasswordExpires: Date,
```

---

### ✅ Step 2: `POST /forgot-password`

```js
const crypto = require("crypto");

exports.forgotPassword = async (req, res) => {
  const user = await User.findOne({ email: req.body.email });
  if (!user) return res.status(400).json({ message: "User not found" });

  const token = crypto.randomBytes(32).toString("hex");
  const hashedToken = crypto.createHash("sha256").update(token).digest("hex");

  user.resetPasswordToken = hashedToken;
  user.resetPasswordExpires = Date.now() + 10 * 60 * 1000; // 10 mins
  await user.save();

  const resetURL = `http://yourdomain.com/reset-password/${token}`;

  // TODO: Send email with resetURL
  res.status(200).json({ message: "Reset link sent to email" });
};
```

---

### ✅ Step 3: `POST /reset-password/:token`

```js
exports.resetPassword = async (req, res) => {
  const hashedToken = crypto.createHash("sha256").update(req.params.token).digest("hex");

  const user = await User.findOne({
    resetPasswordToken: hashedToken,
    resetPasswordExpires: { $gt: Date.now() }
  });

  if (!user) return res.status(400).json({ message: "Token invalid or expired" });

  user.password = await bcrypt.hash(req.body.password, 10);
  user.resetPasswordToken = undefined;
  user.resetPasswordExpires = undefined;
  await user.save();

  res.status(200).json({ message: "Password reset successful" });
};
```

---

### ✅ Step 4: Optional – Send Email

You can use **Nodemailer** to send the email with `resetURL`.

---

### 🛡 Security Tips

* Always **hash** the reset token before storing it.
* Set a short **expiry** (like 10-15 minutes).
* Don't expose sensitive messages like "User not found" in public APIs (to prevent user enumeration).

---

### ✅ Summary

| Route                         | Purpose                          |
| ----------------------------- | -------------------------------- |
| `POST /forgot-password`       | Send reset link to email         |
| `POST /reset-password/:token` | Validate token, set new password |

---

## ✅ **8. Refresh Tokens**

### 🔁 Why Use Refresh Tokens?

Access tokens (JWTs) typically expire in **15 minutes to 1 hour** for security reasons. But logging in again every hour is annoying.

**Solution**:
Use a **refresh token** to issue a **new access token** without forcing the user to log in again.

---

### 🔐 Token Types Recap:

| Token Type        | Purpose                 | Lifetime           | Storage Location    |
| ----------------- | ----------------------- | ------------------ | ------------------- |
| **Access Token**  | Access protected routes | Short (15m – 1h)   | Header or cookie    |
| **Refresh Token** | Get new access tokens   | Long (7 – 30 days) | Secure cookie or DB |

---

## 🧱 Implementation Steps

---

### ✅ Step 1: Generate Both Tokens on Login

```js
const accessToken = jwt.sign({ id: user._id, role: user.role }, process.env.JWT_SECRET, {
  expiresIn: '15m',
});

const refreshToken = jwt.sign({ id: user._id }, process.env.REFRESH_SECRET, {
  expiresIn: '7d',
});
```

---

### ✅ Step 2: Return Both Tokens to Client

```js
res.cookie("refreshToken", refreshToken, {
  httpOnly: true,
  secure: true,
  sameSite: "Strict",
  maxAge: 7 * 24 * 60 * 60 * 1000, // 7 days
});

res.status(200).json({ accessToken });
```

---

### ✅ Step 3: Create `POST /refresh-token` Endpoint

```js
exports.refreshAccessToken = async (req, res) => {
  const token = req.cookies.refreshToken;
  if (!token) return res.status(401).json({ message: "No refresh token" });

  try {
    const decoded = jwt.verify(token, process.env.REFRESH_SECRET);

    const newAccessToken = jwt.sign(
      { id: decoded.id },
      process.env.JWT_SECRET,
      { expiresIn: '15m' }
    );

    res.status(200).json({ accessToken: newAccessToken });
  } catch (err) {
    res.status(403).json({ message: "Invalid or expired refresh token" });
  }
};
```

---

### ✅ Step 4: Secure Refresh Tokens

* Store in **HTTP-only, secure cookies**
* Optionally, save in DB and allow users to log out of specific sessions
* **Blacklist** them on logout if needed (advanced)

---

### 🛡 Refresh Token vs Re-login

| Scenario                     | With Refresh Token        | Without              |
| ---------------------------- | ------------------------- | -------------------- |
| Token expires                | 🔁 Auto-refresh           | 🚫 Logout            |
| User closes browser          | ✅ Still logged in         | 🚫 Must log in again |
| Token stolen (access token)  | ❌ Valid for 15 mins       | ❌ Same               |
| Token stolen (refresh token) | ❌ Big risk unless secured | ❌ Same               |

---

### ✅ Summary

* Use short-lived **access tokens** and long-lived **refresh tokens**.
* Store refresh tokens in **secure cookies** or server DB.
* Create an endpoint to issue new access tokens.

---

## ✅ **9. Token Storage: Headers vs Cookies**

After creating **access** and **refresh tokens**, we need to decide **where to store them** on the client side.

There are **two common approaches**:

---

## 🧾 1. Authorization Headers (Most common for APIs)

### 🔧 How It Works:

* Store token in memory (like React state or localStorage).
* Send token in `Authorization` header with every request.

```http
Authorization: Bearer <access_token>
```

### ✅ Pros:

* Easy to implement in frontend apps.
* Works great with mobile apps and Postman.
* Clean separation of client and server.

### ❌ Cons:

* If stored in `localStorage`, it’s vulnerable to **XSS attacks**.
* Requires custom logic to refresh tokens and handle expiry.

---

## 🍪 2. HTTP-only Cookies (Great for Web Apps)

### 🔧 How It Works:

* Store the **refresh token** in an `HTTPOnly` cookie (can’t be accessed by JS).
* Access token can be stored in memory or also as a cookie.

```js
res.cookie("refreshToken", token, {
  httpOnly: true,
  secure: true, // for HTTPS
  sameSite: "Strict",
  maxAge: 7 * 24 * 60 * 60 * 1000,
});
```

### ✅ Pros:

* Secure against **XSS** (can't be accessed via JS).
* Automatically sent with each request.
* Great for traditional login-based apps (like dashboards).

### ❌ Cons:

* CSRF attacks possible if not protected with `sameSite`, CSRF tokens.
* More complex setup on frontend (need CSRF protection and CORS configs).

---

## 🔐 Best Practice Recommendation

| Use Case                  | Suggested Storage                                                |
| ------------------------- | ---------------------------------------------------------------- |
| API (e.g., mobile or SPA) | Access: Authorization header<br>Refresh: Secure cookie or header |
| Traditional Web App       | Store both tokens in **HTTP-only cookies**                       |

---

### ✅ Summary

| Feature              | Headers                   | Cookies                     |
| -------------------- | ------------------------- | --------------------------- |
| XSS Protection       | ❌ (if using localStorage) | ✅ (HTTPOnly)                |
| CSRF Risk            | ✅                         | ❌ (needs protection)        |
| Access from JS       | ✅                         | ❌                           |
| Auto-Sent in Request | ❌                         | ✅                           |
| Recommended For      | APIs (SPAs, mobile)       | Browser logins (dashboards) |

---