# If every element evaluates to True, it returns True; otherwise, it returns False

numbers = [1, 2, 3, 4, 5]
print(all(numbers))  # Output: True (all non-zero numbers)

mixed_values = [1, 0, 3, 4]
print(all(mixed_values))  # Output: False (0 is treated as False)

conditions = [True, True, False, True]
print(all(conditions))  # Output: False (False present)

# Using all() in a list comprehension for validation
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]

all_passed = all(student["score"] > 70 for student in students)
print(f"Did all students pass? {all_passed}")  # Output: True

grades = {"Alice": 85, "Bob": 0, "Charlie": 78}
print(all(grades))  # Output: False (0-treated key is False)

empty_check = all(("", "Hello", "Python"))
print(empty_check)  # Output: False ("" is False)

# Using all() with custom validation function
def is_valid_age(age):
    return age >= 18

ages = [25, 30, 21, 17]
valid_ages = all(is_valid_age(age) for age in ages)
print(f"Are all ages valid? {valid_ages}")  # Output: False (17 is invalid)