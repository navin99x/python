# create a new dictionary

empty_dict = dict()
print("Empty dictionary:", empty_dict)  # Output: Empty dictionary: {}

# 1. Converting a list of tuples into a dictionary
tuple_list = [("name", "Alice"), ("age", 30), ("city", "Paris")]
converted_dict = dict(tuple_list)
print("Dictionary from list of tuples:", converted_dict)
# Output: {'name': 'Alice', 'age': 30, 'city': 'Paris'}

# 2. Creating a dictionary with keyword arguments
keyword_dict = dict(name="Bob", age=25, city="London")
print("Dictionary with keyword arguments:", keyword_dict)
# Output: {'name': 'Bob', 'age': 25, 'city': 'London'}

# 3. Using a dictionary comprehension with dict()
squares = dict((x, x**2) for x in range(1, 6))
print("Dictionary with squares:", squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 4. Using dict() to copy another dictionary
original_dict = {"a": 1, "b": 2}
copied_dict = dict(original_dict)  # Shallow copy
print("Copied dictionary:", copied_dict)
# Output: {'a': 1, 'b': 2}

# 5. Creating a dictionary from zip() function
keys = ["name", "age", "country"]
values = ["Eve", 28, "Germany"]
zipped_dict = dict(zip(keys, values))
print("Dictionary from zip:", zipped_dict)
# Output: {'name': 'Eve', 'age': 28, 'country': 'Germany'}
