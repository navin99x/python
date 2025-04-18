# converts an integer into a octal string, prefixed with "0o"

num = 10
print(f"Octal representation of {num}: {oct(num)}")  # Output: 0o12

negative_num = -10
print(f"Octal representation of {negative_num}: {oct(negative_num)}")  # Output: -0o12

# Removing the '0o' prefix using slicing
octal_str = oct(10)
print(f"Octal without prefix: {octal_str[2:]}")  # Output: 12