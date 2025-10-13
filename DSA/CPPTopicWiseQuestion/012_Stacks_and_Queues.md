# Stack

## **1️⃣ What is a Stack?**

A **stack** is a **linear data structure** that follows the **LIFO (Last In First Out)** principle.

* **Last element added is the first one to be removed**.
* Think of a stack of plates:

  ```
  Top -> [Plate3]
         [Plate2]
         [Plate1]
  Bottom
  ```

---

## **2️⃣ Basic Operations of Stack**

| Operation          | Description                             |
| ------------------ | --------------------------------------- |
| `push(x)`          | Add element `x` to the top of the stack |
| `pop()`            | Remove the top element from the stack   |
| `top()` / `peek()` | Get the top element without removing it |
| `isEmpty()`        | Check if the stack is empty             |

---

## **3️⃣ Stack Implementation**

### **a) Using Array**

```cpp
#include <iostream>
using namespace std;

class Stack {
    int* arr;
    int topIndex;
    int capacity;
public:
    Stack(int size) {
        arr = new int[size];
        capacity = size;
        topIndex = -1;
    }

    void push(int x) {
        if (topIndex == capacity - 1) {
            cout << "Stack Overflow\n";
            return;
        }
        arr[++topIndex] = x;
    }

    void pop() {
        if (topIndex == -1) {
            cout << "Stack Underflow\n";
            return;
        }
        topIndex--;
    }

    int top() {
        if (topIndex == -1) {
            cout << "Stack is empty\n";
            return -1;
        }
        return arr[topIndex];
    }

    bool isEmpty() {
        return topIndex == -1;
    }
};
```

---

### **b) Using Linked List**

```cpp
struct Node {
    int data;
    Node* next;
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class Stack {
    Node* topNode;
public:
    Stack() {
        topNode = nullptr;
    }

    void push(int x) {
        Node* newNode = new Node(x);
        newNode->next = topNode;
        topNode = newNode;
    }

    void pop() {
        if (!topNode) return;
        Node* temp = topNode;
        topNode = topNode->next;
        delete temp;
    }

    int top() {
        if (!topNode) return -1;
        return topNode->data;
    }

    bool isEmpty() {
        return topNode == nullptr;
    }
};
```

---

## **4️⃣ Stack Example**

```cpp
Stack s;
s.push(10);
s.push(20);
s.push(30);

cout << s.top() << endl; // 30
s.pop();
cout << s.top() << endl; // 20
```

**Output:**

```
30
20
```

---

## **5️⃣ Common Stack Applications**

1. **Expression Evaluation**

   * Convert infix to postfix
   * Evaluate postfix expressions

2. **Undo/Redo Functionality**

3. **Backtracking Problems**

   * Maze solving, pathfinding

4. **Browser History**

   * Back/forward buttons

5. **Call Stack**

   * Function calls in recursion

---

## **1️⃣ Include the Stack Header**

```cpp
#include <stack>
#include <iostream>
using namespace std;
```

---

## **2️⃣ Create a Stack**

```cpp
stack<int> s;  // stack of integers
```

* `stack<int>` creates a stack that stores integers.
* You can also use other types: `stack<string>`, `stack<char>`, etc.

---

## **3️⃣ Push Elements**

```cpp
s.push(10);  // Stack: [10]
s.push(20);  // Stack: [10, 20]
s.push(30);  // Stack: [10, 20, 30]
```

* Adds elements to the **top** of the stack.

---

## **4️⃣ Access the Top Element**

```cpp
cout << "Top element: " << s.top() << endl;  // Output: 30
```

* `top()` returns the element **currently at the top** of the stack.
* It **does not remove** the element.

---

## **5️⃣ Pop Elements**

```cpp
s.pop();  // Removes 30
```

* Removes the **top element**.
* Does **not return** the value (use `top()` before `pop()` if needed).

---

## **6️⃣ Check Size**

```cpp
cout << "Stack size: " << s.size() << endl;  // Output: 2
```

* Returns the **number of elements** in the stack.

---

## **7️⃣ Check if Empty**

```cpp
if (s.empty()) {
    cout << "Stack is empty" << endl;
} else {
    cout << "Stack is not empty" << endl;  // Output here
}
```

* `empty()` returns `true` if the stack has **no elements**, otherwise `false`.

---

## ✅ **Quick Example**

```cpp
#include <stack>
#include <iostream>
using namespace std;

int main() {
    stack<int> s;
    
    s.push(10);
    s.push(20);
    s.push(30);

    cout << "Top element: " << s.top() << endl; // 30
    s.pop();
    cout << "Stack size: " << s.size() << endl; // 2

    if (s.empty()) cout << "Stack is empty" << endl;
    else cout << "Stack is not empty" << endl;

    return 0;
}
```

**Output:**

