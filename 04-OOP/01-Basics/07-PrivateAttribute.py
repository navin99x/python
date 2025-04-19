# Python doesn't have any concept of private attribute
# But by convention we can make a attribute private by either:
# - prefexing attribute name with `_` like: _name, _age
# - prefexing attribute name with `__` like: __name, __age (Name Mangling)

class Counter:
    def __init__(self):
        self.__counter = 0

    def increment(self):
        self.__counter += 1

    def decrement(self):
        self.__counter -= 1

    def reset(self):
        self.__counter = 0


counter = Counter()

counter.increment()
counter.increment()
counter.increment()

# print(counter.__counter)  # Output:  AttributeError
print(counter._Counter__counter)  # Note: (Demonstration only) 
# It is not considered good practice to access private attribute in this way.

# In Python, any attribute prefixed with `__` (double underscores) undergoes name mangling.
# This means the attribute `__counter`` in above class is internally renamed to `_Counter__counter`.
