# The main use case of getter and setter is use to achieve data encaptsulation and validation.

# Important Note: 
# Below code uses explicit getter and setters which is not recommended at all.
# It is only for understanding purpose on how getter & setters works.
# This approach has backward compaiblity & doesn't adhere to modern python conventions.
# Modern Alternative: `@property` decorator.

class PersonDetail:

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if not name:
            raise ValueError ("Name can't be empyt")
        self._name= name
    
    def set_age(self, age):
        if(age < 18):
            raise ValueError ("Age must be greater than 18")
        self._age= age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    
    def __str__(self):
        return f"Name = {self._name}, Age = {self._age}"

person1= PersonDetail("Rakesh" , 20)
person2= PersonDetail("Hari", 40)

print(person1)  # Output: Name = Rakesh, Age = 20
print(person2)  # Output: Name = Hari, Age = 40

print(person2.get_age())  # 40

# person2.set_age(17)  # Output: ValueError: Age must be greater than 18

person2.set_name("Chandrey")  # Output: Name = Chandrey, Age = 40
print(person2)
