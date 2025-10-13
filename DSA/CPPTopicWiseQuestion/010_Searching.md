## **1. Linear Search**

* **Idea:** Check each element one by one until you find the target.
* **Code snippet:**

```cpp
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)
* **Pros:** Works on unsorted arrays.
* **Cons:** Slow for large arrays.

---

## **2. Binary Search**

* **Idea:** Repeatedly divide the sorted array in half to locate the target.
* **Code snippet:**

```cpp
int binarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

* **Time Complexity:** O(log n)
* **Space Complexity:** O(1) iterative / O(log n) recursive
* **Pros:** Fast on sorted arrays.
* **Cons:** Requires array to be sorted.

---

## **3. Interpolation Search**

* **Idea:** Uses a formula to estimate the position of the target based on its value. Works best on **uniformly distributed sorted arrays**.
* **Code snippet:**

```cpp
int interpolationSearch(int arr[], int n, int target) {
    int left = 0, right = n - 1;

    while (left <= right && target >= arr[left] && target <= arr[right]) {
        if (left == right) return arr[left] == target ? left : -1;
        int pos = left + ((double)(right - left) / (arr[right] - arr[left]) * (target - arr[left]));
        if (arr[pos] == target) return pos;
        if (arr[pos] < target) left = pos + 1;
        else right = pos - 1;
    }
    return -1;
}
```

* **Time Complexity:** O(log log n) for uniform data, O(n) worst case
* **Space Complexity:** O(1)
* **Pros:** Faster than binary search for large, uniformly distributed datasets.
* **Cons:** Sensitive to data distribution.

---

### **Summary Table**

| Search Type          | Requirement      | Best Case | Worst Case | Space |
| -------------------- | ---------------- | --------- | ---------- | ----- |
| Linear Search        | None             | O(1)      | O(n)       | O(1)  |
| Binary Search        | Sorted array     | O(1)      | O(log n)   | O(1)  |
| Interpolation Search | Sorted + uniform | O(1)      | O(n)       | O(1)  |

---

# **Binary Search**

---

## **1. Standard Binary Search**

```cpp
int binarySearch(vector<int> &A, int target) {
    int N = A.size();
    int L = 0, R = N - 1;
    while (L <= R) {
        int mid = L + (R - L) / 2;
        if (A[mid] == target) return mid;
        else if (A[mid] < target) L = mid + 1;
        else R = mid - 1;
    }
    return -1;
}
```

---

## **2. First Occurrence**

```cpp
int firstOccurrence(vector<int> &A, int target) {
    int N = A.size();
    int L = 0, R = N - 1;
    while (L <= R) {
        int mid = L + (R - L) / 2;
        if (A[mid] == target && (mid == 0 || A[mid-1] != target)) return mid;
        else if (A[mid] < target) L = mid + 1;
        else R = mid - 1;
    }
    return -1;
}
```

---

## **3. Last Occurrence**

```cpp
int lastOccurrence(vector<int> &A, int target) {
    int N = A.size();
    int L = 0, R = N - 1;
    while (L <= R) {
        int mid = L + (R - L) / 2;
        if (A[mid] == target && (mid == N-1 || A[mid+1] != target)) return mid;
        else if (A[mid] > target) R = mid - 1;
        else L = mid + 1;
    }
    return -1;
}
```

---

## **4. Single Unique Element in Sorted Array**

```cpp
int singleElement(vector<int> &A) {
    int N = A.size();
    int L = 0, R = N - 1;
    while (L <= R) {
        int mid = L + (R - L)/2;
        if ((mid == 0 || A[mid] != A[mid-1]) && (mid == N-1 || A[mid] != A[mid+1])) 
            return A[mid];
        else if (mid < N-1 && A[mid] == A[mid+1]) {
            if (mid % 2 == 0) L = mid + 1;
            else R = mid - 1;
        } else {
            if (mid % 2 == 0) R = mid - 1;
            else L = mid + 1;
        }
    }
    return -1;
}
```

---

## **5. Peak Element**

```cpp
int peakElement(vector<int> &A) {
    int L = 0, R = A.size() - 1;
    while (L < R) {
        int mid = L + (R - L)/2;
        if (A[mid] > A[mid + 1]) R = mid;
        else L = mid + 1;
    }
    return A[L];
}
```

---

## **6. Local Minima**

```cpp
int localMinima(vector<int> &A) {
    int N = A.size();
    int L = 0, R = N - 1;
    while (L <= R) {
        int mid = L + (R - L)/2;
        if ((mid == 0 || A[mid] < A[mid-1]) && (mid == N-1 || A[mid] < A[mid+1]))
            return A[mid];
        else if (mid < N-1 && A[mid] < A[mid + 1]) L = mid + 1;
        else R = mid - 1;
    }
    return A[L];
}
```

