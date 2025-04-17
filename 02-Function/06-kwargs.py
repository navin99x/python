# allow a function to accept variable number of keyword arguemnts

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=30, city="Paris")  

# Output:
# name: Alice
# age: 30
# city: Paris