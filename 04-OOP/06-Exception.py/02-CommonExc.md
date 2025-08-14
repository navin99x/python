# Python Exceptions

## Table of Contents
1. [Introduction](#introduction)
2. [Common Python Exceptions](#common-python-exceptions)
3. [Exception Handling](#exception-handling)
4. [Custom Exceptions](#custom-exceptions)
5. [Best Practices](#best-practices)

## Introduction

Python exceptions are events that occur during program execution that disrupt the normal flow of instructions. When an error occurs, Python raises an exception that can be caught and handled gracefully.


## Common Python Exceptions

### 1. SyntaxError
Occurs when Python cannot parse your code.

```python
# Example 1: Missing colon
if True
    print("Hello")  # SyntaxError: invalid syntax

# Example 2: Mismatched parentheses
print("Hello"  # SyntaxError: unexpected EOF while parsing

# Example 3: Invalid indentation
def my_function():
print("Hello")  # IndentationError: expected an indented block
```

### 2. NameError
Raised when a local or global name is not found.

```python
# Example 1: Using undefined variable
print(undefined_variable)  # NameError: name 'undefined_variable' is not defined

# Example 2: Typo in variable name
my_var = 10
print(my_variable)  # NameError: name 'my_variable' is not defined

# Example 3: Using variable before definition
print(x)
x = 5  # NameError: name 'x' is not defined
```

### 3. TypeError
Occurs when an operation is performed on an inappropriate type.

```python
# Example 1: Adding incompatible types
result = "5" + 3  # TypeError: can only concatenate str (not "int") to str

# Example 2: Calling non-callable object
my_var = 5
my_var()  # TypeError: 'int' object is not callable

# Example 3: Wrong number of arguments
def greet(name):
    return f"Hello, {name}!"

greet()  # TypeError: greet() missing 1 required positional argument: 'name'
```

### 4. ValueError
Raised when a function receives an argument of correct type but inappropriate value.

```python
# Example 1: Invalid string to int conversion
number = int("hello")  # ValueError: invalid literal for int() with base 10: 'hello'

# Example 2: Math domain error
import math
result = math.sqrt(-1)  # ValueError: math domain error

# Example 3: Invalid choice in list
colors = ['red', 'blue', 'green']
colors.remove('yellow')  # ValueError: list.remove(x): x not in list
```

### 5. IndexError
Occurs when trying to access an index that doesn't exist in a sequence.

```python
# Example 1: List index out of range
my_list = [1, 2, 3]
print(my_list[5])  # IndexError: list index out of range

# Example 2: Empty list access
empty_list = []
print(empty_list[0])  # IndexError: list index out of range

# Example 3: Negative index beyond range
print(my_list[-5])  # IndexError: list index out of range
```

### 6. KeyError
Raised when trying to access a dictionary key that doesn't exist.

```python
# Example 1: Missing key in dictionary
person = {'name': 'Alice', 'age': 30}
print(person['height'])  # KeyError: 'height'

# Example 2: Case sensitivity
print(person['Name'])  # KeyError: 'Name' (note the capital N)

# Example 3: Deleted key
del person['age']
print(person['age'])  # KeyError: 'age'
```

### 7. AttributeError
Occurs when trying to access an attribute that doesn't exist.

```python
# Example 1: Non-existent method
my_string = "hello"
my_string.append("world")  # AttributeError: 'str' object has no attribute 'append'

# Example 2: Typo in attribute name
my_list = [1, 2, 3]
my_list.apend(4)  # AttributeError: 'list' object has no attribute 'apend'

# Example 3: Wrong object type
number = 42
print(number.upper())  # AttributeError: 'int' object has no attribute 'upper'
```

### 8. FileNotFoundError
Raised when trying to open a file that doesn't exist.

```python
# Example 1: Non-existent file
with open('missing_file.txt', 'r') as file:
    content = file.read()  # FileNotFoundError: [Errno 2] No such file or directory

# Example 2: Wrong file path
with open('/invalid/path/file.txt', 'r') as file:
    content = file.read()  # FileNotFoundError

# Example 3: Typo in filename
with open('data.txt', 'r') as file:  # but file is actually 'data.csv'
    content = file.read()  # FileNotFoundError
```

### 9. ZeroDivisionError
Occurs when dividing by zero.

```python
# Example 1: Direct division by zero
result = 10 / 0  # ZeroDivisionError: division by zero

# Example 2: Modulo by zero
remainder = 10 % 0  # ZeroDivisionError: integer division or modulo by zero

# Example 3: Variable containing zero
divisor = 0
result = 100 / divisor  # ZeroDivisionError: division by zero
```

### 10. ImportError / ModuleNotFoundError
Raised when an import statement fails.

```python
# Example 1: Non-existent module
import non_existent_module  # ModuleNotFoundError: No module named 'non_existent_module'

# Example 2: Incorrect module name
import numpyy  # ModuleNotFoundError: No module named 'numpyy'

# Example 3: Import from non-existent module
from fake_module import some_function  # ModuleNotFoundError
```

### 11. IndentationError
A subclass of SyntaxError for indentation-related issues.

```python
# Example 1: Missing indentation
def my_function():
print("Hello")  # IndentationError: expected an indented block

# Example 2: Inconsistent indentation
if True:
    print("First line")
   print("Second line")  # IndentationError: unindent does not match any outer indentation level

# Example 3: Unexpected indentation
print("Hello")
    print("World")  # IndentationError: unexpected indent
```

### 12. KeyboardInterrupt
Raised when the user presses Ctrl+C to interrupt the program.

```python
# Example: Long-running loop
try:
    while True:
        pass  # Press Ctrl+C to trigger KeyboardInterrupt
except KeyboardInterrupt:
    print("Program interrupted by user")
```

### 13. OverflowError
Raised when an arithmetic operation is too large to be represented.

```python
# Example 1: Exponential overflow
import math
result = math.exp(1000)  # OverflowError: math range error

# Example 2: Large power operation (in some contexts)
# This might not always raise OverflowError in modern Python
# as it handles large integers well, but can occur with floats
result = 10.0 ** 308  # May raise OverflowError depending on system
```

### 14. RecursionError
Raised when the maximum recursion depth is exceeded.

```python
# Example 1: Infinite recursion
def infinite_recursion():
    return infinite_recursion()

infinite_recursion()  # RecursionError: maximum recursion depth exceeded

# Example 2: Recursive function without base case
def factorial(n):
    return n * factorial(n - 1)  # Missing base case

factorial(5)  # RecursionError: maximum recursion depth exceeded
```

### 15. StopIteration
Raised by iterators to signal the end of iteration.

```python
# Example: Manually calling next() beyond iterator end
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # StopIteration
```

## Exception Handling

### Basic try-except Structure

```python
# Basic exception handling
try:
    risky_operation = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching multiple exceptions with one except block
try:
    # Some risky code
    pass
except (ValueError, TypeError, KeyError) as e:
    print(f"An error occurred: {e}")
```

### Using else and finally

```python
# Complete exception handling structure
try:
    file = open('data.txt', 'r')
    data = file.read()
    number = int(data)
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("File contains invalid data!")
else:
    # Executes only if no exception occurred
    print(f"Successfully read number: {number}")
finally:
    # Always executes, regardless of exceptions
    try:
        file.close()
        print("File closed")
    except NameError:
        print("File was never opened")
```

### Exception Information

```python
# Getting exception details
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")

# Using traceback for detailed error information
import traceback

try:
    result = int("not_a_number")
except ValueError:
    print("Exception occurred:")
    traceback.print_exc()
```

## Custom Exceptions

### Creating Custom Exception Classes

```python
# Basic custom exception
class CustomError(Exception):
    pass

# Custom exception with message
class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# More complex custom exception
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds: Balance {balance}, Attempted withdrawal {amount}"
        super().__init__(message)

# Using custom exceptions
def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw_money(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    print(f"Current balance: {e.balance}")
    print(f"Attempted amount: {e.amount}")
```

### Exception Chaining

```python
# Exception chaining with 'raise from'
def process_data(data):
    try:
        return int(data)
    except ValueError as e:
        raise ValidationError("Data processing failed") from e

try:
    result = process_data("invalid")
except ValidationError as e:
    print(f"Main exception: {e}")
    print(f"Original exception: {e.__cause__}")
```

## Best Practices

### 1. Be Specific with Exception Handling

```python
# Bad: Too broad
try:
    # Some code
    pass
except Exception:
    print("Something went wrong")

# Good: Specific exceptions
try:
    with open('file.txt', 'r') as f:
        data = json.load(f)
        result = data['key'] / data['divisor']
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON format")
except KeyError as e:
    print(f"Missing required key: {e}")
except ZeroDivisionError:
    print("Division by zero")
```

### 2. Use Context Managers for Resource Management

```python
# Good: Using context manager
try:
    with open('file.txt', 'r') as file:
        content = file.read()
        # File automatically closed even if exception occurs
except FileNotFoundError:
    print("File not found")

# Good: Custom context manager for exception handling
from contextlib import contextmanager

@contextmanager
def error_handler():
    try:
        yield
    except ValueError:
        print("Value error occurred")
    except TypeError:
        print("Type error occurred")

with error_handler():
    # Your risky code here
    pass
```

### 3. Logging Exceptions

```python
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    risky_operation()
except Exception as e:
    logger.exception("An error occurred during risky operation")
    # This logs the full traceback
```

### 4. Validation and Early Returns

```python
def process_user_data(user_data):
    # Validate input early
    if not isinstance(user_data, dict):
        raise TypeError("user_data must be a dictionary")
    
    if 'name' not in user_data:
        raise ValueError("user_data must contain 'name' key")
    
    if not user_data['name'].strip():
        raise ValueError("name cannot be empty")
    
    # Process data...
    return f"Hello, {user_data['name']}!"

# Usage with proper error handling
try:
    result = process_user_data({'name': 'Alice'})
    print(result)
except (TypeError, ValueError) as e:
    print(f"Invalid input: {e}")
```

### 5. Re-raising Exceptions

```python
def critical_operation():
    try:
        # Some critical code
        pass
    except Exception as e:
        # Log the error
        logger.error(f"Critical operation failed: {e}")
        # Re-raise the exception for caller to handle
        raise

# Or modify and re-raise
def enhanced_operation():
    try:
        # Some code
        pass
    except ValueError as e:
        # Add context and re-raise
        raise ValueError(f"Enhanced operation failed: {e}") from e
```

This guide covers the most common Python exceptions you'll encounter in everyday programming. Understanding these exceptions and how to handle them properly will help you write more robust and maintainable Python code. Remember to always handle exceptions at the appropriate level of your application and provide meaningful error messages to users.