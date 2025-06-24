import re

def extract_email_parts(email_id):
    """Extract username, domain, and TLD from an email using capturing groups."""
    pattern = r"(\w+)@(\w+)\.(\w+)"  # Not a real email validation
    match = re.match(pattern, email_id)
    
    if match:
        return {
            "match": match,
            "username": match.group(1),
            "domain": match.group(2),
            "tld": match.group(3)
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