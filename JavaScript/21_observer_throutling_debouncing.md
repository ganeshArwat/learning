## Observer Pattern in JavaScript

- The Observer Pattern is a behavioral design pattern that allows objects (observers) to subscribe to changes in another object (subject). When the subject changes, all subscribed observers are notified.

### Where is it Used?

- Event listeners in JavaScript (addEventListener)
- Publish-Subscribe systems
- React's state management (useEffect, Redux)
- WebSockets for real-time updates

### How It Works

- There are two main components:
  - Subject (Observable) – The object being watched
  - Observers (Subscribers) – Objects that get notified when the subject changes

### Basic Example

```js
class Subject {
  constructor() {
    this.observers = []; // List of observers
  }

  subscribe(observer) {
    this.observers.push(observer); // Add observer to the list
  }

  unsubscribe(observer) {
    this.observers = this.observers.filter((obs) => obs !== observer);
  }

  notify(data) {
    this.observers.forEach((observer) => observer.update(data));
  }
}

class Observer {
  constructor(name) {
    this.name = name;
  }

  update(data) {
    console.log(`${this.name} received update:`, data);
  }
}

// Usage
const subject = new Subject();

const observer1 = new Observer("Observer 1");
const observer2 = new Observer("Observer 2");

subject.subscribe(observer1);
subject.subscribe(observer2);

subject.notify("New Data Available!"); // Notifies all observers

subject.unsubscribe(observer1);

subject.notify("More Data!"); // Only Observer 2 receives this update
```

### Real-World Example: Event Listeners

- Event listeners in JavaScript work similarly to the Observer Pattern.
- The button is the Subject.
- The handleClick function is an Observer that runs when the event occurs.

```js
function handleClick() {
  console.log("Button clicked!");
}

document.getElementById("btn").addEventListener("click", handleClick);
```

---

## Intersection Observer API

#### The Intersection Observer API lets you detect when an element enters or exits the viewport (or another parent container). It's used for:

- ✅ Lazy loading images (loading images only when needed)
- ✅ Infinite scrolling (loading more content as the user scrolls)
- ✅ Tracking element visibility (for analytics, animations, etc.)

#### How It Works

- Instead of using scroll events (which can be inefficient), the Intersection Observer API efficiently tracks element visibility.

#### Key Components:

- Target: The element being observed.
- Root: The viewport or a parent container.
- Threshold: A value (0 to 1) defining when the callback should trigger.
- Callback: A function that runs when the target appears/disappears.

### Basic Example : Detect when an element becomes visible in the viewport.

- 📌 Explanation:
  - observer.observe(target) starts observing #myElement.
  - When the element appears in the viewport, the callback logs "Element is visible".

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      console.log("Element is visible:", entry.target);
    }
  });
});

// Target element
const target = document.querySelector("#myElement");
observer.observe(target);
```

### Example: Lazy Loading Images

- Load images only when they come into view.
- 📌 How It Works:
  - Images initially have data-src instead of src.
  - When an image enters the viewport, we replace data-src with src.
  - Then, we unobserve the image (no need to track it anymore).

```js
const images = document.querySelectorAll("img[data-src]");

const imgObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.src = entry.target.dataset.src; // Load image
      observer.unobserve(entry.target); // Stop observing once loaded
    }
  });
});

images.forEach((img) => imgObserver.observe(img));
```

### Example: Infinite Scrolling

- Load more content when the user scrolls down.

- 📌 How It Works:
  - A sentinel (hidden div) at the bottom of the list is tracked.
  - When the sentinel enters the viewport, loadMoreItems() is called.
  - rootMargin: "100px" triggers it before the user reaches the bottom.

```js
const list = document.querySelector("#list");
const sentinel = document.querySelector("#sentinel"); // A hidden div at the bottom

const infiniteScrollObserver = new IntersectionObserver(
  (entries) => {
    if (entries[0].isIntersecting) {
      loadMoreItems(); // Fetch and add more items
    }
  },
  { rootMargin: "100px" }
); // Trigger before reaching the element

