"""
Generator Expression are the expression similar to list comprehension but it returns generator object.
That means it can only be used once.
"""

even_nums = (n for n in range(2, 11, 2))
print(list(even_nums))

try:
    vals = list(even_nums)
    if vals:
        print(vals)
    else:
        raise StopIteration("Genrator object is already used.")
except StopIteration as e:
    print(e)