# Inheritance allow a class to reuse logic of an exising class

class Person():
    """Represent a basic person with name and age"""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name = {self.name}, Age = {self.age}"
    
class Student(Person):
    """Represents a student inheriting attributs from Person"""
    def __init__(self, name: int, age: int, student_id: int):  # method overriding
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):  # method overriding
        return super().__str__() + f", SID = {self.student_id}"

obj1 = Person("Hari", 20)
obj2 = Student("Ram", 21, 200321)

print(obj1)  # Output: Name = Hari, Age = 20
print(obj2)  # Output: Name = Ram, Age = 21, SID = 200321
