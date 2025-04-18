# add a counter to an iterable, making it easy to keep track of the indices while iterating over items in the iterable. 

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# 1. Using a custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry

# 2. Converting enumerate object to a list
enumerate_list = list(enumerate(fruits))
print("Enumerate as list:", enumerate_list)
# Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
