## ✅ **HTML Interview Questions and Answers**

---

### 1. **What is HTML?**

**Answer:**
HTML (**HyperText Markup Language**) is the standard markup language used to create web pages. It defines the structure of web content using elements (tags).

---

### 2. **What are semantic HTML elements?**

**Answer:**
Semantic elements clearly describe their meaning in the code.

Examples:

* `<article>`, `<section>`, `<header>`, `<footer>`, `<nav>`, `<aside>`, `<main>`

These improve **accessibility** and **SEO**.

---

### 3. **What’s the difference between `<div>` and `<span>`?**

**Answer:**

| Element  | Type        | Use Case              |
| -------- | ----------- | --------------------- |
| `<div>`  | Block-level | Layout/grouping       |
| `<span>` | Inline      | Text styling/grouping |

---

### 4. **What is the difference between `id` and `class` attributes?**

**Answer:**

* `id`: Unique identifier for a single element.
* `class`: Reusable identifier that can be applied to multiple elements.

---

### 5. **What is the `DOCTYPE` declaration?**

**Answer:**
`<!DOCTYPE html>` tells the browser to use **HTML5** and renders the page in **standards mode** (not quirks mode).

---

### 6. **What are meta tags in HTML?**

**Answer:**
Meta tags provide metadata about the document (not visible to users). Examples:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

They are essential for **SEO**, **responsive design**, and **character encoding**.

---

### 7. **What is the difference between `relative`, `absolute`, and `fixed` URLs in HTML?**

**Answer:**

* **Relative**: Based on current page location: `./images/logo.png`
* **Absolute**: Full path including domain: `https://site.com/logo.png`
* **Fixed**: Doesn't scroll with page (used with `position: fixed` in CSS)

---

### 8. **What is the purpose of the `alt` attribute in images?**

**Answer:**

* Provides **alternative text** for screen readers or when the image fails to load.
* Important for **accessibility** and **SEO**.

```html
<img src="profile.jpg" alt="Ganesh Arwat's Profile Photo">
```

---

### 9. **What are void elements in HTML?**

**Answer:**
Void elements are self-closing tags and do not have a closing tag.

Examples: `<img>`, `<br>`, `<hr>`, `<input>`, `<meta>`, `<link>`

---

### 10. **What is the difference between `<script>`, `<noscript>`, and `<style>` tags?**

| Tag          | Purpose                         |
| ------------ | ------------------------------- |
| `<script>`   | Embeds JavaScript               |
| `<noscript>` | Content shown if JS is disabled |
| `<style>`    | Embeds CSS styles               |

---

### 11. **What does the `defer` and `async` attribute do in a script tag?**

**Answer:**

```html
<script src="script.js" defer></script>
```

* **`defer`**: Loads JS **after** HTML parsing.
* **`async`**: Loads JS **in parallel**, may run before HTML completes.

---

### 12. **What is the use of `viewport` meta tag?**

**Answer:**
Used for **responsive design** to control how a page is displayed on different screen sizes.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

### 13. **What are data attributes in HTML?**

**Answer:**
Custom attributes that store extra data:

```html
<div data-user-id="123" data-role="admin"></div>
```

Access in JS:

```js
element.dataset.userId; // "123"
```

---

### 14. **What is the difference between `<link>` and `<style>` for CSS?**

**Answer:**

| Tag       | Used for            | Placement            |
| --------- | ------------------- | -------------------- |
| `<link>`  | External stylesheet | `<head>`             |
| `<style>` | Inline CSS block    | `<head>` or `<body>` |

---

### 15. **What are the different types of form input types in HTML5?**

**Answer:**

* `text`, `email`, `number`, `date`, `range`, `color`, `url`, `tel`, `file`, `checkbox`, `radio`, `submit`, `password`, `hidden`

```html
<input type="email">
<input type="date">
<input type="range">
```

---

### 16. **What is the difference between `readonly` and `disabled` input fields?**

**Answer:**

| Attribute  | Editable? | Submitted in Form? |
| ---------- | --------- | ------------------ |
| `readonly` | ❌ No      | ✅ Yes              |
| `disabled` | ❌ No      | ❌ No               |

---

### 17. **What is the purpose of `<label>` in forms?**

**Answer:**
Improves accessibility and usability by linking labels to inputs using the `for` attribute.

```html
<label for="email">Email</label>
<input id="email" type="email">
```

---

### 18. **Difference between block, inline, and inline-block elements?**

| Type           | Starts on new line? | Width customizable? |
| -------------- | ------------------- | ------------------- |
| `block`        | ✅ Yes               | ✅ Yes               |
| `inline`       | ❌ No                | ❌ No                |
| `inline-block` | ❌ No                | ✅ Yes               |

---

### 19. **What is the purpose of `contenteditable` attribute?**

**Answer:**
Makes any element editable by the user in the browser.

```html
<div contenteditable="true">Edit this text</div>
```

---

### 20. **Can you embed an image directly in HTML without a file?**

**Answer:**
Yes, using **Base64** data URI:

```html
<img src="data:image/png;base64,...">
```

---

### 21. **What is the `hidden` attribute in HTML?**

