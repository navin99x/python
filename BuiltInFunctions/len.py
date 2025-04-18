# returns number of items in object

text = "Hello, Python!"
print(f"Length of the string: {len(text)}")  # Output: Length of the string: 14

my_list = [1, 2, 3, 4, 5]
print(f"Number of items in the list: {len(my_list)}")  # Output: Number of items in the list: 5

# similarly can be used with wide variety of objects.


# Handling empty objects
empty_list = []
empty_string = ""
print(f"Length of empty list: {len(empty_list)}")  # Output: 0
print(f"Length of empty string: {len(empty_string)}")  # Output: 0

# Using len() with custom objects
class MyClass:
    def __len__(self):
        return 42

obj = MyClass()
print(f"Length of MyClass instance: {len(obj)}")  # Output: Length of MyClass instance: 42
