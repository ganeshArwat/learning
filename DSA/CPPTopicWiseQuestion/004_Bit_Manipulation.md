
## **Bit Manipulations**

---

### **Q1. Add Binary Strings**

**Problem:**
Given two binary strings `A` and `B`, return their sum as a binary string.

**Constraints:**

* `1 <= length of A, B <= 10^5`
* `A` and `B` are binary strings.

**Examples:**

```
Input:  A = "100", B = "11"   => Output: "111"
Input:  A = "110", B = "10"   => Output: "1000"
```

**Idea:**
Simulate binary addition manually:

1. Pad the shorter string with leading zeros.
2. Add bit by bit from right to left, keeping track of carry.
3. Append result bits and reverse at the end.

**Code:**

```cpp
string addBinary(string A, string B) {
    int lenA = A.size(), lenB = B.size();
    int max_len = max(lenA, lenB);

    string A_padded(max_len - lenA, '0'); A_padded += A;
    string B_padded(max_len - lenB, '0'); B_padded += B;

    string result = "";
    int carry = 0;

    for (int i = max_len - 1; i >= 0; i--) {
        int bitA = A_padded[i] - '0';
        int bitB = B_padded[i] - '0';
        int total = bitA + bitB + carry;
        result.push_back((total % 2) + '0');
        carry = total / 2;
    }

    if (carry) result.push_back('1');
    reverse(result.begin(), result.end());
    return result;
}
```

---

## **Bit Manipulations 1**

---

### **Q1. Set Bit**

**Problem:**
Set the `A`-th and `B`-th bits of `0` and return the decimal value.

**Idea:**
Use bitwise OR `|` with `1 << A` and `1 << B`.

**Code:**

```cpp
int Solution::solve(int A, int B) {
    return (1 << A) | (1 << B);
}
```

---

### **Q2. Unset i-th Bit**

**Problem:**
Unset the `B`-th bit of `A` if it is set.

**Idea:**
Use bitwise AND `&` with NOT mask `~(1 << B)`.

**Code:**

```cpp
int Solution::solve(int A, int B) {
    return A & ~(1 << B);
}
```

---

### **Q3. Check Bit**

**Problem:**
Return `1` if the `B`-th bit in `A` is set, else `0`.

**Idea:**
Use bitwise AND `&` with mask `1 << B`.

**Code:**

```cpp
int Solution::solve(int A, int B) {
    return (A & (1 << B)) ? 1 : 0;
}
```

---

### **Q4. Number of 1 Bits**

**Problem:**
Count the number of `1` bits in the binary representation of `A`.

**Idea:**
Right shift `A` and count bits using `A & 1`.

**Code:**

```cpp
int Solution::numSetBits(int A) {
    int count = 0;
    while(A > 0){
        count += (A & 1);
        A >>= 1;
    }
    return count;
}
```

---

### **Q5. Help From Sam**

**Problem:**
Minimize the number of times you need to add `1` to reach `A` if you can also double your score.

**Idea:**
Count `1`s in binary representation of `A`.

**Code:**

```cpp
int Solution::solve(int A) {
    int count = 0;
    while(A > 0){
        if(A % 2 == 0) A /= 2;
        else { A -= 1; count++; }
    }
    return count;
}
```

---

### **Q6. Toggle i-th Bit**

**Problem:**
Toggle the `B`-th bit in `A`.

**Idea:**
Use XOR `^` with `1 << B`.

**Code:**

```cpp
int Solution::solve(int A, int B) {
    return A ^ (1 << B);
}
```

---

### **Q7. Unset x Bits from Right**

**Problem:**
Unset `B` rightmost bits of `A`.

**Idea:**
Create a mask with rightmost `B` bits unset: `~((1L << B) - 1)`.

**Code:**

```cpp
long Solution::solve(long A, int B) {
    long mask = ~((1L << B) - 1);
    return A & mask;
}
```

---

### **Q8. Finding Good Days**

**Problem:**
Number of days Boomer received food = number of `1`s in binary of `A`.

**Idea:**
Count set bits in `A`.

**Code:**

```cpp
int Solution::solve(int A) {
    int count = 0;
    while(A > 0){
        count += (A & 1);
        A >>= 1;
    }
    return count;
}
```

---

### **Q9. Find nth Magic Number**

