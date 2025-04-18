# performs string interpolation, alignment, padding, precision and supports complex data types.
# Better alternative: `fstring`

name = "Alice"
age = 30
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)
# Output: My name is Alice and I am 30 years old.

# 1. Positional and keyword arguments
positional = "Hello {0}, welcome to {1}!".format("Bob", "Python")
keyword = "Hello {name}, welcome to {language}!".format(name="Charlie", language="Python")
print(positional)  # Hello Bob, welcome to Python!
print(keyword)  # Hello Charlie, welcome to Python!

# 2. Aligning text (left, right, and center alignment)
left = "{:<10}".format("Hello")  # Left-align
right = "{:>10}".format("Hello")  # Right-align
center = "{:^10}".format("Hello")  # Center-align

print(f"Left: {left}")  # Left: Hello     
print(f"Right: {right}")  # Right:      Hello
print(f"Center: {center}")  # Center:   Hello   

# 3. Formatting numbers (precision and padding)
num = 123.45678
formatted = "{:.2f}".format(num)  # Limit to 2 decimal places
padded = "{:08.2f}".format(num)  # Pad with zeroes to make it 8 characters long
print(f"Formatted: {formatted}")  # Formatted: 123.46
print(f"Padded: {padded}")  # Padded: 00123.46

# 4. Formatting percentages
percentage = 0.4567
print("Percentage: {:.2%}".format(percentage))
# Output: Percentage: 45.67%

# 5. Using format() with dictionaries and unpacking
user = {"name": "Eve", "age": 25}
print("Name: {name}, Age: {age}".format(**user))
# Output: Name: Eve, Age: 25

# 6. Formatting large numbers with commas
big_num = 1234567890
print("With commas: {:,}".format(big_num))
# Output: With commas: 1,234,567,890
