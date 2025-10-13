## **Modular Arithmetic & GCD**

---

### **Q1. Pair Sum Divisible by M**

* **Problem:** Count pairs in array `A` whose sum is divisible by `B`. Return result modulo (10^9 + 7).
* **Code:**

```cpp
int Solution::solve(vector<int> &A, int B) {
    const int MOD = 1e9 + 7;
    vector<int> freq(B, 0);
    int ans = 0;
    for (int i = 0; i < A.size(); i++) {
        int X = (A[i] % B + B) % B; // Ensure non-negative
        int Y = (B - X) % B;        // Complement remainder
        ans = (ans + freq[Y]) % MOD;
        freq[X]++;
    }
    return ans;
}
```

---

### **Q2. Greatest Common Divisor**

* **Problem:** Find GCD of `A` and `B` without library functions.
* **Code:**

```cpp
int Solution::gcd(int A, int B) {
    if (B == 0) return A;
    return gcd(B, A % B);
}
```

---

### **Q3. Delete One (Max GCD after removing one element)**

* **Problem:** Delete one element from array `A` to maximize GCD of remaining elements.
* **Code:**

```cpp
int gcd(int A, int B) {
    if(B == 0) return A;
    return gcd(B, A%B);
}

int Solution::solve(vector<int> &A) {
    int n = A.size();
    if (n == 2) return max(A[0], A[1]);
    
    vector<int> prefixGCD(n, 0), suffixGCD(n, 0);
    
    prefixGCD[0] = A[0];
    for (int i = 1; i < n; i++) prefixGCD[i] = gcd(prefixGCD[i-1], A[i]);
    
    suffixGCD[n-1] = A[n-1];
    for (int i = n-2; i >= 0; i--) suffixGCD[i] = gcd(suffixGCD[i+1], A[i]);
    
    int maxGCD = max(suffixGCD[1], prefixGCD[n-2]);
    for (int i = 1; i < n-1; i++) {
        maxGCD = max(maxGCD, gcd(prefixGCD[i-1], suffixGCD[i+1]));
    }
    
    return maxGCD;
}
```

---

### **Q4. Mod Sum**

* **Problem:** Calculate sum of `A[i] % A[j]` for all pairs `(i,j)` modulo (10^9 + 7).
* **Code:**

```cpp
int Solution::solve(vector<int> &A) {
    const int MOD = 1e9 + 7, MAX_VAL = 1000;
    vector<int> freq(MAX_VAL + 1, 0);
    for (int val : A) freq[val]++;
    
    long long sum = 0;
    for (int i = 1; i <= MAX_VAL; i++) {
        for (int j = 1; j <= MAX_VAL; j++) {
            if (freq[i] && freq[j]) {
                sum = (sum + (long long)freq[i] * freq[j] * (i % j)) % MOD;
            }
        }
    }
    
    return (int)sum;
}
```

---

### **Q1. A, B and Modulo**

* **Problem:** Find largest `M` such that `A % M == B % M`.
* **Code:**

```cpp
int Solution::solve(int A, int B) {
    return abs(A - B); // Greatest possible M is the difference
}
```

---

### **Q2. Largest Coprime Divisor**

* **Problem:** Find largest `X` that divides `A` and `gcd(X, B) = 1`.
* **Code:**

```cpp
int gcd(int A, int B) {
    if(B == 0) return A;
    return gcd(B, A % B);
}

int Solution::cpFact(int A, int B) {
    int X = A;
    while (gcd(X, B) != 1) X /= gcd(X, B);
    return X;
}
```

---

### **Q3. Divisor Game**

* **Problem:** Count integers ≤ `A` divisible by both `B` and `C`.
* **Code:**

```cpp
int gcd(int A, int B) {
    if(B == 0) return A;
    return gcd(B, A % B);
}

int Solution::solve(int A, int B, int C) {
    long long lcmBC = (1LL * B * C) / gcd(B, C);
    return A / lcmBC;
}
```

---

## **Combinatorics Basics**

---

### **Q1. Pascal Triangle**

* **Problem:** Print Pascal's triangle up to `A` rows.
* **Code:**

```cpp
vector<vector<int> > Solution::solve(int A) {
    vector<vector<int>> pascal(A, vector<int>(A, 0));
    for (int i = 0; i < A; i++) {
        pascal[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j];
        }
    }
    return pascal;
}
```

---

### **Q2. Excel Column Title**

* **Problem:** Convert integer `A` to its Excel column title.
* **Code:**

```cpp
string Solution::convertToTitle(int A) {
    string result = "";
    while (A > 0) {
        A--; // Zero-based adjustment
        char ch = 'A' + (A % 26);
        result = ch + result;
        A /= 26;
    }
    return result;
}
```

---

### **Q3. Compute nCr % m**

* **Problem:** Compute `nCr % m`.
* **Code:**

