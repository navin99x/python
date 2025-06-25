"""
Syntax: X(?=Y)
-> Match X if it is followed by Y.
"""

import re

def password_validation(password: str) -> bool:
    "Perform password validation"
    pattern = r"^(?=.*\d)(?=.*[A-Z]).{8,}$"
    if re.match(pattern, password):
        return True
    return False

def main():
    password = input("Enter a new password:")
    if not password_validation(password):
        raise ValueError("Password should contain at least 1 digit, 1 uppercase letter and be at least 8 characters long")
    else:
        print("You are in")

if __name__ == "__main__":
    main()