---

## **7. Sorted Insert Position**

```cpp
int searchInsert(vector<int> &A, int B) {
    int L = 0, R = A.size() - 1;
    while (L <= R) {
        int mid = L + (R - L)/2;
        if (A[mid] == B) return mid;
        else if (A[mid] < B) L = mid + 1;
        else R = mid - 1;
    }
    return L;
}
```

---

## **8. Search for a Range**

```cpp
vector<int> searchRange(vector<int> &A, int B) {
    vector<int> result(2, -1);
    int L = 0, R = A.size() - 1;
    
    // Leftmost
    while (L <= R) {
        int mid = L + (R - L)/2;
        if (A[mid] == B) { result[0] = mid; R = mid - 1; }
        else if (A[mid] < B) L = mid + 1;
        else R = mid - 1;
    }
    
    L = 0; R = A.size() - 1;
    // Rightmost
    while (L <= R) {
        int mid = L + (R - L)/2;
        if (A[mid] == B) { result[1] = mid; L = mid + 1; }
        else if (A[mid] < B) L = mid + 1;
        else R = mid - 1;
    }
    
    return result;
}
```

---

## **9. Matrix Search (Sorted Rows)**

```cpp
int searchMatrix(vector<vector<int>> &A, int B) {
    int N = A.size();
    if (N == 0) return 0;
    int M = A[0].size();
    int L = 0, R = N * M - 1;
    
    while (L <= R) {
        int mid = L + (R - L)/2;
        int midValue = A[mid / M][mid % M];
        if (midValue == B) return 1;
        else if (midValue < B) L = mid + 1;
        else R = mid - 1;
    }
    
    return 0;
}
```

---

## **10. Minimum Difference in 2D Array**

```cpp
int findLowerBound(const vector<int>& row, int target) {
    auto it = lower_bound(row.begin(), row.end(), target);
    return it == row.end() ? INT_MAX : *it;
}
int findUpperBound(const vector<int>& row, int target) {
    auto it = upper_bound(row.begin(), row.end(), target);
    return it == row.begin() ? INT_MIN : *(--it);
}

int minDifference2D(int A, int B, vector<vector<int>> &C) {
    for (auto &row : C) sort(row.begin(), row.end());
    int ans = INT_MAX;
    for (int i = 0; i < A-1; ++i) {
        for (int j = 0; j < B; ++j) {
            int a = findLowerBound(C[i+1], C[i][j]);
            int b = findUpperBound(C[i+1], C[i][j]);
            if (a != INT_MAX) ans = min(ans, a - C[i][j]);
            if (b != INT_MIN) ans = min(ans, C[i][j] - b);
        }
    }
    return ans;
}
```

---

## **11. Maximum Height of Staircase**

```cpp
int maxStairHeight(int A) {
    int L = 0, R = A, result = 0;
    while (L <= R) {
        int mid = L + (R - L)/2;
        long long sum = (long long)mid * (mid + 1) / 2;
        if (sum == A) return mid;
        else if (sum < A) { result = mid; L = mid + 1; }
        else R = mid - 1;
    }
    return result;
}
```

---


## 1. Search in Rotated Sorted Array

```cpp
int Solution::search(const vector<int> &A, int B) {
    int N = A.size();
    int left = 0, right = N - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (A[mid] == B) return mid;

        if (A[0] < A[N-1]) {
            if (A[mid] < B) left = mid + 1;
            else right = mid - 1;
        } else {
            if (B >= A[0]) {
                if (A[mid] >= A[0]) {
                    if (A[mid] < B) left = mid + 1;
                    else right = mid - 1;
                } else right = mid - 1;
            } else {
                if (A[mid] <= A[0]) {
                    if (A[mid] < B) left = mid + 1;
                    else right = mid - 1;
                } else left = mid + 1;
            }
        }
    }
    
    return -1;
}
```

---

## 2. Median of Two Sorted Arrays

```cpp
double Solution::findMedianSortedArrays(const vector<int> &A, const vector<int> &B) {
    int n = A.size(), m = B.size();
    if (n > m) return findMedianSortedArrays(B, A);

    int left = 0, right = n;
    while (left <= right) {
        int partitionA = (left + right) / 2;
        int partitionB = (n + m + 1) / 2 - partitionA;

        int maxLeftA = (partitionA == 0) ? INT_MIN : A[partitionA - 1];
        int minRightA = (partitionA == n) ? INT_MAX : A[partitionA];

        int maxLeftB = (partitionB == 0) ? INT_MIN : B[partitionB - 1];
        int minRightB = (partitionB == m) ? INT_MAX : B[partitionB];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            if ((n + m) % 2 == 0)
                return (double)(max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2;
            else
                return (double)max(maxLeftA, maxLeftB);
        } else if (maxLeftA > minRightB) {
            right = partitionA - 1;
        } else {
            left = partitionA + 1;
        }
    }

    return 0.0; // should not reach here
}
```

