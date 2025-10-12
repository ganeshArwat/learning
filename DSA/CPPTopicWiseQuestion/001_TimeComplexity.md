# Time Complexity Notes

---

## 1. What is Time Complexity?

Time complexity is a **measure of the amount of time an algorithm takes to run** as a function of the input size (n).
It helps estimate **performance and efficiency** of an algorithm.

* Denoted as (O(f(n))), where (f(n)) describes how runtime grows with input size.
* Focuses on **growth rate**, not exact runtime.

---

## 2. Common Time Complexities

| Complexity    | Name         | Example                                 |
| ------------- | ------------ | --------------------------------------- |
| (O(1))        | Constant     | Accessing an array element: `arr[i]`    |
| (O(\log n))   | Logarithmic  | Binary search                           |
| (O(n))        | Linear       | Loop over array: `for(int i=0;i<n;i++)` |
| (O(n \log n)) | Linearithmic | Merge sort, Quick sort (average case)   |
| (O(n^2))      | Quadratic    | Nested loops: `for(i) for(j)`           |
| (O(n^3))      | Cubic        | Triple nested loops                     |
| (O(2^n))      | Exponential  | Recursive Fibonacci                     |
| (O(n!))       | Factorial    | Permutations of n elements              |

---

## 3. Rules to Determine Time Complexity

1. **Basic Operations:**
   Assignments, arithmetic operations, comparisons → (O(1))

2. **Loops:**

   * Single loop: (O(n))
   * Nested loops: Multiply iterations → (O(n \cdot m))

3. **Recursion:**
   Solve recurrence relation or use recursion tree method

4. **Conditional Statements:**
   If-else → takes time of the branch executed

5. **Ignore Constants and Lower Order Terms:**

   * (O(2n) \approx O(n))
   * (O(n^2 + n) \approx O(n^2))

---

## 4. Examples

### Linear Time

```cpp
for(int i = 0; i < n; i++) {
    cout << i << " "; // O(n)
}
```

### Quadratic Time

```cpp
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        cout << i << "," << j; // O(n^2)
    }
}
```

### Logarithmic Time

```cpp
int l = 0, r = n-1;
while(l <= r) {
    int mid = (l+r)/2;
    // Binary search -> O(log n)
}
```

### Linearithmic Time

```cpp
sort(arr, arr+n); // Merge sort or quicksort -> O(n log n)
```

---

## 5. Space Complexity

* Measures **memory usage** of an algorithm relative to input size.
* Similar Big-O notation is used.

---

# Time Complexity Examples in C++

---

## 1. Constant Time – (O(1))

* Execution time **does not depend** on input size.
* Example: Accessing an array element, simple arithmetic.

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {1,2,3,4,5};
    cout << arr[2];  // Accessing a single element -> O(1)
    int a = 5 + 10;  // Arithmetic operation -> O(1)
    return 0;
}
```

---

## 2. Logarithmic Time – (O(\log n))

* Divides the problem in half at each step.
* Example: Binary search.

```cpp
#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int key) {
    int l = 0, r = n-1;
    while(l <= r) {
        int mid = (l + r) / 2;
        if(arr[mid] == key) return mid;
        else if(arr[mid] < key) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}

int main() {
    int arr[] = {1,2,3,4,5};
    cout << binarySearch(arr, 5, 3); // O(log n)
}
```

---

## 3. Linear Time – (O(n))

* Execution time grows linearly with input size.
* Example: Single loop through an array.

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1,2,3,4,5};
    int n = 5;
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " "; // O(n)
    }
}
```

---

## 4. Linearithmic Time – (O(n \log n))

* Common in **efficient sorting algorithms**.
* Example: Merge Sort or Quick Sort (average case).

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int arr[] = {5,2,3,1,4};
    int n = 5;
    sort(arr, arr+n); // O(n log n)
    for(int i=0;i<n;i++) cout<<arr[i]<<" ";
}
```

---

## 5. Quadratic Time – (O(n^2))

* Nested loops over the same input.
* Example: Bubble sort, checking all pairs.

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1,2,3};
    int n = 3;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << arr[i] << "," << arr[j] << " "; // O(n^2)
        }
    }
}
```

---

## 6. Cubic Time – (O(n^3))

* Triple nested loops.
* Example: Check all triplets in an array.

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1,2,3};
    int n = 3;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            for(int k = 0; k < n; k++) {
                cout << arr[i] << arr[j] << arr[k] << " "; // O(n^3)
            }
        }
    }
}
```

---

## 7. Exponential Time – (O(2^n))

* Execution doubles with each additional input.
* Example: Recursive Fibonacci (naive).

```cpp
#include <iostream>
using namespace std;

int fib(int n) {
    if(n <= 1) return n;
    return fib(n-1) + fib(n-2); // O(2^n)
}

int main() {
    cout << fib(5);
}
```

---

## 8. Factorial Time – (O(n!))

* Example: Generating all permutations of n elements.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s = "ABC";
    sort(s.begin(), s.end());
    do {
        cout << s << endl; // O(n!)
    } while(next_permutation(s.begin(), s.end()));
}
```

---

### ✅ Summary Table

| Complexity | Example               | Notes                           |
| ---------- | --------------------- | ------------------------------- |
| O(1)       | Access `arr[i]`       | Constant time                   |
| O(log n)   | Binary search         | Divides input                   |
| O(n)       | Single loop           | Linear traversal                |
| O(n log n) | Merge sort, quicksort | Efficient sorting               |
| O(n^2)     | Nested loops          | Pairs in array                  |
| O(n^3)     | Triple nested loops   | Triplets, matrix multiplication |
| O(2^n)     | Recursive Fibonacci   | Exponential growth              |
| O(n!)      | All permutations      | Factorial growth                |

---
