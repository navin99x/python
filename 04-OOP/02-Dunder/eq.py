# `__eq__` is implemented to define the equality logic for comparing two objects using the equal operator (==).

class Person():
    def __init__(self, name:str, nin: int):
        self.name = name
        self.nin = nin  # National Identification Number (NIN)

    def __eq__(self, other):
        return self.nin == other.nin
    
first_person = Person("Hari Poudel", 1234421)
second_person = Person("hari", 1234421)

if(first_person == second_person):
    print("They both are same")
else:
    print("They both are unique")
# Output: They both are same

# Note: Overriding `__eq__` & then not implementing `__hash__` function makes the object unhashable.
# That means they can't be used as key in dict, or set elements.