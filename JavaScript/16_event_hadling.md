## Understanding Events & Event Listeners.

### Events

- Events in JavaScript are actions or occurrences that happen in the browser, such as a user clicking a button, hovering over an element, typing in an input field, or submitting a form. JavaScript allows us to handle these events using event listeners.

### Event Listeners

- An event listener is a function that waits for a specific event to occur on an element and then executes a callback function

### Types of Events

#### 1️⃣ Mouse Events

- These events are triggered when a user interacts with the mouse.
  - click - Fires when an element is clicked.
  - dblclick - Fires when an element is double-clicked.
  - mousedown - Fires when the mouse button is pressed down.
  - mouseup - Fires when the mouse button is released.
  - mouseover - Fires when the mouse enters an element.
  - mouseout - Fires when the mouse leaves an element.
  - mousemove - Fires when the mouse moves over an element.
  - contextmenu - Fires when the right-click context menu is opened.

#### 2️⃣ Keyboard Events

- These events are triggered when a user interacts with the keyboard.
  - keydown - Fires when a key is pressed down.
  - keyup - Fires when a key is released.
  - keypress - (Deprecated) Fires when a key is pressed and held.

#### 3️⃣ Form Events

- These events are triggered when a user interacts with a form element.
  - submit - Fires when a form is submitted.
  - change - Fires when an input value is changed.
  - input - Fires when a user types in an input field.
  - focus - Fires when an input field gains focus.
  - blur - Fires when an input field loses focus.
  - reset - Fires when a form is reset.

#### 4️⃣ Window & Document Events

- These events are triggered by the browser or page lifecycle.
  - load - Fires when the page has fully loaded.
  - DOMContentLoaded - Fires when the HTML document is fully loaded, without waiting for styles/images.
  - resize - Fires when the window is resized.
  - scroll - Fires when the user scrolls the page.
  - unload - Fires when the page is about to be unloaded (deprecated).

#### 5️⃣ Clipboard Events

- These events are triggered when a user copies, cuts, or pastes content.
  - copy - Fires when content is copied.
  - cut - Fires when content is cut.
  - paste - Fires when content is pasted.

#### 6️⃣ Drag & Drop Events

- These events occur when elements are dragged and dropped.
  - drag - Fires while an element is being dragged.
  - dragstart - Fires when dragging starts.
  - dragend - Fires when dragging stops.
  - dragover - Fires when an element is dragged over a drop target.
  - drop - Fires when an element is dropped.

#### 7️⃣ Media Events

- These events are triggered by media elements (audio, video).
  - play - Fires when media starts playing.
  - pause - Fires when media is paused.
  - ended - Fires when media reaches the end.
  - volumechange - Fires when the volume is changed.

#### 8️⃣ Focus & Blur Events

- These events are triggered when an element gains or loses focus.
  - focus - Fires when an element gains focus.
  - blur - Fires when an element loses focus.

#### 9️⃣ Touch Events (For Mobile)

- These events are triggered when a user interacts with a touchscreen.
  - touchstart - Fires when a touch is detected.
  - touchmove - Fires when a touch moves.
  - touchend - Fires when a touch is released.

#### 🔟 Other Events

- animationstart - Fires when a CSS animation starts.
- animationend - Fires when a CSS animation ends.
- transitionend - Fires when a CSS transition ends.
- online - Fires when the browser goes online.
- offline - Fires when the browser goes offline.

## Inline vs. AddEventListener

- There are two common ways to handle events in JavaScript:
  - 1️⃣ Inline event handlers (directly inside HTML)
  - 2️⃣ addEventListener() (JavaScript-based event binding)

### 1️⃣ Inline Event Handlers

- These are event handlers written directly inside the HTML element using attributes like onclick, onmouseover, etc.

```html
<button onclick="alert('Button clicked!')">Click Me</button>
```

```html
<button onclick="sayHello()">Click Me</button>

<script>
  function sayHello() {
    alert("Hello!");
  }
</script>
```

```js
const btn = document.querySelector("button");

function greet(event) {
  console.log("greet:", event);
}

btn.onclick = greet;
```

- Pros of Inline Event Handlers

  - ✅ Quick and easy for small scripts.
  - ✅ No need for separate JavaScript files.

