
# **1️⃣ Linked List Basics**

### **Node Structure**

```cpp
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};
```

### **Creating a simple list**

```cpp
ListNode* head = new ListNode(1);
head->next = new ListNode(2);
head->next->next = new ListNode(3);
// List: 1 -> 2 -> 3
```

### **Traversing a list**

```cpp
ListNode* temp = head;
while (temp != NULL) {
    cout << temp->val << " ";
    temp = temp->next;
}
cout << endl; // Output: 1 2 3
```

---

# **2️⃣ Insertion**

### **Insert at Head**

```cpp
ListNode* newNode = new ListNode(0);
newNode->next = head;
head = newNode;  // New list: 0 -> 1 -> 2 -> 3
```

### **Insert at Kth Position**

```cpp
int pos = 2;
int value = 99;
ListNode* node = new ListNode(value);
ListNode* temp = head;

for (int i = 1; i < pos; i++) temp = temp->next;

node->next = temp->next;
temp->next = node;
// List: 0 -> 1 -> 99 -> 2 -> 3
```

---

# **3️⃣ Deletion**

### **Delete at Position**

```cpp
int pos = 2;
ListNode* temp = head;

if (pos == 0) {
    head = head->next;
} else {
    for (int i = 1; i < pos; i++) temp = temp->next;
    temp->next = temp->next->next;
}
// List after deletion: 0 -> 1 -> 2 -> 3
```

### **Delete all duplicates in sorted list**

```cpp
ListNode* curr = head;
while (curr && curr->next) {
    if (curr->val == curr->next->val) {
        ListNode* nextNode = curr->next;
        curr->next = curr->next->next;
        delete nextNode;
    } else {
        curr = curr->next;
    }
}
```

---

# **4️⃣ Reverse Linked List**

### **Iterative**

```cpp
ListNode* prev = NULL;
ListNode* curr = head;
while (curr) {
    ListNode* nextNode = curr->next;
    curr->next = prev;
    prev = curr;
    curr = nextNode;
}
head = prev;
// List reversed
```

### **Reverse between B and C**

```cpp
int B = 2, C = 4;
ListNode* dummy = new ListNode(0);
dummy->next = head;
ListNode* pre = dummy;
for (int i = 1; i < B; i++) pre = pre->next;

ListNode* start = pre->next;
ListNode* then = start->next;

for (int i = 0; i < C-B; i++) {
    start->next = then->next;
    then->next = pre->next;
    pre->next = then;
    then = start->next;
}
head = dummy->next;
```

---

# **5️⃣ Palindrome Linked List**

```cpp
// Step 1: Find middle
ListNode* slow = head;
ListNode* fast = head;
while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
}

// Step 2: Reverse second half
ListNode* prev = NULL;
while (slow) {
    ListNode* nextNode = slow->next;
    slow->next = prev;
    prev = slow;
    slow = nextNode;
}

// Step 3: Compare halves
ListNode* first = head;
ListNode* second = prev;
bool isPalindrome = true;
while (second) {
    if (first->val != second->val) {
        isPalindrome = false;
        break;
    }
    first = first->next;
    second = second->next;
}
```

---

# **6️⃣ K-Group Reversal**

```cpp
int B = 2; // group size
ListNode* dummy = new ListNode(0);
dummy->next = head;
ListNode* pre = dummy;
ListNode* curr;
ListNode* nex;

// Count total nodes
int count = 0;
curr = head;
while(curr){ count++; curr=curr->next; }

// Reverse in groups
while(count >= B){
    curr = pre->next;
    nex = curr->next;
    for(int i=1;i<B;i++){
        curr->next = nex->next;
        nex->next = pre->next;
        pre->next = nex;
        nex = curr->next;
    }
    pre = curr;
    count -= B;
}
head = dummy->next;
```

---

# **🔑 Patterns & Tips**

1. **Dummy node**: Handles edge cases (head changes) cleanly.
2. **Two pointers**: `prev/curr/next` for reversal.
3. **Slow/Fast pointers**: For finding mid in palindrome or cycle detection.
4. **Iterative traversal**: Always check `NULL` before accessing `next`.
5. **K-group reversal**: Always track group boundaries carefully.

