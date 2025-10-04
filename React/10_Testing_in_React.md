### ✅ **Introduction to Testing in React**

#### 🔍 What is Testing?

**Testing** is the process of verifying that your code behaves as expected. In the context of React applications, it helps ensure:

- Components render correctly
- User interactions behave properly
- Data flows through components as expected
- Edge cases and bugs are caught early

---

#### 🧪 Types of Testing

1. **Unit Testing**

   - Tests **individual functions or components** in isolation.
   - Example: Testing a `Button` component’s onClick behavior.

2. **Integration Testing**

   - Tests how **multiple units/components work together**.
   - Example: A form with multiple inputs and a submit button.

3. **End-to-End (E2E) Testing**

   - Simulates real-world **user interactions** in the browser.
   - Example: A user logs in, fills a form, and submits.

---

#### 🚀 Why Testing is Important in React Apps

- **Reliability**: Catch bugs before your users do
- **Refactor Safely**: Ensures old features still work after changes
- **Documentation**: Tests describe how components are supposed to work
- **Developer Confidence**: Speeds up development without fear of breaking things

---

### ⚙️ **Setting Up Testing Tools**

React testing commonly involves two main tools:

---

#### 1. ✅ **Jest** – JavaScript Testing Framework

- **What is it?**

  - Jest is a powerful test runner and assertion library developed by Facebook.
  - It comes **pre-configured with Create React App (CRA)**.

- **Installation (if not using CRA):**

  ```bash
  npm install --save-dev jest
  ```

- **Key Features:**

  - Zero config (CRA)
  - Snapshot testing
  - Mocking support
  - Test coverage reports

---

#### 2. 🧪 **React Testing Library (RTL)**

- **What is it?**

  - A library to test React components **in a way that reflects how users interact** with the UI.
  - Encourages testing via roles, labels, and visible text.

- **Installation:**

  ```bash
  npm install --save-dev @testing-library/react @testing-library/jest-dom
  ```

- **Helpful Add-on:**

  ```bash
  npm install --save-dev @testing-library/user-event
  ```

---

#### 3. 🌐 **Testing Environment (JSDOM)**

- **What is JSDOM?**

  - A JavaScript-based DOM implementation that simulates a browser environment in Node.js.
  - Jest uses JSDOM behind the scenes so you can render and interact with DOM elements in your tests.

- **No need to install separately** – comes bundled with Jest.

---

### 🛠 File Structure & Naming

- Tests usually live **next to components** or in a `__tests__` folder.
- Naming convention:

  - `Component.test.js` or `Component.spec.js`

---

Perfect! Let's jump into **Point No. 3: 🧪 Writing Basic Tests with Jest**.

---

### 🧪 **Writing Basic Tests with Jest**

---

#### 1. ✅ **Your First Test**

Create a simple test file, e.g., `sum.test.js`:

```js
function sum(a, b) {
  return a + b;
}

test("adds 2 + 3 to equal 5", () => {
  expect(sum(2, 3)).toBe(5);
});
```

Run it using:

```bash
npm test
```

---

#### 2. 🧩 **Basic Syntax in Jest**

- **`describe()`** – groups related tests
- **`test()` / `it()`** – defines a test case
- **`expect()`** – makes an assertion about the result

```js
describe("sum function", () => {
  it("should return correct sum", () => {
    expect(sum(1, 2)).toBe(3);
  });
});
```

---

#### 3. 🔍 **Common Matchers in Jest**

| Matcher              | Description                        |
| -------------------- | ---------------------------------- |
| `toBe()`             | Exact equality (`===`)             |
| `toEqual()`          | Deep equality (objects/arrays)     |
| `toBeNull()`         | Matches `null`                     |
| `toBeTruthy()`       | Checks truthiness                  |
| `toContain()`        | Checks if array contains an item   |
| `toHaveBeenCalled()` | Checks if mock function was called |
| `toMatch()`          | Regex pattern match (strings)      |

---

#### 4. 🧪 Example: Testing a Simple Function

