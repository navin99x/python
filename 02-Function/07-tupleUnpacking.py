def display_info(first_name, last_name, age):
    print(f"{first_name} {last_name} is {age} years old.")

user_data = ("John", "Doe", 25)

# Unpacking the tuple into function arguments
display_info(*user_data)

# Output: John Doe is 25 years old.