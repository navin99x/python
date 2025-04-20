# Used to define human-readable string representation of an object

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        """Return a user-friendly representation of the object."""
        return f"Person(name={self.name}, age={self.age})"

person = Person("Punk", 32)
print(person)  # Output: Person(name=Punk, age=32)