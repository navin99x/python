"""
Demonstrates character sets in Python's re module.

Character sets:
    \\w  -> [A-Za-z0-9_]: Any alphanumeric character or underscore
    \\d  -> [0-9]: Any digit
    \\s  -> [ \t\n\r\f\v]: Any whitespace character

Inverse character sets:
    \\W  -> Not alphanumeric or underscore
    \\D  -> Not a digit
    \\S  -> Not a whitespace character

Negation in sets:
    .      -> Any character
    [^0-5] -> Any character except 0-5
"""

import re

def main():
    """Showcase character set usage with re.findall()."""
    text = "2, 3, and 7 are the first three prime numbers."
    pattern = r"\d"
    print(re.findall(pattern, text))
    
if __name__ == "__main__":
    main()
