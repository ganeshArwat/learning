
### **Selection Sort**

```cpp
for (int i = 0; i < n - 1; i++) {
    int minIndex = i;  // Assume the current index is the minimum
    for (int j = i + 1; j < n; j++) {
        if (arr[j] < arr[minIndex]) {  // Find the minimum element in the remaining array
            minIndex = j;
        }
    }
    if (minIndex != i) {  // Swap only if a smaller element is found
        swap(arr[i], arr[minIndex]);
    }
}
```

* **Explanation:**
  Finds the minimum element in the unsorted part of the array and places it at the correct position.
* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

---

### **Bubble Sort**

```cpp
bool swapped;
for (int i = 0; i < n - 1; i++) {
    swapped = false;
    for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            swap(arr[j], arr[j + 1]);  // Swap adjacent elements if they are in the wrong order
            swapped = true;
        }
    }
    // If no elements were swapped in a pass, the array is already sorted
    if (!swapped) {
        break;
    }
}
```

* **Explanation:**
  Repeatedly moves the largest unsorted element to its correct position.
* **Time Complexity:** O(n²)
* **Best Case:** O(n) if already sorted

---

### **Insertion Sort**

```cpp
for (int i = 1; i < n; i++) {
    int key = arr[i];  // The element to insert into the sorted part
    int j = i - 1;

    // Shift elements of the sorted part that are greater than key to the right
    while (j >= 0 && arr[j] > key) {
        arr[j + 1] = arr[j];
        j--;
    }
    arr[j + 1] = key;  // Place key in the correct position
}
```

* **Explanation:**
  Builds the sorted array one element at a time by inserting the current element into its correct position.
* **Time Complexity:** O(n²)
* **Best Case:** O(n) if already sorted

---

## **1️⃣ Minimum Cost to Remove All Elements**

```cpp
std::sort(A.begin(), A.end(), std::greater<int>());
int cost = 0;
for (int i = 0; i < A.size(); i++) {
    cost += A[i] * (i+1);
}
```

**Explanation:**

* **Idea:** Remove larger elements first → reduces total cost.
* Sorting in **descending order** ensures we remove **largest elements first**.
* Multiply by `(i+1)` because after `i` removals, the cost of removing `A[i]` is counted `i+1` times.

**Time Complexity:** O(n log n) (sorting)
**Example:**
A = [2, 1] → sorted → [2, 1] → cost = 2*1 + 1*2 = 4 ✅

---

## **2️⃣ Noble Integer**

```cpp
std::sort(A.begin(), A.end(), std::greater<int>());
int cnt = 0;
for (int i = 0; i < A.size(); i++) {
    if(i == 0 || A[i] != A[i-1]){
        cnt = i; // Count of numbers greater than A[i]
    }
    if (cnt == A[i]){
        return 1;
    }
}
return -1;
```

**Explanation:**

* **Noble Integer:** Number of integers greater than `p` equals `p`.
* Sort **descending** → easier to count numbers greater than current element.
* Handle **duplicates** by updating `cnt` only when the number changes.

**Time Complexity:** O(n log n) (sorting)

---

## **3️⃣ Kth Smallest Element (Bth)**

```cpp
std::vector<int> vec = A;

for (int i = 0; i < B; ++i) {
    int m = i;
    for (int j = i + 1; j < vec.size(); ++j) {
        if (vec[j] < vec[m]) {
            m = j;
        }
    }
    std::swap(vec[i], vec[m]);
}

return vec[B - 1];
```

**Explanation:**

* Use **partial selection sort** → only do B swaps.
* After B swaps, the **Bth smallest element** is at index `B-1`.
* Optimized if B is small relative to n (as given).

**Time Complexity:** O(B*n) ✅ (better than full sort for small B)

---

## **4️⃣ Arithmetic Progression Check**

```cpp
std::sort(A.begin(), A.end());
int d = A[1] - A[0];

for (int i = 0; i < A.size()-1; i++) {
    if ((A[i+1] - A[i]) != d) {
        return 0;
    }
}
return 1;
```

**Explanation:**