```js
function greet(name) {
  return `Hello, ${name}`;
}

describe("greet()", () => {
  test("returns a greeting message", () => {
    expect(greet("Ganesh")).toBe("Hello, Ganesh");
  });
});
```

---

### ✅ **What is an Assertion?**

An **assertion** is a statement in a test that checks whether a certain condition is **true**. If the condition is **not true**, the test **fails**.

---

### 💡 In Simple Terms:

An assertion asks:

> "Did the code do what I expected it to do?"

---

### 🧪 Example:

```js
expect(sum(2, 3)).toBe(5);
```

Here’s what’s happening:

- `sum(2, 3)` returns a value (in this case, `5`)
- `expect(...)` wraps that result
- `.toBe(5)` asserts that the result **should be 5**

If it's not, Jest will report a failed test.

---

### 🔥 Common Real-Life Analogy:

Imagine you're baking a cake 🍰. After baking, you **check if it tastes sweet**. That **check** is like an **assertion**.

---

### 🧩 **Component Testing with React Testing Library**

React Testing Library (RTL) helps you test **components the way a user would use them**—by interacting with UI elements instead of testing internal details like state or instance methods.

---

#### 1. 🧱 **Rendering Components with `render()`**

```jsx
import { render } from "@testing-library/react";
import MyComponent from "./MyComponent";

test("renders MyComponent", () => {
  render(<MyComponent />);
});
```

- This creates a virtual DOM for the component to be tested.

---

#### 2. 🔍 **Querying the DOM**

RTL provides query methods that simulate how users find elements:

| Query Method             | Use When Element Has...                    |
| ------------------------ | ------------------------------------------ |
| `getByText()`            | Visible text                               |
| `getByRole()`            | Semantic role (e.g., `button`, `textbox`)  |
| `getByLabelText()`       | Associated label                           |
| `getByPlaceholderText()` | Placeholder in input                       |
| `getByTestId()`          | A test-specific identifier (`data-testid`) |

Example:

```jsx
const { getByText } = render(<button>Click Me</button>);
expect(getByText("Click Me")).toBeInTheDocument();
```

---

#### 3. 🧑‍💻 **Simulating User Interactions**

##### 🔥 Option 1: `fireEvent`

```jsx
import { fireEvent } from "@testing-library/react";

fireEvent.click(buttonElement);
fireEvent.change(inputElement, { target: { value: "test" } });
```

##### 🔥 Option 2 (Preferred): `userEvent`

```jsx
import userEvent from "@testing-library/user-event";

await userEvent.click(buttonElement);
await userEvent.type(inputElement, "hello");
```

> ✅ `userEvent` simulates real user behavior more accurately and is recommended over `fireEvent`.

---

### 🧪 Mini Example: Button Click

```jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

function Greet() {
  const [msg, setMsg] = React.useState("");
  return (
    <>
      <button onClick={() => setMsg("Hello")}>Greet</button>
      <p>{msg}</p>
    </>
  );
}

test("displays greeting on button click", async () => {
  render(<Greet />);
  await userEvent.click(screen.getByText("Greet"));
  expect(screen.getByText("Hello")).toBeInTheDocument();
});
```

---

### 📦 **Testing Props, State, and Conditional Rendering**

React components often behave differently depending on:

- The **props** they receive
- Their **internal state**
- The **conditions** in the JSX (like `if`, `ternary`, `&&`)

Testing these behaviors ensures your component behaves as expected in all scenarios.

---

### 1. 🧪 **Testing Component Props**

Test how a component renders differently with different props.

#### ✅ Example:

```jsx
function Welcome({ name }) {
  return <h1>Welcome, {name}!</h1>;
}

// Test
test("renders the name passed as prop", () => {
  render(<Welcome name="Ganesh" />);
  expect(screen.getByText("Welcome, Ganesh!")).toBeInTheDocument();
});
```

---

### 2. 🔁 **Testing Conditional Rendering**

Test if elements appear (or not) based on conditions.

