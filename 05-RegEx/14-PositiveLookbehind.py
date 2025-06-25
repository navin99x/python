"""
Syntax: (?<=Y)X
-> Matches X only if it precedes Y.
"""

import re

def main():
    """Extract dollar amounts from text"""
    text = "Your total bill amount is $40."
    pattern = r"(?<=\$)\d+(?:\.\d+)?"
    match = re.search(pattern, text)
    if match:
        print(f"$ Amount: {match.group()}")

if __name__ == "__main__":
    main()