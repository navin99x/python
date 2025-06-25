"""
Syntax: (?<!Y)X
-> Match X if it doesn't precede Y
"""

import re

def main():
    text = "1 mouse costs $10"
    pattern = r"(?<!\$)\d+"
    match = re.search(pattern, text)
    if match:
        print(f"Quantity: {match.group()}")

if __name__ == "__main__":
    main()