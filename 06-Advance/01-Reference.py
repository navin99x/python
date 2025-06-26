"""
A variable in Python is a label that refers to an object in memory.
When you assign a variable to another, both refer to the same object (and memory address).
If you reassign one variable, it points to a new object, and the memory address changes.
"""

val: int = 20
print(f"val: {val}, id: {hex(id(val))}")  # val: 20, id: 0xb35c08

# Reference count of 20 = 1

tmp: int = val
print(f"tmp: {tmp}, id: {hex(id(tmp))}")  # tmp: 20, id: 0xb35c08

# Reference count of 20 = 2

"""
At this point, both 'val' and 'tmp' refer to the same integer object (20).
Changing 'tmp' to a new value creates a new object in memory for 'tmp'.
"""

tmp = 40
print(f"tmp: {tmp}, id: {hex(id(tmp))}")  # tmp: 40, id: 0xb35e88

# Reference count of 20 = 1
# Reference count of 40 = 1

"""
Now, 'tmp' refers to a new integer object (40), while 'val' still refers to 20.
Assigning another new value to 'tmp' again changes its reference.
"""

tmp = 60
print(f"tmp: {tmp}, id: {hex(id(tmp))}")  # tmp: 60, id: 0xb36108

# Reference count of 20 = 1
# Reference count of 40 = 0 (i.e., Obj is destroyed)
# Reference count of 60 = 1


"""
Summary:
- Variables are references to objects in memory.
- Assigning one variable to another copies the reference, not the object.
- Reassigning a variable points it to a new object, changing its memory address.
"""