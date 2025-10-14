# **Array Cheat Sheet (C++)**

## **1. Array Basics**

```cpp
#include <bits/stdc++.h>
using namespace std;

int arr[5];            // Static array of size 5 (0-indexed)
int arr2[] = {1,2,3};  // Initialize with values
int n = sizeof(arr2)/sizeof(arr2[0]); // Size of array
```

---

## **2. Input/Output**

```cpp
// Input
for(int i=0;i<n;i++) cin >> arr[i];

// Output
for(int i=0;i<n;i++) cout << arr[i] << " ";
```

---

## **3. Common Operations**

### **3.1 Sum / Max / Min**

```cpp
int sum = 0, mx = INT_MIN, mn = INT_MAX;
for(int i=0;i<n;i++){
    sum += arr[i];
    mx = max(mx, arr[i]);
    mn = min(mn, arr[i]);
}
```

### **3.2 Reverse Array**

```cpp
reverse(arr, arr+n); // using STL

// Or manually
for(int i=0;i<n/2;i++) swap(arr[i], arr[n-i-1]);
```

### **3.3 Sort / Binary Search**

```cpp
sort(arr, arr+n);                // Sort ascending
sort(arr, arr+n, greater<int>()); // Sort descending

bool exists = binary_search(arr, arr+n, x); // true if x exists
```

---

## **4. Prefix Sum**

```cpp
int prefix[n];
prefix[0] = arr[0];
for(int i=1;i<n;i++) prefix[i] = prefix[i-1] + arr[i];

// Sum of subarray [l,r]
int sum_sub = prefix[r] - (l>0 ? prefix[l-1] : 0);
```

---

## **5. Sliding Window**

```cpp
int k = 3; // window size
int window_sum = 0;
for(int i=0;i<k;i++) window_sum += arr[i];
for(int i=k;i<n;i++){
    window_sum += arr[i] - arr[i-k];
}
```

---

## **6. Two Pointers**

```cpp
int i=0, j=n-1;
while(i<j){
    if(arr[i]+arr[j]==target) break;
    else if(arr[i]+arr[j]<target) i++;
    else j--;
}
```

---

## **7. Kadane's Algorithm (Max Subarray Sum)**

```cpp
int max_sum = arr[0], curr_sum = arr[0];
for(int i=1;i<n;i++){
    curr_sum = max(arr[i], curr_sum + arr[i]);
    max_sum = max(max_sum, curr_sum);
}
```

---

## **8. Count Frequencies**

```cpp
unordered_map<int,int> freq;
for(int i=0;i<n;i++) freq[arr[i]]++;
```

---

## **9. 2D Arrays**

```cpp
int arr2D[3][4];           // 3 rows, 4 columns
for(int i=0;i<3;i++)
    for(int j=0;j<4;j++)
        cin >> arr2D[i][j];

// Sum of 2D array
int sum = 0;
for(int i=0;i<3;i++)
    for(int j=0;j<4;j++)
        sum += arr2D[i][j];
```

---

## **10. STL Array-Like Structures**

```cpp
vector<int> v = {1,2,3};
v.push_back(4);      // add element
v.pop_back();        // remove last
sort(v.begin(), v.end());
int x = v.size();
```

---

## **11. Common Patterns**

### **11.1 Remove Duplicates (Sorted Array)**

```cpp
int n = unique(arr, arr+size) - arr;
```

### **11.2 Rotate Array**

```cpp
// Rotate left by d
rotate(arr, arr+d, arr+n);
```

### **11.3 Merge Two Sorted Arrays**

```cpp
vector<int> res;
int i=0,j=0;
while(i<n1 && j<n2){
    if(a[i]<b[j]) res.push_back(a[i++]);
    else res.push_back(b[j++]);
}
while(i<n1) res.push_back(a[i++]);
while(j<n2) res.push_back(b[j++]);
```

---

## **12. Bit Manipulation**

```cpp
// Check ith bit
bool bit = arr[i] & (1<<i);

// Set ith bit
arr[i] |= (1<<i);

// Clear ith bit
arr[i] &= ~(1<<i);
```

---

✅ **Tips:**

* Always prefer `vector<int>` in competitive programming for dynamic arrays.
* Use `sort`, `lower_bound`, `upper_bound` for fast operations.
* Prefix sum & sliding window reduce O(n²) → O(n) in subarray sum problems.

---
