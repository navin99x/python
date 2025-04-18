# converts values to integer


print(f"Integer value of 7.9: {int(7.9)}")
# Output: Integer value of 7.9: 7  (decimal part is discarded)

print(f"String '23' converted to integer: {int("23")}")
# Output: String '23' converted to integer: 23

# 1. Base conversion: Binary to integer
binary_str = "1010"
print(f"Binary '{binary_str}' to integer: {int(binary_str, 2)}")
# Output: Binary '1010' to integer: 10

# 2. Base conversion: Hexadecimal to integer
hex_str = "1f"
print(f"Hexadecimal '{hex_str}' to integer: {int(hex_str, 16)}")
# Output: Hexadecimal '1f' to integer: 31

# 3. Base conversion: Octal to integer
octal_str = "25"
print(f"Octal '{octal_str}' to integer: {int(octal_str, 8)}")
# Output: Octal '25' to integer: 21