* Sort the array.
* **Check if difference between consecutive elements is constant.**
* If yes → it's an arithmetic progression (can rearrange to form it).

**Time Complexity:** O(n log n) (sorting)

**Note:** In your code snippet, you had `std::greater<int>()` which is descending.

* Arithmetic progression usually checks **ascending order**, so use default `sort(A.begin(), A.end())`.

---

## **1. Counting Sort**

```cpp
int max_val = *max_element(arr.begin(), arr.end());
int min_val = *min_element(arr.begin(), arr.end());
int range = max_val - min_val + 1;

vector<int> count(range, 0);

// Count occurrences
for(int i = 0; i < n; i++)
    count[arr[i] - min_val]++;

// Rebuild sorted array
int index = 0;
for(int i = 0; i < range; i++)
    while(count[i]--)
        arr[index++] = i + min_val;
```

* **Idea:** Count the occurrences of each number, then reconstruct the array.
* **Time Complexity:** O(n + range)
* **Space Complexity:** O(range)
* **Use Case:** Only integers with a limited range.

---

## **2. Merge Two Sorted Arrays**

```cpp
vector<int> mergeSortedArrays(const vector<int>& A, const vector<int>& B){
    int N = A.size(), M = B.size();
    vector<int> C(N + M);
    int i = 0, j = 0, k = 0;
    
    while(i < N && j < M){
        if(A[i] <= B[j]) C[k++] = A[i++];
        else C[k++] = B[j++];
    }
    
    while(i < N) C[k++] = A[i++];
    while(j < M) C[k++] = B[j++];
    
    return C;
}
```

* **Idea:** Merge two already sorted arrays in O(N + M).

---

## **3. Merge Sort**

```cpp
vector<int> mergeSort(const vector<int>& arr){
    if(arr.size() <= 1) return arr;
    
    int mid = arr.size() / 2;
    vector<int> left = mergeSort(vector<int>(arr.begin(), arr.begin() + mid));
    vector<int> right = mergeSort(vector<int>(arr.begin() + mid, arr.end()));
    
    return mergeSortedArrays(left, right);
}
```

* **Idea:** Divide the array, sort each half recursively, then merge.
* **Time Complexity:** O(n log n)
* **Space Complexity:** O(n)

---

## **4. Inversion Count**

```cpp
int mergeAndCount(vector<int>& A, int s, int mid, int e){
    int len1 = mid - s + 1, len2 = e - mid;
    vector<int> left(len1), right(len2);
    for(int i=0;i<len1;i++) left[i] = A[s+i];
    for(int i=0;i<len2;i++) right[i] = A[mid+1+i];
    
    int i=0,j=0,k=s, invCount=0;
    while(i<len1 && j<len2){
        if(left[i] <= right[j]) A[k++] = left[i++];
        else{
            A[k++] = right[j++];
            invCount += (len1 - i);
        }
    }
    while(i<len1) A[k++] = left[i++];
    while(j<len2) A[k++] = right[j++];
    return invCount;
}

int mergeSortAndCount(vector<int>& A, int s, int e){
    if(s >= e) return 0;
    int mid = s + (e-s)/2;
    int invCount = mergeSortAndCount(A,s,mid) + mergeSortAndCount(A,mid+1,e);
    invCount += mergeAndCount(A,s,mid,e);
    return invCount;
}
```

* **Idea:** Count inversions while merging, using modified merge sort.
* **Time Complexity:** O(n log n)

---

## **5. Reverse Pairs**

```cpp
int mergeAndCountReverse(vector<int>& A, int s, int mid, int e){
    int len1 = mid-s+1, len2 = e-mid, count = 0;
    vector<int> left(len1), right(len2);
    
    for(int i=0;i<len1;i++) left[i] = A[s+i];
    for(int i=0;i<len2;i++) right[i] = A[mid+1+i];
    
    int jj = mid+1;
    for(int i=s;i<=mid;i++){
        while(jj <= e && A[i] > 2LL * A[jj]) jj++;
        count += (jj - (mid+1));
    }
    
    // merge
    int i=0,j=0,k=s;
    while(i<len1 && j<len2){
        if(left[i]<=right[j]) A[k++] = left[i++];
        else A[k++] = right[j++];
    }
    while(i<len1) A[k++] = left[i++];
    while(j<len2) A[k++] = right[j++];
    
    return count;
}
```

