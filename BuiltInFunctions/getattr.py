# retrieve the value of an attribute from an object

class MyClass:
    def __init__(self):
        self.name = "Alice"
        self.age = 30

person = MyClass()

name = getattr(person, "name")  # Equivalent to person.name
print(f"Name: {name}")  # Output: Name: Alice

# 1. Handling a non-existent attribute with a default value
hobby = getattr(person, "hobby", "Unknown")
print(f"Hobby: {hobby}")
# Output: Hobby: Unknown

# 2. Using getattr() with modules
import math
sqrt_function = getattr(math, "sqrt", None)
if sqrt_function:
    print(f"Square root of 16: {sqrt_function(16)}")  # Output: Square root of 16: 4.0
