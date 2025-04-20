# Used to define debugging/developer-friendly representation of an object

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        """Return a precise representation for debugging."""
        return f"Person('{self.name}', {self.age})"

person = Person("Punk", 32)

print(repr(person))  # Output: Person('Alice', 25)

# if `__str__` is not defined python falls back to `__repr__`
print(Person)  # Output: Person('Alice', 25)