```
Top element: 30
Stack size: 2
Stack is not empty
```

---

## **Q1. Passing Game**

**Problem Idea:**

* You have a series of passes in a football game.
* `0` means **pass back** to the previous player.
* Any other ID means **pass forward** to that player.
* We need to know **who has the ball at the end**.

**Why Stack?**

* Stack works perfectly because you can **track the history of ball possession**.
* Push when passing forward, pop when passing back.

**Code:**

```cpp
int Solution::solve(int A, int B, vector<int> &C) {
    stack<int> s;
    s.push(B);  // initial player

    for (int i = 0; i < A; i++) {
        if (C[i] == 0) {
            s.pop();  // back pass
        } else {
            s.push(C[i]);  // forward pass
        }
    }

    return s.top();  // player with ball at the end
}
```

**Example Walkthrough:**

```
Initial: B = 23, Stack: [23]
C[0] = 86 → push → Stack: [23, 86]
C[1] = 63 → push → Stack: [23, 86, 63]
C[2] = 60 → push → Stack: [23, 86, 63, 60]
C[3] = 0 → pop → Stack: [23, 86, 63]
... final stack top = 63
```

✅ Answer: **63**

---

## **Q2. Balanced Parentheses**

**Problem Idea:**

* Check if all `{}`, `[]`, `()` are **balanced**.
* Example: `{([])}` → balanced, `()[]{` → not balanced.

**Why Stack?**

* Push **opening brackets**, pop when **matching closing bracket** is found.

**Code:**

```cpp
int Solution::solve(string A) {
    stack<char> s;
    
    for (char c : A) {
        if (c == '(' || c == '[' || c == '{') {
            s.push(c);
        } else {
            if (s.empty()) return 0;
            if ((c == ')' && s.top() != '(') ||
                (c == ']' && s.top() != '[') ||
                (c == '}' && s.top() != '{')) {
                return 0;
            }
            s.pop();
        }
    }
    
    return s.empty() ? 1 : 0;
}
```

---

## **Q3. Double Character Trouble**

**Problem Idea:**

* Remove consecutive identical characters repeatedly.
* Example: `"abccbc"` → `"ac"`

**Why Stack?**

* Stack allows **checking the previous character** easily.

**Code:**

```cpp
string Solution::solve(string A) {
    stack<char> s;

    for (char c : A) {
        if (!s.empty() && s.top() == c) {
            s.pop();  // remove pair
        } else {
            s.push(c);
        }
    }

    string result;
    while (!s.empty()) {
        result += s.top();
        s.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}
```

---

## **Q4. Evaluate Expression (Reverse Polish Notation)**

**Problem Idea:**

* Evaluate **postfix expressions** like `["2","1","+","3","*"]`
* Postfix means operator comes **after operands**.

**Why Stack?**

* Stack stores **operands**.
* When operator comes, pop two operands → apply operator → push result.

**Code:**

```cpp
int Solution::evalRPN(vector<string> &A) {
    stack<int> s;

    for (string token : A) {
        if (token == "+" || token == "-" || token == "*" || token == "/") {
            int b = s.top(); s.pop();
            int a = s.top(); s.pop();
            if (token == "+") s.push(a + b);
            else if (token == "-") s.push(a - b);
            else if (token == "*") s.push(a * b);
            else s.push(a / b);
        } else {
            s.push(stoi(token));
        }
    }

    return s.top();
}
```

---

## **Q5. Infix to Postfix**

**Problem Idea:**

* Convert **infix** expression `"a+b*(c^d-e)^(f+g*h)-i"` to **postfix**.
* Example output: `"abcd^e-fgh*+^*+i-"`

**Why Stack?**

* Stack stores **operators** until they can be added to postfix.
* Handles **operator precedence** and parentheses.

**Code:**

```cpp
string Solution::solve(string A) {
    string ans;
    stack<char> s;
    map<char, int> precedence;
    precedence['^'] = 3;
    precedence['*'] = 2;
    precedence['/'] = 2;
    precedence['+'] = 1;
    precedence['-'] = 1;
    precedence['('] = 0;

    for (char c : A) {
        if (!precedence.count(c)) { // operand
            ans += c;
        } else if (c == '(') {
            s.push(c);
        } else if (c == ')') {
            while (!s.empty() && s.top() != '(') {
                ans += s.top(); s.pop();
            }
            s.pop(); // remove '('
        } else { // operator
            while (!s.empty() && precedence[s.top()] >= precedence[c]) {
                ans += s.top(); s.pop();
            }
            s.push(c);
        }
    }

    while (!s.empty()) {
        ans += s.top(); s.pop();
    }

    return ans;
}
```

---

### ✅ Summary of Stack Usage

