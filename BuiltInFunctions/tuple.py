# create or convert objects into tuples

empty_tuple = tuple()
print("Empty tuple:", empty_tuple)  # Output: Empty tuple: ()

list_data = [1, 2, 3]
tuple_from_list = tuple(list_data)
print("tuple from list:", tuple_from_list)  # Output: tuple from tuple: (1, 2, 3)

# Real-world example: Splitting a sentence into words
sentence = "Python is amazing!"
words = tuple(sentence.split())
print("Words in sentence:", words)  # Output: Words in sentence: ('Python', 'is', 'amazing!')