## Drag and Drop API

### 🎯 What is the Drag and Drop API?

#### The Drag and Drop API allows users to drag elements from one place to another in a web page.

- ✅ Key Events

| Event     | Description                                                                                  |
| --------- | -------------------------------------------------------------------------------------------- |
| dragstart | Fires when dragging starts                                                                   |
| dragover  | Fires when an element is dragged over a valid drop target (must call event.preventDefault()) |
| drop      | Fires when the dragged element is dropped                                                    |
| dragend   | Fires when the drag operation is completed                                                   |

### 🛠️ Basic Drag and Drop Example

#### 📌 1️⃣ HTML Structure

```html
<style>
  #drag-item {
    width: 100px;
    height: 100px;
    background: blue;
    color: white;
    text-align: center;
    line-height: 100px;
    cursor: grab;
  }

  #drop-zone {
    width: 200px;
    height: 200px;
    background: lightgray;
    text-align: center;
    line-height: 200px;
    margin-top: 20px;
    border: 2px dashed gray;
  }
</style>

<div id="drag-item" draggable="true">Drag Me</div>
<div id="drop-zone">Drop Here</div>
```

#### 📌 2️⃣ JavaScript Code

```js
const dragItem = document.getElementById("drag-item");
const dropZone = document.getElementById("drop-zone");

// Drag Start
dragItem.addEventListener("dragstart", function (event) {
  event.dataTransfer.setData("text", event.target.id);
  event.target.style.opacity = "0.5"; // Visual feedback
});

// Drag End
dragItem.addEventListener("dragend", function (event) {
  event.target.style.opacity = "1";
});

// Allow Drop (Prevent default)
dropZone.addEventListener("dragover", function (event) {
  event.preventDefault();
});

// Handle Drop
dropZone.addEventListener("drop", function (event) {
  event.preventDefault();
  let draggedItemId = event.dataTransfer.getData("text");
  let draggedItem = document.getElementById(draggedItemId);
  dropZone.appendChild(draggedItem);
});
```

#### 🔍 How it Works

- 1. The dragged item has draggable="true".
- 2. dragstart stores the element ID in dataTransfer.
- 3. dragover prevents default behavior to allow dropping.
- 4. drop retrieves the dragged element and appends it to the drop zone.