| Problem                  | Stack Role                                  |
| ------------------------ | ------------------------------------------- |
| Passing Game             | Track **history of ball possession**        |
| Balanced Parentheses     | Check **matching brackets**                 |
| Double Character Trouble | Track **previous character**                |
| Reverse Polish Notation  | Store **operands for operators**            |
| Infix to Postfix         | Store **operators according to precedence** |

---

## **Q1. Min Stack**

**Problem Idea:**

* Implement a stack that can return the **minimum element in O(1) time**.
* Operations: `push`, `pop`, `top`, `getMin`.
* Edge case: if stack is empty, return `-1`.

**Why Stack with Trick?**

* Normal stack doesn't track minimum efficiently.
* We use **trick formula** when pushing smaller values:

[
\text{store } 2x - \text{minEle if x < minEle}
]

* `min_ele` always stores the current minimum.

**Code Explanation:**

```cpp
stack<int> s;
int min_ele;

MinStack::MinStack() {
    min_ele = INT_MAX;
    while(!s.empty()) s.pop();
}

void MinStack::push(int x) {
    if(s.empty()){
        s.push(x);
        min_ele = x;
    } else {
        if(x < min_ele){
            s.push(2*x - min_ele); // special encoding
            min_ele = x;
        } else {
            s.push(x);
        }
    }
}

void MinStack::pop() {
    if(s.empty()) return;
    int top = s.top();
    if(top < min_ele){
        min_ele = 2*min_ele - top; // restore previous minimum
    }
    s.pop();
}

int MinStack::top() {
    if(s.empty()) return -1;
    int top = s.top();
    return (top < min_ele) ? min_ele : top;
}

int MinStack::getMin() {
    return s.empty() ? -1 : min_ele;
}
```

✅ This allows **all operations in O(1) time**.

---

## **Q2. Redundant Braces**

**Problem Idea:**

* Find **extra braces** in an expression.
* Example: `"((a+b))"` → redundant because one pair is enough.

**Why Stack?**

* Stack keeps **track of characters inside parentheses**.
* When we see `)`, check if there was **any operator** inside.
* No operator → redundant.

**Code Explanation:**

```cpp
int Solution::braces(string A) {
    stack<char> st;

    for (char ch : A) {
        if (ch == ')') {
            bool hasOperator = false;

            while (!st.empty() && st.top() != '(') {
                if (st.top() == '+' || st.top() == '-' || st.top() == '*' || st.top() == '/')
                    hasOperator = true;
                st.pop();
            }

            if (!st.empty()) st.pop(); // pop '('
            if (!hasOperator) return 1; // redundant
        } else {
            st.push(ch);
        }
    }

    return 0; // no redundant braces
}
```

---

## **Q3. Check Two Bracket Expressions**

**Problem Idea:**

* Compare two expressions with `+`, `-`, `(`, `)` and **check if equivalent**.
* Example: `-(a+b+c)` and `-a-b-c` → same result.

**Why Stack?**

* Use stack to **track sign flips** due to `-` before parentheses.
* Maintain a **sign multiplier** for each variable.

**Code Explanation:**

```cpp
vector<int> check(string t) {
    vector<int> res(26, 0);
    stack<bool> s;
    s.push(true); // initial sign

    for(int i = 0; i < t.size(); i++) {
        char c = t[i];

        if(c == '+' || c == '-') continue;

        else if(c == '(' && i > 0) {
            if(t[i-1] == '-') s.push(!s.top());
            else s.push(s.top());
        } 
        else if(c >= 'a' && c <= 'z') {
            if(i > 0 && t[i-1] == '-') res[c-'a'] = s.top() ? -1 : 1;
            else res[c-'a'] = s.top() ? 1 : -1;
        } 
        else if(c == ')') s.pop();
    }

    return res;
}

int Solution::solve(string A, string B) {
    vector<int> vec1 = check(A);
    vector<int> vec2 = check(B);

    return (vec1 == vec2) ? 1 : 0;
}
```

**Explanation with Example:**

```
A = "-(a+b+c)"
Initial stack: [true] (positive)
'-' flips sign → push(!top) = false
'(a+b+c)' → assign sign -1 to a,b,c
Stack after ')' → pop
Result: [-1,-1,-1,...]
B = "-a-b-c" → same vector
vec1 == vec2 → 1
```

✅ Works perfectly to **compare expressions ignoring parentheses** using **stack for sign propagation**.

---

## **Q1. Nearest Smaller Element (Previous Smaller)**

**Problem Idea:**

* For every element `A[i]`, find the **nearest smaller element to its left**.
* If none exists, return `-1`.

**Why Stack?**

* Stack stores **indices of elements in increasing order**.
* While processing `A[i]`, pop all elements `>= A[i]`.
* Top of stack → **nearest smaller element**.

**Code:**