---

## 3. Ath Magical Number

```cpp
const int MOD = 1e9 + 7;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
int lcm(int a, int b) { return (a / gcd(a, b)) * b; }
int countMagicalNumbers(long long x, int B, int C, int lcmBC) {
    return x / B + x / C - x / lcmBC;
}

int Solution::solve(int A, int B, int C) {
    long long low = 1, high = (long long) A * min(B, C);
    int lcmBC = lcm(B, C);

    while (low < high) {
        long long mid = low + (high - low) / 2;
        if (countMagicalNumbers(mid, B, C, lcmBC) < A)
            low = mid + 1;
        else
            high = mid;
    }

    return low % MOD;
}
```

---

## 4. Square Root of Integer

```cpp
int Solution::sqrt(int A) {
    if (A == 0 || A == 1) return A;
    long long left = 1, right = A, ans = 0;

    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (mid * mid == A) return mid;
        else if (mid * mid < A) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return ans;
}
```

---

## 5. Add or Not (Max Occurrences)

```cpp
bool check(vector<int> &A, int B, long int mid, int i, vector<long int> &pre) {
    return (A[i] * mid - (pre[i + 1] - pre[i - mid + 1])) <= B;
}

vector<int> Solution::solve(vector<int> &A, int B) {
    sort(A.begin(), A.end());
    vector<int> ans(2, -1);
    vector<long int> pre(A.size() + 1, 0);
    for (int i = 0; i < A.size(); i++) pre[i + 1] = pre[i] + A[i];

    for (int i = 0; i < A.size(); i++) {
        int l = 1, j = i + 1;
        long int maxi = 0;
        while (l <= j) {
            long int mid = (l + j) / 2;
            if (check(A, B, mid, i, pre)) {
                maxi = mid;
                l = mid + 1;
            } else j = mid - 1;
        }
        if (maxi > ans[0]) { ans[0] = maxi; ans[1] = A[i]; }
    }
    return ans;
}
```

---

## 6. Find Smallest Again (B-th smallest triplet sum)

```cpp
int countTripletsLessThanOrEqualTo(vector<int>& A, int N, int target) {
    int count = 0;
    for (int i = 0; i < N - 2; ++i) {
        int j = i + 1, k = N - 1;
        while (j < k) {
            int sum = A[i] + A[j] + A[k];
            if (sum <= target) { count += (k - j); ++j; }
            else --k;
        }
    }
    return count;
}

int Solution::solve(vector<int>& A, int B) {
    int N = A.size();
    sort(A.begin(), A.end());

    int minSum = A[0] + A[1] + A[2];
    int maxSum = A[N-1] + A[N-2] + A[N-3];
    int low = minSum, high = maxSum, result = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        int count = countTripletsLessThanOrEqualTo(A, N, mid);
        if (count >= B) { result = mid; high = mid - 1; }
        else low = mid + 1;
    }

    return result;
}
```

---

## 7. Matrix Median

```cpp
int countLessEqual(const vector<vector<int>> &A, int value) {
    int count = 0, N = A.size(), M = A[0].size();
    for (int i = 0; i < N; ++i) {
        int lo = 0, hi = M - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (A[i][mid] <= value) lo = mid + 1;
            else hi = mid - 1;
        }
        count += lo;
    }
    return count;
}

int Solution::findMedian(vector<vector<int> > &A) {
    int N = A.size(), M = A[0].size();
    int low = INT_MAX, high = INT_MIN;
    for (int i = 0; i < N; ++i) {
        low = min(low, A[i][0]);
        high = max(high, A[i][M-1]);
    }

    int medianPos = (N*M + 1)/2;
    while (low < high) {
        int mid = low + (high - low)/2;
        if (countLessEqual(A, mid) < medianPos) low = mid + 1;
        else high = mid;
    }

    return low;
}
```

---

## 1. Aggressive Cows

```cpp
int Solution::solve(vector<int> &A, int B) {
    sort(A.begin(), A.end());
    int low = 1, high = A.back() - A[0], result = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        int last_position = A[0], count = 1;

        for (int i = 1; i < A.size(); i++) {
            if (A[i] - last_position >= mid) {
                count++;
                last_position = A[i];
            }
            if (count == B) break;
        }

        if (count >= B) {
            result = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return result;
}
```

---

## 2. Painter’s Partition Problem

