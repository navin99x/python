# create or convert objects into lists

empty_list = list()
print("Empty list:", empty_list)  # Output: Empty list: []

tuple_data = (1, 2, 3)
list_from_tuple = list(tuple_data)
print("List from tuple:", list_from_tuple)  # Output: List from tuple: [1, 2, 3]

# Real-world example: Splitting a sentence into words
sentence = "Python is amazing!"
words = list(sentence.split())
print("Words in sentence:", words)  # Output: Words in sentence: ['Python', 'is', 'amazing!']