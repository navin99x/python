#  converts an integer into its binary representation, returning a string prefixed with 0b to indicate it's a binary number.

num = 10
print(f"Binary representation of {num}: {bin(num)}")  # Output: 0b1010

negative_num = -10
print(f"Binary representation of {negative_num}: {bin(negative_num)}")  # Output: -0b1010

# Removing the '0b' prefix using slicing
binary_str = bin(10)
print(f"Binary without prefix: {binary_str[2:]}")  # Output: 1010
