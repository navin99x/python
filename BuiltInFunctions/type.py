# used to determine the type of an object or to dynamically create new classes

print(type(42))         # Output: <class 'int'>
print(type(3.14))       # Output: <class 'float'>
print(type("Python"))   # Output: <class 'str'>
print(type([1, 2, 3]))  # Output: <class 'list'>
print(type(len))   # Output: <class 'builtin_function_or_method'>
print(type(type))        # Output: <class 'type'> (type is itself a type!)

# type with built-in object
class MyClass:
    pass

obj = MyClass()
print(type(obj))  # Output: <class '__main__.MyClass'>


# Dynamically creating a new class using type()
Person = type("Person", (object,), {"greet": lambda self: "Hello!"})
person_instance = Person()
print(person_instance.greet())  # Output: Hello!
