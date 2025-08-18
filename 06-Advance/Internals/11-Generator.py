"""
A generator is a function that contain at least one yeild statements.
When it is called, it returns a generator obj, which is a type of iterator.
Calling next() resumes the function when it was last yielded, untill it hits `StopIteration`.   
"""

def fibonacci_generator(val):
    a, b = 0, 1

    for _ in range(val):
        yield a
        a, b = b, a + b

fib_seq = fibonacci_generator(7)

for n in fib_seq:
    print(n)