---

# **1️⃣ Palindrome Linked List**

**Problem:** Check if a linked list reads the same forward and backward.

**Concepts:**

1. Find middle of the list (slow/fast pointer technique)
2. Reverse second half of the list
3. Compare first half with reversed second half

```cpp
int Solution::lPalin(ListNode* A) {
    if (!A || !A->next) return 1; // Empty or single node list is always palindrome

    // Step 1: Find middle
    ListNode *slow = A, *fast = A;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Step 2: Reverse second half
    ListNode *prev = NULL, *curr = slow;
    while (curr) {
        ListNode* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }

    // Step 3: Compare halves
    ListNode *first = A, *second = prev;
    while (second) {
        if (first->val != second->val) return 0;
        first = first->next;
        second = second->next;
    }
    return 1;
}
```

✅ **Tip:** Slow/Fast pointers → `slow` ends at middle, `fast` reaches end.
✅ Reversing in-place saves memory.

---

# **2️⃣ Remove N-th Node from End**

**Problem:** Delete the B-th node from the end.

**Concepts:**

1. Count length of the list
2. Find the node **just before** the one to delete
3. Remove it by adjusting pointers

```cpp
ListNode* Solution::removeNthFromEnd(ListNode* A, int B) {
    int N = 0;
    ListNode* temp = A;
    while (temp) { N++; temp = temp->next; }

    // If B >= N, remove head
    if (B >= N) return A->next;

    temp = A;
    for (int i = 1; i < N-B; i++) temp = temp->next;

    temp->next = temp->next->next; // Remove B-th node from end
    return A;
}
```

✅ **Tip:** If `B > N`, delete the first node.
✅ Counting first makes it easy to locate the target node.

---

# **3️⃣ Remove Duplicates from Sorted List**

**Problem:** Remove all duplicates so each element appears once.

```cpp
ListNode* Solution::deleteDuplicates(ListNode* A) {
    if (!A) return NULL;
    ListNode* temp = A;
    while (temp->next) {
        if (temp->val == temp->next->val) {
            temp->next = temp->next->next; // Skip duplicate
        } else {
            temp = temp->next;
        }
    }
    return A;
}
```

✅ Works **only for sorted lists**.
✅ Time complexity: O(N), Space: O(1).

---

# **4️⃣ Reverse Linked List Between Positions B and C**

**Problem:** Reverse a sublist in-place.

**Concepts:**

1. Use a **dummy node** to handle edge cases
2. Navigate to node **before B**
3. Reverse nodes B to C using pointer manipulation

```cpp
ListNode* Solution::reverseBetween(ListNode* A, int B, int C) {
    if (!A || B == C) return A;

    ListNode* dummy = new ListNode(0);
    dummy->next = A;
    ListNode* preB = dummy;
    for (int i = 1; i < B; i++) preB = preB->next;

    ListNode* start = preB->next;
    ListNode* then = start->next;
    for (int i = 0; i < C-B; i++) {
        start->next = then->next;
        then->next = preB->next;
        preB->next = then;
        then = start->next;
    }
    return dummy->next;
}
```

✅ **Dummy node trick:** Helps reverse from head without extra checks.
✅ Reverse by **inserting nodes one by one** at start of sublist.

---

# **5️⃣ K-Group Reverse**

**Problem:** Reverse nodes in groups of size B.

```cpp
ListNode* Solution::reverseList(ListNode* A, int B) {
    if (!A || B == 1) return A;

    ListNode* dummy = new ListNode(0);
    dummy->next = A;
    ListNode* pre = dummy;
    ListNode* curr, *nex;

    int count = 0;
    curr = A;
    while (curr) { count++; curr = curr->next; }

    while (count >= B) {
        curr = pre->next;
        nex = curr->next;
        for (int i = 1; i < B; i++) {
            curr->next = nex->next;
            nex->next = pre->next;
            pre->next = nex;
            nex = curr->next;
        }
        pre = curr;
        count -= B;
    }
    return dummy->next;
}
```

