# delete an user-defined object attribute

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = MyClass("Alice", 30)

print("Before deletion:", vars(person))  # Output: {'name': 'Alice', 'age': 30}

# Using delattr() to delete an attribute
delattr(person, "age")

print("After deletion:", vars(person))  # Output: {'name': 'Alice'}
