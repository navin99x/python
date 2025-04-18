# checks whether an object belongs to a specified class or type

print(isinstance(22, int))  # Output: True
print(isinstance("Navin", str))  # Output: True
print(isinstance(3.14, (int, float)))  # Output: True (data is a float)
print(isinstance([1, 2, 3], list))  # Output: True
print(isinstance({"key": "value"}, dict))  # Output: True

# 1. Checking user-defined classes
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))    # Output: True
print(isinstance(dog, Animal))  # Output: True (Dog is a subclass of Animal)
print(isinstance(dog, object))  # Output: True (Everything in Python is an object)