✅ Similar to **reverse between B and C**, but repeated in **groups**.

---

# **6️⃣ Longest Palindromic List**

**Problem:** Find max length palindrome in the list.

**Concepts:**

1. Reverse while traversing
2. Check **odd/even length palindrome** using helper

```cpp
int countPalindrome(ListNode* left, ListNode* right) {
    int length = 0;
    while (left && right && left->val == right->val) {
        length += 2;
        left = left->next;
        right = right->next;
    }
    return length;
}

int Solution::solve(ListNode* A) {
    if (!A) return 0;

    int maxLength = 1;
    ListNode* prev = NULL;
    ListNode* curr = A;

    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;

        // Odd length palindrome (center = curr)
        if (prev) maxLength = max(maxLength, 1 + countPalindrome(prev, next));

        // Even length palindrome (center between prev & curr)
        if (next) maxLength = max(maxLength, countPalindrome(curr, next));

        prev = curr;
        curr = next;
    }
    return maxLength;
}
```

✅ **Trick:** Reverse nodes on the fly while checking palindrome.
✅ Time: O(N²), Space: O(1).

---

# **1️⃣ Sort Linked List (Merge Sort)**

**Problem:** Sort a linked list in `O(n log n)`.

**Concepts:**

* Merge sort works well for linked lists.
* Steps:

  1. Find the middle of the list.
  2. Recursively sort both halves.
  3. Merge the sorted halves.

```cpp
ListNode* merge(ListNode* l1, ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    
    while (l1 && l2) {
        if (l1->val < l2->val) { current->next = l1; l1 = l1->next; }
        else { current->next = l2; l2 = l2->next; }
        current = current->next;
    }
    
    if (l1) current->next = l1;
    if (l2) current->next = l2;
    
    return dummy->next;
}

ListNode* getMiddle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

ListNode* Solution::sortList(ListNode* A) {
    if (!A || !A->next) return A;
    ListNode* mid = getMiddle(A);
    ListNode* nextToMid = mid->next;
    mid->next = NULL;
    
    ListNode* left = sortList(A);
    ListNode* right = sortList(nextToMid);
    
    return merge(left, right);
}
```

✅ **Tip:** Merge sort is preferred because **O(n log n)** works for large lists and avoids random access issues of linked lists.

---

# **2️⃣ Merge Two Sorted Lists**

**Problem:** Merge two sorted lists into one sorted list.

```cpp
ListNode* Solution::mergeTwoLists(ListNode* A, ListNode* B) {
    if (!A) return B;
    if (!B) return A;
    
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    
    while (A && B) {
        if (A->val < B->val) { current->next = A; A = A->next; }
        else { current->next = B; B = B->next; }
        current = current->next;
    }
    
    if (A) current->next = A;
    if (B) current->next = B;
    
    return dummy->next;
}
```

✅ **Trick:** Use a **dummy node** to simplify head handling.

---

# **3️⃣ Remove Loop from Linked List (Floyd’s Cycle Detection)**

**Problem:** Detect a loop and remove it.

**Concepts:**

* Use **slow and fast pointers** to detect cycle.
* Find start of the loop.
* Break the loop.

```cpp
ListNode* Solution::solve(ListNode* A) {
    if (!A || !A->next) return A;
    
    ListNode* slow = A;
    ListNode* fast = A;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) break;
    }
    
    if (slow != fast) return A;  // No loop
    
    slow = A;
    while (slow != fast) { slow = slow->next; fast = fast->next; }
    
    ListNode* cycleStart = slow;
    ListNode* temp = cycleStart;
    while (temp->next != cycleStart) temp = temp->next;
    
    temp->next = NULL; // Remove loop
    return A;
}
```

✅ **Floyd’s Algorithm** is O(N) time, O(1) space.

---

# **4️⃣ Middle Element of Linked List**

**Problem:** Find the middle element. If even nodes, return `(N/2 + 1)`.

```cpp
int Solution::solve(ListNode* A) {
    ListNode* slow = A;
    ListNode* fast = A;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    return slow->val;
}
```

✅ **Trick:** Slow/Fast pointer → slow lands exactly at middle.

