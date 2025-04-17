# Identity Operators in Python: `is` and `is not`

# Identity operators are used to compare the memory locations of two objects.
# They check whether two variables point to the same object in memory.

# Example 1: Using `is`
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False

# Example 2: Using `is not`
x = 10
y = 20
z = 10

print(x is not y)  # True
print(x is not z)  # False

# Example 3: Identity with immutable objects
# Small integers and strings are cached by Python for optimization
str1 = "hello"
str2 = "hello"
str3 = "".join(["he", "llo"])  # Creates a new string object

print(str1 is str2)  # True, because Python caches the string "hello"
print(str1 is str3)  # False, because `str3` is a new object

# Example 4: Identity with mutable objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 is list2)  # False, because lists are mutable and stored in different memory locations
print(list1 == list2)  # True, because the contents of the lists are the same

# Key Takeaways:
# - `is` checks if two variables point to the same object in memory.
# - `is not` checks if two variables point to different objects in memory.
# - Use `==` to compare the values of objects, not their identities.