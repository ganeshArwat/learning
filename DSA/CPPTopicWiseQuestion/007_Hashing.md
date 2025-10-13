
## **HASHING**

---

### **Q1. Frequency of Element Query**

* **Problem:** For each element in array `B`, return its frequency in array `A`.
* **Code:**

```cpp
vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    unordered_map<int, int> hashMap;
    for(int num : A) hashMap[num]++;

    vector<int> result(B.size(), 0);
    for(int i=0; i<B.size(); i++){
        if(hashMap.count(B[i])) result[i] = hashMap[B[i]];
    }

    return result;
}
```

---

### **Q2. Count Distinct Elements**

* **Problem:** Return the number of unique elements in array `A`.
* **Code (unordered_set version):**

```cpp
int Solution::solve(vector<int> &A) {
    unordered_set<int> hs;
    for(int num : A) hs.insert(num);
    return hs.size();
}
```

---

### **Q3. First Repeating Element**

* **Problem:** Find the first repeating element in array `A`. Return -1 if none exist.
* **Code:**

```cpp
int Solution::solve(vector<int> &A) {
    unordered_map<int, int> hashMap;
    for(int num : A) hashMap[num]++;
    for(int num : A) if(hashMap[num] > 1) return num;
    return -1;
}
```

---

### **Q4. Sub-array with 0 Sum**

* **Problem:** Check if `A` contains a non-empty subarray with sum 0. Return 1 if yes, else 0.
* **Code:**

```cpp
int Solution::solve(vector<int> &A) {
    unordered_set<long> prefixSumSet;
    long prefixSum = 0;

    for(int num : A) {
        prefixSum += num;
        if(prefixSum == 0 || prefixSumSet.count(prefixSum)) return 1;
        prefixSumSet.insert(prefixSum);
    }
    return 0;
}
```

---

### **Q5. Common Elements**

* **Problem:** Return all common elements in arrays `A` and `B`. Each element should appear min(count in A, count in B) times.
* **Code:**

```cpp
vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    unordered_map<int, int> countMap;
    vector<int> result;

    for(int num : A) countMap[num]++;
    for(int num : B) {
        if(countMap[num] > 0) {
            result.push_back(num);
            countMap[num]--;
        }
    }

    return result;
}
```

---

### **Q1. Count Unique Elements (Frequency 1)**

* **Problem:** Return the count of elements that appear exactly once in `A`.
* **Code:**

```cpp
int Solution::solve(vector<int> &A) {
    unordered_map<int, int> hashMap;
    for(int num : A) hashMap[num]++;

    int count = 0;
    for(const auto& pair : hashMap) if(pair.second == 1) count++;
    return count;
}
```

---

### **Q2. Count Subarray Zero Sum**

* **Problem:** Count subarrays of `A` whose sum is zero. Return result % (10^9+7).
* **Code:**

```cpp
int Solution::solve(vector<int> &A) {
    const int MOD = 1000000007;
    unordered_map<long, int> prefixSumFrequency;
    prefixSumFrequency[0] = 1;

    long prefixSum = 0;
    int count = 0;

    for(int num : A) {
        prefixSum += num;
        if(prefixSumFrequency.count(prefixSum)) {
            count = (count + prefixSumFrequency[prefixSum]) % MOD;
        }
        prefixSumFrequency[prefixSum]++;
    }

    return count;
}
```

---

## **PROBLEMS**

---

### **Q1. Check Pair Sum**

* **Problem:** Check if a pair exists in `B` such that `Bi + Bj = A`. Return 1 if yes, else 0.
* **Code:**

```cpp
int Solution::solve(int A, vector<int> &B) {
    unordered_set<int> hashSet;
    for (int num : B){
        int check = A - num;
        if (hashSet.count(check)) return 1;
        hashSet.insert(num);
    }
    return 0;
}
```

---

### **Q2. Count Pair Difference**

* **Problem:** Count pairs `(i,j)` such that `A[i] - A[j] = B` and `i ≠ j`. Return result % (10^9+7).
* **Code:**

```cpp
int Solution::solve(vector<int> &A, int B) {
    unordered_map<int, int> freq;
    const int MOD = 1000000007;
    long long count = 0;

    for (int num : A){
        if (freq.count(num - B)) count = (count + freq[num - B]) % MOD;
        if (freq.count(num + B)) count = (count + freq[num + B]) % MOD;
        freq[num]++;
    }

    return count;
}
```

---

### **Q3. Subarray Sum Equals K**

* **Problem:** Count the total number of subarrays with sum equal to `B`.
* **Code:**

```cpp
int Solution::solve(vector<int> &A, int B) {
    int count = 0;
    unordered_map<int, int> hashMap;
    int P = 0;

    for(int num : A){
        P += num;
        if(P == B) count++;
        if(hashMap.count(P - B)) count += hashMap[P - B];
        hashMap[P]++;
    }

    return count;
}
```

---

### **Q4. Distinct Numbers in Window**

* **Problem:** Count distinct numbers in all windows of size `B`.
* **Code:**

