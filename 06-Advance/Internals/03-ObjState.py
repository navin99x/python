"""
Mutable vs Immutable Objects in Python

- Mutable: The internal state of the object can be changed.
  Examples: list, set, dictionary
- Immutable: The internal state of the object cannot be changed.
  Examples: int, float, bool, string, tuple, frozenset

If you try to modify an immutable object, a new object is created and the reference is updated.
For mutable objects, the original object is changed in place.
"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]

# 't' is an immutable tuple, but it contains references to mutable lists l1 and l2.
t = (l1, l2)
print("Original tuple:", t)

# You cannot modify the tuple structure itself,
# but you can modify the mutable objects inside it.
l2.append(7)
print("After modifying l2:", t)
