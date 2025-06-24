"""
By default index is used to access subgroup in a match,
but we can also access subgroup using meaningful name.
Syntax: (?<name>pattern) or (?P<name>pattern)
"""

import re

def extract_email_parts(email_id):
    """Extract username, domain, and TLD from an email using capturing groups."""
    pattern = r"(?P<username>\w+)@(?P<domain>\w+)\.(?P<tld>\w+)"  # Not a real email validation
    match = re.match(pattern, email_id)
    # print(match.groupdict())  # Output: {'username': 'example', 'domain': 'passinbox', 'tld': 'com'}
    if match:
        return {
            "match": match,
            "username": match.group("username"),
            "domain": match.group("domain"),
            "tld": match.group("tld")
        }
    else:
        return dict.fromkeys(["match", "username", "domain", "tld"], None)

def main():
    email = "example@passinbox.com"
    result = extract_email_parts(email)
    print(f"  Username: {result['username']}")
    print(f"  Domain:   {result['domain']}")
    print(f"  TLD:      {result['tld']}")

if __name__ == "__main__":
    main()