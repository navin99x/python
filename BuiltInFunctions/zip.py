# used to combine multiple iterables (such as lists, tuples, or sets) element by element into iterators of tuples. 

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = zip(list1, list2)
print("Zipped result:", list(result))
# Output: Zipped result: [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzipping a zipped object
zipped = zip(list1, list2)
unzipped = zip(*zipped)
list1_unzipped, list2_unzipped = map(list, unzipped)
print("Unzipped list1:", list1_unzipped)
print("Unzipped list2:", list2_unzipped)
# Output:
# Unzipped list1: [1, 2, 3]
# Unzipped list2: ['a', 'b', 'c']
