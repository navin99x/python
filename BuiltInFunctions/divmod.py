# performs division and modulus operations simultaneously and returns the result as a tuple.

dividend = 17
divisor = 5
result = divmod(dividend, divisor)
print(f"Quotient and remainder of {dividend} / {divisor}: {result}")
# Output: Quotient and remainder of 17 / 5: (3, 2)

# 1. Using divmod() with negative numbers
negative_dividend = -17
result_negative = divmod(negative_dividend, divisor)
print(f"Quotient and remainder of {negative_dividend} / {divisor}: {result_negative}")
# Output: (-4, 3)

# 2. Extracting quotient and remainder separately
quotient, remainder = divmod(dividend, divisor)
print(f"Quotient: {quotient}, Remainder: {remainder}")
# Output: Quotient: 3, Remainder: 2
