# check whether an object is callable, meaning it can be called like a function

def my_function():
    return "I am callable!"

print(callable(my_function))  # Output: True (Functions are callable)

# Checking lambda functions
my_lambda = lambda x: x * 2
print(callable(my_lambda))  # Output: True (Lambdas are callable)

my_var = 10
print(callable(my_var))  # Output: False (Integers are not callable)

print(callable(len))  # Output: True (len() is callable)
print(callable([].append))  # Output: True (Methods are callable)


# Working with classes and instances
class MyClass:
    def greet(self):
        return "Hello!"

print(callable(MyClass))  # Output: True (Classes are callable)
my_instance = MyClass()
print(callable(my_instance))  # Output: False (Instances are not callable by default)

# Making a class instance callable using the __call__ method
class CallableClass:
    def __call__(self):
        return "I am a callable object!"

callable_instance = CallableClass()
print(callable(callable_instance))  # Output: True
print(callable_instance())  # Output: I am a callable object!
