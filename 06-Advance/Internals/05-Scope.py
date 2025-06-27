"""
Python follow 'LEGB' rule while searching for name: 
- Local scope: Defined inside function or method
- Enclosing scope (nonlocal scope): Nested function
- Global scope: Top of a module
- Built-in scope: e.g., len, str, list, ...
"""

x = 10  # global scope

def outer():
    x = 20  # local scope for outer() and enclosing scope for inner() 

    def inner():
        x = 30  # local scope
        print("Local:", x)

    inner()
    print("Enclosing:", x)

outer()
print("Global:", x)