```cpp
vector<int> Solution::prevSmaller(vector<int> &A) {
    vector<int> result(A.size(), -1);  
    stack<int> s;  // store indices

    for (int i = 0; i < A.size(); ++i) {
        while (!s.empty() && A[s.top()] >= A[i])
            s.pop();  // remove bigger/equal elements
        
        if (!s.empty())
            result[i] = A[s.top()];  // nearest smaller element
        
        s.push(i);
    }

    return result;
}
```

✅ **Time Complexity:** O(n)
✅ **Space Complexity:** O(n)

---

## **Q2. Largest Rectangle in Histogram**

**Problem Idea:**

* Each bar has width 1 and height `A[i]`.
* Find **largest rectangle area**.

**Why Stack?**

* Stack stores **indices of bars in increasing order**.
* When current bar is smaller → calculate rectangle with bar at stack top as height.
* Width = distance between current index and previous index in stack.

**Code:**

```cpp
int Solution::largestRectangleArea(vector<int> &A) {
    stack<int> s;
    int maxArea = 0, i = 0;

    while (i < A.size()) {
        if (s.empty() || A[i] >= A[s.top()]) s.push(i++);
        else {
            int height = A[s.top()]; s.pop();
            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, height * width);
        }
    }

    while (!s.empty()) {
        int height = A[s.top()]; s.pop();
        int width = s.empty() ? i : i - s.top() - 1;
        maxArea = max(maxArea, height * width);
    }

    return maxArea;
}
```

---

## **Q3. Sum of Max-Min of All Subarrays**

**Problem Idea:**

* Sum of `(max - min)` for all subarrays.
* Use **Next/Previous Greater and Smaller** arrays to count contribution of each element.

**Logic:**

* `maxContribution = (i - prevGreater[i]) * (nextGreater[i] - i)`
* `minContribution = (i - prevSmaller[i]) * (nextSmaller[i] - i)`
* Add `(A[i]*maxContribution - A[i]*minContribution)` to total.

**Code Snippet (Functions for NG, PG, NS, PS):**

```cpp
vector<int> findNextGreater(const vector<int>& A);
vector<int> findPrevGreater(const vector<int>& A);
vector<int> findNextSmaller(const vector<int>& A);
vector<int> findPrevSmaller(const vector<int>& A);

int Solution::solve(vector<int> &A) {
    int n = A.size();
    const int MOD = 1e9+7;

    vector<int> nextGreater = findNextGreater(A);
    vector<int> prevGreater = findPrevGreater(A);
    vector<int> nextSmaller = findNextSmaller(A);
    vector<int> prevSmaller = findPrevSmaller(A);

    long long totalSum = 0;

    for (int i = 0; i < n; ++i) {
        long long maxC = (long long)(i - prevGreater[i]) * (nextGreater[i] - i) % MOD;
        long long minC = (long long)(i - prevSmaller[i]) * (nextSmaller[i] - i) % MOD;
        totalSum = (totalSum + A[i] * maxC - A[i] * minC + MOD) % MOD;
    }

    return (int)totalSum;
}
```

---

## **Q4. Next Greater Element**

**Problem Idea:**

* For each `A[i]`, find the **first greater element to the right**.
* If none → `-1`.

**Why Stack?**

* Stack stores **indices of decreasing elements**.
* If current element > top of stack → it is the **next greater** for all popped elements.

**Code:**

```cpp
vector<int> Solution::nextGreater(vector<int> &A) {
    int n = A.size();
    vector<int> result(n, -1);
    stack<int> s;

    for (int i = 0; i < n; ++i) {
        while (!s.empty() && A[i] > A[s.top()]) {
            result[s.top()] = A[i];
            s.pop();
        }
        s.push(i);
    }

    return result;
}
```

✅ **Time Complexity:** O(n)
✅ **Space Complexity:** O(n)

---

## **Q1. Max Rectangle in Binary Matrix**

**Problem Idea:**

* We have a **binary matrix** (0s and 1s).
* Find the **largest rectangle of 1s**.
* Each row can be treated as a **histogram**, where height is the consecutive 1s in that column.

**How it Works:**

1. Initialize a `height` array of size `cols` with 0.
2. For each row `i`:

   * Update `height[j] = 0` if `A[i][j] == 0` else `height[j] += 1`.
   * Now treat `height` as a histogram → find **largest rectangle**.
3. Use the **Largest Rectangle in Histogram** algorithm we discussed before.

**Code:**

