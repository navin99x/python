class Person:
    """Represents a basic person with name and age."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name = {self.name}, Age = {self.age}"

class School:
    """Represents a school with a name and school ID."""
    def __init__(self, school_name, school_id):
        self.school_name = school_name
        self.school_id = school_id

    def __str__(self):
        return f"School = {self.school_name}, School ID = {self.school_id}"

class Student(Person, School):
    """Represents a student inheriting attributes from both Person and School."""
    def __init__(self, name, age, student_id, school_name, school_id):
        Person.__init__(self, name, age)
        School.__init__(self, school_name, school_id)
        self.student_id = student_id

    def __str__(self):
        return f"{Person.__str__(self)}, Student ID = {self.student_id}, {School.__str__(self)}"

student = Student("Ram", 21, 200321, "Greenwood High", "GH-005")
print(student)  
# Output: Name = Ram, Age = 21, Student ID = 200321, School = Greenwood High, School ID = GH-00522