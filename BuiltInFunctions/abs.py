# returns the absolute value of a given number

int_num = -10
print(f"Absolute value of {int_num}: {abs(int_num)}")  # Output: 10

float_num = -15.75
print(f"Absolute value of {float_num}: {abs(float_num)}")  # Output: 15.75

complex_num = complex(-3, 4)  # Represents (-3 + 4j)
print(f"Absolute value (Magnitude) of {complex_num}: {abs(complex_num)}")  # Output: 5.0

# Using abs() in mathematical calculations
def calculate_distance(x1, x2):
    return abs(x1 - x2)  # Ensures positive distance calculation
