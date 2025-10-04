## ✅ Tailwind CSS Interview Questions & Answers

---

### **1. What is Tailwind CSS?**

**Answer:**
Tailwind CSS is a **utility-first CSS framework** that allows developers to build custom designs **directly in the HTML** by using utility classes like `p-4`, `text-center`, `bg-blue-500`, etc.

---

### **2. How is Tailwind CSS different from Bootstrap?**

| Feature        | Tailwind CSS                   | Bootstrap                |
| -------------- | ------------------------------ | ------------------------ |
| Approach       | Utility-first                  | Component-based          |
| Customization  | Highly customizable via config | Limited customization    |
| Design freedom | Full control over design       | Predefined UI components |
| File size      | Small with PurgeCSS            | Larger by default        |

---

### **3. How do you install Tailwind in a React project?**

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Update `tailwind.config.js`:

```js
content: ["./src/**/*.{js,jsx,ts,tsx}"]
```

In `index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

### **4. What is the purpose of the `tailwind.config.js` file?**

**Answer:**
It’s the **configuration file** where you can:

* Extend the default theme
* Add custom colors, spacing, fonts
* Configure responsive breakpoints
* Add plugins

---

### **5. What are utility classes in Tailwind?**

**Answer:**
They are single-purpose classes like:

* `p-4` → padding
* `text-xl` → font size
* `bg-red-500` → background color
* `flex`, `grid`, `justify-center`, etc.

---

### **6. How does Tailwind handle responsiveness?**

**Answer:**
With **mobile-first breakpoints** using prefixes:

* `sm:` (≥ 640px)
* `md:` (≥ 768px)
* `lg:` (≥ 1024px)
* `xl:` (≥ 1280px)
* `2xl:` (≥ 1536px)

Example:

```html
<p class="text-sm md:text-lg">Responsive Text</p>
```

---

### **7. What is the `@apply` directive?**

**Answer:**
It lets you use Tailwind classes **inside CSS** for reuse:

```css
.btn {
  @apply px-4 py-2 bg-blue-500 text-white rounded;
}
```

---

### **8. What does `group` and `group-hover` do in Tailwind?**

**Answer:**
They allow **parent-child hover** interactions.

```html
<div class="group">
  <p class="opacity-0 group-hover:opacity-100">Hovered!</p>
</div>
```

---

### **9. What is `important` in Tailwind CSS and how to enable it?**

**Answer:**
To avoid CSS specificity issues, enable:

```js
// tailwind.config.js
module.exports = {
  important: true,
};
```

---

### **10. How does Tailwind optimize CSS file size?**

**Answer:**
By using **PurgeCSS** (now built-in) to remove unused styles during production build:

```js
content: ["./src/**/*.{js,jsx,ts,tsx,html}"]
```

---

### **11. How do you center a div using Tailwind?**

```html
<div class="flex justify-center items-center h-screen">
  <p>Centered</p>
</div>
```

---

### **12. How do you make a responsive grid in Tailwind?**

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```

---

### **13. How to handle hover, focus, active states in Tailwind?**

```html
<button class="bg-blue-500 hover:bg-blue-700 focus:ring-2 active:bg-blue-900">
  Hover me
</button>
```

---

### **14. What are some common layout utilities in Tailwind?**

* `container`
* `mx-auto`, `my-4`
* `p-4`, `m-2`
* `flex`, `grid`, `absolute`, `relative`
* `w-full`, `h-screen`, `max-w-lg`

---

### **15. How do you override default theme values in Tailwind?**

```js
// tailwind.config.js
theme: {
  extend: {
    colors: {
      brand: '#1DA1F2',
    },
    spacing: {
      '72': '18rem',
    },
  },
}
```

---

### **16. What plugins are commonly used with Tailwind CSS?**

* `@tailwindcss/forms`
* `@tailwindcss/typography` (prose)
* `@tailwindcss/aspect-ratio`
* `@tailwindcss/line-clamp`

---

### **17. How do you use Tailwind in JSX (React)?**

```jsx
function Button() {
  return <button className="px-4 py-2 bg-green-500 text-white rounded">Click</button>;
}
```

---

### **18. Can you conditionally apply Tailwind classes in React?**

Yes, using template literals or libraries like `clsx` or `classnames`.

```jsx
const isActive = true;
<button className={`${isActive ? 'bg-blue-500' : 'bg-gray-300'} p-2`}>Click</button>
```

---

### **19. How to make a responsive navbar in Tailwind?**

Use `flex`, `hidden`, `md:flex`, etc.

---

### **20. What is arbitrary value support in Tailwind?**

Tailwind lets you use arbitrary values like:

```html
<div class="w-[32rem] bg-[#1da1f2]">Custom Size & Color</div>
```

---

### **21. How can you use conditional styling in Tailwind with React?**

**Answer:**
Using template literals or a utility like `clsx`:

```js
import clsx from 'clsx';

const Button = ({ active }) => (
  <button className={clsx('px-4 py-2', active ? 'bg-blue-600' : 'bg-gray-400')}>
    Submit
  </button>
);
```

---

### **22. What does the `prose` class do in Tailwind?**

**Answer:**
It comes from the **@tailwindcss/typography** plugin and applies elegant typographic styles to content like blog posts.

```html
<article class="prose lg:prose-xl">
  <h1>Tailwind Typography</h1>
  <p>This is styled beautifully with prose.</p>
</article>
```

---

### **23. What is the `aspect-ratio` plugin in Tailwind?**

**Answer:**
Maintains a consistent aspect ratio for elements like images or videos.

```html
<div class="aspect-w-16 aspect-h-9">
  <iframe src="..."></iframe>
</div>
```

---

### **24. How can you hide/show elements based on screen size in Tailwind?**

**Answer:**

```html
<p class="hidden md:block">Visible on medium and above</p>
<p class="block md:hidden">Visible below medium</p>
```

---

### **25. How do you animate elements in Tailwind?**

Tailwind provides basic animation utilities:

```html
<div class="animate-bounce">Bounce</div>
<div class="animate-ping">Ping</div>
```

Or create custom keyframes:

```js
// tailwind.config.js
theme: {
  extend: {
    animation: {
      wiggle: 'wiggle 1s ease-in-out infinite',
    },
    keyframes: {
      wiggle: {
        '0%, 100%': { transform: 'rotate(-3deg)' },
        '50%': { transform: 'rotate(3deg)' },
      },
    },
  },
}
```

---

### **26. How do you add a custom font in Tailwind CSS?**

```js
// tailwind.config.js
theme: {
  extend: {
    fontFamily: {
      custom: ['"Poppins"', 'sans-serif'],
    },
  },
}
```

```html
<h1 class="font-custom">Custom Font</h1>
```

---

### **27. What is a dark mode configuration in Tailwind?**

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class', // or 'media'
}
```

Usage:

```html
<body class="dark">
  <p class="text-black dark:text-white">Text</p>
</body>
```

---

### **28. How can you create hover effects in Tailwind?**

```html
<button class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2">
  Hover me
</button>
```

---

### **29. What is line-clamp in Tailwind?**

It truncates text after a fixed number of lines.

```html
<p class="line-clamp-2">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit...
</p>
```

Requires:

```bash
npm install @tailwindcss/line-clamp
```

---

### **30. How do you use fixed width/height in Tailwind?**

```html
<div class="w-64 h-32 bg-gray-100">Fixed Box</div>
```

Use `w-[400px]` for arbitrary values.

---

### **31. What are Z-index utilities in Tailwind?**

```html
<div class="z-0"></div>
<div class="z-10"></div>
<div class="z-50"></div>
```

Useful for modals, dropdowns, sticky headers.

---

### **32. What are some common Tailwind utility prefixes?**

| Prefix         | Use Case                |
| -------------- | ----------------------- |
| `hover:`       | On hover                |
| `focus:`       | On focus                |
| `md:`          | On medium screen        |
| `sm:hover:`    | On small screen + hover |
| `dark:`        | On dark mode            |
| `group-hover:` | On group hover          |

---

### **33. How do you implement a modal in Tailwind?**

With utilities like `fixed`, `inset-0`, `bg-black/50` (for backdrop), and `z-50`.

---

### **34. Can Tailwind be used with CSS Modules?**

Yes. But you often use Tailwind directly in JSX, or combine with `clsx` for conditional class merging.

---

### **35. How can you visually debug spacing in Tailwind?**

Add borders or backgrounds:

```html
<div class="bg-red-100 border border-red-500 m-4 p-4">Debug Spacing</div>
```

---

### **36. What are pseudo-class utilities in Tailwind?**

* `hover:`
* `focus:`
* `disabled:`
* `active:`
* `checked:`
* `group-hover:`

---

### **37. What’s the difference between `max-w-` and `w-` in Tailwind?**

* `w-` sets exact width
* `max-w-` sets max allowed width

```html
<div class="w-full max-w-xl mx-auto">Responsive container</div>
```

---

### **38. What are important Tailwind layout helpers?**

* `container`
* `flex`, `grid`
* `relative`, `absolute`, `sticky`, `fixed`
* `w-screen`, `h-screen`
* `overflow-auto`, `overflow-hidden`

---

### **39. What is arbitrary variant support in Tailwind CSS?**

Apply variants dynamically like:

```html
<div class="[&>h1]:text-3xl">
  <h1>Big title</h1>
</div>
```

---

### **40. What is DaisyUI and how is it related to Tailwind CSS?**

**Answer:**
DaisyUI is a **Tailwind-based UI component library** that adds pre-designed components like buttons, modals, navbars, and themes — all built with Tailwind utilities.

```bash
npm install daisyui
```

---