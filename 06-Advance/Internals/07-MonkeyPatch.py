"""
Allow to modify or extend the behaviour of existing modules, class and function.

Use case: 
- testing
- dynamic behaviour
- bug fixing
"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    

def extract_first_name(self: Person) -> str:
    return self.name.split(" ")[0]

# Monkey patching
Person.get_first_name = extract_first_name  # type: ignore

# test
obj = Person("Ram Bahadur", 28)
print(obj.get_first_name())  # type: ignore