- Cons of Inline Event Handlers
  - ❌ Only one event handler can be assigned for every event in an element.
  - ❌ Not scalable – Difficult to manage in large projects.
  - ❌ Mixes HTML and JavaScript, which reduces code readability.
  - ❌ Cannot attach multiple event listeners to the same element.

### 2️⃣ addEventListener() Method

- This method allows us to attach event listeners dynamically in JavaScript without modifying the HTML.

```html
<button id="btn">Click Me</button>

<script>
  document.getElementById("btn").addEventListener("click", function () {
    alert("Button clicked!");
  });
</script>
```

- Pros of addEventListener()

  - ✅ Separation of concerns – Keeps JavaScript separate from HTML.
  - ✅ Can attach multiple event listeners to the same element.
  - ✅ Supports event capturing and bubbling (important for event delegation).

- Cons of addEventListener()
  - ❌ Slightly more code than inline handlers.
  - ❌ Requires DOM to be fully loaded before execution.

### 3️⃣ Can We Remove Event Listeners?

- Only addEventListener() allows us to remove an event handler.

```html
<button id="btn">Click Me</button>

<script>
  function showAlert() {
    alert("Button clicked!");
  }

  let btn = document.getElementById("btn");
  btn.addEventListener("click", showAlert);

  // Removing the event listener after 5 seconds
  setTimeout(() => {
    btn.removeEventListener("click", showAlert);
    alert("Event listener removed!");
  }, 5000);
</script>
```

## Event Object & Properties

- The event object (event or e) contains information about the event that occurred, such as the target element, mouse position, key pressed, and more.
- When an event occurs (like a click, keypress, or mouse move), the event object is automatically passed to the event handler function.

### 1️⃣ Accessing the Event Object

```html
<button id="btn">Click Me</button>

<script>
  document.getElementById("btn").addEventListener("click", function (event) {
    console.log(event); // Logs the event object
  });
</script>
```

### 2️⃣ Event Properties

#### 🔹 timestamp

- Returns the time (in milliseconds) when the event occurred.
- Useful for measuring time between events.

```js
document.addEventListener("click", function (event) {
  console.log("Event Timestamp:", event.timeStamp);
});
```

#### 🔹 target

- Returns the element that triggered the event.
- If you click a `<button>`, it will log "BUTTON".

```js
document.addEventListener("click", function (event) {
  console.log("Clicked Element:", event.target.tagName);
});
```

#### 🔹 preventDefault()

- Prevents the default action of an element (e.g., stopping a form submission or preventing a link from navigating).

```js
<a href="https://google.com" id="link">Google</a>

<script>
document.getElementById("link").addEventListener("click", function (event) {
    event.preventDefault(); // Prevents navigation
    console.log("Default action prevented");
});
</script>
```

#### 🔹 toElement (Deprecated) & srcElement

- toElement: Returns the element the pointer moved into (Mouse Events).
- srcElement: Similar to target, but mainly used in older versions of Internet Explorer.

#### 🔹 currentTarget

- Refers to the element on which the event listener is attached (not the element that triggered the event).
- If you click the button,
  - target will be "child"
  - currentTarget will be "parent"

```html
<div id="parent">
  <button id="child">Click Me</button>
</div>

<script>
  document.getElementById("parent").addEventListener("click", function (event) {
    console.log("Target:", event.target.id); // Clicked element (child)
    console.log("Current Target:", event.currentTarget.id); // Element with listener (parent)
  });
</script>
```

#### 🔹 clientX & clientY (Mouse Position in Viewport)

- Returns the X and Y coordinates of the mouse pointer relative to the viewport (browser window).

```js
document.addEventListener("mousemove", function (event) {
  console.log("Mouse Position:", event.clientX, event.clientY);
});
```

#### 🔹 screenX & screenY (Mouse Position in Screen)

- Returns the X and Y coordinates relative to the screen (including taskbar, multiple monitors, etc.).

```js
document.addEventListener("mousemove", function (event) {
  console.log("Screen Position:", event.screenX, event.screenY);
});
```

#### 🔹 `altKey`, `ctrlKey`, `shiftKey` (Modifier Keys)

