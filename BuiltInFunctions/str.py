# returns a string representation of an object, typically in a form that is human readable

print(str(42))  # Output: '42'
print(str([1, 2, 3]))  # Output: '[1, 2, 3]'

# Using str() with special characters
special_chars = "Tab\tNewline\nQuote\'"
print(str(special_chars)) 
# Output:
# Tab     Newline
# Quote'

# Custom str() method in a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

p = Person("Bob", 25)
print(str(p))  # Output: Bob is 25 years old.
