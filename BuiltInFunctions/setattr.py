# used to dynamically sets or updates an attribute of an object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

setattr(p, "age", 31)
print(f"Updated age: {p.age}")  # Output: Updated age: 31

# Adding a new attribute dynamically
setattr(p, "city", "New York")
print(f"Person's city: {p.city}")  # Output: Person's city: New York
