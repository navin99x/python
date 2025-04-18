#  slice object representing the set of indices specified by range

my_list = [10, 20, 30, 40, 50, 60]
s = slice(3, None)
print(my_list[s])  # Output: [40, 50, 60]


s = slice(0, 6, 2)
print(my_list[s])  # Output: [10, 30, 50]


# Reusing slice objects with multiple sequences
s = slice(1, 4)
list1 = [100, 200, 300, 400, 500]
tuple1 = ('A', 'B', 'C', 'D', 'E')

print(list1[s])  # Output: [200, 300, 400]
print(tuple1[s])  # Output: ('B', 'C', 'D')

# Alternative slicing syntax (comparison to slice())
print(my_list[1:5])  # Equivalent to slice(1, 5)
print(my_list[0:6:2])  # Equivalent to slice(0, 6, 2)