# allow a function to accept a variable number of positional arguments

def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")  

# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!