```cpp
int Solution::solve(int n, int r, int m) {
    int arr[n+1][r+1];
    for(int i=0;i<=n;i++) arr[i][0]=1;
    for(int j=1;j<=r;j++) arr[0][j]=0;
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=r;j++){
            arr[i][j]=(arr[i-1][j]%m + arr[i-1][j-1]%m) % m;
        }
    }
    return arr[n][r] % m;
}
```

---

### **Q1. Excel Column Number**

* **Problem:** Convert Excel column title to number.
* **Code:**

```cpp
int Solution::titleToNumber(string A) {
    int column_number = 0, base = 26;
    for (char c : A) {
        int value = c - 'A' + 1;
        column_number = column_number * base + value;
    }
    return column_number;
}
```

---

### **Q2. Number of Digit One**

* **Problem:** Count number of digit `1` in all numbers ≤ `A`.
* **Code:**

```cpp
int Solution::solve(int A) {
    long long count = 0, factor = 1, num = A;
    while (num > 0) {
        long long digit = num % 10;
        num /= 10;
        count += num * factor;
        if (digit > 1) count += factor;
        else if (digit == 1) count += (A % factor) + 1;
        factor *= 10;
    }
    return count;
}
```

---

### **Q3. Consecutive Numbers Sum**

* **Problem:** Find the number of ways to express `A` as a sum of consecutive positive integers.
* **Code:**

```cpp
int Solution::solve(int A) {
    int count = 0, k = 1;
    while (k * (k - 1) / 2 < A) {
        if ((A - k * (k - 1) / 2) % k == 0) {
            int m = (A - k * (k - 1) / 2) / k;
            if (m > 0) ++count;
        }
        ++k;
    }
    return count;
}
```
---

## **Prime Numbers**

---

### **Q1. Sorted Permutation Rank**

* **Problem:** Find the rank of string `A` amongst its lexicographically sorted permutations (no repeated characters). Return rank % 1000003.
* **Code:**

```cpp
const int MOD = 1000003;
vector<long long> factorial(1001, 1);

void precomputeFactorials() {
    for (int i = 2; i <= 1000; ++i) {
        factorial[i] = (factorial[i - 1] * i) % MOD;
    }
}

int Solution::findRank(string A) {
    precomputeFactorials();
    int n = A.length();
    long long rank = 1;
    for (int i = 0; i < n; ++i) {
        int count_smaller = 0;
        for (int j = i + 1; j < n; ++j) {
            if (A[j] < A[i]) ++count_smaller;
        }
        rank = (rank + (count_smaller * factorial[n - i - 1]) % MOD) % MOD;
    }
    return rank;
}
```

---

### **Q2. Count of Divisors**

* **Problem:** Return the count of divisors for each element in array `A`.
* **Code:**

```cpp
const int MAXN = 1000000;

vector<int> precomputeDivisors() {
    vector<int> divisor_count(MAXN + 1, 0);
    for (int i = 1; i <= MAXN; ++i) {
        for (int j = i; j <= MAXN; j += i) {
            ++divisor_count[j];
        }
    }
    return divisor_count;
}

vector<int> Solution::solve(vector<int> &A) {
    vector<int> divisor_count = precomputeDivisors();
    vector<int> result;
    for (int num : A) result.push_back(divisor_count[num]);
    return result;
}
```

---

### **Q3. Find All Primes**

* **Problem:** Find all prime numbers in range `[1, A]`.
* **Code:**

```cpp
vector<int> Solution::solve(int A) {
    vector<bool> is_prime(A + 1, true);
    vector<int> primes;
    if (A < 2) return primes;
    
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= A; ++p) {
        if (is_prime[p]) {
            for (int multiple = p * p; multiple <= A; multiple += p) {
                is_prime[multiple] = false;
            }
        }
    }
    for (int num = 2; num <= A; ++num) {
        if (is_prime[num]) primes.push_back(num);
    }
    return primes;
}
```

---

### **Q1. Prime Sum**

* **Problem:** Given even number `A > 2`, return two primes whose sum equals `A`. Return lexicographically smallest.
* **Code:**

```cpp
vector<int> Solution::primesum(int A) {
    vector<int> isprime(A + 1, 1);
    isprime[0] = isprime[1] = 0;

    for (int i = 2; i * i <= A; ++i) {
        if (isprime[i]) {
            for (int j = i * i; j <= A; j += i) isprime[j] = 0;
        }
    }

    for (int i = 2; i <= A / 2; ++i) {
        if (isprime[i] && isprime[A - i]) return {i, A - i};
    }
    return {};
}
```

---

### **Q2. Lucky Numbers**

* **Problem:** Count numbers ≤ `A` having exactly 2 distinct prime divisors.
* **Code:**

```cpp
int Solution::solve(int A) {
    vector<int> prime_factors_count(A + 1, 0);
    for (int i = 2; i <= A; ++i) {
        if (prime_factors_count[i] == 0) {
            for (int j = i; j <= A; j += i) prime_factors_count[j]++;
        }
    }
    int lucky_count = 0;
    for (int i = 1; i <= A; ++i) {
        if (prime_factors_count[i] == 2) lucky_count++;
    }
    return lucky_count;
}
```

---