```cpp
const int MOD = 10000003;

bool isPossible(int A, vector<int> &C, long long time) {
    long long sum = 0;
    int painters = 1;

    for (int i = 0; i < C.size(); i++) {
        sum += C[i];
        if (sum > time) {
            sum = C[i];
            painters++;
            if (painters > A) return false;
        }
    }
    return true;
}

int Solution::paint(int A, int B, vector<int> &C) {
    long long maxElement = *max_element(C.begin(), C.end());
    long long sum = 0;
    for (int x : C) sum += x;

    long long lo = maxElement, hi = sum, answer = 0;

    while (lo <= hi) {
        long long mid = (lo + hi) / 2;
        if (isPossible(A, C, mid)) {
            answer = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }

    return (int)((answer * B) % MOD);
}
```

---

## 3. Special Integer (Max Subarray Size K)

```cpp
bool canHaveSubarrayOfSizeK(vector<int> &A, int n, int K, int B) {
    long long sum = 0;
    for (int i = 0; i < K; i++) sum += A[i];
    if (sum > B) return false;

    for (int i = K; i < n; i++) {
        sum += A[i] - A[i - K];
        if (sum > B) return false;
    }
    return true;
}

int Solution::solve(vector<int> &A, int B) {
    int n = A.size(), low = 1, high = n, result = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (canHaveSubarrayOfSizeK(A, n, mid, B)) {
            result = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return result;
}
```

---

## 4. Allocate Books

```cpp
bool isFeasible(const vector<int>& A, int B, int maxPages) {
    int studentCount = 1, currentSum = 0;

    for (int pages : A) {
        if (currentSum + pages > maxPages) {
            studentCount++;
            currentSum = pages;
            if (studentCount > B) return false;
        } else {
            currentSum += pages;
        }
    }

    return true;
}

int Solution::books(vector<int> &A, int B) {
    int N = A.size();
    if (N < B) return -1;

    int totalSum = 0, maxPages = A[0];
    for (int pages : A) {
        totalSum += pages;
        if (pages > maxPages) maxPages = pages;
    }

    int low = maxPages, high = totalSum, result = high;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (isFeasible(A, B, mid)) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return result;
}
```

---

## **1️⃣ Recursive Binary Search**

### **Idea:**

* You have a **sorted array**.
* Pick the middle element.
* If it’s equal to the target → found!
* If it’s smaller → search the **right half**.
* If it’s larger → search the **left half**.
* Repeat until search space is empty.

### **Example:**

Array: `[1, 3, 5, 7, 9]`, target = `5`

1. mid = 2 → arr[2] = 5 → Found! ✅

### **Code:**

```cpp
int recursiveBinarySearch(const vector<int>& arr, int target, int left, int right) {
    if (left > right) return -1; // base case: not found
    int mid = left + (right - left) / 2;

    if (arr[mid] == target) return mid;
    else if (arr[mid] > target) return recursiveBinarySearch(arr, target, left, mid - 1);
    else return recursiveBinarySearch(arr, target, mid + 1, right);
}
```

* **Time Complexity:** O(log n)
* **Space Complexity:** O(log n) due to recursion stack

---

## **2️⃣ Lower Bound**

### **Idea:**

* Finds the **first index** where the target can be inserted without breaking the order.
* Think of it as: “Where does this number **fit** in a sorted array?”

### **Example:**

Array: `[1, 3, 3, 5, 7]`, target = `3`

* Lower bound = index `1` (first `3`)

### **Code:**

```cpp
int lowerBound(const vector<int>& arr, int target) {
    int left = 0, right = arr.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] >= target) right = mid;
        else left = mid + 1;
    }
    return left;
}
```

* **Time Complexity:** O(log n)

---

## **3️⃣ Floor and Ceil**

* **Floor(x):** largest element ≤ x
* **Ceil(x):** smallest element ≥ x

### **Example:**

Array: `[1, 3, 5, 7]`, x = 4

* Floor = 3
* Ceil = 5

### **Code:**

```cpp
int findFloor(int arr[], int n, int x) {
    int low = 0, high = n - 1, ans = -1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] <= x) { ans = arr[mid]; low = mid + 1; }
        else high = mid - 1;
    }
    return ans;
}

int findCeil(int arr[], int n, int x) {
    int low = 0, high = n - 1, ans = -1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] >= x) { ans = arr[mid]; high = mid - 1; }
        else low = mid + 1;
    }
    return ans;
}
```

* **Time Complexity:** O(log n)

---

## **4️⃣ Search in Rotated Sorted Array with Duplicates**

### **Idea:**

* Sometimes an array is **rotated**, e.g., `[4,5,6,7,0,1,2]`.
* Binary search must **detect which half is sorted**.
* Duplicates make it tricky, so we handle the edge case where `low == mid == high`.

### **Example:**

Array: `[2,5,6,0,0,1,2]`, target = `0`

* mid = 3 → arr[mid] = 0 → Found ✅

### **Code:**