```cpp
vector<int> Solution::dNums(vector<int> &A, int B) {
    unordered_map<int, int> hashMap;
    vector<int> result;

    for(int i = 0; i < B; i++) hashMap[A[i]]++;
    result.push_back(hashMap.size());

    for(int i = B; i < A.size(); i++){
        hashMap[A[i]]++;
        if(--hashMap[A[i-B]] == 0) hashMap.erase(A[i-B]);
        result.push_back(hashMap.size());
    }

    return result;
}
```

---

### **Q5. Longest Subarray Zero Sum**

* **Problem:** Find length of the longest subarray with sum 0.
* **Code:**

```cpp
int Solution::solve(vector<int> &A) {
    unordered_map<long, int> prefixSumMap;
    int maxLength = 0;
    long prefixSum = 0;

    for(int i = 0; i < A.size(); i++){
        prefixSum += A[i];
        if(prefixSum == 0) maxLength = i + 1;
        if(prefixSumMap.count(prefixSum)) maxLength = max(maxLength, i - prefixSumMap[prefixSum]);
        else prefixSumMap[prefixSum] = i;
    }

    return maxLength;
}
```

---

### **Q1. Count Pair Sum (Pairs counted once)**

* **Problem:** Count pairs `(i,j)` such that `A[i] + A[j] = B` (`i ≠ j`), counting each pair only once. Return % (10^9+7).
* **Code:**

```cpp
int Solution::solve(vector<int> &A, int B) {
    const int MOD = 1000000007;
    unordered_map<int, int> freq;
    long long count = 0;

    for(int num : A){
        if(freq.count(B - num)) count = (count + freq[B - num]) % MOD;
        freq[num]++;
    }

    return count;
}
```

---

### **Q2. Subarray with Given Sum**

* **Problem:** Find the first continuous subarray which adds to `B`. Return [-1] if none.
* **Code:**

```cpp
vector<int> Solution::solve(vector<int> &A, int B) {
    int n = A.size(), left = 0;
    long long currentSum = 0;

    for(int right = 0; right < n; right++){
        currentSum += A[right];
        while(currentSum > B && left <= right){
            currentSum -= A[left++];
        }
        if(currentSum == B) return vector<int>(A.begin() + left, A.begin() + right + 1);
    }

    return vector<int>(1, -1);
}
```

---

### **Q1. Longest Increasing Subsequence**

* **Problem:** Find the length of the longest strictly increasing subsequence in an array.
* **Code:**

```cpp
int Solution::lis(const vector<int> &A) {
    if(A.empty()) return 0;
    int n = A.size();
    vector<int> dp(n, 1);

    for(int i = 1; i < n; i++) {
        for(int j = 0; j < i; j++) {
            if(A[i] > A[j]) dp[i] = max(dp[i], dp[j] + 1);
        }
    }

    return *max_element(dp.begin(), dp.end());
}
```

---

### **Q2. Longest Subarray Zero Sum**

* **Problem:** Length of the longest subarray with sum 0.
* **Code:**

```cpp
int Solution::solve(vector<int> &A) {
    unordered_map<long long, int> hm;
    long long sum = 0;
    int max_len = 0;

    for(int i = 0; i < A.size(); i++) {
        sum += A[i];
        if(sum == 0) max_len = i + 1;
        else if(hm.find(sum) != hm.end()) max_len = max(max_len, i - hm[sum]);
        else hm[sum] = i;
    }

    return max_len;
}
```

---

### **Q1. Colorful Number**

* **Problem:** Check if all consecutive subsequence products of a number’s digits are unique.
* **Code:**

```cpp
int Solution::colorful(int A) {
    string num = to_string(A);
    unordered_set<long long> productSet;

    for(int i = 0; i < num.size(); i++) {
        long long product = 1;
        for(int j = i; j < num.size(); j++) {
            product *= (num[j] - '0');
            if(productSet.count(product)) return 0;
            productSet.insert(product);
        }
    }

    return 1;
}
```

---

### **Q2. Count Subarrays with Unique Elements**

* **Problem:** Count all subarrays with unique elements. Return `% 10^9+7`.
* **Code:**

```cpp
const int MOD = 1e9 + 7;

int Solution::solve(vector<int> &A) {
    int n = A.size(), l = 0, result = 0;
    unordered_set<int> window;

    for(int r = 0; r < n; r++) {
        while(window.find(A[r]) != window.end()) {
            window.erase(A[l++]);
        }
        window.insert(A[r]);
        result = (result + (r - l + 1)) % MOD;
    }

    return result;
}
```

---

### **Q3. Sort Array in Given Order**

* **Problem:** Sort array `A` such that the relative order of elements in `B` is preserved; append remaining elements in sorted order.
* **Code:**

```cpp
vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    unordered_map<int, int> freqMap;
    for(int num : A) freqMap[num]++;

    vector<int> result;

    // Add elements from B
    for(int num : B) {
        if(freqMap.find(num) != freqMap.end()) {
            int count = freqMap[num];
            result.insert(result.end(), count, num);
            freqMap.erase(num);
        }
    }

    // Collect remaining and sort
    vector<int> remaining;
    for(auto &entry : freqMap) remaining.insert(remaining.end(), entry.second, entry.first);
    sort(remaining.begin(), remaining.end());
    result.insert(result.end(), remaining.begin(), remaining.end());

    return result;
}
```
