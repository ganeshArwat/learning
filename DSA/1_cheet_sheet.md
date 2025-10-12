Absolutely! I can convert your C++ code reference into **well-structured Markdown notes**. I’ll organize it section-wise, with proper headings, code blocks, and explanations for readability. Here’s the conversion:

---

# C++ Reference Notes

---

## Basics

```cpp
#include <bits/stdc++.h>
using namespace std;

// Min and Max
int maxVal = INT_MIN;
int minVal = INT_MAX;

max(maxVal, current_profit);
min(minVal, current_profit);

// MOD operation
const int MOD = 1e9 + 7;

// Count set bits
int num  = 7;
int cnt  = __builtin_popcount(num); // number of set bits

long long num2 = 1234567843232;
long long cnt2 = __builtin_popcountll(num2);

// Permutations
string s = "abc";
sort(s.begin(), s.end());

do {
    cout << s << endl;
} while(next_permutation(s.begin(), s.end()));

// Max and Min elements in array
int a[] = {1, 2, 3, 4, 5};
int n = sizeof(a)/sizeof(a[0]);
int maxele = *max_element(a, a+n);
int minele = *min_element(a, a+n);
```

---

## Pairs

```cpp
pair<int, int> p = {1, 2};
cout << p.first << " " << p.second;

pair<int, pair<int,int>> q = {1, {2,3}};
cout << q.first << " " << q.second.first << " " << q.second.second;

pair<int,int> arr[] = {{1,2}, {3,4}, {5,6}};
cout << arr[1].second;
```

---

## Arrays

```cpp
int numbers[5];               // declaration
int numbers[5] = {1,2,3,4,5}; // declaration + initialization
int numbers[] = {1,2,3,4,5};  // size inferred

numbers[0] = 10; // update element
int value = numbers[1]; // access element

// Looping
for(int i=0;i<5;i++) cout << numbers[i] << " ";

// Multidimensional Array
int matrix[3][3] = {
    {1,2,3},
    {4,5,6},
    {7,8,9}
};
```

---

## Vectors

```cpp
#include <vector>

// Declaration & Initialization
vector<int> v;           // empty vector
vector<int> v1(5);       // 5 elements default 0
vector<int> v2(5, -1);   // 5 elements, all -1
vector<int> v3(v1);      // copy constructor

// Operations
v.push_back(1);
v.emplace_back(2);

vector<pair<int,int>> vp;
vp.push_back({1,2});
vp.emplace_back(1,2);

v.pop_back();
cout << v[0] << v.at(0) << v.front() << v.back() << v.size();

// Erase
v.erase(v.begin()+1);
v.erase(v.begin()+1, v.begin()+3);

// Insert
v.insert(v.begin(), 300);
v.insert(v.begin()+1, 2, 200);
v.insert(v.begin(), v2.begin(), v2.end());

v.swap(v2);
v.clear();
v.empty();

// Iterators
for(auto it=v.begin(); it!=v.end(); it++)
    cout << *it << " ";

for(auto it:v)
    cout << it << " ";
```

---

## 2D Vector Reference

```cpp
vector<vector<int>> &A;
```

---

## Sorting

```cpp
// Ascending
sort(A.begin(), A.end());
sort(a, a+n);

// Descending
sort(A.begin(), A.end(), greater<int>());
sort(a, a+n, greater<int>());

// Partial sort
sort(a+2, a+4);

// Comparator for pairs
bool comp(pair<int,int> &a, pair<int,int> &b){
    if(a.first < b.first) return true;
    else if(a.first == b.first) return a.second > b.second;
    return false;
}

pair<int,int> arr[] = {{1,2},{3,4},{5,6}};
sort(arr, arr+n, comp);

// Min Max of array
int arr2[] = {10,20,5,40,50};
int n2 = sizeof(arr2)/sizeof(arr2[0]);
int minEle = *min_element(arr2, arr2+n2);
int maxEle = *max_element(arr2, arr2+n2);
```

---

## Unordered Map

```cpp
unordered_map<string,int> umap;

umap["apple"] = 1;
umap["banana"] = 2;

// Access
cout << umap["apple"] << endl;

// Check existence
if(umap.count("apple") > 0) { ... }
if(umap.find("banana") != umap.end()) { ... }

// Iterate
for(auto &p: umap)
    cout << p.first << " " << p.second << endl;

// Erase & size
umap.erase("orange");
cout << umap.size();
```

---

## Unordered Set

```cpp
unordered_set<int> uset;
uset.insert(10);
uset.insert(20);
uset.insert(30);

uset.erase(20);
cout << uset.size();
```

---

## Set

```cpp
set<int> s;
s.insert(1);
s.emplace(2);

auto it = s.find(1);
s.erase(it);

auto lb = s.lower_bound(1);
auto ub = s.upper_bound(1);
```

---

## Multiset

```cpp
multiset<int> ms;
ms.insert(1);
ms.count(1);
ms.erase(ms.find(1));
ms.erase(ms.find(1), ms.find(1)+2);
```

---

## Map

```cpp
map<int,int> m;
m[1] = 3;
m.emplace({1,3});
m.insert({1,3});

for(auto it:m) cout << it.first << " " << it.second << endl;

auto it = m.find(1);
cout << it->second;
```

---

## Binary Search

```cpp
int left = 0, right = A, result = 0;

while(left <= right){
    int mid = left + (right-left)/2;
    long long sum = (long long)mid*(mid+1)/2;

    if(sum == A) return mid;
    else if(sum < A) { result = mid; left = mid+1; }
    else right = mid-1;
}
return result;
```

---

## Linked List

