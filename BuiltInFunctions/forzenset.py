# creates an immutable set

regular_set = {1, 2, 3}
immutable_set = frozenset(regular_set)
print("Immutable frozenset:", immutable_set)
# Output: Immutable frozenset: frozenset({1, 2, 3})

# 1. Attempting to modify a frozenset (raises an error)
try:
    immutable_set.add(4)  # Error: frozensets cannot be modified
except AttributeError as e:
    print(f"Error: {e}")
# Output: Error: 'frozenset' object has no attribute 'add'

# 2. Set operations with frozenset
other_set = {3, 4, 5}
union = immutable_set | other_set  # Output: {1, 2, 3, 4, 5}
intersection = immutable_set & other_set  # Output: {3}
difference = immutable_set - other_set  # Output: {1, 2}
