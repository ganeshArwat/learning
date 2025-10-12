
# C++ Debugging, Pointers, Functions, and Struct Notes

---

## 1. Debugging

### Debugging Arrays

```cpp
for(int i = 0; i < ocupied_seats.size(); i++){
    cout << ", " << ocupied_seats[i] << " ";
}
```

---

## 2. Basics

```cpp
#include <bits/stdc++.h>
using namespace std;

int minVal = INT_MAX;
int maxVal = INT_MIN;
```

---

## 3. Pointers

1. **Pointer Declaration**
   A pointer is declared by placing an asterisk `*` in front of the variable name.

2. **Dereferencing**
   Using `*`, you can access or modify the value at the memory address stored in the pointer.

3. **Address-of Operator (`&`)**
   Used to get the memory address of a variable.

```cpp
int a = 10;      // Declare integer
int* p;          // Declare pointer to int
p = &a;          // Store address of 'a' in pointer 'p'

cout << "Value of a: " << a << endl;          // 10
cout << "Address of a: " << &a << endl;       // Memory address
cout << "Pointer p holds address: " << p << endl;
cout << "Value at address held by p: " << *p << endl; // Dereference

// Modifying via pointer
*p = 20;
cout << "New value of a: " << a << endl;      // 20
```

### Pointers and Arrays

```cpp
int arr[3] = {10, 20, 30};
int* p = arr;  // Points to arr[0]

cout << *p << endl; // 10
p++;
cout << *p << endl; // 20
```

---

## 4. Pass Arguments to a Function

### Pass by Value

* Function receives a **copy** of the variable.
* Original value remains unchanged.

```cpp
void myFunction(int x) {
    x += 10;  // Only local copy changed
}

int main() {
    int num = 5;
    myFunction(num);
    cout << num; // 5
}
```

---

### Pass by Reference

* Function receives a **reference** to the original variable.
* Changes inside function affect original variable.

```cpp
void myFunction(int &x) {
    x += 10;
}

int main() {
    int num = 5;
    myFunction(num);
    cout << num; // 15
}
```

---

### Pass by Pointer

* Function receives the **memory address** of variable.
* Modify the actual value using dereferencing.

```cpp
void myFunction(int *x) {
    *x += 10;  // Modify actual value
}

int main() {
    int num = 5;
    myFunction(&num);  // Pass address
    cout << num; // 15
}
```

---

## 5. Struct (Structure)

* **Struct**: User-defined type to group variables under one name.
* Members are **public by default**.

```cpp
// Define a struct for 2D Point
struct Point {
    int x;  // x-coordinate
    int y;  // y-coordinate

    void printPoint() {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

int main() {
    Point p1;   // Declare struct object
    p1.x = 10;  // Assign values
    p1.y = 20;

    cout << "Point coordinates are: ";
    p1.printPoint();  // Output: (10, 20)

    return 0;
}
```

---

This Markdown now covers:

* **Debugging arrays**
* **Pointer basics** (declaration, dereference, arrays)
* **Function argument passing** (value, reference, pointer)
* **Struct definition and usage**

---
