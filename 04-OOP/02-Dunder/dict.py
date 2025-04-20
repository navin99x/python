# `__dict__` stores the attributes that are explicitlly assigned to instance/class in the form of dictionary

class Demo:
    "Demo Class"
    default = 100

    def __init__(self):
        self.value = 5

    def fn():
        pass


obj = Demo()

print(Demo.__dict__)
# Output:
# {'__module__': '__main__', '__firstlineno__': 3, '__doc__': 'Demo Class', 'default': 100, '__init__': <function Demo.__init__ at 0x00000176192A8180>, 'fn': <function Demo.fn at 0x00000176192A80E0>, '__static_attributes__': ('value',), '__dict__': <attribute '__dict__' of 'Demo' objects>, '__weakref__': <attribute '__weakref__' of 'Demo' objects>}
print(obj.__dict__)  # Output: {'value': 5}