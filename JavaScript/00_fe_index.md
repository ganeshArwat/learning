## 01-Intro to the DOM and DOM Manipulation

- Overview of Browser

  - 1. What is a Browser?
  - 2. How Browsers Work (High-Level Process)
  - 3. Key Components of a Browser
  - 4. The Rendering Process of a Web Page

- What is the DOM?

- Accessing the DOM with JavaScript

- Understanding the DOM Tree (Nodes, Elements, Attributes, Text)

  - What is a Node in the DOM?
    - Types of Node
      - Document Node
      - Element Node
      - Attribute Node
      - Text Node
      - Comment Node
  - Parent, Child & Sibling Relationships in the DOM Tree
    - Parrent
    - Child
    - Sibling
  - Dom Api
  - Common Document Properties:
    - document.title
    - document.URL
    - document.domain
    - document.body

- Selecting Elements

  - getElementById("title");
  - getElementsByClassName("text");
  - getElementsByTagName("p");
  - querySelector(".text");
  - querySelectorAll(".text");

- Selecting parent, child, sibling elements

  - 1. Selecting the Parent Element
    - ele.parentElement;
  - 2. Selecting Child Elements
    - ele.children (HTMLCollection of elements) (index from 0)
    - ele.firstElementChild
    - ele.lastElementChild

- Selecting Sibling Elements

  - ele.nextElementSibling
  - previousElementSibling

- HtmlCollection vs NodeList

  - 1. What is an HTMLCollection?
    - getElementsByTagName(), getElementsByClassName() return HtmlCollection
  - 2. What is a NodeList?
    - querySelectorAll(), childNodes retuns Nodelist
  - 3. Converting to an Array
    - using Array.from()
    - using spread syntax

- How to manage Attributes

  - 1. Get an Attribute
    - Use getAttribute()
  - 2. Set or Change an Attribute
    - Use setAttribute()
  - 3. Remove an Attribute
    - removeAttribute()
  - 4. Check if an Attribute Exists
    - hasAttribute()

- Changing Content

  - 1. Using innerHTML (Changes the full HTML content)
  - 2. Using innerText (Changes only visible text)
  - 3. Using textContent (Includes hidden text as well)
  - innerHTML vs innerText vs textContent

- Changing Styles

  - 1. Using style Property (Inline Styles)
    - ele.style.propertyName = "value";
  - 2. Using classList Methods
    - element.classList.add("highlight");
    - element.classList.remove("highlight");
    - element.classList.toggle("dark-mode");
    - element.classList.contains("highlight")
    - element.classList.replace("old-class", "new-class");

- Creating Elements

  - Steps to Create an Element
  - 1. Using document.createElement()
  - 2. Set attributes or content → .setAttribute(), .textContent, .innerHTML
  - 3. Append the element to the DOM → .appendChild() or .append()
    - ✅ appendChild() – Adds the element as the last child.
    - ✅ append() – Can add multiple elements or text at once.
    - ✅ prepend() – Adds the element as the first child.
    - ✅ insertBefore() – Inserts an element before another specified element

- Cloning Elements (cloneNode())

  - let clonedElement = element.cloneNode(true); // true -> Deep copy, false -> Shallow copy

- Replacing Elements

  - oldElement.parentNode.replaceChild(newElement, oldElement);

- Removing Elements

  - parentElement.removeChild(childElement) – Works in all browsers.
  - element.remove() – Modern method (not supported in older IE versions).

- Performance Considerations in DOM Manipulation (Minimizing reflows and repaints)

  - 1. Avoid Direct DOM Manipulations in Loops
    - let fragment = document.createDocumentFragment();
  - 2. Use display: none Before Making Bulk Changes
  - 3. Modify Classes Instead of Inline Styles
  - 4. Read and Write DOM Properties Separately
  - 5. Use requestAnimationFrame() for Animations
  - 6. Minimize Layout Thrashing

- Shadow DOM & Web Components (Intro) (Encapsulation and component-based development)

  - 1. What is the Shadow DOM?
  - 2. Creating a Shadow DOM
  - 3. Web Components (Overview)
  - 4. Creating a Web Component (Custom Element + Shadow DOM)

## 02-Events & Event Handling, Bubbling & capturing

- Understanding Events & Event Listeners.
- Event Object & Properties
  - timestamp, target, preventDefault, toElement, srcElement, currentTarget, clientX, clientY, screenX, screenY, altkey, ctrlKey, shiftKey, key
- Event Propagation (Bubbling & Capturing)
- Event Delegation

## 03-Frontend Machine Coding Round: Overview & Case Studies

- Types of Frontend Machine Coding Problems
- How to Ace Frontend Machine Coding Rounds?
- Case Study 1: To-Do List App (React)
- Case Study 2: Auto-Suggest Search Bar

## 03_A-Backend Machine Coding Round: Overview & Case Studies

- Types of Backend Machine Coding Problems
- How to Ace Backend Machine Coding Rounds?
- Case Study 1: URL Shortener (Node.js + Express + MongoDB)
- Case Study 2: Rate Limiter (Express + Redis)

## 04-JavaScript Memory Leaks: Causes & Prevention

- Common Causes of Memory Leaks
  - Unused Global Variables & Timers
  - Forgotten Timers & Intervals
  - Event Listeners Not Removed
  - Closures Holding References
  - Detached DOM Elements

## 05-Http Protocol and Network Optimization

- Key Concepts of HTTP

  - Client-Server Model
  - HTTP Request Methods
  - HTTP Status Codes
  - Headers in HTTP
  - Stateless Nature
  - HTTP vs. HTTPS
  - Http 1 and Http 2 (remaining)

- Rendering Patterns

- Network Optimization
  - Reduce HTTP Requests
  - Use Caching
  - Enable Compression
  - Use a CDN (Content Delivery Network)
  - Optimize Images
  - Reduce DNS Lookups
  - Keep-Alive & HTTP/2
  - Optimize Database Queries

## 06-Observer, Throttling, Debouncing

- Observer
- Intersection Observer API (for lazy loading, infinite scrolling)
- MutationObserver (Observing DOM Changes)
- ResizeObserver
- Debouncing
- Throttling
- Debouncing vs Throttling
- Abort Controller

## 07-Local Storage & Session Storage

- Cookies
- Working with LocalStorage & SessionStorage
- Working with IndexedDB

## 08-Drag and Drop api

- drag and drop api
- Dragging multiple elements
- Dragging files from the system
- Custom styles when dragging

## Animations & Effects using DOM

- Creating Animations using JavaScript (setInterval, setTimeout, requestAnimationFrame)
- Drag and Drop API
