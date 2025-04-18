# A tuple is an immutable sequence of elements. Once a tuple is created, its elements cannot be changed, added, or removed.

# Using parentheses
my_tuple = (1, 2, 3, 4, 5)

# Without parentheses (comma-separated values)
another_tuple = 4, 5, 6

# Single-element tuple (note the trailing comma)
single_element = (42,)

# Using the tuple() constructor
constructed_tuple = tuple([1, 2, 3])  # From a list

# methods (count, index)
print(my_tuple.count(2))  # Count occurrences of 2
print(my_tuple.index(3))  # Find index of first occurrence of 3