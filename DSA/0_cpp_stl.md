
# C++ STL & Basics Reference Notes

---

## 1. Pairs

```cpp
#include <bits/stdc++.h>
using namespace std;

// Simple pair
pair<int,int> p = {1,2};
cout << p.first << " " << p.second;

// Pair of pair
pair<int, pair<int,int>> q = {1, {2,3}};
cout << q.first << " " << q.second.first << " " << q.second.second;

// Array of pairs
pair<int,int> arr[] = {{1,2},{3,4},{5,6}};
cout << arr[1].second;
```

---

## 2. Vectors

```cpp
#include <vector>
using namespace std;

vector<int> v;
v.push_back(1);
v.emplace_back(2);

// Vector of pairs
vector<pair<int,int>> vp;
vp.push_back({1,2});
vp.emplace_back(1,2);

v.pop_back();

// Initialization
vector<int> v1(5);        // 5 elements, default 0
vector<int> v2(5, 0);     // 5 elements, all 0
vector<int> v3(5, -1);    // 5 elements, all -1
vector<int> v4(v1);       // copy constructor

// Iterators
vector<int>::iterator it = v.begin();
it++;
cout << *it;

it = it + 2;
cout << *it;

// Access elements
cout << v[0] << v.at(0) << v.front() << v.back() << v.size();

// Traversal
for(vector<int>::iterator it=v.begin(); it!=v.end(); it++)
    cout << *it << " ";

for(auto it:v)
    cout << it << " ";

// Erase
v.erase(v.begin()+1);
v.erase(v.begin()+1, v.begin()+3);

// Insert
v.insert(v.begin(), 300);
v.insert(v.begin()+1, 2, 200);
v.insert(v.begin(), v2.begin(), v2.end());

// Swap and clear
v1.swap(v2);
v.clear();
cout << v.empty();
```

---

## 3. List (Doubly Linked List)

```cpp
#include <list>
using namespace std;

list<int> ls;

ls.push_back(1);
ls.emplace_back(2);

ls.push_front(1);
ls.emplace_front(2);

ls.pop_front();
ls.pop_back();
```

---

## 4. Deque

```cpp
#include <deque>
using namespace std;

deque<int> dq;

dq.push_back(1);
dq.emplace_back(2);
dq.push_front(1);
dq.emplace_front(2);

dq.pop_back();
dq.pop_front();

dq.front();
dq.back();
```

---

## 5. Stack

```cpp
#include <stack>
using namespace std;

stack<int> st;

st.push(1);
st.emplace(2);

st.pop();
st.top();

st.size();
st.empty();
```

---

## 6. Queue

```cpp
#include <queue>
using namespace std;

queue<int> q;

q.push(1);
q.emplace(2);

q.pop();
q.front();
q.back();

q.front() += 4; // modify front element

q.size();
q.empty();
```

---

## 7. Priority Queue (Heap)

```cpp
#include <queue>
using namespace std;

// Max Heap
priority_queue<int> maxPQ;
maxPQ.push(1);
maxPQ.emplace(2);

maxPQ.top();
maxPQ.pop();

// Min Heap
priority_queue<int, vector<int>, greater<int>> minPQ;
```

---

## 8. Set

```cpp
#include <set>
using namespace std;

set<int> s;

s.insert(1);
s.emplace(2);

auto it = s.find(1);
s.erase(it);
s.erase(2);

s.lower_bound(1);
s.upper_bound(1);
```

---

## 9. Multiset

```cpp
#include <set>
using namespace std;

multiset<int> ms;

ms.insert(1);
ms.insert(1);
ms.insert(1);

ms.erase(1); // erase all 1s

int cnt = ms.count(1);

ms.erase(ms.find(1));
ms.erase(ms.find(1), ms.find(1)+2);
```

---

## 10. Unordered Set

```cpp
#include <unordered_set>
using namespace std;

unordered_set<int> us;

us.insert(1);
us.insert(1); // duplicate ignored
us.insert(2);
```

---

## 11. Map

```cpp
#include <map>
using namespace std;

map<int,int> m1;
map<int,pair<int,int>> m2;
map<pair<int,int>,int> m3;

m1[1] = 3;
m1.emplace({1,3});
m1.insert({1,3});

// Traversal
for(auto it:m1)
    cout << it.first << " " << it.second << endl;

// Access element
cout << m1[1];

auto it = m1.find(1);
cout << it->second;
```

---

## 12. Sorting

```cpp
#include <algorithm>
using namespace std;

sort(a, a+n);
sort(a.begin(), a.end());

sort(a+2, a+4);
sort(a, a+n, greater<int>());

// Sorting pairs with custom comparator
pair<int,int> arr[] = {{1,2},{3,4},{5,6}};

bool comp(pair<int,int> &a, pair<int,int> &b){
    if(a.first < b.first) return true;
    else if(a.first == b.first) return a.second > b.second;
    return false;
}

sort(arr, arr+n, comp);
```

---

## 13. Basics

```cpp
// Count set bits
int num = 7;
int cnt = __builtin_popcount(num);

long long num2 = 1234567843232;
long long cnt2 = __builtin_popcountll(num2);

// Permutations
string s = "abc";
sort(s.begin(), s.end());
do{
    cout << s << endl;
} while(next_permutation(s.begin(), s.end()));

// Min/Max in array
int maxele = *max_element(a, a+n);
int minele = *min_element(a, a+n);
```

