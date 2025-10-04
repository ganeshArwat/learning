### 1. **What is Bootstrap?**

**Answer:**
Bootstrap is a **free, open-source CSS framework** used to build **responsive and mobile-first websites**. It includes CSS, JS, and ready-made components like modals, navbars, buttons, etc.

---

### 2. **What are the key features of Bootstrap?**

**Answer:**

* Responsive grid system
* Predefined CSS classes
* Ready-to-use UI components
* Utility classes for spacing, colors, etc.
* JavaScript plugins (Modals, Tooltips, Collapse)

---

### 3. **Which layout system does Bootstrap use?**

**Answer:**
Bootstrap uses a **12-column grid system** based on Flexbox.

```html
<div class="row">
  <div class="col-6">Left</div>
  <div class="col-6">Right</div>
</div>
```

---

### 4. **What is the difference between `container`, `container-fluid`, and `container-xxl`?**

| Class              | Behavior                                     |
| ------------------ | -------------------------------------------- |
| `.container`       | Responsive fixed-width container             |
| `.container-fluid` | Always full-width                            |
| `.container-xxl`   | Fixed width at `xxl` (1400px) and full below |

---

### 5. **What are the breakpoint ranges in Bootstrap 5?**

| Breakpoint  | Prefix | Width ≥ |
| ----------- | ------ | ------- |
| Extra small | `none` | 0px     |
| Small       | `sm`   | 576px   |
| Medium      | `md`   | 768px   |
| Large       | `lg`   | 992px   |
| X-Large     | `xl`   | 1200px  |
| XX-Large    | `xxl`  | 1400px  |

---

### 6. **How does Bootstrap handle responsiveness?**

**Answer:**
With:

* Media queries
* Responsive grid system
* Utility classes (`d-none d-md-block`, etc.)
* Flexbox-based layout

---

### 7. **How do you create a responsive layout in Bootstrap?**

```html
<div class="container">
  <div class="row">
    <div class="col-md-4">Column 1</div>
    <div class="col-md-8">Column 2</div>
  </div>
</div>
```

---

### 8. **What are utility classes in Bootstrap?**

**Answer:**
Single-purpose classes that quickly style elements. Examples:

* `.text-center`, `.bg-primary`, `.mt-3`, `.p-2`, `.d-flex`

---

### 9. **What is the use of `.d-none`, `.d-block`, `.d-sm-none`, etc.?**

**Answer:**
Responsive display utilities to show/hide elements.

```html
<div class="d-none d-md-block">Hidden on xs & sm</div>
```

---

### 10. **How do you create a navbar using Bootstrap?**

```html
<nav class="navbar navbar-expand-md navbar-light bg-light">
  <a class="navbar-brand" href="#">Brand</a>
  <div class="collapse navbar-collapse">
    <ul class="navbar-nav">
      <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
    </ul>
  </div>
</nav>
```

---

### 11. **How to add a modal in Bootstrap?**

```html
<button data-bs-toggle="modal" data-bs-target="#myModal">Open</button>

<div class="modal fade" id="myModal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">Title</div>
      <div class="modal-body">Content</div>
      <div class="modal-footer">
        <button data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
```

---

### 12. **What are Bootstrap buttons?**

**Answer:**
Use `.btn` with variants like `.btn-primary`, `.btn-danger`, etc.

```html
<button class="btn btn-success">Submit</button>
```

---

### 13. **What’s the difference between `col`, `col-auto`, and `col-6`?**

| Class      | Description                 |
| ---------- | --------------------------- |
| `col`      | Equal-width column          |
| `col-auto` | Auto width based on content |
| `col-6`    | 6/12 = 50% width            |

---

### 14. **How to align items using Bootstrap flex utilities?**

```html
<div class="d-flex justify-content-between align-items-center">
  <!-- items -->
</div>
```

---

### 15. **How to use Bootstrap with React?**

**Answer:**
Install Bootstrap via npm or use CDN.

```bash
npm install bootstrap
```

Import in `index.js` or `App.js`:

```js
import 'bootstrap/dist/css/bootstrap.min.css';
```

---

### 16. **Can Bootstrap be customized?**

**Answer:**
Yes, using:

* CSS overrides
* Custom SCSS variables
* Bootstrap customizer

---

### 17. **How do you create a responsive card layout using Bootstrap?**

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top">
  <div class="card-body">
    <h5 class="card-title">Title</h5>
    <p class="card-text">Text</p>
    <a href="#" class="btn btn-primary">Go</a>
  </div>
