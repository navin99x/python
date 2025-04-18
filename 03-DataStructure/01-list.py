values = []  # Initialize an empty list

# append
values.append(10)
values.append(20)
values.append(30)
print(values)  # Output: [10, 20, 30]

# insert
values.insert(4 , 40)
print(values)  # Output: [10, 20, 30, 40]

# extend
values.extend([50, 60])
print(values)  # Output: [10, 20, 30, 40, 50, 60]

# pop(-1)
values.pop(0)
print(values)  # Output: [20, 30, 40, 50, 60]

# remove
values.remove(60)
print(values)  # Output: [20, 30, 40, 50]

# copy
new_values = values.copy()
print(new_values)  # Output: [20, 30, 40, 50]

# sort
values.sort(reverse = True)
print(values)  # Output: [50, 40, 30, 20]

# reverse
values.reverse()
print(values)  # Output: [20, 30, 40, 50]

# count
print(values.count(20))  # Output: 1

# index
print(values.index(40))  # Output: 2

# clear
values.clear()
print(values)  # Output: []