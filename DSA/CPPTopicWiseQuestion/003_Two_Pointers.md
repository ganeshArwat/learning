
# **📌 Two Pointers**

---

## **Q1. Container With Most Water**

**Problem:** Find two lines in an array forming the container with maximum water.
**Approach:** Two pointers, move the pointer with smaller height inward.

```cpp
int Solution::maxArea(vector<int> &A) {
    int left = 0, right = A.size() - 1, max_area = 0;
    while (left < right) {
        int area = min(A[left], A[right]) * (right - left);
        max_area = max(max_area, area);
        if (A[left] < A[right]) left++;
        else right--;
    }
    return max_area;
}
```

---

## **Q2. Subarray with Given Sum**

**Problem:** Find first continuous subarray with sum = B.
**Approach:** Sliding window for positive integers.

```cpp
vector<int> Solution::solve(vector<int> &A, int B) {
    int start = 0, curr_sum = 0;
    for (int end = 0; end < A.size(); end++) {
        curr_sum += A[end];
        while (curr_sum > B && start <= end) curr_sum -= A[start++];
        if (curr_sum == B) return vector<int>(A.begin() + start, A.begin() + end + 1);
    }
    return {-1};
}
```

---

## **Q3. Pairs with Given Sum II (Sorted Array)**

**Problem:** Count pairs `(i,j)` such that `A[i]+A[j]=B`.
**Approach:** Two pointers + count duplicates.

```cpp
int Solution::solve(vector<int> &A, int B) {
    int i = 0, j = A.size() - 1, mod = 1e9+7;
    long long ans = 0;
    while(i < j){
        if(A[i]+A[j]<B) i++;
        else if(A[i]+A[j]>B) j--;
        else{
            if(A[i]==A[j]){
                long long n=j-i+1;
                ans += n*(n-1)/2;
                break;
            } else {
                long long ci=1, cj=1;
                while(i+1<j && A[i]==A[i+1]){ci++; i++;}
                while(j-1>i && A[j]==A[j-1]){cj++; j--;}
                ans=(ans+ci*cj)%mod;
                i++; j--;
            }
        }
    }
    return ans%mod;
}
```

---

## **Q4. Pairs with Given Difference**

**Problem:** Count distinct pairs with difference = B.
**Approach:** HashSet, handle B=0 separately.

```cpp
int Solution::solve(vector<int> &A, int B){
    int ans=0;
    if(B==0){
        unordered_map<int,int> mp;
        for(int v:A) if(++mp[v]==2) ans++;
        return ans;
    }
    unordered_set<int> s;
    for(int v:A){
        if(!s.count(v)){
            if(s.count(v+B)) ans++;
            if(s.count(v-B)) ans++;
        }
        s.insert(v);
    }
    return ans;
}
```

---

## **Q5. 3 Sum Closest**

**Problem:** Find sum of three numbers closest to B.
**Approach:** Sort + two pointers.

```cpp
int Solution::threeSumClosest(vector<int> &A, int B){
    sort(A.begin(), A.end());
    int sum=0, diff=INT_MAX;
    for(int i=0;i<A.size();i++){
        int l=0,r=A.size()-1;
        while(l<r){
            if(l==i) l++;
            else if(r==i) r--;
            else{
                int currSum = A[i]+A[l]+A[r];
                if(abs(B-currSum)<=abs(diff)){diff=B-currSum; sum=currSum;}
                if(currSum<B) l++;
                else r--;
            }
        }
    }
    return sum;
}
```

---

## **Q6. Array 3 Pointers**

**Problem:** Minimize `max(|A[i]-B[j]|, |B[j]-C[k]|, |C[k]-A[i]|)`.
**Approach:** Move pointer with minimum value.

```cpp
int Solution::minimize(const vector<int> &A, const vector<int> &B, const vector<int> &C){
    int i=0,j=0,k=0, minMaxDiff=INT_MAX;
    while(i<A.size() && j<B.size() && k<C.size()){
        int a=A[i], b=B[j], c=C[k];
        minMaxDiff = min(minMaxDiff, max({abs(a-b), abs(b-c), abs(c-a)}));
        if(a<=b && a<=c) i++;
        else if(b<=a && b<=c) j++;
        else k++;
    }
    return minMaxDiff;
}
```

---

## **Q7. Max Continuous Series of 1s**

