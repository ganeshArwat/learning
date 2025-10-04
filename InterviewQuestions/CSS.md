## ✅ **CSS Interview Questions and Answers**

---

### 1. **What is CSS?**

**Answer:**
CSS (**Cascading Style Sheets**) is used to control the layout and styling of HTML elements (colors, fonts, spacing, etc.).

---

### 2. **What are the different types of CSS?**

**Answer:**

1. **Inline** – Style inside HTML tag

   ```html
   <p style="color:red">Text</p>
   ```
2. **Internal** – In `<style>` inside `<head>`

   ```html
   <style>p { color: red; }</style>
   ```
3. **External** – Linked CSS file

   ```html
   <link rel="stylesheet" href="style.css">
   ```

---

### 3. **What is the difference between `id` and `class` selectors in CSS?**

**Answer:**

| Attribute | Selector | Use              |
| --------- | -------- | ---------------- |
| `id`      | `#id`    | Unique styling   |
| `class`   | `.class` | Reusable styling |

---

### 4. **What is the Box Model in CSS?**

**Answer:**
Every HTML element is a box with:

```
| Margin |
| Border |
| Padding |
| Content |
```

It defines spacing and layout.

---

### 5. **What’s the difference between `relative`, `absolute`, `fixed`, and `sticky` positioning?**

**Answer:**

| Type       | Relative To                                            | Scrolls? |
| ---------- | ------------------------------------------------------ | -------- |
| `relative` | Own original spot                                      | ✅        |
| `absolute` | Nearest positioned ancestor                            | ✅        |
| `fixed`    | Viewport                                               | ❌ Fixed  |
| `sticky`   | Toggles between `relative` and `fixed` based on scroll |          |

---

### 6. **What is specificity in CSS?**

**Answer:**
Specificity determines **which style rule is applied** when there are conflicting rules.

Order:
`inline style > #id > .class > tag`

---

### 7. **What is the difference between `em`, `rem`, `px`, and `%`?**

**Answer:**

| Unit  | Based On           |
| ----- | ------------------ |
| `px`  | Fixed pixels       |
| `em`  | Parent font size   |
| `rem` | Root font size     |
| `%`   | Relative to parent |

Use `rem`/`em` for responsive design.

---

### 8. **What is Flexbox in CSS?**

**Answer:**
A layout module to arrange elements in a row/column easily.

```css
display: flex;
justify-content: space-between;
align-items: center;
```

---

### 9. **What are Grid and Flexbox differences?**

| Feature   | Flexbox            | Grid              |
| --------- | ------------------ | ----------------- |
| Axis      | 1D (row or column) | 2D (row + column) |
| Alignment | Easier inline      | Complex layouts   |
| Use Case  | Nav bars, cards    | Page layout       |

---

### 10. **What are pseudo-classes and pseudo-elements?**

**Answer:**

* **Pseudo-class**: `:hover`, `:focus`, `:nth-child()`
* **Pseudo-element**: `::before`, `::after`, `::first-line`

Example:

```css
button:hover { background: blue; }
p::first-letter { font-size: 200%; }
```

---

### 11. **What does `z-index` do in CSS?**

**Answer:**
Controls **stacking order** of elements (higher = on top). Only works with positioned elements.

```css
z-index: 999;
```

---

### 12. **What is the difference between `visibility: hidden` and `display: none`?**

| Property             | Effect                      |
| -------------------- | --------------------------- |
| `display: none`      | Removes element from layout |
| `visibility: hidden` | Hides but occupies space    |

---

### 13. **How can you center an element horizontally and vertically?**

**Answer:**

Using Flexbox:

```css
display: flex;
justify-content: center;
align-items: center;
```

Or with `margin: auto` and fixed width.

---

### 14. **What is `inherit`, `initial`, and `unset` in CSS?**

**Answer:**

* `inherit`: Inherit from parent.
* `initial`: Reset to default CSS value.
* `unset`: Inherit if inheritable, otherwise initial.

---

### 15. **What is the difference between `min-width`, `max-width`, and `width`?**

| Property    | Use                       |
| ----------- | ------------------------- |
| `width`     | Exact width               |
| `min-width` | Minimum size (can grow)   |
| `max-width` | Maximum size (can shrink) |

Useful in responsive layouts.

---

### 16. **How do media queries work in CSS?**

**Answer:**
Used for **responsive design**:

```css
@media (max-width: 768px) {
  body { background: lightgray; }
}
```

---

### 17. **What is the difference between `static` and `relative` positioning?**

**Answer:**

* `static`: Default position, cannot be changed.
* `relative`: Moves relative to its original position.

---

### 18. **What is the difference between `inline`, `block`, and `inline-block`?**

| Display Type   | Starts on New Line | Width/Height |
| -------------- | ------------------ | ------------ |
| `block`        | ✅ Yes              | ✅ Yes        |
| `inline`       | ❌ No               | ❌ No         |
| `inline-block` | ❌ No               | ✅ Yes        |

---

### 19. **What are transitions in CSS?**

**Answer:**
Adds smooth animation between property changes.

```css
transition: all 0.3s ease;
```

---

### 20. **What is the difference between `opacity: 0` and `visibility: hidden`?**

**Answer:**

| Property             | Visible? | Clickable? | Occupies space? |
| -------------------- | -------- | ---------- | --------------- |
| `opacity: 0`         | ❌        | ✅ Yes      | ✅ Yes           |
| `visibility: hidden` | ❌        | ❌ No       | ✅ Yes           |

