# Everything in pyton is a Class.

class Student:
    pass

std = Student()
print(isinstance(std, Student))  # True

# Note: Class iteself is an instance of `type` class.
print(isinstance(Student, type))  # True