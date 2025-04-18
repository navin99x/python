# list the attributes and methods of an object
# When called with no arguments, it list the names in current local scope

# 1. Using dir() without arguments (Current Scope)
x = 10
def my_function():
    return "Hello, World!"

print("Names in the current scope:")
print(dir())
# Output: List of names including 'x' and 'my_function'

# 2. Using dir() on built-in objects
print("\nAttributes and methods of a list:")
print(dir([]))
# Output: List of methods like 'append', 'clear', 'pop', etc.

# 3. Using dir() on custom objects
class MyClass:
    def __init__(self):
        self.name = "Alice"

    def greet(self):
        return f"Hello, {self.name}!"

obj = MyClass()
print("\nAttributes and methods of MyClass:")
print(dir(obj))
# Output: Includes '__init__', 'greet', and 'name'

# 4. Using dir() on modules
import math
print("\nAttributes and methods of math module:")
print(dir(math))
# Output: Includes 'sin', 'cos', 'pi', etc.

# 5. Filtering output for better readability
print("\nFilter only callable methods:")
callable_methods = [item for item in dir([]) if callable(getattr([], item))]
print(callable_methods)
# Output: ['append', 'clear', 'copy', 'count', ...]
