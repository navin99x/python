# In Programming, method and function are two different entities.

class Demo:
    def fn(self):
        pass

demo = Demo()

print(type(Demo.fn))  # Output: <class 'function'>
print(type(demo.fn))  # Output: <class 'method'>

print(Demo.fn is demo.fn)  # Output: False

# Conclusion:
# When you define a function inside a class, it is treated as a function at the class level.
# A function becomes a method when it is accessed through an object instance.
# By default, when you call a method using an object, the reference to that object (self) is passed as the first argument. i.e, `Demo.fn(demo)` equivalent to `demo.fn()`
