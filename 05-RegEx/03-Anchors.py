"""
Anchors are used to match to the specific position within the string.
It includes: 

^   -> Beginning of the string
$   -> End of the string
\b -> Word boundary
\\B -> Non-Word boudary
"""

import re

def main():
    """Anchors Example"""
    text = "The quick brown fox jumps over the lazy dog. The dog barks loudly at the fox"

    # Using `^` Anchor
    matches = re.finditer(r"^The", text)
    for match in matches:
        print(f"Matches to '{match.group()}', at the range of {match.span()}")

    # Using `$` Anchor
    matches = re.finditer(r"fox$", text)
    for match in matches:
        print(f"Matched at '{match.group()}', at the range of {match.span()}")

if __name__ == "__main__":
    main()