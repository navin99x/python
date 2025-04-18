#  creates an iterator object from an iterable

my_list = [1, 2, 3, 4]
iterator = iter(my_list)  # Create an iterator
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
# Use for loop for iteration

# 1. Custom objects with iter()
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

counter = Counter(1, 5)
for count in counter:
    print(count)
# Output:
# 1
# 2
# 3
# 4