## Overview of Browser

### 1. What is a Browser?

#### A web browser is software that allows users to access, retrieve, and display content from the World Wide Web (WWW). The most common browsers include:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari
- Opera

### 2. How Browsers Work (High-Level Process)

1. User enters a URL - (e.g., https://www.example.com)
2. DNS Lookup happens - Converts the domain name to an IP address.
3. HTTP Request sent - The browser requests the webpage from the server.
4. Server responds - Sends back HTML, CSS, JavaScript, and other resources.
5. Browser renders the page - Converts the received content into a visual representation.

### 3. Key Components of a Browser

- User Interface (UI): The visible part of the browser that displays the webpage.
- Browser Engine: Acts as a bridge between the UI and the rendering engine.
- Rendering Engine: Converts HTML, CSS, and JavaScript into a visible webpage. Different browsers use different rendering engines (e.g., Chrome uses Blink, Firefox uses Gecko).
- Networking: Handles the communication between the browser and the server.
- JavaScript Engine: Executes JavaScript code (e.g., V8 for Chrome, SpiderMonkey for Firefox).
- Storage: Includes LocalStorage, SessionStorage, Cache, Cookies, and IndexedDB.

### 4. The Rendering Process of a Web Page

1. Parsing HTML - The browser converts HTML into a DOM Tree.
2. Parsing CSS - The browser applies styles and creates the CSSOM (CSS Object Model).
3. JavaScript Execution - If JavaScript modifies the page, it updates the DOM.
4. Layout Calculation - The browser calculates the positions of elements.
5. Painting & Compositing - The final visual representation is displayed on the screen.

## What is the DOM?

#### The DOM (Document Object Model) is a programming interface provided by the browser that allows JavaScript to interact with and manipulate web pages dynamically.

### Visual Representation of a Simple DOM Tree

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

```
Document
 ├── <html>
 │    ├── <head>
 │    │    ├── <title> - "My Page"
 │    ├── <body>
 │         ├── <h1> - "Hello World"
 │         ├── <p> - "This is a paragraph."
```

## Accessing the DOM with JavaScript

- JavaScript provides a built-in document object to interact with the DOM.

```js
console.log(document.title); // Outputs: My Page
document.title = "New Title"; // Changes the page title
```

## Understanding the DOM Tree (Nodes, Elements, Attributes, Text)

#### The DOM Tree is a hierarchical representation of an HTML document, where each part of the page (tags, attributes, text, etc.) is a node.

### 1. What is a Node in the DOM?

- A node is any individual component of the DOM tree. Everything in the DOM (elements, attributes, text, etc.) is a node.

### Types of Nodes

#### Document Node

- The topmost node in the DOM tree.
- Represents the entire webpage.
- Can be accessed using document.

```js
console.log(document); // Outputs the entire DOM structure
```

#### Element Node

- Represents HTML elements (`<h1>`, `<p>`, `<div>`, etc.).
- Can contain other elements, attributes, or text.

```js
console.log(document.body); // Outputs the <body> element
console.log(document.getElementById("title")); // Selects <h1> element
```

#### Attribute Node

- Represents attributes like id, class, href, etc.
- Part of an element node (not a child of it)

```js
let heading = document.getElementById("title");
console.log(heading.getAttribute("id")); // Outputs: title
```

#### Text Node

- Represents the actual text content inside an element.

```js
let heading = document.getElementById("title");
console.log(heading.textContent); // Outputs: Hello World
```

## Comment Node

- Represents comments inside HTML.

```html
<!-- This is a comment -->
```

```js
console.log(document.childNodes); // Includes comment nodes
```

### Parent, Child & Sibling Relationships in the DOM Tree

- The DOM tree follows a hierarchical structure:
- ✅ Parent Node - The node that contains child nodes.
- ✅ Child Node - A node inside another node.
- ✅ Sibling Nodes - Nodes that share the same parent.

```html
<body>
  <h1 id="title">Hello</h1>
  <p>Paragraph</p>
</body>
```

- `<body>` is the parent of `<h1>` and `<p>`.

- `<h1>` and `<p>` are siblings.

## Dom Api

-The DOM API (Document Object Model API) provides methods and properties that allow us to select, manipulate, and interact with HTML elements dynamically using JavaScript.

### Common Document Properties:

#### document.title

- Gets or sets the page title.

#### document.URL

- Gets the current page URL.

#### document.domain

- Gets the domain name of the page.

#### document.body

- Returns the `<body>` element.

## Selecting Elements

- The DOM API provides multiple ways to select elements in JavaScript.

### A) getElementById(id) (Selects a single element by id)

```js
let heading = document.getElementById("title");
console.log(heading); // Outputs: <h1 id="title">Hello World</h1>
```

### B) getElementsByClassName(className) (Selects multiple elements by class)

```js
let paragraphs = document.getElementsByClassName("text");
console.log(paragraphs); // Outputs: HTMLCollection of <p> elements
```

### C) getElementsByTagName(tagName) (Selects elements by tag name)

```js
let allParagraphs = document.getElementsByTagName("p");
console.log(allParagraphs); // Outputs: HTMLCollection of <p> elements
```

### D) querySelector(selector) (Selects the first matching element)

```js
let firstParagraph = document.querySelector(".text");
console.log(firstParagraph); // Outputs: <p class="text">Paragraph 1</p>
```

### E) querySelectorAll(selector) (Selects all matching elements)

```js
let allParagraphs = document.querySelectorAll(".text");
console.log(allParagraphs); // Outputs: NodeList of <p> elements
```

## Selecting parent, child, sibling elements

The DOM provides various methods to navigate between elements based on their relationships.

---

### 1. Selecting the Parent Element

Use `parentElement` to get the direct parent of an element.

```js
let child = document.getElementById("child");
let parent = child.parentElement;
console.log(parent); // Outputs: <div id="container">...</div>

// Nth parent
let child = document.getElementById("child");

// Select the 2nd parent (grandparent)
let nthParent = child;
for (let i = 0; i < 2; i++) {
  if (nthParent.parentElement) {
    nthParent = nthParent.parentElement;
  } else {
    console.log("No more parents");
    break;
  }
}
console.log(nthParent.id); // Outputs: grandparent
```

### 2. Selecting Child Elements

Use `children` or `firstElementChild` / `lastElementChild` to access child elements.

```js
let list = document.getElementById("list");

// Get all child elements
console.log(list.children); // Outputs: HTMLCollection of <li> elements

// Get the first child element
console.log(list.firstElementChild); // Outputs: <li>Item 1</li>

// Get the last child element
console.log(list.lastElementChild); // Outputs: <li>Item 3</li>

// Selecting child elements by index
let list = document.getElementById("list");

// Select the 2nd child (index 1)
let secondChild = list.children[1];
console.log(secondChild.textContent); // Outputs: Item 2

// Using querySelector with nth-child (1-based index)
let thirdChild = document.querySelector("#list li:nth-child(3)");
console.log(thirdChild.textContent); // Outputs: Item 3
```

### 3. Selecting Sibling Elements

Use `nextElementSibling` and `previousElementSibling` to navigate between sibling elements.

```js
let secondItem = document.getElementById("second");

// Get the next sibling
console.log(secondItem.nextElementSibling); // Outputs: <li id="third">Item 3</li>

// Get the previous sibling
console.log(secondItem.previousElementSibling); // Outputs: <li id="first">Item 1</li>
```

## HtmlCollection vs NodeList

- When selecting elements in the DOM, you often get either an HTMLCollection or a NodeList. While they look similar, they have key differences in behavior and methods.

---

### 1. What is an HTMLCollection?

- A live collection of elements.
- Automatically updates when the DOM changes.
- Only contains Element nodes (not text nodes or comments).
- Indexed like an array but not a real array.
- Can be accessed via item(index) or [] notation

```js
let divs = document.getElementsByTagName("div"); // Returns an HTMLCollection
console.log(divs.length); // Outputs number of <div> elements
console.log(divs[0]); // Access the first <div>
```

### 2. What is a NodeList?

- A static or live collection of nodes.
- Can contain Element nodes, Text nodes, and Comments.
- Supports forEach() (if it's a static NodeList).
- Can be accessed via item(index) or [] notation.

```js
let items = document.querySelectorAll("li"); // Returns a NodeList
console.log(items.length); // Outputs number of <li> elements
items.forEach((item) => console.log(item.textContent)); // Works only for NodeList
```

### 3. Converting to an Array

- Since both HTMLCollection and NodeList are not real arrays, you may need to convert them.

Convert to an array using Array.from()

```js
let divsArray = Array.from(document.getElementsByTagName("div"));
divsArray.forEach((div) => console.log(div.textContent));
```

Convert to an array using spread syntax

```js
let listItems = [...document.querySelectorAll("li")];
listItems.forEach((item) => console.log(item.textContent));
```

#### Summary

| Feature                      | **HTMLCollection**                                   | **NodeList**                                     |
| ---------------------------- | ---------------------------------------------------- | ------------------------------------------------ |
| **Live Updates**             | ✅ Yes (updates when DOM changes)                    | ❌ No (for `querySelectorAll`)                   |
| **Supports forEach()**       | ❌ No                                                | ✅ Yes (for `querySelectorAll`)                  |
| **Contains Only Elements**   | ✅ Yes                                               | ❌ No (includes text & comments in `childNodes`) |
| **Accessed Like an Array**   | ✅ Yes (but no array methods)                        | ✅ Yes (some array-like features)                |
| **Selectors that return it** | `getElementsByTagName()`, `getElementsByClassName()` | `querySelectorAll()`, `childNodes`               |

## How to manage Attributes

- Attributes provide additional information about an element (e.g., `id`, `class`, `src`, `href`, `alt`).

### **1. Get an Attribute**

Use `getAttribute()`.

```js
let img = document.querySelector("img");
console.log(img.getAttribute("src")); // Get the `src` of an image
```

### **2. Set or Change an Attribute**

Use `setAttribute()`.

```js
img.setAttribute("src", "new-image.jpg"); // Change image source
img.setAttribute("alt", "New Image Description");

// Directly Changing an Attribute
document.querySelector("a").href = "https://example.com";
```

### **3. Remove an Attribute**

Use `removeAttribute()`.

```js
img.removeAttribute("alt"); // Removes `alt` attribute
```

### **4. Check if an Attribute Exists**

Use `hasAttribute()`.

```js
console.log(img.hasAttribute("src")); // Returns true or false
```

## Changing Content

### 1. Using innerHTML (Changes the full HTML content)

```js
document.querySelector("#box").innerHTML = "<strong>New Content</strong>";
```

### 2. Using innerText (Changes only visible text)

```js
document.querySelector("#box").innerText = "New Text";
```

### 3. Using textContent (Includes hidden text as well)

```js
document.querySelector("#box").textContent = "New Text";
```

### innerHTML vs innerText vs textContent

```js
let div = document.querySelector("#demo");

console.log(div.innerHTML); // Shows all HTML inside
console.log(div.innerText); // Shows only visible text
console.log(div.textContent); // Shows all text (including hidden text)
```

## Changing Styles

- JavaScript allows us to modify an element’s styles dynamically using the .style property.

---

### 1. Using style Property (Inline Styles)

We can directly set CSS properties on an element using JavaScript.

```js
let box = document.querySelector("#box");
box.style.color = "red"; // Changes text color to red
box.style.backgroundColor = "yellow"; // Sets background color to yellow
box.style.fontSize = "20px"; // Increases font size
box.style.border = "2px solid black"; // Adds a border
```

### **CSS Manipulation via JavaScript (classList.add(), classList.toggle())**

### 2. Using classList Methods

- Adding a Class (classList.add())
- Adds a class to the selected element.

```js
let element = document.querySelector("#box");
element.classList.add("highlight");
```

- Removing a Class (classList.remove())
- Removes a class from the element.

```js
element.classList.remove("highlight");
```

- Toggling a Class (classList.toggle())
- Adds the class if it's not present, removes it if it is.

```js
element.classList.toggle("dark-mode");
```

- Checking if a Class Exists (classList.contains())
- Returns true if the class exists, false otherwise.

```js
console.log(element.classList.contains("highlight")); // true or false
```

- Replacing a Class (classList.replace())
- Replaces an existing class with another.

```js
element.classList.replace("old-class", "new-class");
```

## Creating Elements

#### JavaScript allows us to create new HTML elements dynamically using the `document.createElement()` method. These elements can then be modified and added to the DOM.

### Steps to Create an Element

1. Create the element → document.createElement("tag")
2. Set attributes or content → .setAttribute(), .textContent, .innerHTML
3. Append the element to the DOM → .appendChild() or .append()

### 1. Using document.createElement()

- The createElement() method creates a new HTML element but does not add it to the document until explicitly appended.
- At this point, the element exists in memory but is not yet part of the page.

```js
let newElement = document.createElement("p"); // Create a <p> element
newElement.textContent = "This is a new paragraph."; // Add text
```

### 2. Appending an Element to the DOM

- Once an element is created, we can insert it into the document using:
- ✅ appendChild() – Adds the element as the last child.
- ✅ append() – Can add multiple elements or text at once.
- ✅ prepend() – Adds the element as the first child.
- ✅ insertBefore() – Inserts an element before another specified element.

```js
let container = document.getElementById("container");

// Append as the last child
container.appendChild(newElement);

// Append multiple elements or text
container.append("New Text ", newElement);

// Prepend as the first child
container.prepend(newElement);

// Insert before an existing element
let referenceElement = document.querySelector("#container p");
container.insertBefore(newElement, referenceElement);
```

## Cloning Elements (cloneNode())

- The cloneNode() method creates an exact copy of an element.

```js
// syntax
let clonedElement = element.cloneNode(true); // true -> Deep copy, false -> Shallow copy
```

```html
<div id="original">Hello, I am the original!</div>
<button onclick="cloneElement()">Clone</button>

<script>
  function cloneElement() {
    let original = document.getElementById("original");
    let clone = original.cloneNode(true); // Deep clone with child nodes
    clone.id = "cloned"; // Change ID to avoid duplicates
    document.body.appendChild(clone); // Append clone to the body
  }
</script>
```

## Replacing Elements

- The replaceChild(newElement, oldElement) method replaces an existing element with a new one.

```html
<p id="oldText">This is the old text.</p>
<button onclick="replaceElement()">Replace</button>

<script>
  function replaceElement() {
    let oldElement = document.getElementById("oldText");
    let newElement = document.createElement("p");
    newElement.textContent = "This is the new text!";
    oldElement.parentNode.replaceChild(newElement, oldElement);
  }
</script>
```

## Removing Elements

- We can remove elements using:
- ✅ parentElement.removeChild(childElement) – Works in all browsers.
- ✅ element.remove() – Modern method (not supported in older IE versions).

- Example 1: Removing an Element (Traditional Method)

```html
<p id="toRemove">Click the button to remove me.</p>
<button onclick="removeElement()">Remove</button>

<script>
  function removeElement() {
    let element = document.getElementById("toRemove");
    element.parentNode.removeChild(element); // Remove from parent
  }
</script>
```

- Example 2: Removing an Element (Modern Method)

```html
<p id="modernRemove">I will be removed with .remove()</p>
<button onclick="removeMe()">Remove</button>

<script>
  function removeMe() {
    document.getElementById("modernRemove").remove();
  }
</script>
```

## Performance Considerations in DOM Manipulation (Minimizing reflows and repaints)

- Efficient DOM manipulation is essential for smooth and fast web applications. Poorly optimized operations can cause reflows and repaints, leading to laggy user experiences.

### 1. Understanding Reflow and Repaint

- 🔹 Reflow: The browser recalculates the layout of the page when DOM changes affect size, position, or visibility of elements.
- 🔹 Repaint: The browser redraws elements when style changes (like colors, shadows, or visibility) without affecting layout.

### 2. How to Minimize Reflows and Repaints

#### ✅ 1. Avoid Direct DOM Manipulations in Loops

- ❌ Bad: Modifies the DOM multiple times inside a loop.

```js
for (let i = 0; i < 1000; i++) {
  let p = document.createElement("p");
  p.textContent = `Item ${i}`;
  document.body.appendChild(p); // Causes reflow on every iteration
}
```

- ✅ Good: Uses Document Fragment for batch operations.

```js
let fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  let p = document.createElement("p");
  p.textContent = `Item ${i}`;
  fragment.appendChild(p); // Adds elements to memory, not DOM
}
document.body.appendChild(fragment); // Single reflow & repaint
```

#### ✅ 2. Use display: none Before Making Bulk Changes

- Setting display: none removes an element from the rendering flow, allowing multiple changes without triggering reflows.

```js
let container = document.getElementById("container");
container.style.display = "none"; // Hide before updating
// Perform heavy DOM changes
container.style.display = "block"; // Show again (single reflow)
```

#### ✅ 3. Modify Classes Instead of Inline Styles

- Applying inline styles triggers layout recalculations multiple times. Instead, modify CSS classes to apply multiple style changes at once.
- ❌ Bad:

```js
element.style.width = "200px";
element.style.height = "100px";
element.style.margin = "10px";
```

- ✅ Good:

```js
element.classList.add("new-style"); // Predefined class in CSS
```

#### ✅ 4. Read and Write DOM Properties Separately

- Reading DOM properties like offsetHeight, scrollTop, clientWidth, etc., triggers reflows because the browser recalculates styles before returning values.
- ❌ Bad:

```js
element.style.width = element.offsetWidth + 10 + "px"; // Causes reflow
```

- ✅ Good:

```js
let width = element.offsetWidth; // Read first
element.style.width = width + 10 + "px"; // Modify later
```

#### ✅ 5. Use requestAnimationFrame() for Animations

- Avoid setInterval() for animations, as it doesn’t sync with the browser’s rendering cycle. Instead, use requestAnimationFrame().

```js
function animate() {
  element.style.left = element.offsetLeft + 1 + "px";
  requestAnimationFrame(animate); // Optimized for smooth animations
}
requestAnimationFrame(animate);
```

#### ✅ 6. Minimize Layout Thrashing

- Layout thrashing occurs when multiple reads and writes to the DOM happen alternately, forcing repeated reflows.
- ❌ Bad:

```js
for (let i = 0; i < elements.length; i++) {
  elements[i].style.height = elements[i].offsetHeight + "px"; // Triggers multiple reflows
}
```

- ✅ Good:

```js
let heights = [];
for (let i = 0; i < elements.length; i++) {
  heights.push(elements[i].offsetHeight); // Read in one go
}
for (let i = 0; i < elements.length; i++) {
  elements[i].style.height = heights[i] + "px"; // Modify separately
}
```

## Shadow DOM & Web Components (Intro) (Encapsulation and component-based development)

### 1. What is the Shadow DOM?

- The Shadow DOM is a way to encapsulate styles and markup within a component, preventing it from being affected by the global CSS of a webpage.
- Key Features of the Shadow DOM

  - ✅ Encapsulation – Styles and markup inside a Shadow DOM are isolated from the rest of the document.
  - ✅ Avoids CSS Conflicts – External styles won’t affect the Shadow DOM, and vice versa.
  - ✅ Used in Web Components – It is a core part of Web Components, enabling reusable UI elements.

- Example Without Shadow DOM (Style Conflict)
- Problem: The `<p>` inside #myComponent gets affected by the global style.

```html
<style>
  p {
    color: red;
  }
</style>
<p>Outside Paragraph</p>
<div id="myComponent"></div>

<script>
  let div = document.getElementById("myComponent");
  div.innerHTML = "<p>Inside Component</p>"; // This p will also turn red
</script>
```

### 2. Creating a Shadow DOM

- To prevent such conflicts, we use the Shadow DOM.
- ✅ Example: Using Shadow DOM for Encapsulation

```html
<div id="host"></div>

<script>
  let host = document.getElementById("host");
  let shadowRoot = host.attachShadow({ mode: "open" }); // Attach Shadow DOM
  shadowRoot.innerHTML = `
    <style>
      p { color: blue; } /* Styles only apply inside the Shadow DOM */
    </style>
    <p>Inside Shadow DOM</p>
  `;
</script>
```

- Now, the `<p>` inside the Shadow DOM remains blue, even if the global CSS is red!

- Shadow DOM Modes

  - open: The Shadow DOM is accessible via JavaScript (element.shadowRoot).
  - closed: The Shadow DOM is completely hidden from external scripts.

```js
let shadowRoot = host.attachShadow({ mode: "closed" });
console.log(host.shadowRoot); // null (cannot be accessed)
```

### 3. Web Components (Overview)

Web Components allow developers to create custom, reusable HTML elements using the following technologies:

- 1️⃣ Custom Elements – Define new HTML tags (`<custom-button>`, `<user-card>`).
- 2️⃣ Shadow DOM – Encapsulate styles and structure within the component.
- 3️⃣ HTML Templates – Reusable HTML structures without rendering until needed.

### 4. Creating a Web Component (Custom Element + Shadow DOM)

```html
<!-- Web Component Usage -->
<custom-button></custom-button>

<script>
  class CustomButton extends HTMLElement {
    constructor() {
      super();
      let shadow = this.attachShadow({ mode: "open" });

      shadow.innerHTML = `
        <style>
          button { background: blue; color: white; padding: 10px; border: none; }
        </style>
        <button>Click Me</button>
      `;
    }
  }

  customElements.define("custom-button", CustomButton);
</script>
```
