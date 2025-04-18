# filter elements from an iterable (like a list, tuple, or set) based on a condition specified by a function

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print("Odd numbers:", list(odd_numbers))
# Output: [1, 3, 5]

# 1. Filtering a list of strings
names = ["Alice", "Bob", "", "Charlie", "Dave", None]
non_empty_names = filter(lambda name: bool(name) and name.strip(), names)
print("Non-empty names:", list(non_empty_names))
# Output: ['Alice', 'Bob', 'Charlie', 'Dave']

# 2. Filtering a dictionary (by its keys or values)
students = {"Alice": 85, "Bob": 65, "Charlie": 90, "Dave": 40}
passed_students = filter(lambda student: students[student] >= 70, students)
print("Students who passed:", list(passed_students))
# Output: ['Alice', 'Charlie']
