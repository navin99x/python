# converts an integer into a hexadecimal string, prefixed with "0x"

num = 10
print(f"Hexadecimal representation of {num}: {hex(num)}")  # Output: 0xa

negative_num = -10
print(f"Hexadecimal representation of {negative_num}: {hex(negative_num)}")  # Output: -0xa

# Removing the '0x' prefix using slicing
hex_str = hex(10)
print(f"Hexadecimal without prefix: {hex_str[2:]}")  # Output: a