infiniteScrollObserver.observe(sentinel);
```

---

## MutationObserver (Observing DOM Changes) 🚀

#### The MutationObserver API lets you watch for changes in the DOM, such as:

- ✅ Adding or removing elements
- ✅ Changing attributes (like class, style, etc.)
- ✅ Modifying text content

- It's useful for:
  - ✔️ Detecting dynamic UI updates
  - ✔️ Watching for changes in a single-page app
  - ✔️ Reacting to DOM modifications in real-time

### How It Works

- Create a MutationObserver and define what changes to observe.
- Attach it to a target element.
- The callback function executes whenever a change occurs.

### Basic Example: Watching for DOM Changes

- 📌 Explanation:
  - We observe #myElement for changes in child elements, attributes, and nested elements (subtree: true).
  - Whenever a change happens, it gets logged.

```js
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    console.log("Mutation detected:", mutation);
  });
});

// Target element to observe
const targetNode = document.querySelector("#myElement");

// Configuration options: What changes to watch?
const config = { childList: true, attributes: true, subtree: true };

// Start observing
observer.observe(targetNode, config);
```

### Example: Detecting Added or Removed Elements

- 📌 Use case: Detect when new elements are dynamically added to the page (like new messages in a chat).

```js
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === "childList") {
      console.log("Element added or removed:", mutation);
    }
  });
});

observer.observe(document.body, { childList: true });
```

### Example: Watching for Attribute Changes

```js
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === "attributes") {
      console.log(`Attribute ${mutation.attributeName} changed`);
    }
  });
});

const button = document.querySelector("#myButton");
observer.observe(button, { attributes: true });
```

### Stopping the Observer

- If you no longer need to track changes, stop the observer to improve performance.

```js
observer.disconnect(); // Stops observing
```

---

## Debouncing in JavaScript

#### Debouncing is a performance optimization technique that delays the execution of a function until after a specified time has passed since the last time it was called.

- 🛠 Use Cases:
  - ✅ Search input optimization (reducing API calls)
  - ✅ Window resizing events
  - ✅ Button click handling (to prevent accidental multiple clicks)

### How It Works

- If an event keeps firing rapidly (e.g., typing in a search box), the function will only execute after the user stops for a specified delay.

### Basic Example: Debouncing a Function

- 📌 Explanation:
  - clearTimeout(timer) resets the timer whenever the function is triggered.
  - setTimeout() ensures the function runs only after the delay.

```js
function debounce(func, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => func.apply(this, args), delay);
  };
}
```

### Example: Debounced Search Input

- 📌 How It Works:
  - The search function won't run until the user stops typing for 500ms.
  - This prevents unnecessary API calls on every keystroke.

```js
const searchInput = document.getElementById("search");

function fetchResults(query) {
  console.log("Fetching results for:", query);
}

const debouncedFetchResults = debounce(fetchResults, 500);

searchInput.addEventListener("input", (e) => {
  debouncedFetchResults(e.target.value);
});
```

### Example: Preventing Button Spam Clicks

```js
const button = document.getElementById("submit");

function handleClick() {
  console.log("Button clicked!");
}

button.addEventListener("click", debounce(handleClick, 300));
```

---

## Throttling in JavaScript 🚀

#### Throttling ensures that a function executes at most once in a specified time interval, no matter how many times the event is triggered.

- 🛠 Use Cases:
  - ✅ Handling scroll events (e.g., infinite scroll)
  - ✅ Optimizing window resize events
  - ✅ Preventing button spam clicks
  - ✅ Improving performance for real-time applications

### How It Works

- Unlike debouncing, which delays execution until the event stops, throttling executes the function at regular intervals while the event is happening.

### Basic Example: Throttling a Function

- 📌 Explanation:
  - Date.now() checks the current timestamp.
  - The function only runs if enough time (interval) has passed since the last execution.

```js
function throttle(func, interval) {
  let lastExecutedTime = 0;
  return function (...args) {
    const now = Date.now();
    if (now - lastExecutedTime >= interval) {
      func.apply(this, args);
      lastExecutedTime = now;
    }
  };
}
```

### Example: Throttling Scroll Events

- 📌 How It Works:
  - The function executes once per second no matter how fast the user scrolls.
  - Reduces performance overhead caused by frequent scroll events.

```js
const handleScroll = () => {
  console.log("Scroll event triggered at", new Date().toLocaleTimeString());
};

