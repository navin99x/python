# return the Boolean value (True or False) of an object

print(bool(1))       # Output: True 
print(bool(0))       # Output: False 
print(bool(-5))      # Output: True 

print(bool("Hello")) # Output: True
print(bool(""))      # Output: False

print(bool([1, 2]))  # Output: True
print(bool([]))      # Output: False

print(bool(None))    # Output: False
print(bool(False))   # Output: False


# Evaluating custom objects
class MyClass:
    def __bool__(self):
        return True

obj = MyClass()
print(bool(obj))  # Output: True (Custom objects can override `__bool__`)

# Using bool() in real-world scenarios: input validation
user_input = ""
is_valid = bool(user_input)
if is_valid:
    print("Input is valid.")
else:
    print("Input is invalid.")  # Output: Input is invalid.
