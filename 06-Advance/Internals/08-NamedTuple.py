from collections import namedtuple

Person = namedtuple("Person", ("name", "age", "gender"))

obj = Person("Ram Bahadur", 30, 'M')

print(isinstance(obj, tuple))  # True
print(obj.name)  # Ram Bahadur
print(obj[1])  # 30


"""
Features: immutable, named fields, memory efficient than dict or custom class.
"""