* **Idea:** Count `(i,j)` pairs where `A[i] > 2*A[j]` while merging.

---

## **6. Minimum Absolute Difference**

```cpp
int minAbsDiff(vector<int>& A){
    sort(A.begin(), A.end());
    int minDiff = INT_MAX;
    for(int i=1;i<A.size();i++)
        minDiff = min(minDiff, A[i] - A[i-1]);
    return minDiff;
}
```

* **Idea:** Sort array first, then check adjacent differences.

---

## **7. Max Chunks To Make Sorted**

```cpp
int maxChunks(vector<int>& A){
    int maxVal = -1, chunks = 0;
    for(int i=0;i<A.size();i++){
        maxVal = max(maxVal, A[i]);
        if(maxVal == i) chunks++;
    }
    return chunks;
}
```

* **Idea:** Count chunks where maximum so far equals current index.

---

## **1. Quick Sort**

```cpp
int partition(vector<int>& A, int low, int high) {
    int pivot = A[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (A[j] <= pivot) {
            i++;
            swap(A[i], A[j]);
        }
    }
    swap(A[i + 1], A[high]);
    return i + 1;
}

void quickSort(vector<int>& A, int low, int high) {
    if (low < high) {
        int pi = partition(A, low, high);
        quickSort(A, low, pi - 1);
        quickSort(A, pi + 1, high);
    }
}
```

* **Idea:** Partition array around a pivot, recursively sort left and right halves.
* **Time Complexity:** O(n log n) average, O(n²) worst-case.
* **Space Complexity:** O(log n) recursion stack.

---

## **2. Custom Comparator Problems**

### a) Tens Digit Sorting

```cpp
bool compare(int a, int b) {
    int tensA = (a / 10) % 10;
    int tensB = (b / 10) % 10;
    if(tensA != tensB) return tensA < tensB;
    return a > b;
}

vector<int> tensDigitSort(vector<int>& A){
    sort(A.begin(), A.end(), compare);
    return A;
}
```

* **Idea:** Sort by tens digit ascending, then by value descending if tie.

---

### b) Factor Sort

```cpp
int countFactors(int n){
    int count = 0;
    for(int i=1;i*i<=n;i++){
        if(n % i == 0){
            count += (i*i == n) ? 1 : 2;
        }
    }
    return count;
}

vector<int> factorSort(vector<int>& A){
    sort(A.begin(), A.end(), [](int a,int b){
        int fA = countFactors(a);
        int fB = countFactors(b);
        return (fA == fB) ? a < b : fA < fB;
    });
    return A;
}
```

* **Idea:** Sort by number of distinct factors; tie-breaker: smaller number first.

---

### c) Largest Number

```cpp
bool compareStr(const string &a, const string &b){
    return a + b > b + a;
}

string largestNumber(vector<int>& A){
    vector<string> strNums;
    for(int num: A) strNums.push_back(to_string(num));
    sort(strNums.begin(), strNums.end(), compareStr);
    
    string result;
    for(const auto &s: strNums) result += s;
    return result[0] == '0' ? "0" : result;
}
```

* **Idea:** Custom comparator: join numbers as strings to form largest value.

---

### d) B Closest Points to Origin

```cpp
inline int squaredDistance(int x,int y){ return x*x + y*y; }

bool comparePoints(const vector<int>& a, const vector<int>& b){
    return squaredDistance(a[0],a[1]) < squaredDistance(b[0],b[1]);
}

vector<vector<int>> closestPoints(vector<vector<int>> &A, int B){
    sort(A.begin(), A.end(), comparePoints);
    return vector<vector<int>>(A.begin(), A.begin() + B);
}
```

* **Idea:** Sort points by squared Euclidean distance; return first B points.

---

