class Fibonacci:
    """Generates fibonacci using iterator protcols."""

    def __init__(self, val):
        self.val = val
        self.current = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.val:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current += 1
        return result

fib_seq = Fibonacci(7)

for n in fib_seq:
    print(n)

