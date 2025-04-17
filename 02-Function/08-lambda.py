students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 91}
]

# Sort by score
sorted_students = sorted(students, key=lambda student: student["score"])
print(sorted_students)

# Output: [{'name': 'Bob', 'score': 72}, {'name': 'Alice', 'score': 85}, {'name': 'Charlie', 'score': 91}]