### e) Sort Colors (Dutch National Flag)

```cpp
vector<int> sortColors(vector<int>& A){
    int low=0, mid=0, high=A.size()-1;
    while(mid <= high){
        if(A[mid]==0) swap(A[low++], A[mid++]);
        else if(A[mid]==1) mid++;
        else swap(A[mid], A[high--]);
    }
    return A;
}
```

* **Idea:** 3-way partitioning for 0, 1, 2; O(n) time, O(1) space.

---

### f) Wave Array

```cpp
vector<int> waveArray(vector<int>& A){
    sort(A.begin(), A.end());
    for(int i=0;i<A.size()-1;i+=2)
        swap(A[i], A[i+1]);
    return A;
}
```

* **Idea:** Sort first, then swap adjacent pairs for wave pattern `a1 >= a2 <= a3 ...`.

---

## **1. Basic Sorting Algorithms**

| Algorithm          | Idea                                                                 | Time Complexity | Space Complexity | Stable? |
| ------------------ | -------------------------------------------------------------------- | --------------- | ---------------- | ------- |
| **Bubble Sort**    | Repeatedly swap adjacent elements if they are in wrong order.        | O(n²)           | O(1)             | Yes     |
| **Selection Sort** | Select the minimum (or maximum) element and swap with current index. | O(n²)           | O(1)             | No      |
| **Insertion Sort** | Build sorted array by inserting one element at a time.               | O(n²)           | O(1)             | Yes     |

**Key points:**

* Simple, intuitive.
* Good for small arrays or nearly sorted arrays.

---

## **2. Efficient Sorting Algorithms**

| Algorithm         | Idea                                                                     | Time Complexity             | Space Complexity | Stable? |
| ----------------- | ------------------------------------------------------------------------ | --------------------------- | ---------------- | ------- |
| **Merge Sort**    | Divide array into halves, sort recursively, then merge.                  | O(n log n)                  | O(n)             | Yes     |
| **Quick Sort**    | Partition array around a pivot, recursively sort partitions.             | O(n log n) avg, O(n²) worst | O(log n)         | No      |
| **Heap Sort**     | Build a max-heap and extract max repeatedly.                             | O(n log n)                  | O(1)             | No      |
| **Counting Sort** | Count occurrences and rebuild array (works for integers in small range). | O(n + range)                | O(range)         | Yes     |
| **Radix Sort**    | Sort integers digit by digit using stable counting sort.                 | O(n * k)                    | O(n + k)         | Yes     |

**Key points:**

* Merge/Quick are general-purpose.
* Counting/Radix are great for integers with limited range.

---

## **3. Special-Purpose / Linear Time Sorting**

* **Sort Colors (0,1,2)** → Dutch National Flag (3-way partitioning)
* **Wave Array** → Sort + swap adjacent pairs
* **Largest Number Problem** → Sort numbers using custom comparator on string concatenation
* **Closest Points to Origin** → Sort by distance using custom comparator

---

## **4. Comparator / Custom Sorting**

* **Idea:** Define your own “less-than” rule.
* Examples:

  * Tens digit sort → first by tens digit, tie-breaker by value.
  * Factor sort → sort by number of distinct factors.
  * Largest number → sort strings `a+b > b+a`.

---

## **5. Sorting Patterns in Problems**

1. **Remove Elements / Cost Problems** → Sort descending to minimize cost.
2. **Noble Integers** → Sort descending, track count of greater elements.
3. **Kth Smallest** → Selection approach or partial sort.
4. **Inversion Count / Reverse Pairs** → Merge Sort + counting technique.
5. **Chunking / Partitioning** → Track max or min during iteration after sort.

---

### **Tips / Takeaways**

* **Use built-in `sort()`** in C++ whenever possible (O(n log n), stable if using `stable_sort`).
* **Use counting/radix** for integers with small ranges (faster than comparison sorts).
* **Use custom comparators** for complex ordering rules.
* **Merge Sort is reliable** for counting problems like inversions.
* **Quick Sort is practical** but beware worst-case O(n²) if array is already nearly sorted.
