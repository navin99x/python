# ued to access methods and attributes of a parent (or superclass) from a child (or subclass

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        print("Hello from Child!")
        super().greet() 

c = Child()
c.greet()
# Output:
# Hello from Child!
# Hello from Parent!

# UseCase: Extending Parent's __init__ method using super()
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(f"Dog's name: {dog.name}, Breed: {dog.breed}")
# Output: Dog's name: Buddy, Breed: Golden Retriever

# Demonstrating the Method Resolution Order (MRO)
class X:
    def greet(self):
        print("Hello from X")

class Y:
    def greet(self):
        print("Hello from Y")

class Z(X, Y):  # Multiple inheritance
    def greet(self):
        super().greet()

z = Z()
z.greet()
# Output: Hello from X

print(Z.__mro__)  # Shows the MRO (Method Resolution Order)
# Output: (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)