#### ✅ Example:

```jsx
function LoginStatus({ isLoggedIn }) {
  return <p>{isLoggedIn ? "Logged In" : "Please log in"}</p>;
}

// Test
test("shows correct message when logged out", () => {
  render(<LoginStatus isLoggedIn={false} />);
  expect(screen.getByText("Please log in")).toBeInTheDocument();
});
```

---

### 3. 🔄 **Testing State Changes**

You can simulate state changes (like toggling UI) through user actions.

#### ✅ Example:

```jsx
function ToggleText() {
  const [visible, setVisible] = React.useState(false);
  return (
    <>
      <button onClick={() => setVisible(!visible)}>Toggle</button>
      {visible && <p>Now you see me!</p>}
    </>
  );
}

// Test
test("shows text after clicking toggle", async () => {
  render(<ToggleText />);
  expect(screen.queryByText("Now you see me!")).toBeNull();

  await userEvent.click(screen.getByText("Toggle"));

  expect(screen.getByText("Now you see me!")).toBeInTheDocument();
});
```

---

### 📝 **Testing Forms and Controlled Inputs**

In React, forms often use **controlled components**, meaning the form inputs are tied to component state. When testing them, we simulate user typing and validate behavior such as input changes, validation messages, and form submission.

---

### 🔧 1. **Simulating Input Changes**

Use `userEvent.type` to simulate typing into input fields.

#### ✅ Example:

```jsx
function NameForm() {
  const [name, setName] = React.useState("");
  return (
    <>
      <input
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <p data-testid="display">{name}</p>
    </>
  );
}

// Test
test("updates input value on typing", async () => {
  render(<NameForm />);
  const input = screen.getByPlaceholderText("Enter name");

  await userEvent.type(input, "Ganesh");
  expect(screen.getByTestId("display")).toHaveTextContent("Ganesh");
});
```

---

### ✅ 2. **Testing Form Submission**

You should simulate filling inputs and submitting the form.

#### ✅ Example:

```jsx
function LoginForm({ onSubmit }) {
  const [email, setEmail] = React.useState("");
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit(email);
      }}
    >
      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
}

// Test
test("submits the form with email", async () => {
  const handleSubmit = jest.fn();
  render(<LoginForm onSubmit={handleSubmit} />);

  await userEvent.type(screen.getByPlaceholderText("Email"), "ganesh@test.com");
  await userEvent.click(screen.getByText("Submit"));

  expect(handleSubmit).toHaveBeenCalledWith("ganesh@test.com");
});
```

---

### ❌ 3. **Testing Validation (Optional)**

### 🌐 **Mocking API Calls with MSW (Mock Service Worker)**

**MSW** is a modern tool to **mock API calls at the network level** in a way that simulates real-life interactions. Unlike `jest.mock`, which mocks modules, **MSW intercepts actual HTTP requests**, making your tests more realistic.

---

### 🔧 1. **Why MSW?**

- Mocks real `fetch`/XHR requests (no need to mock modules).
- Works for both frontend and backend tests.
- Keeps the component logic untouched.
- Supports REST and GraphQL.

---

### 🧰 2. **Basic Setup**

Install MSW:

```bash
npm install msw --save-dev
```

Create a mock handler:

```js
// src/mocks/handlers.js
import { rest } from "msw";

export const handlers = [
  rest.get("/api/user", (req, res, ctx) => {
    return res(ctx.status(200), ctx.json({ name: "Ganesh" }));
  }),
];
```

Set up the server:

```js
// src/mocks/server.js
import { setupServer } from "msw/node";
import { handlers } from "./handlers";

export const server = setupServer(...handlers);
```

Configure it for testing:

```js
// src/setupTests.js
import { server } from "./mocks/server";

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

> ✅ `setupTests.js` is automatically run by Jest (in CRA projects).

---

### ✅ 3. **Example Test Using MSW**

```jsx
// Component: UserInfo.jsx
import { useEffect, useState } from "react";

