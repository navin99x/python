#__init__ is used as a counstructor in python

class Student:

    def __init__(self, name, age, major):
        self.name= name     #instance attribute
        self.age= age
        self.course= major

    
    def print_data(self):       #instance method
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")


std= Student("hari", 20, "csit")

std.print_data()
# Student.print_data(std)  # Equivalent

"""
notes:
- "__init__" is used to initialize object attribute
- first parameter of method is always the refernce to the object that calls the specific method i.e, `self` by convention
- '__init__" method is automatically called when a new instance from an class is created
- instance attribute and method can only be accessed by the object derived from that class only
"""