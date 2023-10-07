# Section 1: *Introduction to Python*

---

## Basic

### 1. Introduction to Python programming language
**Exercise:** Print a greeting message.
```python
# Exercise: Print "Hello, Python!" to the console.
print("Hello, Python!")
```

### 2. Setting up Python environment
**Exercise:** Check the Python version installed on your system.
```python
# Exercise: Use the following command in your terminal or command prompt to check the Python version.
# python --version
```

### 3. Variables, data types, and operators
**Exercise:** Create variables of different data types and print them.
```python
# Exercise: Create a string, integer, and float variable. Then, print them.

name = "John"  # This is a string variable
age = 25       # This is an integer variable
height = 5.9   # This is a float variable

print(name)
print(age)
print(height)
```

### 4. Control flow: if statements, loops
**Exercise:** Write a program that checks if a number is even or odd.
```python
# Exercise: Check if the given number is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

**Exercise:** Use a loop to print numbers from 1 to 5.
```python
# Exercise: Print numbers from 1 to 5 using a loop.

for i in range(1, 6):
    print(i)
```

### 5. Functions and modules
**Exercise:** Create a function that returns the square of a number.
```python
# Exercise: Define a function that returns the square of a given number.

def square(num):
    return num * num

# Test the function
print(square(5))  # This should print 25
```

### 6. Input and output operations
**Exercise:** Read a user's name from input and greet them.
```python
# Exercise: Read the user's name and print a greeting message.

name = input("Enter your name: ")
print(f"Hello, {name}!")
```

---

## Medium

### 1. Introduction to Python programming language
**Exercise:** Use a list comprehension to generate a list of squares for numbers from 1 to 10.
```python
# Exercise: Generate a list of squares for numbers from 1 to 10 using list comprehension.
squares = [x**2 for x in range(1, 11)]
print(squares)
```

### 2. Setting up Python environment
**Exercise:** Install a popular Python package using `pip`.
```python
# Exercise: Use the following command in your terminal or command prompt to install the 'requests' package.
# pip install requests
```

### 3. Variables, data types, and operators
**Exercise:** Create a dictionary of three students with their names as keys and grades as values. Then, calculate the average grade.
```python
# Exercise: Create a dictionary of students and calculate the average grade.

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

average_grade = sum(students.values()) / len(students)
print(f"The average grade is: {average_grade}")
```

### 4. Control flow: if statements, loops
**Exercise:** Write a program that prints the Fibonacci sequence up to the 10th term.
```python
# Exercise: Print the Fibonacci sequence up to the 10th term.

a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
```

### 5. Functions and modules
**Exercise:** Create a module named `math_operations.py` with functions for addition, subtraction, multiplication, and division. Then, import this module and use its functions.
```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# main.py
# from math_operations import add, subtract, multiply, divide

# Test the functions
# print(add(5, 3))  # This should print 8
# print(divide(9, 3))  # This should print 3
```

### 6. Input and output operations
**Exercise:** Read a file named `data.txt` and count the number of lines, words, and characters in it.
```python
# Exercise: Read the file 'data.txt' and count lines, words, and characters.

with open('data.txt', 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
```

---

## Advanced

### 1. Introduction to Python programming language
**Exercise:** Implement a generator function that yields prime numbers indefinitely.
```python
# Exercise: Create a generator that yields prime numbers.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Test the generator
gen = prime_generator()
for _ in range(10):
    print(next(gen))
```

### 2. Setting up Python environment
**Exercise:** Set up a virtual environment, activate it, and install a package within it.
```python
# Exercise: Use the following commands in your terminal or command prompt.

# Create a virtual environment named 'myenv'
# python -m venv myenv

# Activate the virtual environment
# On Windows: myenv\Scripts\activate
# On macOS and Linux: source myenv/bin/activate

# Install a package within the virtual environment
# pip install numpy
```

### 3. Variables, data types, and operators
**Exercise:** Implement a class that represents a complex number and supports basic operations (addition, subtraction, multiplication).
```python
# Exercise: Create a class for complex numbers and implement basic operations.

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Test the class
a = ComplexNumber(3, 2)
b = ComplexNumber(1, 7)
print(a + b)
print(a - b)
print(a * b)
```

### 4. Control flow: if statements, loops
**Exercise:** Implement the quicksort algorithm.
```python
# Exercise: Implement the quicksort algorithm.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Test the algorithm
print(quicksort([3, 6, 8, 10, 1, 2, 1]))
```

### 5. Functions and modules
**Exercise:** Use decorators to measure the execution time of a function.
```python
import time

# Exercise: Create a decorator to measure function execution time.

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Function finished execution")

slow_function()
```

### 6. Input and output operations
**Exercise:** Serialize a Python object to a JSON file and then deserialize it back to a Python object.
```python
import json

# Exercise: Serialize and deserialize a Python object using JSON.

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Serialize to JSON file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Deserialize from JSON file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)
```
