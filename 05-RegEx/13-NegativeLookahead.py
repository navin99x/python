"""
Syntax: X(?!Y)
-> Match X only if it is not followed by Y.
"""

import re

def filter_email(emails: list) -> list:
    "Returns emails other than noreply ones"
    pattern = r"^(?!noreply).*@"
    return [email for email in emails if re.match(pattern, email)]

def main():
    emails = ["noreply@example.com", "hello@example.com", "noreply2@example.com", "world@example.com"]
    filtered_emails = filter_email(emails)
    print(filtered_emails)

if __name__ == "__main__":
    main()