</div>
```

---

### 18. **What is the difference between `.form-control` and `.form-check`?**

| Class           | Purpose                    |
| --------------- | -------------------------- |
| `.form-control` | Inputs, textareas, selects |
| `.form-check`   | Checkboxes & radio groups  |

---

### 19. **How does Bootstrap support accessibility (a11y)?**

**Answer:**

* Uses ARIA attributes in JS components (e.g., `aria-hidden`, `aria-label`)
* Focus management in modals, dropdowns
* Screen-reader-only class: `.visually-hidden`

---

### 20. **What are spacing utility classes in Bootstrap?**

```html
.mt-3  /* margin-top */
.p-2   /* padding: 0.5rem */
.ms-4  /* margin-start (left in LTR) */
```

Format:
`{property}{sides}-{breakpoint}-{size}`

Examples:

* `.mt-2`, `.mb-4`, `.px-3`, `.py-5`

---

### 21. **What is the difference between Bootstrap 4 and Bootstrap 5?**

| Feature           | Bootstrap 4              | Bootstrap 5                     |
| ----------------- | ------------------------ | ------------------------------- |
| jQuery Dependency | Required                 | Removed                         |
| Grid System       | Based on Flexbox         | Improved with new gutter system |
| Utility API       | Limited                  | Enhanced, customizable          |
| Form Elements     | Legacy styling           | Overhauled with new classes     |
| Icons             | No built-in icon library | Introduced Bootstrap Icons      |

---

### 22. **What are Bootstrap helper classes?**

**Answer:**
Helper classes are quick utility classes for layout and spacing:

* `.text-center`, `.float-end`, `.position-relative`
* `.border`, `.rounded`, `.shadow`, etc.

---

### 23. **What is the difference between `collapse` and `accordion` in Bootstrap?**

**Collapse:**

```html
<a data-bs-toggle="collapse" href="#demo">Toggle</a>
<div id="demo" class="collapse">Content</div>
```

**Accordion:** (grouped collapsible items)

```html
<div class="accordion" id="myAccordion">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" data-bs-toggle="collapse" data-bs-target="#a1">
        Accordion #1
      </button>
    </h2>
    <div id="a1" class="accordion-collapse collapse show" data-bs-parent="#myAccordion">
      <div class="accordion-body">Content 1</div>
    </div>
  </div>
</div>
```

---

### 24. **How do you center a div vertically and horizontally in Bootstrap 5?**

```html
<div class="d-flex justify-content-center align-items-center vh-100">
  <div>Centered content</div>
</div>
```

---

### 25. **What is the order utility in Bootstrap?**

Used with Flexbox layout to change the order of items.

```html
<div class="order-1">Item 1</div>
<div class="order-0">Item 2</div>
```

---

### 26. **What is the difference between `.align-items-center` and `.justify-content-center`?**

| Class                     | Affects                          |
| ------------------------- | -------------------------------- |
| `.align-items-center`     | Vertical alignment (cross axis)  |
| `.justify-content-center` | Horizontal alignment (main axis) |

Both used in flexbox layout (`.d-flex`).

---

### 27. **How do you add responsive tables in Bootstrap?**

```html
<div class="table-responsive">
  <table class="table table-striped">
    ...
  </table>
</div>
```

---

### 28. **How to make columns stack vertically on small screens?**

Bootstrap’s grid is responsive by default. Example:

```html
<div class="row">
  <div class="col-md-6">Left</div>
  <div class="col-md-6">Right</div>
</div>
```

On screens `< 768px`, both columns will stack.

---

### 29. **What is the difference between `btn-group` and `btn-toolbar`?**

* `.btn-group`: Groups buttons side-by-side.
* `.btn-toolbar`: Groups multiple `.btn-group`s.

```html
<div class="btn-toolbar">
  <div class="btn-group">
    <button class="btn btn-primary">1</button>
    <button class="btn btn-primary">2</button>
  </div>
</div>
```

---

### 30. **How to disable Bootstrap tooltips or popovers on mobile?**

By adding this:

```js
if (window.innerWidth > 768) {
  new bootstrap.Tooltip(document.querySelector('[data-bs-toggle="tooltip"]'));
}
```

---

### 31. **What is the z-index utility in Bootstrap?**

Bootstrap provides utility classes like `.z-0`, `.z-1`, `.z-3`, etc., to manage stacking order.

---

### 32. **How do you create a sticky header or footer?**

```html
<header class="sticky-top bg-white">Header</header>
<footer class="fixed-bottom bg-dark text-white">Footer</footer>
```

---

### 33. **What is the difference between `.position-relative`, `.position-absolute`, `.position-fixed`, and `.position-sticky`?**

| Class                | Behavior                                       |
| -------------------- | ---------------------------------------------- |
| `.position-relative` | Positioned relative to normal flow             |
| `.position-absolute` | Positioned relative to nearest relative parent |
| `.position-fixed`    | Fixed to viewport                              |
| `.position-sticky`   | Sticks to position when scrolling              |

---

### 34. **How do you use Bootstrap in React?**

* Install: `npm install bootstrap`
* Import in `index.js` or `App.js`:

```js
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
```

---

### 35. **How to use Bootstrap with React components like modals or tooltips?**

Since Bootstrap is jQuery-free (v5), you can trigger modals/tooltips using refs or libraries like [react-bootstrap](https://react-bootstrap.github.io/) or [reactstrap](https://reactstrap.github.io/).

Example with `react-bootstrap`:

```js
import { Modal, Button } from 'react-bootstrap';

<Modal show={show}>
  <Modal.Header closeButton>Title</Modal.Header>
  <Modal.Body>Content</Modal.Body>
</Modal>
```

---

### 36. **How can you quickly create a responsive grid layout in Bootstrap?**

```html
<div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
  <div class="col">Item 1</div>
  <div class="col">Item 2</div>
  ...
</div>
```

---

### 37. **What are gutters in Bootstrap Grid?**

**Answer:**
Gaps between columns. You can control them using:

* `.g-0` to `.g-5` (both axes)
* `.gx-3`, `.gy-2` (horizontal/vertical only)

---

### 38. **How to hide/show elements only on specific devices?**

```html
<div class="d-none d-md-block">Visible on md and up</div>
<div class="d-md-none">Visible below md</div>
```

---

### 39. **How to use Bootstrap icons?**

Install:

```bash
npm install bootstrap-icons
```

Use:

```html
<i class="bi bi-house-door-fill"></i>
```

In React:

```js
import 'bootstrap-icons/font/bootstrap-icons.css';
```

---

### 40. **How to customize Bootstrap variables using SCSS?**

* Copy `_variables.scss`
* Change values (like `$primary`)
* Compile your custom SCSS build

---