window.addEventListener("scroll", throttle(handleScroll, 1000));
```

### Example: Throttling Button Clicks

- 📌 Use case: Ensures the button can only be clicked once every 2 seconds.

```js
const button = document.getElementById("myButton");

function handleClick() {
  console.log("Button clicked!");
}

button.addEventListener("click", throttle(handleClick, 2000));
```

---

## Debouncing vs. Throttling

- Both debouncing and throttling optimize performance by controlling how often a function executes, but they work differently.

### 🔍 Key Differences:

| Feature                     | **Debounce**                                                      | **Throttle**                                                                      |
| --------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Definition**              | Executes function **after a delay**, resetting if triggered again | Executes function **at fixed intervals**, no matter how many times it's triggered |
| **Best for**                | Search boxes, API calls, form validation                          | Scroll events, window resizing, button spam prevention                            |
| **Execution frequency**     | **Only once** after the last event                                | **Repeatedly** at fixed intervals                                                 |
| **Delays execution?**       | ✅ Yes                                                            | ❌ No                                                                             |
| **Ensures last call runs?** | ✅ Yes                                                            | ❌ No                                                                             |

### 🛠 When to Use What?

#### ✅ Use Debouncing When:

- 1️⃣ User Input Handling

  - Example: Live search (waits until user stops typing before fetching results)

- 2️⃣ Auto-Saving Forms
  - Example: Saving form data after user stops typing for 2 seconds

#### ✅ Use Throttling When:

- 1️⃣ Scrolling Events
  - Example: Infinite scrolling (only checks position every 500ms)
- 2️⃣ Window Resize Events

  - Example: Adjusting layout at most once per second

- 3️⃣ Button Click Prevention
  - Example: Preventing spam clicks on a button

---

## AbortController

#### The AbortController API allows us to abort fetch requests, event listeners, or other asynchronous tasks before they complete. This is useful for cancelling API requests, stopping infinite loops, or preventing memory leaks.

### 🛠 Use Cases:

- ✅ Cancelling API Requests (e.g., if a user types a new search query before the previous fetch completes)
- ✅ Stopping Event Listeners (e.g., removing unnecessary listeners for performance)
- ✅ Aborting Long-running Tasks (e.g., stopping a timer or interval)

### 🔍 Basic Syntax

- 📌 The signal is passed to the function we want to control, and calling abort() cancels it.

```js
const controller = new AbortController();
const signal = controller.signal;

// Abort the operation
controller.abort();
```

### 🛠 Example 1: Cancelling a Fetch Request

- ✅ If the request is still pending after 2 seconds, it gets aborted.
- ✅ No unnecessary API calls when a user navigates away or changes input quickly.

```js
const controller = new AbortController();
const signal = controller.signal;

fetch("https://jsonplaceholder.typicode.com/posts", { signal })
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => {
    if (error.name === "AbortError") {
      console.log("Fetch request was aborted!");
    } else {
      console.error("Fetch error:", error);
    }
  });

// Cancel the request after 2 seconds
setTimeout(() => {
  controller.abort();
}, 2000);
```

### 🛠 Example 2: Using AbortController in a Search Input

- ✅ Prevents unnecessary API calls when typing quickly.
- ✅ Ensures only the latest query fetches data.

```js
let controller;

document.getElementById("search").addEventListener("input", async (e) => {
  if (controller) controller.abort(); // Cancel previous request

  controller = new AbortController();
  const signal = controller.signal;

  try {
    const response = await fetch(
      `https://api.example.com/search?q=${e.target.value}`,
      { signal }
    );
    const data = await response.json();
    console.log("Search Results:", data);
  } catch (error) {
    if (error.name === "AbortError") {
      console.log("Previous request aborted!");
    } else {
      console.error("Fetch error:", error);
    }
  }
});
```

### 🛠 Example 3: Removing Event Listeners with AbortController

- ✅ Prevents unnecessary event listeners, saving memory.
- ✅ Stops tracking mouse movement after 5 seconds.

```js
const controller = new AbortController();
const signal = controller.signal;

document.addEventListener(
  "mousemove",
  () => {
    console.log("Mouse is moving...");
  },
  { signal }
);

// Remove event listener after 5 seconds
setTimeout(() => {
  controller.abort();
  console.log("Mousemove event listener removed!");
}, 5000);
```