```cpp
int largestRectangleArea(const vector<int>& heights) {
    stack<int> st;
    int maxArea = 0, index = 0;

    while (index < heights.size()) {
        if (st.empty() || heights[st.top()] <= heights[index]) {
            st.push(index++);
        } else {
            int topOfStack = st.top(); st.pop();
            int area = heights[topOfStack] * (st.empty() ? index : index - st.top() - 1);
            maxArea = max(maxArea, area);
        }
    }

    while (!st.empty()) {
        int topOfStack = st.top(); st.pop();
        int area = heights[topOfStack] * (st.empty() ? index : index - st.top() - 1);
        maxArea = max(maxArea, area);
    }

    return maxArea;
}

int Solution::maximalRectangle(vector<vector<int>> &A) {
    if (A.empty() || A[0].empty()) return 0;

    int rows = A.size(), cols = A[0].size();
    vector<int> height(cols, 0);
    int maxRectangle = 0;

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            height[j] = (A[i][j] == 0) ? 0 : height[j] + 1;
        }
        maxRectangle = max(maxRectangle, largestRectangleArea(height));
    }

    return maxRectangle;
}
```

✅ **Time Complexity:** O(N * M)
✅ **Space Complexity:** O(M)

---

## **Q2. Sort Stack Using Another Stack**

**Problem Idea:**

* You are given a stack.
* Sort it **using only one extra stack** (no recursion).
* Return the sorted elements in ascending order.

**How it Works:**

1. Use `tempStack` to build sorted elements.
2. For each element `current` in `inputStack`:

   * While top of `tempStack > current`, pop from `tempStack` back to `inputStack`.
   * Push `current` to `tempStack`.
3. After all elements are processed, `tempStack` contains **sorted elements in descending order**.
4. Reverse them to get ascending order.

**Code:**

```cpp
vector<int> Solution::solve(vector<int> &A) {
    stack<int> inputStack, tempStack;
    vector<int> result;

    // Push all elements into inputStack
    for (int num : A) inputStack.push(num);

    // Sort using tempStack
    while (!inputStack.empty()) {
        int current = inputStack.top(); inputStack.pop();

        while (!tempStack.empty() && tempStack.top() > current) {
            inputStack.push(tempStack.top());
            tempStack.pop();
        }

        tempStack.push(current);
    }

    // Transfer sorted elements to result (ascending order)
    while (!tempStack.empty()) {
        result.push_back(tempStack.top());
        tempStack.pop();
    }

    reverse(result.begin(), result.end());
    return result;
}
```

✅ **Time Complexity:** O(n²) (worst case)
✅ **Space Complexity:** O(n)

---

# Queue

---

## **1. What is a Queue?**

A **queue** is a linear data structure that follows the **FIFO** principle:

**FIFO → First In, First Out**

* The first element added to the queue will be the first one to be removed.
* Think of it like a line at a ticket counter: the person who comes first gets served first.

---

## **2. Basic Operations in a Queue**

| Operation        | Description                                          |
| ---------------- | ---------------------------------------------------- |
| `enqueue`        | Add an element to the **rear** (end) of the queue    |
| `dequeue`        | Remove an element from the **front** of the queue    |
| `peek` / `front` | Look at the element at the front without removing it |
| `isEmpty`        | Check if the queue is empty                          |
| `size`           | Number of elements in the queue                      |

---

## **3. Example**

Imagine a queue of numbers:

```
Queue: 10, 20, 30
```

* **Enqueue 40:** Add at the rear → `10, 20, 30, 40`
* **Dequeue:** Remove from front → `20, 30, 40`
* **Peek/Front:** 20

---

## **4. Types of Queues**

1. **Simple Queue** – basic FIFO.
2. **Circular Queue** – last position connects back to the first to utilize space efficiently.
3. **Priority Queue** – elements are dequeued based on priority, not order of insertion.
4. **Deque (Double-Ended Queue)** – insertion and deletion at both ends.

---

## **1. Queue using STL (`queue` library)**

C++ provides a built-in `queue` in the `<queue>` header.

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;

    // Enqueue (push)
    q.push(10);
    q.push(20);
    q.push(30);

    cout << "Front element: " << q.front() << endl; // 10
    cout << "Rear element: " << q.back() << endl;   // 30

    // Dequeue (pop)
    q.pop();
    cout << "After dequeue, front: " << q.front() << endl; // 20

    // Check if empty
    if (q.empty())
        cout << "Queue is empty" << endl;
    else
        cout << "Queue is not empty" << endl;

    // Size
    cout << "Queue size: " << q.size() << endl;

    return 0;
}
```

**Output:**

```
Front element: 10
Rear element: 30
After dequeue, front: 20
Queue is not empty
Queue size: 2
```

---

## **2. Queue using Array (Manual Implementation)**

```cpp
#include <iostream>
using namespace std;

#define SIZE 5

class Queue {
private:
    int arr[SIZE];
    int front, rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    bool isEmpty() {
        return front == -1;
    }

    bool isFull() {
        return rear == SIZE - 1;
    }