```cpp
bool searchInARotatedSortedArrayII(vector<int>& arr, int k) {
    int low = 0, high = arr.size() - 1;
    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == k) return true;

        // handle duplicates
        if (arr[low] == arr[mid] && arr[mid] == arr[high]) {
            low++; high--; 
            continue;
        }

        if (arr[low] <= arr[mid]) { // left part sorted
            if (arr[low] <= k && k <= arr[mid]) high = mid - 1;
            else low = mid + 1;
        } else { // right part sorted
            if (arr[mid] <= k && k <= arr[high]) low = mid + 1;
            else high = mid - 1;
        }
    }
    return false;
}
```

* **Time Complexity:** O(log n) average, O(n) worst-case with duplicates

---

# **5️⃣ Minimum in Rotated Sorted Array**

### **Problem:**

* You have a **rotated sorted array** like `[4,5,6,7,0,1,2]`.
* Find the **minimum element**.

### **Intuition:**

1. If `arr[low] <= arr[high]`, the array is already sorted → `arr[low]` is minimum.
2. Otherwise, check which half is sorted:

   * If left half is sorted (`arr[low] <= arr[mid]`) → minimum must be on **right half**.
   * Else → minimum is in **left half**.

### **Example:**

Array: `[4,5,6,7,0,1,2]`

* mid = 3 → arr[mid] = 7
* left part `[4,5,6,7]` sorted → min in right `[0,1,2]`
* min = 0 ✅

### **Code:**

```cpp
int findMin(vector<int>& arr) {
    int low = 0, high = arr.size() - 1;
    int ans = INT_MAX;
    
    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[low] <= arr[high]) { // sorted space
            ans = min(ans, arr[low]);
            break;
        }

        if (arr[low] <= arr[mid]) { // left sorted
            ans = min(ans, arr[low]);
            low = mid + 1;
        } else { // right sorted
            ans = min(ans, arr[mid]);
            high = mid - 1;
        }
    }
    return ans;
}
```

* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

# **6️⃣ Count Rotations in Rotated Sorted Array**

### **Problem:**

* Rotated sorted array: `[15, 18, 2, 3, 6, 12]`
* Find **how many times array is rotated**.

### **Intuition:**

* Number of rotations = **index of minimum element**.
* So we can use the `findMin` logic and **return index instead of value**.

### **Code:**

```cpp
int countRotations(vector<int>& arr) {
    int low = 0, high = arr.size() - 1;

    while (low <= high) {
        if (arr[low] <= arr[high]) return low; // array already sorted

        int mid = (low + high) / 2;
        int next = (mid + 1) % arr.size();
        int prev = (mid + arr.size() - 1) % arr.size();

        if (arr[mid] <= arr[next] && arr[mid] <= arr[prev])
            return mid; // mid is minimum

        if (arr[mid] >= arr[low])
            low = mid + 1;
        else
            high = mid - 1;
    }
    return 0;
}
```

* **Time Complexity:** O(log n)

---

# **7️⃣ Nth Root of an Integer**

### **Problem:**

* Given `n` and `m`, find the **integer x** such that `x^n = m`.

### **Intuition:**

1. The answer is in range `[1, m]`.
2. Use **binary search on x**:

   * If `mid^n == m` → found
   * If `mid^n < m` → move right
   * If `mid^n > m` → move left

### **Code:**

```cpp
int checkPower(int mid, int n, int m) {
    long long ans = 1;
    for (int i = 1; i <= n; i++) {
        ans *= mid;
        if (ans > m) return 2; // mid^n > m
    }
    if (ans == m) return 1; // exact match
    return 0; // mid^n < m
}

int NthRoot(int n, int m) {
    int low = 1, high = m;
    while (low <= high) {
        int mid = (low + high) / 2;
        int result = checkPower(mid, n, m);

        if (result == 1) return mid;
        else if (result == 0) low = mid + 1;
        else high = mid - 1;
    }
    return -1; // no integer root
}
```

### **Example:**

* n = 3, m = 27 → answer = 3

* n = 2, m = 10 → answer = -1 (no integer root)

* **Time Complexity:** O(log m × n)

* **Space Complexity:** O(1)

---

✅ So far we have covered:

* Basic binary search (recursive)
* Lower bound / Upper bound
* Floor / Ceil
* Rotated sorted array search
* Minimum in rotated array
* Count rotations
* Nth root

---

# **1️⃣ Koko Eating Bananas**

### **Problem:**

* Koko has piles of bananas.
* Each hour, she eats `k` bananas from one pile.
* Find the **minimum `k`** such that she finishes all bananas in `h` hours.

### **Intuition:**

* If `k` is **large**, she finishes faster → too big is okay but we want **minimum k**.
* If `k` is **small**, she takes more time → maybe exceeds `h`.

