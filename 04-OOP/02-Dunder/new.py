"""
`object` is the root of class hierarchy i.e., all classes ultimately inherits from `object` 
"""


class Person():
    def __init__(self, name):
        self.__name = name

obj = object.__new__(Person)
print(obj.__dict__)

obj.__init__("John")
print(obj.__dict__)

"""
When you create new object of a class python calls `__new__` method to allocate memory at first.
Then calls `__init__` to initialize the instance.
"""

# Application of `__new__` methods:
# Singletons: Only one instance of a class can be created.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
s1 = Singleton()
s2 = Singleton()

print(s1 is s2) # Output: True

# Another application lies when creating subclass of immutable type like `int`, `str`
# In that case you need to modify `__new__`.