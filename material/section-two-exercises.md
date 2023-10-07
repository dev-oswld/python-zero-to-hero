# Section 2: *Object-Oriented Programming in Python*

---

## Basic

### 1. Introduction to object-oriented programming (OOP) concepts
**Exercise:** Describe in your own words what Object-Oriented Programming (OOP) is and list its four main principles.
```plaintext
# Exercise: Write a brief description of OOP and its four main principles.
# (This is a theoretical exercise. The answer can be written in a notebook or discussed in a group.)
```

### 2. Classes, objects, and instances
**Exercise:** Create a class named `Car` with attributes for `color` and `brand`. Then, create an instance of this class and print its attributes.
```python
# Exercise: Create a Car class and an instance of it.

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

# Create an instance of the Car class
my_car = Car("red", "Toyota")

# Print the attributes of the instance
print(my_car.color)  # This should print "red"
print(my_car.brand)  # This should print "Toyota"
```

### 3. Inheritance and polymorphism
**Exercise:** Create a base class named `Animal` with a method `speak()`. Then, create two subclasses `Dog` and `Cat` that override the `speak()` method.
```python
# Exercise: Use inheritance to create Dog and Cat subclasses from the Animal base class.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Test the subclasses
dog = Dog()
cat = Cat()
print(dog.speak())  # This should print "Woof!"
print(cat.speak())  # This should print "Meow!"
```

### 4. Encapsulation and abstraction
**Exercise:** Create a class named `BankAccount` with private attributes for `balance` and methods to deposit, withdraw, and check the balance.
```python
# Exercise: Create a BankAccount class with encapsulation.

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds"

    def check_balance(self):
        return f"Current balance: ${self.__balance}"

# Test the class
account = BankAccount()
print(account.deposit(100))  # This should print the new balance after depositing $100
print(account.withdraw(50))  # This should print the new balance after withdrawing $50
print(account.check_balance())  # This should print the current balance
```

### 5. File handling in Python
**Exercise:** Write a string to a file named `sample.txt` and then read the content of the file.
```python
# Exercise: Write to a file and then read its content.

content = "Hello, this is a sample text."

# Write to the file
with open('sample.txt', 'w') as file:
    file.write(content)

# Read from the file
with open('sample.txt', 'r') as file:
    read_content = file.read()
    print(read_content)  # This should print "Hello, this is a sample text."
```

---

## Medium

### 1. Introduction to object-oriented programming (OOP) concepts
**Exercise:** Identify and explain the OOP concept (either inheritance, encapsulation, polymorphism, or abstraction) demonstrated in a given piece of code.
```python
# Exercise: Review the code below and identify which OOP concept it demonstrates. Explain your answer.
# (This is a theoretical exercise. The answer can be written in a notebook or discussed in a group.)

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
```

### 2. Classes, objects, and instances
**Exercise:** Create a class named `Rectangle` with attributes for `length` and `width`. The class should have methods to calculate the area and perimeter. Then, create instances and test these methods.
```python
# Exercise: Create a Rectangle class with methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create instances and test
rect = Rectangle(4, 5)
print(rect.area())      # This should print 20
print(rect.perimeter()) # This should print 18
```

### 3. Inheritance and polymorphism
**Exercise:** Create a base class `Vehicle` with a method `fuel_efficiency()`. Then, create subclasses `Car` and `Motorcycle` that override the method based on their fuel efficiency.
```python
# Exercise: Use inheritance and polymorphism to demonstrate fuel efficiency.

class Vehicle:
    def fuel_efficiency(self):
        pass

class Car(Vehicle):
    def fuel_efficiency(self):
        return "25 miles per gallon"

class Motorcycle(Vehicle):
    def fuel_efficiency(self):
        return "50 miles per gallon"

# Test the subclasses
car = Car()
bike = Motorcycle()
print(car.fuel_efficiency())  # This should print "25 miles per gallon"
print(bike.fuel_efficiency()) # This should print "50 miles per gallon"
```