So, **binary search on k** (1 → max pile) works.

### **Code:**

```cpp
int findMax(vector<int> &v) {
    int maxi = INT_MIN;
    for (int x : v) maxi = max(maxi, x);
    return maxi;
}

int calculateTotalHours(vector<int> &v, int k) {
    int totalH = 0;
    for (int x : v) totalH += ceil((double)x / k);
    return totalH;
}

int minimumRateToEatBananas(vector<int> v, int h) {
    int low = 1, high = findMax(v);
    while (low <= high) {
        int mid = (low + high) / 2;
        int totalH = calculateTotalHours(v, mid);
        if (totalH <= h) high = mid - 1; // possible → try smaller k
        else low = mid + 1; // need bigger k
    }
    return low;
}
```

---

# **2️⃣ Minimum Days to Make M Bouquets**

### **Problem:**

* You have an array `arr[i]` representing the bloom day of each flower.
* You need `m` bouquets, each consisting of `k` consecutive flowers.
* Find the **minimum day** to get `m` bouquets.

### **Binary Search Approach:**

* Search on **day** (min → max bloom day).
* Use a helper to check if `m` bouquets are possible on `mid` day.

### **Code:**

```cpp
bool possible(vector<int> &arr, int day, int m, int k) {
    int cnt = 0, bouquets = 0;
    for (int x : arr) {
        if (x <= day) cnt++;
        else { bouquets += cnt / k; cnt = 0; }
    }
    bouquets += cnt / k;
    return bouquets >= m;
}

int roseGarden(vector<int> arr, int k, int m) {
    long long val = 1ll * m * k;
    int n = arr.size();
    if (val > n) return -1; // impossible

    int low = *min_element(arr.begin(), arr.end());
    int high = *max_element(arr.begin(), arr.end());

    while (low <= high) {
        int mid = (low + high) / 2;
        if (possible(arr, mid, m, k)) high = mid - 1;
        else low = mid + 1;
    }
    return low;
}
```

---

# **3️⃣ Smallest Divisor Given a Threshold**

### **Problem:**

* Given `arr` and `threshold`, find **smallest divisor** such that sum of `ceil(arr[i]/div)` ≤ threshold.

### **Binary Search Approach:**

* Search on divisor (1 → max element).

### **Code:**

```cpp
int sumByD(vector<int> &arr, int div) {
    int sum = 0;
    for (int x : arr) sum += ceil((double)x / div);
    return sum;
}

int smallestDivisor(vector<int>& arr, int limit) {
    int low = 1, high = *max_element(arr.begin(), arr.end());

    while (low <= high) {
        int mid = (low + high) / 2;
        if (sumByD(arr, mid) <= limit) high = mid - 1;
        else low = mid + 1;
    }
    return low;
}
```

---

# **4️⃣ Capacity to Ship Packages within D Days**

### **Problem:**

* Given weights of packages and `d` days.
* Find **minimum capacity** of ship to ship all packages in `d` days.

### **Binary Search Approach:**

* Search on capacity (`max weight → sum of all weights`).
* Count days required for capacity `mid`.

### **Code:**

```cpp
int findDays(vector<int> &weights, int cap) {
    int days = 1, load = 0;
    for (int w : weights) {
        if (load + w > cap) { days++; load = w; }
        else load += w;
    }
    return days;
}

int leastWeightCapacity(vector<int> &weights, int d) {
    int low = *max_element(weights.begin(), weights.end());
    int high = accumulate(weights.begin(), weights.end(), 0);

    while (low <= high) {
        int mid = (low + high) / 2;
        if (findDays(weights, mid) <= d) high = mid - 1;
        else low = mid + 1;
    }
    return low;
}
```

---

# **5️⃣ Kth Missing Positive Number**

### **Problem:**

* Array of sorted positive numbers, find **kth missing positive integer**.

### **Binary Search Approach:**

* Count missing numbers until mid: `arr[mid] - (mid + 1)`
* Adjust search space accordingly.

### **Code:**

```cpp
int missingK(vector<int> &vec, int n, int k) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        int missing = vec[mid] - (mid + 1);
        if (missing < k) low = mid + 1;
        else high = mid - 1;
    }
    return k + high + 1;
}
```

---

# **6️⃣ Split Array - Largest Sum**

### **Problem:**

* Divide array into `k` subarrays to **minimize the largest sum** among subarrays.

### **Binary Search Approach:**

* Search on **maxSum** (max element → sum of array).
* Count partitions required for a mid sum.

### **Code:**