export function UserInfo() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/api/user")
      .then((res) => res.json())
      .then(setUser);
  }, []);

  return user ? <h1>{user.name}</h1> : <p>Loading...</p>;
}
```

```jsx
// Test
import { render, screen } from "@testing-library/react";
import { UserInfo } from "./UserInfo";

test("renders user fetched from API", async () => {
  render(<UserInfo />);
  expect(screen.getByText("Loading...")).toBeInTheDocument();

  const name = await screen.findByText("Ganesh");
  expect(name).toBeInTheDocument();
});
```

---

### 📌 Bonus: Dynamic Responses

You can override handlers in specific tests using `server.use(...)`.

```js
import { rest } from "msw";
import { server } from "../mocks/server";

server.use(
  rest.get("/api/user", (req, res, ctx) => {
    return res(ctx.status(500));
  })
);
```

---

### 🚀 **End-to-End Testing (E2E) with Cypress or Playwright**

End-to-End (E2E) testing simulates a real user’s journey, from interacting with the UI to performing actions like clicking buttons, filling forms, and navigating between pages. This is typically done to ensure the entire application works as expected.

We’ll focus on two popular E2E testing tools: **Cypress** and **Playwright**.

---

### 1. **What is E2E Testing?**

E2E testing tests the entire application in a real-world environment, checking both front-end and back-end interactions. It’s crucial for detecting issues that unit or integration tests can’t catch.

---

### 2. **Cypress: Easy and Fast E2E Testing**

Cypress is a **JavaScript testing framework** used for E2E testing. It runs directly in the browser, giving it unique access to the DOM, which helps simulate user interactions effectively.

#### ✅ **Features of Cypress**:

- **Time travel**: You can pause your tests and inspect the state of your app.
- **Automatic waiting**: Cypress waits for elements to appear, making tests stable.
- **Real-time reloading**: Your tests rerun instantly after code changes.
- **Test in the browser**: Tests run in the actual browser for a more accurate experience.

#### 🔧 **Setup**:

```bash
npm install cypress --save-dev
```

In your project’s `package.json`, add a script to open Cypress:

```json
"scripts": {
  "test:e2e": "cypress open"
}
```

Now, run the command:

```bash
npm run test:e2e
```

This will open Cypress, where you can create a new test.

#### 🧪 **Example Test with Cypress**:

```js
describe("User login", () => {
  it("should allow the user to login", () => {
    cy.visit("/login");
    cy.get('input[name="username"]').type("user123");
    cy.get('input[name="password"]').type("password");
    cy.get('button[type="submit"]').click();
    cy.contains("Welcome, user123");
  });
});
```

---

### 3. **Playwright: Advanced E2E Testing**

Playwright is a newer, but **powerful** tool for E2E testing. It supports multiple browsers (Chrome, Firefox, Safari) and offers better cross-browser testing.

#### ✅ **Features of Playwright**:

- **Cross-browser support**: Runs tests on Chrome, Firefox, and WebKit.
- **Parallel testing**: Speed up tests by running them in parallel.
- **Headless browser support**: Run tests in headless mode for faster execution.

#### 🔧 **Setup**:

```bash
npm install playwright --save-dev
```

Add the following script to `package.json`:

```json
"scripts": {
  "test:e2e": "playwright test"
}
```

#### 🧪 **Example Test with Playwright**:

```js
import { test, expect } from "@playwright/test";

test("login test", async ({ page }) => {
  await page.goto("/login");
  await page.fill('input[name="username"]', "user123");
  await page.fill('input[name="password"]', "password");
  await page.click('button[type="submit"]');
  await expect(page.locator("text=Welcome, user123")).toBeVisible();
});
```

---

### 4. **When to Use E2E Testing**

- **Critical flows**: Test user login, sign-up, checkout, and other crucial user journeys.
- **Cross-browser compatibility**: Test the app in different browsers (Cypress and Playwright support this).
- **Integration of services**: When you need to test the integration between front-end and back-end (like API calls).

---
