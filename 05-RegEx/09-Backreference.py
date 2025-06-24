"""
Syntax: \\N or \\g<N>

Usages:
- Matching repeating word or phrase
- Validating data formats (HTML tags).
- Replacing repeated characters or patterns.
"""

import re

def main():
    text = "'that is too big'. she said"
    pattern = r"(['\"])(.*?)\1"
    match = re.match(pattern, text)
    print(match)

if __name__ == "__main__":
    main()