---

# **5️⃣ Swap Nodes in Pairs**

**Problem:** Swap every 2 adjacent nodes **in-place**.

```cpp
ListNode* Solution::swapPairs(ListNode* head) {
    if (!head || !head->next) return head;
    
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* prev = dummy;
    
    while (head && head->next) {
        ListNode* first = head;
        ListNode* second = head->next;
        
        first->next = second->next;
        second->next = first;
        prev->next = second;
        
        prev = first;
        head = first->next;
    }
    
    return dummy->next;
}
```

✅ **Tip:** Only swap **pointers**, not node values.

---

# **6️⃣ Reorder List (L0→Ln→L1→Ln-1...)**

**Problem:** Reorder a list in-place.

**Concepts:**

1. Find middle.
2. Reverse second half.
3. Merge halves alternatingly.

```cpp
ListNode* reverse(ListNode* head) {
    ListNode* prev = NULL;
    while (head) {
        ListNode* nxt = head->next;
        head->next = prev;
        prev = head;
        head = nxt;
    }
    return prev;
}

ListNode* Solution::reorderList(ListNode* A) {
    if (!A->next || !A->next->next) return A;
    
    ListNode* slow = A;
    ListNode* fast = A;
    while (fast->next && fast->next->next) { slow = slow->next; fast = fast->next->next; }
    
    ListNode* head2 = reverse(slow->next);
    slow->next = NULL;
    ListNode* head1 = A;
    
    ListNode* dummy = new ListNode(-1);
    ListNode* node = dummy;
    bool flag = true;
    
    while (head2) {
        if (flag) { node->next = head1; node = head1; head1 = head1->next; flag = false; }
        else { node->next = head2; node = head2; head2 = head2->next; flag = true; }
    }
    if (head1) node->next = head1;
    return dummy->next;
}
```

✅ **Trick:** Merge two halves alternatingly for reorder.

---

# **7️⃣ Add Two Numbers Represented as Linked Lists**

**Problem:** Digits stored in **reverse order**, return sum as a linked list.

```cpp
ListNode* Solution::addTwoNumbers(ListNode* A, ListNode* B) {
    ListNode* dummy = new ListNode(-1);
    ListNode* curr = dummy;
    int carry = 0;
    
    while (A || B || carry) {
        int x = A ? A->val : 0;
        int y = B ? B->val : 0;
        int sum = x + y + carry;
        carry = sum / 10;
        curr->next = new ListNode(sum % 10);
        curr = curr->next;
        if (A) A = A->next;
        if (B) B = B->next;
    }
    
    return dummy->next;
}
```

✅ Handles **different lengths** and carry efficiently.

---

# Doubly Linked List

---

## **1️⃣ What is a Doubly Linked List?**

A **Doubly Linked List** is a type of linked list in which **each node has two pointers**:

1. **prev** → points to the **previous node**
2. **next** → points to the **next node**

```
NULL <- [prev|data|next] <-> [prev|data|next] <-> [prev|data|next] -> NULL
```

**Key points:**

* Allows **traversal in both directions** (forward and backward).
* Extra pointer (`prev`) compared to singly linked list.
* Useful for **insertions/deletions at both ends** efficiently.

---

## **2️⃣ Node Structure**

Here’s a basic C++ struct for a doubly linked list node:

```cpp
struct Node {
    int data;
    Node* prev;
    Node* next;
    
    Node(int val) {
        data = val;
        prev = nullptr;
        next = nullptr;
    }
};
```

---

## **3️⃣ Basic Operations**

### **a) Insert at the Beginning**

```cpp
void insertAtHead(Node*& head, int val) {
    Node* newNode = new Node(val);
    newNode->next = head; // new node points to old head
    if (head != nullptr) head->prev = newNode; // old head points back
    head = newNode; // update head
}
```

**Example:**

```
Insert 10 -> 10
Insert 20 -> 20 <-> 10
Insert 30 -> 30 <-> 20 <-> 10
```

---

### **b) Insert at the End**

