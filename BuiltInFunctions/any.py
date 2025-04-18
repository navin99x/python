# If at least one value evaluates to True, it returns True; otherwise, it returns False.

numbers = [0, 0, 3, 0]
print(any(numbers))  # Output: True (3 is truthy)

false_list = [0, None, False, ""]
print(any(false_list))  # Output: False (No truthy value)

# Using any() for validation checks
responses = ["", "No", "Yes", ""]
valid_response = any(res.lower() == "yes" for res in responses)
print(f"Was there a 'Yes' response? {valid_response}")  # Output: True

# Checking dictionary values (only checks values, not keys)
grades = {"Alice": 0, "Bob": 85, "Charlie": 0}
print(any(grades.values()))  # Output: True (85 is truthy)


# Using any() with custom validation function
def has_discount(prices):
    return any(price < 50 for price in prices)

product_prices = [60, 75, 40, 90]
print(f"Does any product have a discount? {has_discount(product_prices)}")  # Output: True (40 < 50)
