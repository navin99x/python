"""
Iterable - object that can be looped over & has `__iter__` method that returns an iterator.
Iterator - object that can produce value one at a time. It has both `__iter__` & `__next__` method implemented.
"""

list = [2, 4, 6, 8]  # list is an iterable
get_vals = iter(list)  # get_vals is an iterator

for _ in get_vals:
    pass