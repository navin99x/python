# Python by default uses `__dict__` to manage instance attribute which consueme more memory.
# `__dict__` allow to add more attributes to the instance during runtime.
# where as, `__slots__` uses tuple, uses less memory & prevent adding more attributes during runtime.

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
    
def main():
    point = Point2D(10, 20)

    print(point)  # Output: Point2D(10, 20)
    
    # adding attributes during run time
    # point.z = 5  # AttributeError

    print(point.__slots__)  # Output: ('x', 'y')
    # print(point.__dict__)  # AttributeError
    

if __name__ == "__main__":
    main()