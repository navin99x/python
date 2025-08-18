# By only defining getter (`@property`) only on a attribute or method it becames read-only.
# In short if there is a method that doesn't take any argument , you can change it's property

import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property  # read-only attribute
    def radius(self):
        return self._radius
    
    @property  # read-only method
    def area(self): 
        return math.pi * self._radius ** 2


c = Circle(10)
print(c.area)  # Output: 314.15....
# Read-only method is internally turned into attribute like property,
# therefore can be accessed without any paranthesis

# c.radius = 20  # AttributeError