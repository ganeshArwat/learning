
### **1️⃣ Class & Object**

```cpp
class Car {
public:
    string brand;
    int speed;

    void display() {
        cout << "Brand: " << brand << ", Speed: " << speed << " km/h" << endl;
    }
};

int main() {
    Car car1;          // Create object car1
    car1.brand = "Toyota"; // Set attribute
    car1.speed = 120;      // Set attribute
    car1.display();        // Call method
    return 0;
}
```

**Explanation:**

* `class Car` defines a blueprint for car objects.
* `brand` and `speed` are **public attributes**.
* `display()` is a **member function** to show object info.
* `car1` is an **instance** of `Car`.

---

### **2️⃣ Getters & Setters**

```cpp
void setName(string n) { name = n; }
void setAge(int a) { if(a >= 0) age = a; else cout << "Invalid age!\n"; }
string getName() { return name; }
int getAge() { return age; }
```

**Usage:**

```cpp
p.setName("John");
p.setAge(25);
cout << p.getName() << endl;
cout << p.getAge() << endl;
```

**Explanation:**

* **Getter**: Returns private attribute.
* **Setter**: Updates private attribute with validation.
* Protects internal state of object (`Encapsulation`).

---

### **3️⃣ Constructor**

* **Default Constructor:** Sets default values.

```cpp
Person() {
    name = "Unknown";
    age = 0;
    cout << "Default Constructor called.\n";
}
Person p; // Calls default constructor
```

* **Parameterized Constructor:** Allows passing values at object creation.

```cpp
Person(string n, int a) {
    name = n;
    age = a;
    cout << "Parameterized Constructor called.\n";
}
Person p("John", 25);
```

* **Copy Constructor:** Creates new object as a copy of another.

```cpp
Person(const Person& p) {
    name = p.name;
    age = p.age;
    cout << "Copy Constructor called.\n";
}
Person p2 = p1; // Copy constructor called
```

---

### **4️⃣ Destructor**

```cpp
~Person() {
    cout << "Destructor called for " << name << ".\n";
}
```

* Automatically called when object goes out of scope.
* Cleans up resources.
* For dynamic objects (`new`), must explicitly call `delete`.

---

### **5️⃣ Static & Dynamic Allocation**

```cpp
Person p1("John", 30);       // Static (stack)
Person* p2 = new Person("Alice", 25); // Dynamic (heap)
delete p2; // Destructor called for p2
```

* **Stack objects**: Automatically destroyed.
* **Heap objects**: Need manual deletion.

---

### **6️⃣ Shallow vs Deep Copy**

**Shallow Copy:**

```cpp
Shallow(const Shallow& obj) {
    data = obj.data; // Copies pointer only
}
```

* Both objects share the same memory.
* Changes in one affect the other.
* Can cause **double deletion issues**.

**Deep Copy:**

```cpp
Deep(const Deep& obj) {
    data = new int(*obj.data); // New memory allocation
}
```

* Each object has its own copy.
* Safe for dynamic memory.

---

## **1️⃣ Copy Assignment Operator**

```cpp
Person p1("John");      // Constructor
p1.display();

Person p2("Alice");     // Constructor
p2.display();

p2 = p1;                // Copy Assignment
p2.display();
```

**Explanation:**

* `p1` and `p2` are two objects.
* `p2 = p1;` uses the **copy assignment operator**, which **copies the values of attributes from p1 to p2**.
* Difference from **Copy Constructor**:

  * **Copy constructor** is used when a **new object is being created** using another object.
  * **Copy assignment** is used **after an object is already created**.

---

## **2️⃣ Static Variables**

```cpp
void counterFunction() {
    static int count = 0;  // Static variable
    count++;               // Increment each call
    cout << "Count: " << count << endl;
}

int main() {
    counterFunction();  // Count: 1
    counterFunction();  // Count: 2
    counterFunction();  // Count: 3
    return 0;
}
```

**Explanation:**

* `static int count` retains its value **across function calls**.
* Normal local variables are destroyed when function exits, but **static persists**.
* Useful for **tracking counters, IDs, etc.**

---

## **3️⃣ Static Member Variables (in Classes)**

```cpp
class MyClass {
public:
    static int count;  // Shared among all objects

    MyClass() { count++; }

    static void showCount() {
        cout << "Count: " << count << endl;
    }
};

// Definition outside the class
int MyClass::count = 0;

int main() {
    MyClass obj1;
    MyClass obj2;

    MyClass::showCount();  // Accessed without object. Output: Count: 2
}
```

**Explanation:**

* `static` variables belong to **class, not to any object**.
* **All objects share the same static variable.**
* Must be **defined outside the class**.

---

## **4️⃣ Static Member Functions**

```cpp
class MyClass {
private:
    static int count;

public:
    MyClass() { count++; }

    static void showCount() { cout << "Count: " << count << endl; }
};

int MyClass::count = 0;

int main() {
    MyClass obj1;
    MyClass obj2;

    MyClass::showCount();  // Output: Count: 2
}
```

**Explanation:**

* Can be called **without any object**.
* Can only access **static members** inside it.

---

## **5️⃣ Static Function (Global Scope)**

```cpp
static void myFunction() {
    cout << "This function can only be called in this file." << endl;
}

int main() {
    myFunction();
}
```

**Explanation:**

* `static` at global scope means **function visibility is limited to this file**.
* It **cannot be used outside this translation unit**.

---

## **6️⃣ Abstraction**

