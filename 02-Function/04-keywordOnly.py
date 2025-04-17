# To enforce keyword-only arguments place arguments after the * separator in the function definition


def greet(*, name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet(name="Alice"))  # Works
print(greet(name="Bob", greeting="Hi"))  # Works
print(greet("Charlie"))  # TypeError: missing keyword argument