    void enqueue(int x) {
        if (isFull()) {
            cout << "Queue Overflow\n";
            return;
        }
        if (isEmpty()) front = 0;
        rear++;
        arr[rear] = x;
        cout << x << " enqueued\n";
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow\n";
            return;
        }
        cout << arr[front] << " dequeued\n";
        if (front == rear) {
            front = rear = -1; // Queue becomes empty
        } else {
            front++;
        }
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return;
        }
        cout << "Queue elements: ";
        for (int i = front; i <= rear; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    q.display();

    q.dequeue();
    q.display();

    return 0;
}
```

**Output:**

```
10 enqueued
20 enqueued
30 enqueued
Queue elements: 10 20 30
10 dequeued
Queue elements: 20 30
```

---

✅ **Key Points in C++ Queues:**

1. STL `queue` is easiest to use.
2. Manual implementation using arrays gives understanding of **front** and **rear** pointers.
3. For large dynamic queues, use **`std::deque`** or **linked list implementation**.

---

# **1️⃣ Queue Using Linked List**

A **linked list queue** dynamically grows as elements are added.
We maintain two pointers:

* `front` → points to the first element (to dequeue).
* `rear` → points to the last element (to enqueue).

### **Code:**

```cpp
#include <iostream>
using namespace std;

// Node structure
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Queue class
class Queue {
private:
    Node* front;  
    Node* rear;   
    int currentSize;

public:
    // Constructor
    Queue() : front(nullptr), rear(nullptr), currentSize(0) {}

    // Enqueue: add element at rear
    void enqueue(int element) {
        Node* newNode = new Node(element);
        if (rear == nullptr) {  // Queue empty
            front = rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
        currentSize++;
        cout << "Enqueued " << element << endl;
    }

    // Dequeue: remove element from front
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty. Cannot dequeue." << endl;
            return;
        }
        Node* temp = front;
        front = front->next;
        if (front == nullptr) rear = nullptr; // Queue is empty now
        cout << "Dequeued " << temp->data << endl;
        delete temp;
        currentSize--;
    }

    // Get front element
    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return -1;
        }
        return front->data;
    }

    // Get rear element
    int getRear() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return -1;
        }
        return rear->data;
    }

    // Check if empty
    bool isEmpty() {
        return front == nullptr;
    }

    // Size
    int size() {
        return currentSize;
    }

    // Destructor
    ~Queue() {
        while (!isEmpty()) {
            dequeue();
        }
    }
};

// Driver
int main() {
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "Front: " << q.getFront() << endl;
    cout << "Rear: " << q.getRear() << endl;

    q.dequeue();
    cout << "Front after dequeue: " << q.getFront() << endl;

    return 0;
}
```

✅ **Key Points:**

* `enqueue()` → O(1) time.
* `dequeue()` → O(1) time.
* Dynamic memory means no size limit.
* `front` moves forward on dequeue, `rear` always points to last node.

---

# **2️⃣ Queue Using 2 Stacks**

A **queue using 2 stacks** is a common **algorithmic trick**.

* `stack1` → store elements as they come (enqueue).
* `stack2` → store elements in reverse order to simulate dequeue.

### **Code:**

```cpp
#include <iostream>
#include <stack>
using namespace std;

class Queue {
private:
    stack<int> stack1;
    stack<int> stack2;

    // Move elements from stack1 to stack2
    void transferStack1ToStack2() {
        while (!stack1.empty()) {
            stack2.push(stack1.top());
            stack1.pop();
        }
    }

public:
    // Enqueue
    void enqueue(int element) {
        stack1.push(element);
        cout << "Enqueued " << element << endl;
    }

    // Dequeue
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty. Cannot dequeue." << endl;
            return;
        }
        if (stack2.empty()) transferStack1ToStack2();
        cout << "Dequeued " << stack2.top() << endl;
        stack2.pop();
    }

    // Get front
    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return -1;
        }
        if (stack2.empty()) transferStack1ToStack2();
        return stack2.top();
    }

    // Check if empty
    bool isEmpty() {
        return stack1.empty() && stack2.empty();
    }
};

// Driver
int main() {
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "Front: " << q.getFront() << endl;

    q.dequeue();
    cout << "Front after dequeue: " << q.getFront() << endl;

    return 0;
}
```

✅ **Key Points:**

* `enqueue()` → O(1) time.
* `dequeue()` → Amortized O(1) (elements move from stack1 to stack2 only when stack2 is empty).
* Clever way to **simulate a queue with only stacks**.

---

💡 **Visualization for 2 Stacks Queue:**

```
Enqueue: push to stack1
stack1: [10,20,30] (bottom -> top)