```cpp
void insertAtTail(Node*& head, int val) {
    Node* newNode = new Node(val);
    if (head == nullptr) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != nullptr) temp = temp->next;
    temp->next = newNode;
    newNode->prev = temp;
}
```

---

### **c) Delete a Node**

```cpp
void deleteNode(Node*& head, Node* delNode) {
    if (head == nullptr || delNode == nullptr) return;
    
    // If node to delete is head
    if (head == delNode) head = delNode->next;
    
    if (delNode->next != nullptr) delNode->next->prev = delNode->prev;
    if (delNode->prev != nullptr) delNode->prev->next = delNode->next;
    
    delete delNode;
}
```

---

### **d) Traverse Forward**

```cpp
void printForward(Node* head) {
    Node* temp = head;
    while (temp) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}
```

### **e) Traverse Backward**

```cpp
void printBackward(Node* tail) {
    Node* temp = tail;
    while (temp) {
        cout << temp->data << " ";
        temp = temp->prev;
    }
    cout << endl;
}
```

---

## **4️⃣ Visualization**

```
Head
 ↓
NULL <- 10 <-> 20 <-> 30 -> NULL
             ↑         ↑
           prev       next
```

* `10.prev` = NULL, `10.next` = 20
* `20.prev` = 10, `20.next` = 30
* `30.prev` = 20, `30.next` = NULL

---

## **5️⃣ Advantages over Singly Linked List**

1. Can traverse **both directions**.
2. **Efficient insertion/deletion** at both ends or in the middle.
3. Easier to implement **LRU Cache, Undo/Redo, Browser History**.

---

# **1️⃣ Intersection of Two Linked Lists**

**Problem:** Find the node where two singly linked lists intersect.

**Concepts:**

* If lists intersect, they share the tail nodes.
* Use **two pointers** and switch heads to equalize path lengths.
* Time complexity: **O(n + m)**, Space: **O(1)**.

**Code & Explanation:**

```cpp
ListNode* Solution::getIntersectionNode(ListNode* A, ListNode* B) {
    if (!A || !B) return nullptr;
    
    ListNode* pA = A;
    ListNode* pB = B;
    
    while (pA != pB) {
        pA = (pA == nullptr) ? B : pA->next;
        pB = (pB == nullptr) ? A : pB->next;
    }
    
    return pA; // Either intersection or nullptr
}
```

✅ **Trick:** Switching the heads ensures both pointers travel **same total length** before meeting.

---

# **2️⃣ LRU Cache**

**Problem:** Implement an LRU cache with `get` and `set` in **O(1)**.

**Concepts:**

* Use a **Doubly Linked List** to maintain order.
* Use a **HashMap** to store keys → node pointers.
* `head` = LRU, `tail` = MRU.

**Code Snippet & Explanation:**

```cpp
class Node {
public:
    int key, val;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

Node* head;
Node* tail;
int N;   // current size
int MAX; // capacity
map<int, Node*> mp;

void remove(Node* x) {
    x->prev->next = x->next;
    x->next->prev = x->prev;
}

void insertEnd(Node* x) {
    x->next = tail;
    x->prev = tail->prev;
    tail->prev->next = x;
    tail->prev = x;
}

Node* removeFront() {
    Node* temp = head->next;
    remove(temp);
    return temp;
}

LRUCache::LRUCache(int capacity) {
    head = new Node(0,0);
    tail = new Node(0,0);
    head->next = tail;
    tail->prev = head;
    MAX = capacity;
    N = 0;
    mp.clear();
}

int LRUCache::get(int key) {
    if (mp.find(key) != mp.end()) {
        remove(mp[key]);
        insertEnd(mp[key]);
        return mp[key]->val;
    }
    return -1;
}

void LRUCache::set(int key, int value) {
    if (mp.find(key) != mp.end()) {
        remove(mp[key]);
        mp[key]->val = value;
        insertEnd(mp[key]);
    } else {
        Node* newNode = new Node(key, value);
        mp[key] = newNode;
        if (N == MAX) {
            Node* t = removeFront();
            mp.erase(t->key);
            insertEnd(newNode);
        } else {
            N++;
            insertEnd(newNode);
        }
    }
}
```