```cpp
int countPartitions(vector<int> &a, int maxSum) {
    int partitions = 1;
    long long subarraySum = 0;
    for (int x : a) {
        if (subarraySum + x <= maxSum) subarraySum += x;
        else { partitions++; subarraySum = x; }
    }
    return partitions;
}

int largestSubarraySumMinimized(vector<int> &a, int k) {
    int low = *max_element(a.begin(), a.end());
    int high = accumulate(a.begin(), a.end(), 0);

    while (low <= high) {
        int mid = (low + high) / 2;
        int partitions = countPartitions(a, mid);
        if (partitions > k) low = mid + 1;
        else high = mid - 1;
    }
    return low;
}
```

---

# **7️⃣ Minimize Max Distance to Gas Station**

### **Problem:**

* Stations on a line, can add `k` new stations.
* Minimize **maximum distance between stations**.

### **Binary Search Approach:**

* Search on distance (0 → max distance).
* Count required stations for mid distance.

### **Code:**

```cpp
int numberOfGasStationsRequired(long double dist, vector<int> &arr) {
    int cnt = 0;
    for (int i = 1; i < arr.size(); i++) {
        int numberInBetween = (arr[i] - arr[i-1]) / dist;
        if ((arr[i] - arr[i-1]) == dist * numberInBetween) numberInBetween--;
        cnt += numberInBetween;
    }
    return cnt;
}

long double minimiseMaxDistance(vector<int> &arr, int k) {
    long double low = 0, high = 0;
    for (int i = 0; i < arr.size() - 1; i++) high = max(high, (long double)(arr[i+1] - arr[i]));

    long double diff = 1e-6;
    while (high - low > diff) {
        long double mid = (low + high) / 2.0;
        if (numberOfGasStationsRequired(mid, arr) > k) low = mid;
        else high = mid;
    }
    return high;
}
```

---

# **8️⃣ Median of 2 Sorted Arrays**

### **Problem:**

* Two sorted arrays, find **median** in O(log(min(n,m))).

### **Binary Search Approach:**

* Binary search on **smaller array**, partition both arrays.
* Maintain left ≤ right condition across partitions.

### **Code:**

```cpp
double median(vector<int>& a, vector<int>& b) {
    if (a.size() > b.size()) return median(b, a);
    int n1 = a.size(), n2 = b.size();
    int left = (n1 + n2 + 1) / 2;
    int low = 0, high = n1;

    while (low <= high) {
        int mid1 = (low + high) / 2;
        int mid2 = left - mid1;

        int l1 = (mid1 == 0 ? INT_MIN : a[mid1-1]);
        int r1 = (mid1 == n1 ? INT_MAX : a[mid1]);
        int l2 = (mid2 == 0 ? INT_MIN : b[mid2-1]);
        int r2 = (mid2 == n2 ? INT_MAX : b[mid2]);

        if (l1 <= r2 && l2 <= r1) {
            if ((n1+n2) % 2) return max(l1, l2);
            else return (double)(max(l1,l2) + min(r1,r2)) / 2.0;
        }
        else if (l1 > r2) high = mid1 - 1;
        else low = mid1 + 1;
    }
    return 0;
}
```

---


# **1️⃣ Kth Element of 2 Sorted Arrays**

### **Problem:**

* Given 2 sorted arrays `a` and `b`, find the **kth smallest element** in the merged array.

### **Intuition:**

* Similar to **median of 2 sorted arrays**, we **binary search on one array** to partition left/right such that `k` elements are on the left.
* Check conditions with neighbors (`l1, l2, r1, r2`) to see if partition is valid.

### **Code:**

```cpp
int kthElement(vector<int> &a, vector<int>& b, int m, int n, int k) {
    if (m > n) return kthElement(b, a, n, m, k);

    int low = max(0, k - n), high = min(k, m);

    while (low <= high) {
        int mid1 = (low + high) / 2;
        int mid2 = k - mid1;

        int l1 = (mid1 == 0 ? INT_MIN : a[mid1 - 1]);
        int l2 = (mid2 == 0 ? INT_MIN : b[mid2 - 1]);
        int r1 = (mid1 == m ? INT_MAX : a[mid1]);
        int r2 = (mid2 == n ? INT_MAX : b[mid2]);

        if (l1 <= r2 && l2 <= r1) return max(l1, l2);
        else if (l1 > r2) high = mid1 - 1;
        else low = mid1 + 1;
    }
    return 0;
}
```

✅ Key idea: Partition arrays such that **left part contains k elements**.

---

# **2️⃣ Row with Maximum 1s in a Binary Matrix**

### **Problem:**

* Binary matrix with rows sorted (0 → 1).
* Find **row index with maximum 1s**.

### **Intuition:**

* For each row, use **binary search** to find the first `1`.
* Number of 1s = `m - index_of_first_1`.

### **Code:**