**Problem:**
Find the Ath magic number. Magic numbers = sum of unique powers of 5.

**Idea:**
Check bits of `A`; if bit `i` is set, add `5^i` to result.

**Code:**

```cpp
int Solution::solve(int A) {
    int magic = 0;
    int powerOf5 = 5;

    for(int i = 0; i < 31; i++){
        if(A & (1 << i)) magic += powerOf5;
        powerOf5 *= 5;
    }

    return magic;
}
```

---

## **Bit Manipulations 2**

---

### **Q1. Single Number**

**Problem:**
In an array where every element appears twice except one, find the single element.

**Idea:**
Use XOR: `x ^ x = 0`, `x ^ 0 = x`. XOR all numbers gives the single number.

**Code:**

```cpp
int Solution::singleNumber(const vector<int> &A) {
    int ans = 0;
    for(int num : A){
        ans ^= num;
    }
    return ans;
}
```

---

### **Q2. Single Number II**

**Problem:**
In an array where every element appears thrice except one, find that element.

**Idea:**
Count bits at each position modulo 3. Reconstruct the number from bits.

**Code:**

```cpp
int Solution::singleNumber(const vector<int> &A) {
    int ans = 0;
    for(int b = 0; b < 31; b++){
        int count = 0;
        for(int num : A){
            if(num & (1 << b)) count++;
        }
        if(count % 3 == 1){
            ans |= (1 << b);
        }
    }
    return ans;
}
```

---

### **Q3. Single Number III**

**Problem:**
Array has two unique numbers; all others appear twice. Find the two unique numbers.

**Idea:**

1. XOR all elements → gives `x ^ y`.
2. Find a set bit in XOR to separate numbers into two groups.
3. XOR each group individually.

**Code:**

```cpp
vector<int> Solution::solve(vector<int> &A) {
    int xo = 0;
    for(int num : A) xo ^= num;

    int b = 0;
    while(!(xo & (1 << b))) b++;

    int x = 0, y = 0;
    for(int num : A){
        if(num & (1 << b)) x ^= num;
        else y ^= num;
    }

    if(x > y) return {y, x};
    return {x, y};
}
```

---

### **Q4. Find Two Missing Numbers**

**Problem:**
Array of length N contains distinct numbers in [1, N+2]. Two numbers are missing. Find them.

**Idea:**
Use sum and sum of squares formulas to solve equations.

**Code:**

```cpp
vector<int> Solution::solve(vector<int> &A) {
    int N = A.size();
    long long totalSum = (N + 2LL) * (N + 3) / 2;
    long long totalSquareSum = (N + 2LL) * (N + 3) * (2*(N+2) + 1) / 6;

    long long arraySum = 0, arraySquareSum = 0;
    for(int num : A){
        arraySum += num;
        arraySquareSum += 1LL * num * num;
    }

    long long sumDiff = totalSum - arraySum; 
    long long squareSumDiff = totalSquareSum - arraySquareSum; 
    long long xySum = (sumDiff * sumDiff - squareSumDiff) / 2;

    long long discriminant = sumDiff * sumDiff - 4 * xySum;
    int x = (sumDiff + sqrt(discriminant)) / 2;
    int y = sumDiff - x;

    if(x > y) return {y, x};
    return {x, y};
}
```

---

### **Q5. Maximum AND Pair**

**Problem:**
Find maximum `A[i] & A[j]` for all pairs.

**Idea:**
Check each bit from 31 → 0. Keep numbers with that bit set if ≥2 numbers have it.

**Code:**

```cpp
int Solution::solve(vector<int> &A) {
    int ans = 0;
    for(int b = 31; b >= 0; b--){
        int count = 0;
        for(int num : A) if(num & (1 << b)) count++;
        if(count >= 2){
            ans |= (1 << b);
            for(int &num : A) if(!(num & (1 << b))) num = 0;
        }
    }
    return ans;
}
```

---

### **Q6. Subarray OR Sum**

**Problem:**
Sum of bitwise OR of all subarrays modulo 10^9+7.

**Idea:**
For each bit, count subarrays containing it and add contribution.

**Code:**