---

### 21. **What are `calc()`, `clamp()`, `min()`, and `max()` in CSS?**

**Answer:**
CSS math functions for responsive and dynamic designs:

```css
width: calc(100% - 50px);
font-size: clamp(1rem, 2vw, 2rem);
width: min(50vw, 400px);
```

| Function  | Purpose                                |
| --------- | -------------------------------------- |
| `calc()`  | Performs calculations                  |
| `min()`   | Takes the smaller value                |
| `max()`   | Takes the larger value                 |
| `clamp()` | Provides min, preferred, and max range |

---

### 22. **What is the difference between `nth-child()` and `nth-of-type()`?**

**Answer:**

```css
li:nth-child(2)      /* second child regardless of tag */
li:nth-of-type(2)    /* second <li> only */
```

* `:nth-child()` → Based on **all types** of siblings
* `:nth-of-type()` → Based on **same element type**

---

### 23. **What is the difference between `auto`, `scroll`, `hidden`, and `visible` in `overflow`?**

| Value     | Description                          |
| --------- | ------------------------------------ |
| `visible` | Default – content overflows freely   |
| `hidden`  | Cuts off overflow (no scrollbar)     |
| `scroll`  | Always shows scrollbar               |
| `auto`    | Shows scrollbar **only when needed** |

---

### 24. **What is the stacking context in CSS?**

**Answer:**
It defines how elements are layered on top of each other using `z-index`.

* New stacking context is created by:

  * `position: relative/absolute/fixed` with `z-index`
  * `opacity < 1`
  * `transform`, `filter`, `will-change`, etc.

---

### 25. **How can you create a triangle in CSS?**

**Answer:**
Using borders:

```css
.triangle {
  width: 0;
  height: 0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
  border-bottom: 20px solid red;
}
```

---

### 26. **How to apply styles based on parent hover? (CSS-only)**

**Answer:**

```css
.parent:hover .child {
  color: red;
}
```

CSS can style **child on parent hover**, but not **parent on child hover** (without JS).

---

### 27. **How do you make an element full-screen in CSS?**

**Answer:**

```css
.fullscreen {
  position: fixed;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
}
```

Useful for modals, overlays, mobile menus.

---

### 28. **What is the difference between `vh/vw` and `%`?**

| Unit | Based on                     |
| ---- | ---------------------------- |
| `%`  | Relative to parent container |
| `vw` | 1% of viewport width         |
| `vh` | 1% of viewport height        |

---

### 29. **How to make a responsive image or video container?**

**Answer:**

```css
.responsive {
  position: relative;
  padding-top: 56.25%; /* 16:9 ratio */
}
.responsive iframe {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
}
```

---

### 30. **What’s the difference between `:root` and `html` in CSS?**

**Answer:**

* `:root` is a special selector targeting the root of the document (same as `html`), but it has **higher specificity**.
* Used for **CSS variables**:

```css
:root {
  --primary-color: #1e90ff;
}
```

---

### 31. **What are custom properties (CSS variables)?**

**Answer:**

```css
:root {
  --main-color: #ff0000;
}
h1 {
  color: var(--main-color);
}
```

They support runtime updates with JavaScript.

---

### 32. **What is `will-change` in CSS?**

**Answer:**
Gives the browser a hint to optimize specific properties for performance (used with animation):

```css
.will-animate {
  will-change: transform, opacity;
}
```

Use with caution — can affect memory.

---

### 33. **What is the difference between `transition`, `animation`, and `transform`?**

| Property     | Purpose                                             |
| ------------ | --------------------------------------------------- |
| `transition` | Smooth change on trigger (hover, click)             |
| `animation`  | Keyframe-based timeline animation                   |
| `transform`  | Applies 2D/3D changes like scale, rotate, translate |

---

### 34. **How can you hide an element but keep it accessible to screen readers?**

**Answer:**

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  clip: rect(1px, 1px, 1px, 1px);
  overflow: hidden;
}
```

---

### 35. **What is the difference between `display: none` vs `opacity: 0` vs `visibility: hidden`?**

| Property             | Visible | Space Taken | Interactable           |
| -------------------- | ------- | ----------- | ---------------------- |
| `display: none`      | ❌       | ❌           | ❌                      |
| `opacity: 0`         | ❌       | ✅           | ✅ (use pointer-events) |
| `visibility: hidden` | ❌       | ✅           | ❌                      |

---

### 36. **How to style a checkbox or radio button?**

**Answer:** Use `appearance: none` (or hide input + use label):

```css
input[type="checkbox"] {
  appearance: none;
  width: 20px;
  height: 20px;
  background: #eee;
}
```

Or wrap inside a label and use `::before` + `:checked`.

---

### 37. **What is a media feature?**

**Answer:**
Part of a media query, e.g.:

```css
@media (prefers-color-scheme: dark) {
  body { background: #121212; }
}
```

Other examples: `(orientation: portrait)`, `(min-width: 768px)`, etc.

---

### 38. **How to apply styles only for printing?**

```css
@media print {
  body { color: black; background: white; }
}
```

---

### 39. **How can you style the first letter or line of a paragraph?**

```css
p::first-letter {
  font-size: 200%;
  color: red;
}
p::first-line {
  font-weight: bold;
}
```

---

### 40. **What is `pointer-events: none`?**

**Answer:**
Disables clicks, hovers, etc.

```css
button.disabled {
  pointer-events: none;
  opacity: 0.6;
}
```

---
