# applies a specified function to each item in an iterable (like a list, tuple, or string) and returns an iterator

def square(x):
    return x**2

numbers = [1, 2, 3, 4]
cubed_numbers = map(lambda x: x**3, numbers)
print("Cubed numbers:", list(cubed_numbers))  # Output: Cubed numbers: [1, 8, 27, 64]

# Applying map() with strings
names = ["Alice", "Bob", "Charlie"]
uppercase_names = map(str.upper, names)
print("Uppercase names:", list(uppercase_names))  # Output: Uppercase names: ['ALICE', 'BOB', 'CHARLIE']

# Real-world example: Parsing data
data = ["1", "2", "3"]
parsed_data = map(int, data)
print("Parsed integers:", list(parsed_data))  # Output: Parsed integers: [1, 2, 3]
