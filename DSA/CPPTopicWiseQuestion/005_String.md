
## **String Basics**

---

### **Q1. Toggle Case**

* **Problem:** Convert lowercase letters to uppercase and vice versa.
* **Code:**

```cpp
string Solution::solve(string A) {
    for (int i = 0; i < A.length(); i++) {
        char ch = A[i];
        if ('a' <= ch && ch <= 'z') A[i] = ch - 32;
        else A[i] = ch + 32;
    }
    return A;
}
```

* **Trick:** ASCII difference between `'a'` and `'A'` is 32.

---

### **Q2. Simple Reverse**

* **Problem:** Reverse a string in-place.
* **Code:**

```cpp
string Solution::solve(string A) {
    int i = 0, j = A.length() - 1;
    while (i < j) swap(A[i++], A[j--]);
    return A;
}
```

* **Trick:** Two-pointer swap.

---

### **Q3. Reverse Words in a String**

* **Problem:** Reverse the string **word by word**; remove extra spaces.
* **Code:**

```cpp
string Solution::solve(string A) {
    int start = 0, end = A.size() - 1;
    while (start <= end && A[start] == ' ') start++;
    while (end >= start && A[end] == ' ') end--;

    vector<string> words;
    stringstream ss(A.substr(start, end - start + 1));
    string word;
    while (ss >> word) words.push_back(word);

    reverse(words.begin(), words.end());

    string res;
    for (int i = 0; i < words.size(); i++) {
        res += words[i];
        if (i != words.size() - 1) res += ' ';
    }
    return res;
}
```

* **Trick:** Use `stringstream` to split by spaces.

---

### **Q4. Longest Palindromic Substring**

* **Problem:** Find the longest contiguous palindrome.
* **Code:**

```cpp
string Solution::longestPalindrome(string A) {
    int n = A.size();
    int maxLen = 1, start = 0;

    auto expand = [&](int l, int r){
        while(l >= 0 && r < n && A[l] == A[r]) { l--; r++; }
        return r - l - 1;
    };

    for (int i = 0; i < n; i++) {
        int len1 = expand(i, i);       // Odd length
        int len2 = expand(i, i + 1);   // Even length
        int len = max(len1, len2);
        if (len > maxLen) {
            maxLen = len;
            start = i - (len - 1) / 2;
        }
    }
    return A.substr(start, maxLen);
}
```

* **Trick:** Expand around **center** for odd/even length.

---

### **Q1. Longest Common Prefix (LCP)**

* **Problem:** Find the longest common prefix in a list of strings.
* **Code:**

```cpp
string Solution::longestCommonPrefix(vector<string> &A) {
    if(A.empty()) return "";
    string prefix = A[0];
    for(int i = 1; i < A.size(); i++) {
        int j = 0;
        while(j < prefix.size() && j < A[i].size() && prefix[j] == A[i][j]) j++;
        prefix = prefix.substr(0, j);
    }
    return prefix;
}
```

* **Trick:** Iteratively reduce the prefix.

---

### **Q2. Count Occurrences of "bob"**

* **Problem:** Count the number of times `"bob"` appears.
* **Code:**

```cpp
int Solution::solve(string A) {
    int count = 0;
    for(int i = 2; i < A.size(); i++)
        if(A[i-2] == 'b' && A[i-1] == 'o' && A[i] == 'b') count++;
    return count;
}
```

---

### **Q3. Amazing Substrings**

* **Problem:** Count substrings starting with a vowel.
* **Code:**

```cpp
int Solution::solve(string A) {
    long result = 0;
    const string vowels = "aeiouAEIOU";
    for(long i = 0; i < A.size(); i++)
        if(vowels.find(A[i]) != string::npos)
            result += (A.size() - i);
    return result % 10003;
}
```

* **Trick:** Number of substrings starting at index `i` = `length - i`.

---

### **Q4. Is Alphanumeric**

* **Problem:** Check if all characters are alphanumeric `[a-zA-Z0-9]`.
* **Code:**

```cpp
int Solution::solve(vector<char> &A) {
    for(char ch : A) 
        if(!((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9')))
            return 0;
    return 1;
}
```

---

### **Q5. String Rotation**

* **Problem:** Check if `s2` is a rotation of `s1` using only **one call** to `isSubstring`.

* **Example:** `"waterbottle"` is a rotation of `"erbottlewat"`.

* **Code:**

```cpp
// Function to check if s2 is a substring of s1
bool isSubstring(const std::string& s1, const std::string& s2) {
    return s1.find(s2) != std::string::npos;
}

// Function to check if s2 is a rotation of s1
bool isRotation(const std::string& s1, const std::string& s2) {
    // Lengths must be equal and non-empty
    if (s1.length() != s2.length() || s1.empty()) {
        return false;
    }
    
    // Concatenate s1 with itself
    std::string concatenated = s1 + s1;

    // Check if s2 is a substring of concatenated string
    return isSubstring(concatenated, s2);
}

int main() {
    std::string s1 = "waterbottle";
    std::string s2 = "erbottlewat";

    if (isRotation(s1, s2)) {
        std::cout << s2 << " is a rotation of " << s1 << std::endl;
    } else {
        std::cout << s2 << " is not a rotation of " << s1 << std::endl;
    }

    return 0;
}
```

* **Trick Explained:**
  Any rotation of a string `s1` will always be a **substring of `s1 + s1`**.

  * Example:
    `s1 = "waterbottle"`
    `s1+s1 = "waterbottlewaterbottle"`
    `s2 = "erbottlewat"` is found inside `s1+s1`. ✅

---