**Problem:** Maximize 1s by flipping at most B zeros.
**Approach:** Sliding window, track zero count.

```cpp
vector<int> Solution::maxone(vector<int> &A, int B){
    int left=0,right=0,maxLen=0,maxStart=0,zeroCount=0;
    while(right<A.size()){
        if(A[right]==0) zeroCount++;
        while(zeroCount>B){
            if(A[left]==0) zeroCount--;
            left++;
        }
        if(right-left+1>maxLen){maxLen=right-left+1; maxStart=left;}
        right++;
    }
    vector<int> res;
    for(int i=maxStart;i<maxStart+maxLen;i++) res.push_back(i);
    return res;
}
```

---

## **Q8. Count Rectangles with Area < B**

**Problem:** Count rectangles with distinct configurations < B.
**Approach:** Two pointers.

```cpp
int Solution::solve(vector<int> &A, int B){
    int n=A.size();
    long long ans=0;
    int l=0,r=n-1;
    while(l<=r){
        long long prod=(long long)A[l]*A[r];
        if(prod<B){ans+=(2*(r-l)+1); l++;}
        else r--;
    }
    return ans%1000000007;
}
```

---

## **Q9. Closest Pair from Sorted Arrays**

**Problem:** Find pair `(A[i],B[j])` closest to C.
**Approach:** Two pointers: left on A, right on B.

```cpp
vector<int> Solution::solve(vector<int> &A, vector<int> &B, int C){
    int left=0,right=B.size()-1,i=-1,j=-1,diff=INT_MAX;
    while(left<A.size() && right>=0){
        int sum=A[left]+B[right], currDiff=abs(sum-C);
        if(currDiff<diff){diff=currDiff;i=left;j=right;}
        else if(currDiff==diff && A[left]==A[i]) j=right;
        if(sum>C) right--;
        else if(sum<C) left++;
        else break;
    }
    return {A[i], B[j]};
}
```

---

## **Two Pointers & Sliding Window Problems Cheat Sheet**

---

### 1. **Maximum Points You Can Obtain from Cards**

**Problem:** Pick `k` cards from either end to maximize sum.
**Idea:** Sliding window by considering `k` from left + right.

```cpp
int maxSum(vector<int>& nums, int k) {
    int n = nums.size();
    int lsum = 0;
    for (int i = 0; i < k; i++) lsum += nums[i];

    int maxSum = lsum;
    int rsum = 0, ri = n - 1;

    for (int i = k - 1; i >= 0; i--) {
        lsum -= nums[i];
        rsum += nums[ri--];
        maxSum = max(maxSum, lsum + rsum);
    }

    return maxSum;
}
```

---

### 2. **Longest Substring Without Repeating Characters**

**Problem:** Find length of substring with unique characters.
**Idea:** Sliding window + hashmap to track last occurrence.

```cpp
int longestSubstringWithoutRepeatingCharacters(const string &s) {
    vector<int> hash(256, -1);
    int l = 0, maxlen = 0;
    for (int r = 0; r < s.size(); r++) {
        if (hash[s[r]] != -1) l = max(l, hash[s[r]] + 1);
        maxlen = max(maxlen, r - l + 1);
        hash[s[r]] = r;
    }
    return maxlen;
}
```

---

### 3. **Max Consecutive Ones III** (at most k zeros allowed)

**Idea:** Count zeros, shrink window if zeros > k.

```cpp
int maxConsecutiveOnes(vector<int>& nums, int k) {
    int l = 0, maxlen = 0, zeros = 0;
    for (int r = 0; r < nums.size(); r++) {
        if (nums[r] == 0) zeros++;
        while (zeros > k) if (nums[l++] == 0) zeros--;
        maxlen = max(maxlen, r - l + 1);
    }
    return maxlen;
}
```

---

### 4. **Fruit Into Baskets / Longest Subarray with At Most K Distinct**

**Idea:** Sliding window + hashmap to track counts of elements.

```cpp
int totalFruit(vector<int>& arr, int K) {
    unordered_map<int,int> map;
    int l = 0, maxlen = 0;
    for (int r = 0; r < arr.size(); r++) {
        map[arr[r]]++;
        while (map.size() > K) {
            if (--map[arr[l]] == 0) map.erase(arr[l]);
            l++;
        }
        maxlen = max(maxlen, r - l + 1);
    }
    return maxlen;
}
```

