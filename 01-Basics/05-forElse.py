def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, stop checking
            break
    else:
        return True  # No divisors found

print(is_prime(17))  # Output: True
print(is_prime(18))  # Output: False