```cpp
int Solution::solve(vector<int> &A) {
    const int MOD = 1000000007;
    int N = A.size();
    long long result = 0;

    for(int bit = 0; bit < 31; bit++){
        long long contribution = 0;
        int lastIndex = -1;

        for(int i = 0; i < N; i++){
            if(A[i] & (1 << bit)) lastIndex = i;
            contribution += (lastIndex + 1);
            contribution %= MOD;
        }

        result += (contribution * (1LL << bit)) % MOD;
        result %= MOD;
    }

    return result;
}
```

---

### **Q7. Strange Equality**

**Problem:**
Find XOR of `X` (largest smaller than A with `X^A = X+A`) and `Y` (smallest larger than A with `Y^A = Y+A`).

**Idea:**
`XOR = 0` with bits that cause carry. Find rightmost set bit and use it to compute X and Y.

**Code:**

```cpp
int Solution::solve(int A) {
    if(A == 0) return 0;
    int rightmost_set_bit = A & (A - 1);
    int X = A ^ rightmost_set_bit;
    int Y = A + rightmost_set_bit;
    return X ^ Y;
}
```

---

### **Q8. Min XOR Value**

**Problem:**
Find minimum XOR of any pair in an array.

**Idea:**
Sort the array. Minimum XOR occurs between adjacent elements.

**Code:**

```cpp
int Solution::findMinXor(vector<int> &A) {
    sort(A.begin(), A.end());
    int minXOR = INT_MAX;
    for(int i = 0; i < A.size()-1; i++){
        minXOR = min(minXOR, A[i] ^ A[i+1]);
    }
    return minXOR;
}
```

---

### **Q9. Sum of XOR of All Pairs**

**Problem:**
Sum of XOR of all pairs modulo 10^9+7.

**Idea:**
For each bit, calculate contribution as `countOnes * countZeros * (1 << bit)`.

**Code:**

```cpp
int Solution::solve(vector<int> &A) {
    const int MOD = 1000000007;
    long long result = 0;
    int N = A.size();

    for(int bit = 0; bit <= 30; bit++){
        long long countOnes = 0;
        for(int num : A) if(num & (1 << bit)) countOnes++;
        long long pairs = countOnes * (N - countOnes) % MOD;
        result = (result + pairs * (1LL << bit) % MOD) % MOD;
    }

    return result;
}
```

### **1️⃣ XOR of Numbers in a Range**

* **XOR from 1 to N** can be computed in **O(1)** using a pattern based on `N % 4`:

```cpp
int xorFrom1ToN(int N) {
    if (N % 4 == 0) return N;
    if (N % 4 == 1) return 1;
    if (N % 4 == 2) return N + 1;
    return 0; // N % 4 == 3
}
```

* **XOR from L to R**:

```cpp
int xorFromLToR(int L, int R) {
    return xorFrom1ToN(R) ^ xorFrom1ToN(L - 1);
}
```

**Explanation:**

* XOR of a sequence `[1, N]` repeats every 4 numbers:

  * `N % 4 == 0 → N`
  * `N % 4 == 1 → 1`
  * `N % 4 == 2 → N + 1`
  * `N % 4 == 3 → 0`
* Then, XOR from `L` to `R` is just `xorFrom1ToN(R) ^ xorFrom1ToN(L-1)`.

---

### **2️⃣ Divide Two Integers Using Bit Manipulation**

* **No multiplication or division operator.**
* Use **bit shifting** to repeatedly subtract multiples of the divisor.

```cpp
int divide(int dividend, int divisor) {
    if (divisor == 0) return INT_MAX; 
    if (dividend == INT_MIN && divisor == -1) return INT_MAX; // Overflow

    bool negative = (dividend < 0) ^ (divisor < 0);

    long long a = abs((long long)dividend);
    long long b = abs((long long)divisor);
    long long result = 0;

    while (a >= b) {
        long long temp = b, multiple = 1;
        while (a >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }
        a -= temp;
        result += multiple;
    }

    result = negative ? -result : result;

    if (result > INT_MAX) return INT_MAX;
    if (result < INT_MIN) return INT_MIN;

    return (int)result;
}
```

**Explanation:**

1. Convert both numbers to **positive**.
2. Use **bit shifts (`<<`)** to find largest multiples of divisor that fit into dividend.
3. Subtract and accumulate the quotient.
4. Adjust the **sign** at the end.

✅ This ensures **O(log N)** runtime without using `/` or `*`.