- Returns true if the Alt, Ctrl, or Shift key was pressed during an event.

```js
document.addEventListener("click", function (event) {
  if (event.ctrlKey) {
    console.log("Ctrl key was pressed!");
  }
});
```

#### 🔹 key (Keyboard Key Pressed)

- Returns the key that was pressed in a keydown or keyup event.

```js
document.addEventListener("keydown", function (event) {
  console.log("Key Pressed:", event.key);
});
```

## Event Propagation (Bubbling & Capturing)

- When an event occurs on an element inside another element, the event can propagate (travel) through the DOM in two phases:

  - 1️⃣ Event Capturing (Trickling Down) – Top to Bottom
  - 2️⃣ Event Bubbling – Bottom to Top

- 🔹 Example: Understanding Event Propagation

```html
<div id="parent" style="padding: 20px; background: lightblue;">
  <button id="child">Click Me</button>
</div>

<script>
  document.getElementById("parent").addEventListener("click", function () {
    console.log("Parent Clicked!");
  });

  document.getElementById("child").addEventListener("click", function () {
    console.log("Child Clicked!");
  });
</script>
```

- If you click the `<button>` (#child), the output will be:

```
Child Clicked!
Parent Clicked!
```

### 1️⃣ Event Bubbling (Bottom to Top)

- The event starts from the clicked element (child) and moves upward to its ancestors (parent, body, etc.).
- Default behavior in JavaScript.

```js
document.getElementById("child").addEventListener(
  "click",
  function () {
    console.log("Child Clicked!");
  },
  false
); // `false` means Bubbling Phase (default)

document.getElementById("parent").addEventListener(
  "click",
  function () {
    console.log("Parent Clicked!");
  },
  false
);
```

### 2️⃣ Event Capturing (Trickling Down)

- The event starts from the top (document/root) and moves downward to the target element.
- This occurs if we pass true as the third argument in addEventListener().

```js
document.getElementById("child").addEventListener(
  "click",
  function () {
    console.log("Child Clicked!");
  },
  true
); // `true` means Capturing Phase

document.getElementById("parent").addEventListener(
  "click",
  function () {
    console.log("Parent Clicked!");
  },
  true
);
```

- Clicking the `<button>` (#child) will output:

```
Parent Clicked!
Child Clicked!
```

### 3️⃣ Stopping Event Propagation

- 🔹 stopPropagation()
  - Prevents the event from bubbling up or capturing down.

```js
document.getElementById("child").addEventListener("click", function (event) {
  event.stopPropagation(); // Stops propagation
  console.log("Child Clicked!");
});

document.getElementById("parent").addEventListener("click", function () {
  console.log("Parent Clicked!");
});
```

- Clicking the `<button>` (#child) will output:
- (No "Parent Clicked!" because propagation is stopped.)

```
Child Clicked!
```

## Event Delegation (Efficient Event Handling)

#### ❓ What is Event Delegation?

- Instead of adding event listeners to multiple child elements, we add a single listener to a parent and detect which child triggered the event using event.target.

#### 🔹 Why Use Event Delegation?

- ✅ Efficient – No need to attach multiple event listeners.
- ✅ Handles dynamic elements – Works for elements added later via JavaScript.

### 🔹 Example Without Delegation (Bad Practice)

- 🚨 Problem: If new buttons are added dynamically, they won't have event listeners.

```html
<button class="btn">Button 1</button>
<button class="btn">Button 2</button>
<button class="btn">Button 3</button>

<script>
  const buttons = document.querySelectorAll(".btn");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      console.log("Button Clicked!");
    });
  });
</script>
```

### 🔹 Example With Event Delegation (Best Practice)

- ✅ Now it works for existing & dynamically added buttons!

```html
<div id="buttonContainer">
  <button class="btn">Button 1</button>
  <button class="btn">Button 2</button>
  <button class="btn">Button 3</button>
</div>

<script>
  document
    .getElementById("buttonContainer")
    .addEventListener("click", function (event) {
      if (event.target.classList.contains("btn")) {
        // Checks if clicked element is a button
        console.log(event.target.textContent + " Clicked!");
      }
    });
</script>
```