### 4. Encapsulation and abstraction
**Exercise:** Create a class `Person` with private attributes for `age` and `name`. Implement methods to set and get these attributes, ensuring that age is always non-negative and name is not empty.
```python
# Exercise: Create a Person class with encapsulation and abstraction.

class Person:
    def __init__(self):
        self.__age = 0
        self.__name = ""

    def set_age(self, age):
        if age >= 0:
            self.__age = age

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if name:
            self.__name = name

    def get_name(self):
        return self.__name

# Test the class
person = Person()
person.set_age(25)
person.set_name("John")
print(person.get_age())  # This should print 25
print(person.get_name()) # This should print "John"
```

### 5. File handling in Python
**Exercise:** Read a file named `data.txt` and count the number of occurrences of a specific word in it.
```python
# Exercise: Count the occurrences of a specific word in 'data.txt'.

word_to_count = "Python"

with open('data.txt', 'r') as file:
    content = file.read()
    word_count = content.lower().split().count(word_to_count.lower())

print(f"The word '{word_to_count}' appears {word_count} times in the file.")
```

---

## Advanced

### 1. Introduction to object-oriented programming (OOP) concepts
**Exercise:** Analyze a given software requirement and design a class diagram that incorporates the four main OOP principles.
```plaintext
# Exercise: Given the requirement to design a library management system, create a class diagram.
# The system should have books, members, staff, and borrowing transactions. 
# (This is a theoretical exercise. The answer can be sketched on paper or using a UML tool.)
```

### 2. Classes, objects, and instances
**Exercise:** Design a `Database` class that can handle basic CRUD (Create, Read, Update, Delete) operations. Use a dictionary to simulate the database.
```python
# Exercise: Create a Database class for basic CRUD operations.

class Database:
    def __init__(self):
        self.__data = {}

    def create(self, key, value):
        if key not in self.__data:
            self.__data[key] = value
            return f"Record {key} created."
        return f"Record {key} already exists."

    def read(self, key):
        return self.__data.get(key, "Record not found.")

    def update(self, key, value):
        if key in self.__data:
            self.__data[key] = value
            return f"Record {key} updated."
        return f"Record {key} not found."

    def delete(self, key):
        if key in self.__data:
            del self.__data[key]
            return f"Record {key} deleted."
        return f"Record {key} not found."

# Test the class
db = Database()
print(db.create("001", "John"))  # This should print "Record 001 created."
print(db.read("001"))           # This should print "John"
print(db.update("001", "Jane")) # This should print "Record 001 updated."
print(db.delete("001"))         # This should print "Record 001 deleted."
```

### 3. Inheritance and polymorphism
**Exercise:** Create a base class `Shape` with methods `area()` and `perimeter()`. Implement subclasses `Circle`, `Rectangle`, and `Triangle` that provide specific implementations for these methods.
```python
import math

# Exercise: Use inheritance and polymorphism to calculate area and perimeter for different shapes.

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# Test the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)
print(circle.area(), circle.perimeter())
print(rectangle.area(), rectangle.perimeter())
print(triangle.area(), triangle.perimeter())
```

### 4. Encapsulation and abstraction
**Exercise:** Design a `SecureDatabase` class that extends the previous `Database` class. This new class should encrypt data before storing and decrypt data before retrieving.
```python
# Exercise: Extend the Database class to add encryption and decryption.

class SecureDatabase(Database):
    def __encrypt(self, data):
        return data[::-1]  # Simple encryption by reversing the string

    def __decrypt(self, data):
        return data[::-1]  # Simple decryption by reversing the string

    def create(self, key, value):
        return super().create(key, self.__encrypt(value))

    def read(self, key):
        data = super().read(key)
        if data != "Record not found.":
            return self.__decrypt(data)
        return data

    def update(self, key, value):
        return super().update(key, self.__encrypt(value))

# Test the class
secure_db = SecureDatabase()
print(secure_db.create("001", "John"))  # This should print "Record 001 created."
print(secure_db.read("001"))           # This should print "John"
print(secure_db.update("001", "Jane")) # This should print "Record 001 updated."
```

### 5. File handling in Python
**Exercise:** Read a file named `log.txt` and filter out any lines that contain error messages. Write the filtered content to a new file named `filtered_log.txt`.
```python
# Exercise: Filter out error messages from 'log.txt' and write to 'filtered_log.txt'.

with open('log.txt', 'r') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if "ERROR" not in line]

with open('filtered_log.txt', 'w') as file:
    file.writelines(filtered_lines)
```
