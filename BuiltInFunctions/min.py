# returns the smallest item in an iterable

numbers = [10, 45, 32, 99, 5]
min_number = min(numbers)
print("Smallest number:", min_number)  # Output: Largest number: 5

# Using key with min function
students = [
    {"name": "Alice", "score": 85}, 
    {"name": "Bob", "score": 92}, 
    {"name": "Charlie", "score": 78}
    ]

smallest_scorer = min(students, key=lambda student: student["score"])
print("Student with lowest score:", smallest_scorer)
# Output: Student with lowest score: {'name': 'Charlie', 'score': 78}
