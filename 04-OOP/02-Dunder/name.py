# `__name__` variable is automatically set when the python script is executed.
# it's value depends on how file is executed
# - if a file is executed directly then it's value is set to `__main__`
# - if a file is imported as module then it's value is set to be `<filename>`

# The main use case is to differentiate between script execution and module import.

# use case
def area(radius: int) -> float:
    "Calculate area of a circle with given radius"

    return 3.14 * radius ** 2

def main():
    radius: int = int(input("Enter radius of circle: "))
    print(f"Area of circle with radius {radius} is {area(radius):.2f} sq unit.")

if __name__ == "__main__":
    main()


# Introspection: Another usecase is to dynamically insepct class name
class Demo:
    pass

print(Demo.__name__)  # Output: Demo

# Do note that in the context of class: `__name__` is the special attribut of class itself rather than it's namespace or properties. 
# As a result it is not included in class dictionary `__dir__` & output of `dir()`

# print(Demo.dir())  # `__name__` is not listed but do exists.