# Section 3: *Python Libraries for Automation*

---

## Basic

### 1. Overview of essential Python libraries for automation
**Exercise:** List down at least five Python libraries that are commonly used for automation tasks and write a brief description of each.
```plaintext
# Exercise: List and describe five Python libraries for automation.
# (This is a theoretical exercise. The answer can be written in a notebook or discussed in a group.)
```

### 2. Working with web automation libraries (e.g., Selenium, BeautifulSoup)
**Exercise:** Use BeautifulSoup to parse an HTML string and extract the text inside the `<p>` tag.
```python
from bs4 import BeautifulSoup

# Exercise: Parse the HTML and extract text from the <p> tag.

html_content = "<html><head><title>Title</title></head><body><p>This is a paragraph.</p></body></html>"

soup = BeautifulSoup(html_content, 'html.parser')
paragraph_text = soup.p.text

print(paragraph_text)  # This should print "This is a paragraph."
```

### 3. Introduction to unit testing with the unittest library
**Exercise:** Write a simple function to add two numbers and then create a unit test to test this function.
```python
# Exercise: Write a function and its unit test.

def add_numbers(a, b):
    return a + b

# To test the function, you can use the unittest library.
# Here's a simple test case:

# import unittest

# class TestAddition(unittest.TestCase):
#     def test_add_numbers(self):
#         self.assertEqual(add_numbers(2, 3), 5)

# if __name__ == "__main__":
#     unittest.main()
```

### 4. Logging with the logging Library
**Exercise:** Set up basic logging to capture messages of level INFO and above. Log a few messages of different severity levels.
```python
import logging

# Exercise: Set up basic logging and log messages.

logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
```

### 5. Regular Expressions
**Exercise:** Use a regular expression to validate if a given string is a valid email address.
```python
import re

# Exercise: Validate an email address using a regular expression.

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

# Test the function
print(is_valid_email("example@email.com"))  # This should print True
print(is_valid_email("example-email"))      # This should print False
```

---

## Medium

## Section 3: *Python Libraries for Automation*

### 1. Overview of essential Python libraries for automation
**Exercise:** Research and write a short Python script that uses the `os` library to list all files in the current directory and their sizes.
```python
import os

# Exercise: List all files in the current directory and their sizes using the os library.

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        size = os.path.getsize(filename)
        print(f"{filename}: {size} bytes")
```

### 2. Working with web automation libraries (e.g., Selenium, BeautifulSoup)
**Exercise:** Use Selenium to open a web browser, navigate to a website, and take a screenshot.
```python
# Note: This exercise requires the installation of Selenium and the appropriate web driver for the browser you're using.

# from selenium import webdriver

# Exercise: Use Selenium to open a browser, navigate to a website, and take a screenshot.

# driver = webdriver.Chrome()  # Use the appropriate driver for your browser
# driver.get("https://www.google.com")
# driver.save_screenshot("screenshot.png")
# driver.quit()
```

### 3. Introduction to unit testing with the unittest library
**Exercise:** Write a function that checks if a string is a palindrome. Then, create unit tests to test various cases.
```python
# Exercise: Write a palindrome checker function and its unit tests.

def is_palindrome(s):
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]

# To test the function, you can use the unittest library.
# Here's a simple test case:

# import unittest

# class TestPalindrome(unittest.TestCase):
#     def test_palindrome(self):
#         self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
#         self.assertFalse(is_palindrome("Hello"))
#         self.assertTrue(is_palindrome("Madam"))

# if __name__ == "__main__":
#     unittest.main()
```

### 4. Logging with the logging Library
**Exercise:** Set up logging to capture messages of level WARNING and above. Also, configure it to write logs to a file named `app.log`.
```python
import logging

# Exercise: Set up logging to capture messages and write to a file.

logging.basicConfig(filename='app.log', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
```

### 5. Regular Expressions
**Exercise:** Use a regular expression to extract all phone numbers from a given text.
```python
import re

# Exercise: Extract phone numbers from a text using a regular expression.

text = "Contact us at 123-456-7890 or 987-654-3210."

pattern = r"\d{3}-\d{3}-\d{4}"
phone_numbers = re.findall(pattern, text)

print(phone_numbers)  # This should print ['123-456-7890', '987-654-3210']
```

---

## Advanced

### 1. Overview of essential Python libraries for automation
**Exercise:** Use the `subprocess` library to execute a shell command that fetches the current system's uptime.
```python
import subprocess

# Exercise: Fetch the system's uptime using the subprocess library.

result = subprocess.run(['uptime'], capture_output=True, text=True)
print(result.stdout)
```

### 2. Working with web automation libraries (e.g., Selenium, BeautifulSoup)
**Exercise:** Use Selenium to automate a login process on a dummy website (like http://example.com). Fill in the username and password fields, submit the form, and capture any resulting message.
```python
# Note: This is a hypothetical exercise as http://example.com doesn't have a login form. 
# However, the code structure can be applied to websites with actual login forms.

# from selenium import webdriver

# Exercise: Use Selenium to automate a login process.

# driver = webdriver.Chrome()
# driver.get("http://example.com/login")

# username_field = driver.find_element_by_id("username")
# password_field = driver.find_element_by_id("password")

# username_field.send_keys("dummy_username")
# password_field.send_keys("dummy_password")

# login_button = driver.find_element_by_id("login_button")
# login_button.click()

# message = driver.find_element_by_id("message").text
# print(message)

# driver.quit()
```

### 3. Introduction to unit testing with the unittest library
**Exercise:** Implement a mock object in a unit test to simulate a database connection for testing a function without actually connecting to a real database.
```python
# Note: This exercise requires the `unittest.mock` library.

# import unittest
# from unittest.mock import MagicMock

# Exercise: Use a mock object to simulate a database connection.

# def get_user_data(db_connection, user_id):
#     return db_connection.fetch_data(user_id)

# class TestDatabaseConnection(unittest.TestCase):
#     def test_get_user_data(self):
#         mock_db = MagicMock()
#         mock_db.fetch_data.return_value = {"id": 1, "name": "John"}

#         result = get_user_data(mock_db, 1)
#         self.assertEqual(result, {"id": 1, "name": "John"})

# if __name__ == "__main__":
#     unittest.main()
```

### 4. Logging with the logging Library
**Exercise:** Set up logging to capture messages of all severity levels. Configure it to write logs to a file named `detailed_app.log` and format the messages to include the timestamp, log level, and the actual message.
```python
import logging

# Exercise: Set up detailed logging to capture messages and write to a file.

logging.basicConfig(filename='detailed_app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
```

### 5. Regular Expressions
**Exercise:** Use a regular expression to validate a complex password. The password should be at least 8 characters, contain both uppercase and lowercase characters, have at least one numerical digit, and contain at least one special character (e.g., @, #, $, %, &, *, !).
```python
import re

# Exercise: Validate a complex password using a regular expression.

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]{8,}$"
    return bool(re.match(pattern, password))

# Test the function
print(is_valid_password("Password123!"))  # This should print True
print(is_valid_password("password123"))   # This should print False
```

## References
- [What is Python?](https://www.python.org/doc/essays/blurb/)
- [Python Crash Course, 2nd Edition](https://www.oreilly.com/library/view/python-crash-course/9781492071266/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

## [Go to home](../README.md)
