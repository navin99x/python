# convert a number or string to a floating-point number (decimal). 

int_num = 5
float_num = float(int_num)
print(f"Float representation of {int_num}: {float_num}")
# Output: Float representation of 5: 5.0

# 1. Converting strings to floats
float_str = "3.14"
float_value = float(float_str)
print(f"Float value of '{float_str}': {float_value}")
# Output: Float value of '3.14': 3.14

# 2. Handling special float values
print("Positive infinity:", float("inf"))  # Output: inf
print("Negative infinity:", float("-inf"))  # Output: -inf
print("Not a Number (NaN):", float("nan"))  # Output: nan
print(float(True))  # Output: 1.0
print(float(False))  # Output: 0.0