```cpp
struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(NULL) {}
};

// Insert node at position
ListNode* insertNode(ListNode* A, int B, int C){
    ListNode* new_node = new ListNode(B);
    if(A == NULL) return new_node;

    if(C == 0){ new_node->next = A; return new_node; }

    ListNode* temp = A;
    int count=0;
    while(temp->next != NULL){
        count++;
        if(count == C-1){ temp = temp->next; break; }
        temp = temp->next;
    }
    new_node->next = temp->next;
    temp->next = new_node;
    return A;
}
```

---

## List

```cpp
list<int> ls;
ls.push_back(1);
ls.emplace_back(2);
ls.push_front(1);
ls.emplace_front(2);
```

---

## Stack

```cpp
stack<int> s;
s.push(10); s.push(20); s.push(30);
cout << s.top();
s.pop();
cout << s.size();
```

---

## Queue

```cpp
queue<int> q;
q.push(10); q.push(20); q.push(30);
cout << q.front() << " " << q.back();
q.pop();
cout << q.size();
```

---

## Deque

```cpp
deque<int> dq;
dq.push_back(1); dq.emplace_back(2);
dq.push_front(1); dq.emplace_front(2);
dq.pop_back(); dq.pop_front();
dq.front(); dq.back();
```

---

## Trees (Preorder Traversal)

```cpp
void preorder(TreeNode* node, vector<int> &result){
    if(node == NULL) return;
    result.push_back(node->val);
    preorder(node->left, result);
    preorder(node->right, result);
}

vector<int> preorderTraversal(TreeNode* A){
    vector<int> result;
    preorder(A,result);
    return result;
}
```

---

## Heap / Priority Queue

```cpp
// Max Heap
priority_queue<int> maxHeap;
maxHeap.push(10); maxHeap.push(20);

// Min Heap
priority_queue<int, vector<int>, greater<int>> minHeap;
minHeap.push(10); minHeap.push(30);

// Array to Heap
vector<int> heap = {10,20,15};
make_heap(heap.begin(), heap.end());
heap.push_back(25);
push_heap(heap.begin(), heap.end());

while(!heap.empty()){
    pop_heap(heap.begin(), heap.end());
    cout << heap.back() << " ";
    heap.pop_back();
}
```

---

## Graphs

### 1. Graph Representation

```cpp
#include <vector>
using namespace std;

// Adjacency List Representation
int V = 5; // number of vertices
vector<int> adj[V];

// Adding edges (undirected graph)
adj[0].push_back(1);
adj[1].push_back(0);

adj[0].push_back(2);
adj[2].push_back(0);

// Weighted Graph (pair = {neighbor, weight})
vector<pair<int,int>> wAdj[V];
wAdj[0].push_back({1, 10}); // edge 0-1 with weight 10
wAdj[1].push_back({0, 10});
```

---

### 2. BFS (Breadth-First Search)

```cpp
#include <queue>

void BFS(int start, vector<int> adj[], int V){
    vector<bool> visited(V, false);
    queue<int> q;
    
    visited[start] = true;
    q.push(start);
    
    while(!q.empty()){
        int node = q.front(); q.pop();
        cout << node << " ";
        
        for(int neighbor : adj[node]){
            if(!visited[neighbor]){
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}
```

---

### 3. DFS (Depth-First Search)

```cpp
void DFSUtil(int node, vector<int> adj[], vector<bool> &visited){
    visited[node] = true;
    cout << node << " ";
    
    for(int neighbor : adj[node]){
        if(!visited[neighbor]){
            DFSUtil(neighbor, adj, visited);
        }
    }
}

void DFS(int start, vector<int> adj[], int V){
    vector<bool> visited(V, false);
    DFSUtil(start, adj, visited);
}
```

---

### 4. Dijkstra’s Algorithm (Shortest Path)

```cpp
#include <queue>
#include <vector>
using namespace std;

void dijkstra(int src, vector<pair<int,int>> adj[], int V){
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;
    
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({0, src});
    
    while(!pq.empty()){
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        
        if(d > dist[u]) continue;
        
        for(auto edge : adj[u]){
            int v = edge.first;
            int weight = edge.second;
            
            if(dist[u] + weight < dist[v]){
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    
    // Print distances
    for(int i=0;i<V;i++) cout << "Vertex " << i << ": " << dist[i] << endl;
}
```

---

### 5. Topological Sort (DAG)

```cpp
#include <stack>

void topologicalSortUtil(int node, vector<int> adj[], vector<bool> &visited, stack<int> &s){
    visited[node] = true;
    for(int neighbor : adj[node]){
        if(!visited[neighbor])
            topologicalSortUtil(neighbor, adj, visited, s);
    }
    s.push(node);
}

void topologicalSort(int V, vector<int> adj[]){
    vector<bool> visited(V, false);
    stack<int> s;
    
    for(int i=0;i<V;i++)
        if(!visited[i])
            topologicalSortUtil(i, adj, visited, s);
    
    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    }
}
```

---

### 6. Detect Cycle in Directed Graph (DFS + Recursion)

```cpp
bool isCyclicUtil(int node, vector<int> adj[], vector<bool> &visited, vector<bool> &recStack){
    visited[node] = true;
    recStack[node] = true;
    
    for(int neighbor : adj[node]){
        if(!visited[neighbor] && isCyclicUtil(neighbor, adj, visited, recStack))
            return true;
        else if(recStack[neighbor])
            return true;
    }
    
    recStack[node] = false;
    return false;
}

bool isCyclic(int V, vector<int> adj[]){
    vector<bool> visited(V, false);
    vector<bool> recStack(V, false);
    
    for(int i=0;i<V;i++)
        if(!visited[i] && isCyclicUtil(i, adj, visited, recStack))
            return true;
    
    return false;
}
```

---