```cpp
class Shape {
public:
    virtual void draw() = 0; // Pure virtual function
    void showInfo() { cout << "I am a shape." << endl; }
    virtual ~Shape() { cout << "Shape destroyed" << endl; }
};

class Rectangle : public Shape {
public:
    void draw() override { cout << "Drawing a rectangle" << endl; }
};

class Circle : public Shape {
public:
    void draw() override { cout << "Drawing a circle" << endl; }
};

int main() {
    Shape* shape1 = new Rectangle();
    Shape* shape2 = new Circle();

    shape1->draw();     // Polymorphism
    shape2->draw();

    shape1->showInfo(); // Common method
    shape2->showInfo();

    delete shape1;
    delete shape2;
}
```

**Explanation:**

* `Shape` is an **abstract class** (has at least one pure virtual function).
* Cannot create `Shape` object directly.
* `Rectangle` and `Circle` **override draw()**.
* Shows **runtime polymorphism** using **base class pointer**.
* `virtual destructor` ensures derived objects are destroyed properly.

---

✅ At this point, you’ve learned:

* Copy assignment vs copy constructor
* Static variables & functions (local & class)
* Abstraction & pure virtual functions
* Polymorphism basics with abstract class

---

## **1️⃣ Single Inheritance**

```cpp
class Vehicle {
public:
    string brand;
    void honk() {
        cout << "Vehicle horn: Beep Beep!" << endl;
    }
};

class Car : public Vehicle {
public:
    void displayBrand() {
        cout << "Car brand: " << brand << endl;
    }
};
```

**Explanation:**

* `Car` inherits from `Vehicle`.
* `Car` can use **brand** and **honk()** directly.
* Single inheritance = **1 base, 1 derived**.

---

## **2️⃣ Multilevel Inheritance**

```cpp
class Animal {
public:
    void eat() { cout << "Eating food..." << endl; }
    void sleep() { cout << "Sleeping..." << endl; }
};

class Mammal : public Animal {
public:
    void breathe() { cout << "Breathing air..." << endl; }
};

class Dog : public Mammal {
public:
    void bark() { cout << "Barking..." << endl; }
};
```

**Explanation:**

* Dog → Mammal → Animal.
* `Dog` can use **bark(), breathe(), eat(), sleep()**.
* Multilevel inheritance = **chain of inheritance**.

---

## **3️⃣ Multiple Inheritance**

```cpp
class Vehicle {
public:
    void drive() { cout << "Driving the vehicle..." << endl; }
};

class Engine {
public:
    void start() { cout << "Starting the engine..." << endl; }
};

class Car : public Vehicle, public Engine {
public:
    void honk() { cout << "Car horn: Beep Beep!" << endl; }
};
```

**Explanation:**

* `Car` inherits from **two base classes**.
* Can access **drive()** and **start()** directly.
* Multiple inheritance = **1 derived, multiple base**.

---

## **4️⃣ Hierarchical Inheritance**

```cpp
class Shape {
public:
    void display() { cout << "Displaying shape..." << endl; }
};

class Circle : public Shape {
public:
    void drawCircle() { cout << "Drawing circle..." << endl; }
};

class Rectangle : public Shape {
public:
    void drawRectangle() { cout << "Drawing rectangle..." << endl; }
};
```

**Explanation:**

* Multiple derived classes from **same base class**.
* Circle and Rectangle **share Shape’s properties/methods**.

---

## **5️⃣ Hybrid Inheritance**

```cpp
class Animal {
public:
    void breathe() { cout << "Animal is breathing" << endl; }
};

class Mammal : public Animal {
public:
    void walk() { cout << "Mammal is walking" << endl; }
};

class Bird : public Animal {
public:
    void fly() { cout << "Bird is flying" << endl; }
};

class Bat : public Mammal, public Bird {
public:
    void hangUpsideDown() { cout << "Bat is hanging upside down" << endl; }
};
```

**Explanation:**

* Combination of **multilevel + multiple inheritance**.
* Bat inherits from both **Mammal** and **Bird**, which in turn inherit from **Animal**.
* Note: This can create **ambiguity for members of Animal** (solved using **virtual inheritance**).

---

## **6️⃣ Diamond Problem**

```cpp
class A {
public:
    void show() { cout << "Class A" << endl; }
};

class B : public A {
public:
    void show() { cout << "Class B" << endl; }
};

class C : public A {
public:
    void show() { cout << "Class C" << endl; }
};

class D : public B, public C {
    // D.show() is ambiguous!
};
```

**Explanation:**

* D inherits **B** and **C**, both inherit **A**.
* If you call `D.show()`, compiler **doesn’t know whether to use B::show() or C::show()**.
* **Solution:** Use **virtual inheritance** to ensure **only one copy of A exists**.

---

## **7️⃣ Function Overloading**

* **Same function name** but **different parameters**.

```cpp
class Example {
public:
    void show(int x) { cout << "Integer: " << x << endl; }
    void show(double y) { cout << "Double: " << y << endl; }
};
```

---

## **8️⃣ Operator Overloading**

* Give **custom behavior to operators**.

```cpp
class Complex {
public:
    int real, imag;
    Complex(int r, int i) : real(r), imag(i) {}
    Complex operator + (Complex const &c) {
        return Complex(real + c.real, imag + c.imag);
    }
};
```

---

## **9️⃣ Method Overriding**

* **Derived class changes base class method** behavior.

```cpp
class Base {
public:
    virtual void display() { cout << "Base display" << endl; }
};

class Derived : public Base {
public:
    void display() override { cout << "Derived display" << endl; }
};
```

---

✅ After this, you fully understand:

* All types of **inheritance**
* Diamond problem
* Function/operator overloading
* Method overriding

---
