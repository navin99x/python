# slot behaviours in inheritance

# case-I. parent has `__slots__`, child doesn't
class Parent:
    __slots__ = ('x', 'y')

class Child(Parent):
    pass  # No __slots__ defined in the child class

obj = Child()
obj.x, obj.y = 10, 20  # Stored in parent's slots
obj.z = 5  # Dynamically added to __dict__ since child has no slots

print(obj.__slots__)  # Output: ('x', 'y') - Parent's slots are inherited
print(obj.__dict__)   # Output: {'z': 20} - Attributes added dynamically


# case-II. Both parent and child define `__slots__`
class Parent:
    __slots__ = ('x', 'y')

class Child(Parent):
    __slots__ = ('z',)  # Child slots add more attributes

obj = Child()
obj.x, obj.y = 10, 20  # Stored in parent's slots
obj.z = 5  # Stored in child's slots

print(obj.__slots__)  # Output: ('z',) - Child's slots are visible
print(Parent.__slots__)  # Output: ('x', 'y') - Explicitly accessing parent slots