Dequeue:
stack2 empty → transfer stack1 to stack2
stack2: [30,20,10] (top -> bottom)
Pop from stack2 → 10 (FIFO behavior)
```

---

Absolutely! Let’s go **step by step** and understand all the problems you’ve shared. I’ll explain the **logic, approach, and code** clearly so it’s easy to grasp.

---

# **1️⃣ Queue Using Stacks (FIFO Queue)**

The idea: simulate a **queue** using **two stacks**.

* `stack1` → for enqueue (push).
* `stack2` → for dequeue (pop/peek).

**Approach:**

* Push new elements into `stack1`.
* When dequeuing or peeking: if `stack2` is empty, transfer all elements from `stack1` to `stack2` (reverses order, giving FIFO behavior).

### **Code:**

```cpp
#include <iostream>
#include <stack>
using namespace std;

class UserQueue {
private:
    stack<int> stack1, stack2;

    void moveStack1ToStack2() {
        while (!stack1.empty()) {
            stack2.push(stack1.top());
            stack1.pop();
        }
    }

public:
    void push(int X) {
        stack1.push(X);
    }

    int pop() {
        if (stack2.empty()) moveStack1ToStack2();
        int front = stack2.top();
        stack2.pop();
        return front;
    }

    int peek() {
        if (stack2.empty()) moveStack1ToStack2();
        return stack2.top();
    }

    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};

int main() {
    UserQueue q;
    q.push(10);
    q.push(20);
    cout << q.pop() << endl;  // 10
    cout << q.peek() << endl; // 20
    cout << q.empty() << endl; // false
}
```

**✅ Key Points:**

* `push` → O(1)
* `pop/peek` → Amortized O(1)

---

# **2️⃣ Perfect Numbers (Palindrome with 1 & 2, Even Length)**

The idea: generate numbers with **only 1 and 2**, form a **palindrome**, and find the A-th number.

* Use a **queue** to generate numbers level by level (BFS style).
* Mirror the number to make it palindrome.

### **Code:**

```cpp
#include <iostream>
#include <queue>
using namespace std;

string perfectNumber(int A) {
    queue<string> q;
    q.push("1");
    q.push("2");

    string firstHalf, perfectNum;

    for (int i = 0; i < A; ++i) {
        firstHalf = q.front();
        q.pop();

        perfectNum = firstHalf + string(firstHalf.rbegin(), firstHalf.rend());

        q.push(firstHalf + "1");
        q.push(firstHalf + "2");
    }

    return perfectNum;
}

int main() {
    cout << perfectNumber(2) << endl; // 22
    cout << perfectNumber(3) << endl; // 111
}
```

**✅ Key Points:**

* BFS generates numbers in order.
* Use **string reverse** to create palindrome.

---

# **3️⃣ Sliding Window Maximum (Ice Cream Truck Problem)**

The idea: for each **window of size B**, find the **maximum** efficiently.

* Use a **deque** to store indices of elements in decreasing order.
* The front of the deque is always the **maximum of current window**.

### **Code:**

```cpp
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

vector<int> slidingMaximum(const vector<int> &A, int B) {
    vector<int> result;
    deque<int> dq;

    for (int i = 0; i < A.size(); ++i) {
        if (!dq.empty() && dq.front() == i - B) dq.pop_front();

        while (!dq.empty() && A[dq.back()] <= A[i]) dq.pop_back();

        dq.push_back(i);

        if (i >= B - 1) result.push_back(A[dq.front()]);
    }

    return result;
}

int main() {
    vector<int> arr = {1, 3, -1, -3, 5, 3, 6, 7};
    int B = 3;
    vector<int> res = slidingMaximum(arr, B);

    for (int x : res) cout << x << " "; // 3 3 5 5 6 7
}
```

**✅ Key Points:**

* Efficient: O(n) using deque.
* Avoids recomputing maximum for each window.

---

# **4️⃣ N integers containing only 1, 2, 3**

The idea: generate numbers with digits **1, 2, 3** in increasing order.

* Use **queue** and BFS style generation.
* Start with 1, 2, 3 → append 1, 2, 3 to each number.

### **Code:**

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> generateNumbers(int A) {
    vector<int> result;
    queue<int> q;

    q.push(1);
    q.push(2);
    q.push(3);

    while (result.size() < A) {
        int current = q.front();
        q.pop();

        result.push_back(current);

        q.push(current*10 + 1);
        q.push(current*10 + 2);
        q.push(current*10 + 3);
    }

    return result;
}

int main() {
    int A = 7;
    vector<int> res = generateNumbers(A);

    for (int x : res) cout << x << " "; // 1 2 3 11 12 13 21
}
```

**✅ Key Points:**

* BFS style ensures ascending order.
* Queue stores “current numbers” to generate next numbers.

---

💡 **Summary of Queue Usage:**

1. **Queue of stacks** → simulate FIFO using LIFO.
2. **Queue for generating numbers** → BFS ensures order.
3. **Deque for sliding window max** → maintain decreasing elements efficiently.

---

# **1️⃣ Reversing Elements of Queue**

**Problem:** Reverse the first `B` elements of an array using a **queue and stack**.