**Answer:**
It hides the element from the page without using CSS:

```html
<div hidden>This won't be visible</div>
```

It can be toggled via JavaScript (`element.hidden = false;`).

---

### 22. **What is the difference between `<b>` vs `<strong>` and `<i>` vs `<em>`?**

**Answer:**

| Tag        | Purpose               | Meaning     |
| ---------- | --------------------- | ----------- |
| `<b>`      | Bold text             | Visual only |
| `<strong>` | Emphasized importance | Semantic    |
| `<i>`      | Italic text           | Visual only |
| `<em>`     | Emphasized stress     | Semantic    |

Semantic tags improve accessibility and SEO.

---

### 23. **What is a `<fieldset>` and `<legend>` tag used for?**

**Answer:**

* `<fieldset>`: Groups related form inputs.
* `<legend>`: Title for the `<fieldset>` group.

```html
<fieldset>
  <legend>Contact Info</legend>
  <input type="text" placeholder="Name" />
</fieldset>
```

---

### 24. **What is the difference between `<script>` in `<head>` vs `<body>`?**

**Answer:**

* In `<head>`: Blocks rendering unless `defer` or `async` used.
* In `<body>` (end): Best for performance so HTML loads first.

---

### 25. **What is the `tabindex` attribute?**

**Answer:**
Controls the tab order of elements on a page.

* `tabindex="0"`: Element is focusable in normal tab order
* `tabindex="-1"`: Focusable only via JS (`element.focus()`)
* `tabindex="1+"`: Custom tab order (not recommended)

---

### 26. **Can you have multiple `<main>` tags in a page?**

**Answer:**
No. There should be only **one `<main>` element per page**, and it must be unique for accessibility.

---

### 27. **What is the use of `<template>` tag?**

**Answer:**
Defines HTML that is not rendered unless used via JavaScript. Common in frameworks.

```html
<template id="myTemplate">
  <div class="card">Hello</div>
</template>
```

---

### 28. **What’s the use of the `<progress>` and `<meter>` elements?**

**Answer:**

```html
<progress value="40" max="100"></progress> <!-- Task progress -->
<meter value="0.7" min="0" max="1"></meter> <!-- Confidence meter -->
```

* `<progress>`: Indeterminate or task progress
* `<meter>`: Scalar measurements (e.g., disk usage, battery)

---

### 29. **What is ARIA in HTML?**

**Answer:**
**ARIA** = Accessible Rich Internet Applications. Used to make web apps more accessible to screen readers.

Examples:

```html
<div role="button" tabindex="0">Click Me</div>
<input aria-label="Search field">
```

---

### 30. **How do you disable auto-complete in a form input?**

**Answer:**

```html
<input type="text" autocomplete="off">
```

Or on the `<form>` itself:

```html
<form autocomplete="off">
```

---

### 31. **What’s the difference between `<iframe>` and `<embed>`?**

**Answer:**

* `<iframe>`: Embed entire external pages (e.g., YouTube, another site)
* `<embed>`: Embed media like PDFs, flash (deprecated), etc.

---

### 32. **What is the difference between `rel="stylesheet"` and `rel="preload"`?**

**Answer:**

```html
<link rel="stylesheet" href="style.css">
<link rel="preload" href="style.css" as="style">
```

* `stylesheet`: Loads and applies CSS.
* `preload`: Starts loading early, but you must apply manually or elsewhere.

---

### 33. **How to create a responsive image using HTML?**

**Answer:**

```html
<img src="image.jpg" style="max-width:100%; height:auto;" alt="Image">
```

Or use the `srcset` attribute for different screen sizes.

---

### 34. **What is `contenteditable` vs `input` field?**

**Answer:**

* `contenteditable` makes any element editable.
* `input` is form control.

Use `contenteditable` when building rich text editors.

---

### 35. **What are global attributes in HTML?**

**Answer:**
Attributes that can be applied to any HTML element:

* `id`, `class`, `style`, `title`, `hidden`, `draggable`, `tabindex`, `data-*`, `contenteditable`, etc.

---

### 36. **What is the `lang` attribute in HTML?**

**Answer:**

```html
<html lang="en">
```

Defines the language of the page for:

* Accessibility tools (screen readers)
* SEO
* Auto translation

---

### 37. **How can you make an HTML element focusable?**

**Answer:**

* Use `tabindex="0"` to make a non-input element focusable.
* You can also use `autofocus` on input fields.

```html
<div tabindex="0">Focusable</div>
```

---

### 38. **What is the difference between `download` and `target="_blank"` in a link?**

```html
<a href="file.pdf" download>Download</a>
<a href="https://google.com" target="_blank">Open in new tab</a>
```

* `download`: Triggers file download
* `target="_blank"`: Opens link in new tab

---

### 39. **How do you create an accessible button with a `div`?**

**Answer:**

```html
<div role="button" tabindex="0" onclick="doSomething()">Click Me</div>
```

But prefer real `<button>` for accessibility.

---

### 40. **How do you preload images or fonts in HTML?**

**Answer:**

```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin="anonymous">
```

Improves performance by prioritizing critical assets.

---
