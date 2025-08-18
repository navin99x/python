# round(number, ndigits)

# positive ndigits rounds floating-point number to a specified number of decimal places

print(round(2.888, 2))  # 2.89
print(round(2.71823, 3))  # 2.718

# zero ndigits rounds to nearest integer

print(round(2.7, 0))  # 3
print(round(4.3))  # 4 (defaultw)

# negative ndigit round to power of 10

print(round(17, -1))  # 20 (nearest 10)
print(round(243, -2))  # 200 (nearest 200)

# banker's rounding ( if a number is halfway betn two integer, python rounds to the nearest even number.)

print(round(2.5)) # 2
print(round(3.5)) # 4
