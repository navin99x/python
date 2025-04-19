# It is an independent funtion defined within a class
# i.e, it is similar to regular function except it is defined inside class such that it can only be accessed by class and it's object

# Imagine a scenario where you need to validate email addresses before creating User instances. 
# Since email validation doesn't depend on instance attributes, we can define it as a static method inside the User class.

import re

class User:
    def __init__(self, name: str, email: str):
        if not self.validate_email(email):
            raise ValueError("Invalid email format")
        self.name = name
        self.email = email

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email format using regex.
        Returns True if valid, False otherwise.
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

user1 = User("Alice", "alice@example.com")
print(f"User created: {user1.name}, {user1.email}")

# Using the static method independently without creating an instance
print(User.validate_email("test@domain.com"))  # Output: True
print(User.validate_email("invalid-email"))  # Output: False  

# Use case of static method:
# - to define utility methods or group a logically related functions into a class.