**Approach:**

1. Push all elements into a queue (`q`).
2. Pop the first `B` elements from the queue and push them into a stack (`s`).

   * Stack reverses the order of these elements.
3. Pop elements from the stack to result → reversed order.
4. Append remaining elements from the queue → original order.

### **Code:**

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

vector<int> reverseFirstB(vector<int> &A, int B) {
    queue<int> q;
    stack<int> s;
    vector<int> result;

    // Insert all elements into queue
    for (int num : A) q.push(num);

    // Reverse first B elements
    for (int i = 0; i < B; ++i) {
        s.push(q.front());
        q.pop();
    }

    // Add reversed elements to result
    while (!s.empty()) {
        result.push_back(s.top());
        s.pop();
    }

    // Add remaining elements
    while (!q.empty()) {
        result.push_back(q.front());
        q.pop();
    }

    return result;
}

int main() {
    vector<int> A = {1, 2, 3, 4, 5};
    int B = 3;
    vector<int> res = reverseFirstB(A, B);

    for (int x : res) cout << x << " "; // 3 2 1 4 5
}
```

**✅ Key Point:** Stack reverses the order, queue maintains the rest.

---

# **2️⃣ Sum of Min and Max of Subarrays of Size B**

**Problem:** For each subarray of size `B`, compute sum of **minimum + maximum**.

**Efficient Approach:**

* Use **two deques**: one for **max**, one for **min**.
* Deque stores **indices of elements** in decreasing/increasing order.
* Slide the window → remove out-of-window elements.

### **Code:**

```cpp
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

vector<int> Subarray(vector<int> &A, int B, string op) {
    deque<int> dq;
    vector<int> ans;
    int n = A.size();

    for (int i = 0; i < B; i++) {
        if (op == "max") {
            while (!dq.empty() && A[dq.back()] <= A[i]) dq.pop_back();
        } else {
            while (!dq.empty() && A[dq.back()] >= A[i]) dq.pop_back();
        }
        dq.push_back(i);
    }

    ans.push_back(A[dq.front()]);

    for (int i = B; i < n; i++) {
        if (op == "max") {
            while (!dq.empty() && A[dq.back()] <= A[i]) dq.pop_back();
        } else {
            while (!dq.empty() && A[dq.back()] >= A[i]) dq.pop_back();
        }
        dq.push_back(i);

        if (dq.front() == i - B) dq.pop_front();

        ans.push_back(A[dq.front()]);
    }

    return ans;
}

int sumOfMinMax(vector<int> &A, int B) {
    vector<int> maxSub = Subarray(A, B, "max");
    vector<int> minSub = Subarray(A, B, "min");
    int n = maxSub.size();
    long long sum = 0;
    long long MOD = 1000000007;

    for (int i = 0; i < n; i++) {
        sum = (sum + maxSub[i] + minSub[i] + MOD) % MOD;
    }

    return (int)sum;
}

int main() {
    vector<int> A = {2, 5, -1, 7, -3, -1, -2};
    int B = 4;
    cout << sumOfMinMax(A, B) << endl; // 18
}
```

**✅ Key Points:**

* Deque maintains **candidates for max/min** in O(1) amortized per operation.
* Total complexity → **O(n)**.

---

# **3️⃣ First Unique Letter in a Stream**

**Problem:** For a stream of letters, after each letter, output **first non-repeating character**; if none, output `#`.

**Approach:**

1. Use **unordered_map** to store **frequency** of each character.
2. Use **queue** to store characters in order of appearance.
3. For each new character:

   * Increment frequency.
   * Push into queue if it’s first occurrence.
   * Pop from queue until front is **unique**.
4. Append front of queue to result; if empty → `#`.

### **Code:**

```cpp
#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;

string firstUniqueLetter(string A) {
    unordered_map<char, int> freq;
    queue<char> q;
    string result;

    for (char ch : A) {
        freq[ch]++;

        if (freq[ch] == 1) q.push(ch);

        while (!q.empty() && freq[q.front()] > 1) q.pop();

        if (q.empty()) result += '#';
        else result += q.front();
    }

    return result;
}

int main() {
    string A = "abadbc";
    cout << firstUniqueLetter(A) << endl; // aabbc#
}
```

**✅ Key Points:**

* Queue keeps track of **first unique character in order**.
* Map keeps **frequency count**.
* Total complexity → **O(n)**.

---

💡 **Summary of Techniques:**

| Problem                     | Data Structure  | Purpose                                           |
| --------------------------- | --------------- | ------------------------------------------------- |
| Reverse first B elements    | Queue + Stack   | Queue stores all, Stack reverses first B          |
| Sum of min/max in subarrays | Deque           | Maintain candidates for max/min in sliding window |
| First unique letter         | Queue + HashMap | Queue for order, HashMap for frequency            |

---
