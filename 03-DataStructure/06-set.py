# create empty set

my_set = set()  # my_set = {}  This is an empty dictionary not set.

my_set.add(10)
my_set.add(20)
my_set.add(30)

print(my_set)  # Output: {10, 20, 30}

# remove() removes an item & if not present raise error
# my_set.remove(90) # Output: KeyError

# discard() remove an item & if not present ignores it
my_set.discard(90)

print(my_set)  # Output: {10, 20, 30}

# pop() removes random item and returns it
print (my_set.pop())  # Output: 10
