# To make a function that only take positional argument: add , / after the parameters

def divide(x, y, /):
    return x / y

print(divide(10, 2))  # Works
print(divide(x=10, y=2))  # Raises a TypeError