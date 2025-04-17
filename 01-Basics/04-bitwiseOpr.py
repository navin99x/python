# Demonstrating all bitwise operators in Python

a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
print("a & b =", a & b)  # 1010 & 0100 = 0000 (0)

# Bitwise OR
print("a | b =", a | b)  # 1010 | 0100 = 1110 (14)

# Bitwise XOR
print("a ^ b =", a ^ b)  # 1010 ^ 0100 = 1110 (14)

# Bitwise NOT
print("~a =", ~a)        # ~1010 = -(1010 + 1) = -11

# Left Shift (adds 0 to right effectively multiplying by 2)
print("a << 1 =", a << 1)  # 1010 << 1 = 10100 (20)

# Right Shift (removes rightmost bit & fill leftmost bit based on sign, effectively dividing by 2)
print("a >> 1 =", a >> 1)  # 1010 >> 1 = 0101 (5)