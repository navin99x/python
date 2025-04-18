#  checks whether a given class is a subclass of another class

class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # Output: True (Dog is a subclass of Animal)
print(issubclass(Animal, Dog))  # Output: False (Animal is NOT a subclass of Dog)

print(issubclass(bool, int))  # Output: True (In Python, bool is a subclass of int)