✅ **Trick:** Doubly linked list allows **O(1) removal & insertion**, hash map provides **O(1) lookup**.

---

# **3️⃣ Palindrome Linked List**

**Problem:** Check if a singly linked list is a palindrome.

**Concepts:**

* Find middle with **slow/fast pointer**.
* Reverse the second half.
* Compare both halves.

```cpp
ListNode* reverseList(ListNode* head) {
    ListNode* prev = NULL;
    while (head) {
        ListNode* nextNode = head->next;
        head->next = prev;
        prev = head;
        head = nextNode;
    }
    return prev;
}

int Solution::lPalin(ListNode* A) {
    if (!A || !A->next) return 1;
    
    ListNode* slow = A;
    ListNode* fast = A;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    ListNode* secondHalf = reverseList(slow);
    ListNode* firstHalf = A;
    
    while (secondHalf) {
        if (firstHalf->val != secondHalf->val) return 0;
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }
    
    return 1;
}
```

✅ **Tip:** Optional: restore list by reversing second half again.

---

# **4️⃣ Partition List**

**Problem:** Partition nodes based on value B, preserving relative order.

**Concepts:**

* Use **two separate lists**: less than B, greater/equal B.
* Connect them at the end.

```cpp
ListNode* Solution::partition(ListNode* A, int B) {
    ListNode* lessHead = new ListNode(0);
    ListNode* greaterHead = new ListNode(0);
    ListNode* less = lessHead;
    ListNode* greater = greaterHead;
    
    while (A) {
        if (A->val < B) { less->next = A; less = A; }
        else { greater->next = A; greater = A; }
        A = A->next;
    }
    
    greater->next = NULL;
    less->next = greaterHead->next;
    
    ListNode* newHead = lessHead->next;
    delete lessHead;
    delete greaterHead;
    return newHead;
}
```

✅ **Trick:** Using dummy nodes makes **edge cases (head, empty)** easy.

---

# **5️⃣ Longest Palindromic Sublist**

**Problem:** Find length of longest palindrome **in linked list**.

**Concepts:**

* Reverse first half **while traversing**.
* Check palindrome using helper function.
* O(1) space.

```cpp
int palindromeLength(ListNode* it1, ListNode* it2) {
    int ans = 0;
    while (it1 && it2 && it1->val == it2->val) {
        ans += 2;
        it1 = it1->next;
        it2 = it2->next;
    }
    return ans;
}

int Solution::solve(ListNode* A) {
    if (!A) return 0;
    if (!A->next) return 1;
    
    ListNode* prev = NULL;
    ListNode* temp = A;
    int ans = 0;
    
    while (temp->next) {
        ListNode* nxt = temp->next;
        ListNode* nxtnxt = temp->next->next;
        
        temp->next = prev;  // Reverse current node
        
        int ans1 = palindromeLength(temp, nxt);      // even-length palindrome
        int ans2 = 1 + palindromeLength(temp, nxtnxt); // odd-length
        
        ans = max(ans, max(ans1, ans2));
        prev = temp;
        temp = nxt;
    }
    
    return ans;
}
```

✅ **Trick:** This is like **Manacher’s algorithm for linked list**.

---

# **6️⃣ Flatten a Multilevel Doubly Linked List**

**Problem:** Each node has `right` and `down` pointers. Flatten into **sorted list using down**.

**Concepts:**

* Use **merge two sorted lists** recursively.
* Flatten `right` first, then merge with current list.

```cpp
ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
    if (!a) return b;
    if (!b) return a;
    
    ListNode* result;
    if (a->val < b->val) {
        result = a;
        result->down = mergeTwoLists(a->down, b);
    } else {
        result = b;
        result->down = mergeTwoLists(a, b->down);
    }
    return result;
}

ListNode* flatten(ListNode* root) {
    if (!root || !root->right) return root;
    
    root->right = flatten(root->right); // flatten right first
    root = mergeTwoLists(root, root->right); // merge current with right
    return root;
}
```

✅ **Tip:** This is **like merge sort** for multilevel lists. Use `down` for final links.

---

