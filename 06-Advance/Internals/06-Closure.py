"""
A closure is a function that has access to its own scope,
as well as the scope of its outer functions,
even when the outer function has finished executing.
"""

def outer():
    value = 20

    def inner():
        print(f"Value: {value}")
    
    return inner    # outer() returns a closure

closure = outer()
closure()

# In a nutshell:
# A closure is a function with an extended scope that contains free variable.