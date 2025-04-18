# create or convert objects into set

empty_set = set()
print("Empty list:", empty_set)  # Output: Empty set: set()

tuple_data = (1, 2, 3)
set_from_tuple = set(tuple_data)
print("Set from tuple:", set_from_tuple)  # Output: Set from tuple: {1, 2, 3}

# Real-world example: Splitting a sentence into words
sentence = "Python is amazing!"
words = set(sentence.split())
print("Words in sentence:", words)  # Output: Words in sentence: {'Python', 'is', 'amazing!'}
# the order may differ in your case