#  returns the unique memory address of an object

x = 42
y = 42
print(f"id of x: {id(x)}")
print(f"id of y: {id(y)}")  
# Output: Both have the same id due to integer caching in Python

lst = [1, 2, 3]
print(f"Original list id: {id(lst)}")
lst.append(4)
print(f"Modified list id: {id(lst)}")  
# Output: Same id (Lists are mutable, so the object remains the same)