# Python Basics Guide

## Table of Contents

- [Core Concepts](#core-concepts)
  - [Variables and Data Types](#variables-and-data-types)
  - [Naming Conventions](#naming-conventions)
  - [Comments & Documentation](#comments--documentation)
- [Operators](#operators)
  - [Arithmetic](#arithmetic)
  - [Assignment](#assignment)
  - [Comparison](#comparison)
  - [Logical](#logical)
  - [Identity](#identity)
  - [Membership](#membership)
  - [Bitwise](#bitwise)
- [Control Flow](#control-flow)
  - [Conditional Statements](#conditional-statements)
  - [Ternary Operator](#ternary-operator)
  - [Loops](#loops)
- [Functions](#functions)
  - [Basic Function](#basic-function)
  - [Function Parameters](#function-parameters)
  - [Lambda Functions](#lambda-functions)
- [Data Structures](#data-structures)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Sets](#sets)
- [Modules and Imports](#modules-and-imports)
- [Exception Handling](#exception-handling)
  - [Common Built-in Exceptions](#common-built-in-exceptions)
- [File Handling](#file-handling)
  - [File Modes](#file-modes)
- [Type Conversion](#type-conversion)
- [Useful Built-in Functions](#useful-built-in-functions)

## Core Concepts

### Variables and Data Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text data | `name = "Python"` |
| `int` | Integer numbers | `count = 42` |
| `float` | Decimal numbers | `pi = 3.14159` |
| `bool` | Boolean values | `is_active = True` |
| `list` | Ordered, mutable collection | `fruits = ["apple", "banana"]` |
| `tuple` | Ordered, immutable collection | `coords = (10, 20)` |
| `dict` | Key-value pairs | `user = {"name": "Alice", "age": 25}` |
| `set` | Unordered collection of unique items | `unique_ids = {101, 102, 103}` |
| `None` | Represents absence of value | `result = None` |

### Naming Conventions

- Variables, Functions: `snake_case`
- Constants: `SCREAMING_SNAKE_CASE`
- Classes: `PascalCase`

### Comments & Documentation

```python
# Single line comment

"""
Multi-line docstring
Used to document modules, functions, classes, or methods
"""

def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
    """
    return 3.14159 * radius ** 2
```

## Operators

### Arithmetic
- Addition: `a + b`
- Subtraction: `a - b`
- Multiplication: `a * b`
- Division: `a / b` (returns float)
- Floor Division: `a // b` (returns int)
- Modulus: `a % b` (remainder)
- Exponentiation: `a ** b` (power)

### Assignment
- Basic: `x = 5`
- Compound: `x += 2`, `x -= 1`, `x *= 3`, `x /= 2`, etc.

### Comparison
- Equal: `a == b`
- Not equal: `a != b`
- Greater/Less than: `a > b`, `a < b`
- Greater/Less than or equal: `a >= b`, `a <= b`

### Logical
- AND: `a and b`
- OR: `a or b`
- NOT: `not a`

### Identity
- Is: `a is b` (checks if objects are the same)
- Is not: `a is not b`

### Membership
- In: `a in b` (checks if a is in b)
- Not in: `a not in b`

### Bitwise
- AND: `a & b`
- OR: `a | b`
- XOR: `a ^ b`
- NOT: `~a`
- Shift: `a << b`, `a >> b`

## Control Flow

### Conditional Statements

```python
if condition:
    # code block

elif another_condition:
    # code block

else:
    # code block
```

### Ternary Operator

```python
result = value_if_true if condition else value_if_false
```

### Loops

```python
# For loop
for item in iterable:
    # code block
else:  # Optional
    # executes after loop completes normally (not after break)

# While loop
while condition:
    # code block
else:  # Optional
    # executes after loop completes normally (not after break)

# Loop control
break       # Exit the loop
continue    # Skip to next iteration
pass        # Do nothing placeholder
```

## Functions

### Basic Function

```python
def function_name(parameter1: datatype, parameter2:datatype) -> return_type:
    """Docstring describing the function"""
    # function body
    return result
```

### Function Parameters

```python
# Default parameters
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# Positional-only parameters (Python 3.8+)
def add(a, b, /):  # Parameters before / are positional-only
    return a + b

# Keyword-only parameters
def divide(*, numerator, denominator):  # Parameters after * are keyword-only
    return numerator / denominator

# Variable-length arguments
def func(*args, **kwargs):
    # args is a tuple of positional arguments
    # kwargs is a dictionary of keyword arguments
    pass
```

### Lambda Functions

```python
# Anonymous functions
square = lambda x: x ** 2
```

## Data Structures

### Lists

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Accessing elements
first_fruit = fruits[0]  # apple
last_fruit = fruits[-1]  # cherry

# Slicing
subset = fruits[1:3]  # ["banana", "cherry"]

# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
```

**List Methods**:
- `list.append(item)` - Add item to end
- `list.extend(iterable)` - Add all items from iterable
- `list.insert(index, item)` - Insert item at index
- `list.remove(item)` - Remove first occurrence of item
- `list.pop([index])` - Remove and return item at index (default: last)
- `list.clear()` - Remove all items
- `list.index(item)` - Get index of first occurrence
- `list.count(item)` - Count occurrences
- `list.sort()` - Sort in place
- `list.reverse()` - Reverse in place
- `list.copy()` - Return shallow copy

### Tuples

```python
# Creating tuples
point = (10, 20)
single_item = (42,)  # Note the comma
```

**Tuple Methods**:
- `tuple.count(item)` - Count occurrences
- `tuple.index(item)` - Get index of first occurrence

### Dictionaries

```python
# Creating dictionaries
user = {"name": "Alice", "age": 25}
user_alt = dict(name="Alice", age=25)

# Accessing elements
name = user["name"]  # Alice
age = user.get("age", 0)  # Returns 0 if "age" not found

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Dictionary Methods**:
- `dict.get(key, default)` - Get value for key, return default if key missing
- `dict.keys()` - Return view of keys
- `dict.values()` - Return view of values
- `dict.items()` - Return view of (key, value) pairs
- `dict.update(other)` - Update with key/value pairs from other
- `dict.pop(key, default)` - Remove and return value for key
- `dict.popitem()` - Remove and return a (key, value) pair
- `dict.setdefault(key, default)` - Get value for key, set default if key missing
- `dict.clear()` - Remove all items
- `dict.copy()` - Return shallow copy

### Sets

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3}

# Set operations
union = fruits | {"orange", "grape"}
intersection = {1, 2, 3} & {2, 3, 4}  # {2, 3}
difference = {1, 2, 3} - {2, 3, 4}  # {1}
symmetric_difference = {1, 2, 3} ^ {2, 3, 4}  # {1, 4}
```

**Set Methods**:
- `set.add(item)` - Add item
- `set.remove(item)` - Remove item (raises KeyError if missing)
- `set.discard(item)` - Remove item if present
- `set.pop()` - Remove and return an arbitrary item
- `set.clear()` - Remove all items
- `set.union(other)` - Return union of sets (or `|`)
- `set.intersection(other)` - Return intersection (or `&`)
- `set.difference(other)` - Return difference (or `-`)
- `set.symmetric_difference(other)` - Return symmetric difference (or `^`)
- `set.issubset(other)` - Test if set is subset (or `<=`)
- `set.issuperset(other)` - Test if set is superset (or `>=`)
- `set.isdisjoint(other)` - Test if no elements in common

## Modules and Imports

```python
# Import entire module
import math

# Import with alias
import numpy as np

# Import specific items
from datetime import datetime, timedelta

# Import all items (not recommended)
from math import *

# Define what can be imported when using "from module import *"
__all__ = ['function1', 'function2']
```

## Exception Handling

```python
try:
    # Code that might raise an exception
    result = 10 / 0

except ZeroDivisionError as e:
    # Handle specific exception
    print(f"Error: {e}")

except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")

else:
    # Executes if no exception occurs
    print("Operation successful")

finally:
    # Always executes
    print("Cleanup code")
```

### Common Built-in Exceptions
- `Exception` - Base for all exceptions
- `TypeError` - Wrong type of operand/argument
- `ValueError` - Right type but wrong value
- `NameError` - Name not found
- `IndexError` - Index out of range
- `KeyError` - Key not found in dictionary
- `FileNotFoundError` - File not found
- `ZeroDivisionError` - Division by zero

## File Handling

```python
# Reading a file
with open("filename.txt", "r") as file:
    content = file.read()  # Read entire file
    # OR
    lines = file.readlines()  # Read all lines into a list
    # OR
    line = file.readline()  # Read next line

# Writing to a file
with open("filename.txt", "w") as file:  # "w" overwrites, "a" appends
    file.write("Hello, world!\n")
    file.writelines(["Line 1\n", "Line 2\n"])
```

### File Modes
- `"r"` - Read (default)
- `"w"` - Write (creates new file or truncates existing)
- `"a"` - Append
- `"x"` - Exclusive creation
- `"b"` - Binary mode (added to other modes)
- `"t"` - Text mode (default)
- `"+"` - Update (read and write)

## Type Conversion

- `int(x)` - Convert to integer
- `float(x)` - Convert to float
- `str(x)` - Convert to string
- `bool(x)` - Convert to boolean
- `list(x)` - Convert to list
- `tuple(x)` - Convert to tuple
- `set(x)` - Convert to set
- `dict(x)` - Convert to dictionary

## Useful Built-in Functions

- `len(obj)` - Return length of object
- `range(start, stop, step)` - Create a sequence
- `enumerate(iterable)` - Return (index, value) pairs
- `zip(*iterables)` - Combine multiple iterables
- `map(function, iterable)` - Apply function to all items
- `filter(function, iterable)` - Filter items by function
- `sorted(iterable)` - Return sorted list
- `reversed(seq)` - Return reversed iterator
- `min(iterable)`, `max(iterable)` - Get minimum/maximum
- `sum(iterable)` - Sum of items
- `any(iterable)` - True if any item is True
- `all(iterable)` - True if all items are True
- `input([prompt])` - Read user input
- `print(*objects)` - Print objects
