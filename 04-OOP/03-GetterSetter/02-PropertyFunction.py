# yet another way to define getter & setter is using `property()` built-in function.
# Modern Alternative: `@property` decorator.

class PersonDetail:

    def __init__(self, name, age):
        self.name= name
        self.age= age

    def set_name(self, name):
        if not name:
            raise ValueError("Name can't be empty")
        self._name= name
        
    def set_age(self, age):
        if(age< 18):
            raise ValueError ("Age must be greater than 18")
        
        self._age= age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    
    def __str__(self):
        return f"Name = {self._name}, Age = {self._age}"

    age= property(fset= set_age, fget= get_age)
    name= property(fset= set_name, fget= get_name)

person1= PersonDetail("Rakesh", 20)     
person2= PersonDetail("Hari", 40)

print(person1)  # Output: Name = Rakesh, Age = 20
print(person2)  # Output: Name = Hari, Age = 40

print(person2.age)  # Output: 40
# Whenever we are using `age`, Python internally refers to `age` property object which take necessary action of either storing or retriving value for `_age` attribute

person2.name= "Chandrey"
print(person2.age)

"""
Explanation:
- The only differnce between the approach defined in `01-Explicit.py` and here is that in `01-Explicit.py` we have to call getter and setter method manually to store and access `name` & `age` attribute.
- While in this approach, the class is implemented with property function which allow user to interact with `age` and `name` variable directly with thier names but internally it calls get and set method for both these attributes.
"""