---

### 5. **Longest Substring With At Most K Distinct Characters**

**Idea:** Same as above but for string.

```cpp
int lengthOfLongestSubstringKDistinct(string s, int K) {
    unordered_map<char,int> map;
    int l = 0, maxlen = 0;
    for (int r = 0; r < s.size(); r++) {
        map[s[r]]++;
        while (map.size() > K) {
            if (--map[s[l]] == 0) map.erase(s[l]);
            l++;
        }
        maxlen = max(maxlen, r - l + 1);
    }
    return maxlen;
}
```

---

### 6. **Number of Substrings Containing All Three Characters**

**Idea:** Track last seen index for `'a','b','c'` and count substrings ending at current index.

```cpp
int countSubstringsContainingAllChars(string s) {
    vector<int> last(3, -1);
    int cnt = 0;
    for (int i = 0; i < s.size(); i++) {
        last[s[i]-'a'] = i;
        if (last[0]!=-1 && last[1]!=-1 && last[2]!=-1)
            cnt += 1 + min({last[0], last[1], last[2]});
    }
    return cnt;
}
```

---

### 7. **Longest Repeating Character Replacement**

**Idea:** Keep max frequency char in window, shrink if replacements > K.

```cpp
int longestRepeatingCharacterReplacement(string S, int K) {
    vector<int> hash(26, 0);
    int l = 0, maxlen = 0, maxf = 0;
    for (int r = 0; r < S.size(); r++) {
        hash[S[r]-'A']++;
        maxf = max(maxf, hash[S[r]-'A']);
        while ((r-l+1) - maxf > K) hash[S[l++]-'A']--;
        maxlen = max(maxlen, r-l+1);
    }
    return maxlen;
}
```

---

### 8. **Binary Subarrays With Sum = K**

**Idea:** Count subarrays with sum ≤ K, then subtract to get exact K.

```cpp
int F_less_equal_K(vector<int>& arr, int k) {
    int l = 0, sum = 0, count = 0;
    for (int r = 0; r < arr.size(); r++) {
        sum += arr[r];
        while (sum > k) sum -= arr[l++];
        count += r-l+1;
    }
    return count;
}
int countSubarraysWithSum(vector<int>& arr, int k) {
    return F_less_equal_K(arr, k) - F_less_equal_K(arr, k-1);
}
```

---

### 9. **Count Nice Subarrays (Exactly K Odd Numbers)**

**Idea:** Convert odd → 1, even → 0, then use same ≤ K trick.

```cpp
int countNiceSubarrays(vector<int>& nums, int K) {
    vector<int> arr(nums.size());
    for (int i = 0; i < nums.size(); i++) arr[i] = nums[i]%2;
    return F_less_equal_K(arr, K) - F_less_equal_K(arr, K-1);
}
```

---

### 10. **Subarray With K Different Integers**

**Idea:** Count at most K distinct subarrays → subtract to get exactly K.

```cpp
int F(vector<int>& arr, int K) {
    unordered_map<int,int> map;
    int l = 0, count = 0;
    for (int r = 0; r < arr.size(); r++) {
        map[arr[r]]++;
        while (map.size() > K) if (--map[arr[l++]] == 0) map.erase(arr[l-1]);
        count += r-l+1;
    }
    return count;
}
int subarraysWithKDistinct(vector<int>& nums, int K) {
    return F(nums, K) - F(nums, K-1);
}
```

---

### 11. **Minimum Window Substring**

**Idea:** Sliding window + hashmap to track required chars.

```cpp
string minWindow(string s, string t) {
    if (s.empty() || t.empty()) return "";
    unordered_map<char,int> target;
    for(char c:t) target[c]++;
    
    unordered_map<char,int> window;
    int l = 0, have = 0, need = target.size(), minLen = INT_MAX, start = 0;
    
    for(int r=0;r<s.size();r++){
        char c = s[r]; 
        window[c]++;
        if(target.count(c) && window[c]==target[c]) have++;
        
        while(have==need){
            if(r-l+1<minLen) {minLen = r-l+1; start=l;}
            char left = s[l];
            window[left]--;
            if(target.count(left) && window[left]<target[left]) have--;
            l++;
        }
    }
    return minLen==INT_MAX?"":s.substr(start,minLen);
}
```

