"""
By default all the quantifier works in greedy mode i.e,
try to accomodate as much match as possible.
However we can add `?` at the end to make the quantifier non-greedy.
"""

import re

def main():

    s = '<button type="submit" class="btn">Send</button>'

    # pattern = '".+"'    # Greedy mode
    pattern = '".+?"'   # Non-Greedy mode
    matches = re.finditer(pattern, s)

    for match in matches:
        print(match.group())

if __name__ == "__main__":
    main()