# sorts elements of an iterable

numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)  
# Output: Sorted numbers: [1, 2, 5, 7, 9]

sorted_numbers_desc = sorted(numbers, reverse=True)
print("Numbers in descending order:", sorted_numbers_desc)  
# Output: Numbers in descending order: [9, 7, 5, 2, 1]

# Using key parameter for sorting
words = ["apple", "banana", "fig"]
sorted_by_length = sorted(words, key=len)
print("Sorted by length:", sorted_by_length)  
# Output: Sorted by length: ['fig', 'apple', 'banana']

# Sorting tuples with key (e.g., by second element)
pairs = [(1, 2), (3, 1), (5, 4)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted pairs by second element:", sorted_pairs)
# Output: Sorted pairs by second element: [(3, 1), (1, 2), (5, 4)]
