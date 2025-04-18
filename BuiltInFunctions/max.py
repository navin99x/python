# returns the largest item in an iterable

numbers = [10, 45, 32, 99, 5]
max_number = max(numbers)
print("Largest number:", max_number)  # Output: Largest number: 99

# Using key with max function
students = [
    {"name": "Alice", "score": 85}, 
    {"name": "Bob", "score": 92}, 
    {"name": "Charlie", "score": 78}
    ]

highest_scorer = max(students, key=lambda student: student["score"])
print("Student with highest score:", highest_scorer)
# Output: Student with highest score: {'name': 'Bob', 'score': 92}
