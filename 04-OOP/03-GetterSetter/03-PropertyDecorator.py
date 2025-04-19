# Ultimate way to manage getters & setters.

class PersonDetail:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name can't be empty")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Age must be greater than 18")
        self._age = age

    def __str__(self):
        return f"Name = {self._name}, Age = {self._age}"

person = PersonDetail('Rakesh', 20)
print(person)  # Output: Name = Rakesh, Age = 20

"""
Basic Synatx:

class MyClass:
    def __init__(self, attr):
        self.prop = attr

    @property
    def prop(self):
        return self._attr

    @prop.setter
    def prop(self, value):
        self._attr = value
"""