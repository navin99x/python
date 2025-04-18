# retrieve the next item from an iterator

my_list = [10, 20, 30]
iterator = iter(my_list)  # Convert list to iterator

print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30

# Providing a default value
iterator = iter(my_list)
print(next(iterator, "No more items"))  # Output: 10
print(next(iterator, "No more items"))  # Output: 20
print(next(iterator, "No more items"))  # Output: 30
print(next(iterator, "No more items"))  # Output: No more items
