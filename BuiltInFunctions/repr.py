# returns a string representation of an object, typically in a form that can recreate the object

print(repr(42))  # Output: '42'
print(repr([1, 2, 3]))  # Output: '[1, 2, 3]'

# Using repr() with special characters
special_chars = "Tab\tNewline\nQuote\'"
print(repr(special_chars))  # Output: "'Tab\\tNewline\\nQuote\\''" (Escaped properly)

# Custom repr() method in a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Bob", 25)
print(repr(p))  # Output: "Person(name='Bob', age=25)"