```cpp
int lowerBound(vector<int> arr, int n, int x) {
    int low = 0, high = n - 1, ans = n;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] >= x) { ans = mid; high = mid - 1; }
        else low = mid + 1;
    }
    return ans;
}

int rowWithMax1s(vector<vector<int>> &matrix, int n, int m) {
    int cnt_max = 0, index = -1;
    for (int i = 0; i < n; i++) {
        int cnt_ones = m - lowerBound(matrix[i], m, 1);
        if (cnt_ones > cnt_max) { cnt_max = cnt_ones; index = i; }
    }
    return index;
}
```

✅ **Binary search** reduces row scan from O(m) → O(log m).

---

# **3️⃣ Search in a 2D Matrix (Flattened)**

### **Problem:**

* 2D matrix sorted row-wise and column-wise.
* Check if `target` exists.

### **Intuition:**

* Flatten 2D → 1D index, apply **binary search**.

### **Code:**

```cpp
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int n = matrix.size(), m = matrix[0].size();
    int low = 0, high = n * m - 1;

    while (low <= high) {
        int mid = (low + high) / 2;
        int row = mid / m, col = mid % m;
        if (matrix[row][col] == target) return true;
        else if (matrix[row][col] < target) low = mid + 1;
        else high = mid - 1;
    }
    return false;
}
```

---

# **4️⃣ Search in Row and Column Wise Sorted Matrix**

### **Problem:**

* Matrix sorted **row-wise & column-wise**.
* Find `target`.

### **Intuition:**

* Start from **top-right corner**:

  * If bigger → move left.
  * If smaller → move down.

### **Code:**

```cpp
bool searchElement(vector<vector<int>>& matrix, int target) {
    int n = matrix.size(), m = matrix[0].size();
    int row = 0, col = m - 1;

    while (row < n && col >= 0) {
        if (matrix[row][col] == target) return true;
        else if (matrix[row][col] < target) row++;
        else col--;
    }
    return false;
}
```

✅ Complexity: **O(n + m)**

---

# **5️⃣ Find Peak Element in 2D Matrix**

### **Problem:**

* A **peak element** is greater than neighbors (up, down, left, right).

### **Intuition:**

* Pick **middle column**, find **max in column**.
* Compare with neighbors to decide moving left/right.
* Apply **binary search on columns**.

### **Code:**

```cpp
int getMaxInColumn(const vector<vector<int>>& matrix, int midCol, int& maxRow) {
    int maxValue = matrix[0][midCol], n = matrix.size();
    maxRow = 0;
    for (int i = 1; i < n; ++i) {
        if (matrix[i][midCol] > maxValue) { maxValue = matrix[i][midCol]; maxRow = i; }
    }
    return maxValue;
}

pair<int,int> findPeak2D(const vector<vector<int>>& matrix) {
    int rows = matrix.size(), cols = matrix[0].size();
    int left = 0, right = cols - 1;

    while (left <= right) {
        int midCol = (left + right) / 2, maxRow;
        int maxValue = getMaxInColumn(matrix, midCol, maxRow);

        bool leftBigger = (midCol > 0 && matrix[maxRow][midCol-1] > maxValue);
        bool rightBigger = (midCol < cols-1 && matrix[maxRow][midCol+1] > maxValue);

        if (!leftBigger && !rightBigger) return {maxRow, midCol};
        else if (leftBigger) right = midCol - 1;
        else left = midCol + 1;
    }
    return {-1,-1};
}
```

✅ Complexity: **O(rows * log cols)**

---

# **6️⃣ Median of a Row-Wise Sorted Matrix**

### **Problem:**

* Find median of a **row-wise sorted matrix**.

### **Intuition:**

* **Binary search on answer space (min → max value)**
* Count numbers ≤ mid in each row using **upperBound**.

### **Code:**

```cpp
int upperBound(vector<int> &arr, int x, int n) {
    int low = 0, high = n - 1, ans = n;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] > x) { ans = mid; high = mid - 1; }
        else low = mid + 1;
    }
    return ans;
}

int countSmallEqual(vector<vector<int>> &matrix, int m, int n, int x) {
    int cnt = 0;
    for (int i = 0; i < m; i++) cnt += upperBound(matrix[i], x, n);
    return cnt;
}

int median(vector<vector<int>> &matrix, int m, int n) {
    int low = INT_MAX, high = INT_MIN;
    for (int i = 0; i < m; i++) { low = min(low, matrix[i][0]); high = max(high, matrix[i][n-1]); }

    int req = (n*m)/2;
    while (low <= high) {
        int mid = (low + high)/2;
        int smallEqual = countSmallEqual(matrix, m, n, mid);
        if (smallEqual <= req) low = mid + 1;
        else high = mid - 1;
    }
    return low;
}
```

✅ **Binary search on value space** reduces complexity to **O(32 * m * log n)**.

---
