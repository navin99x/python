"""
RegEx Quantifiers:

`*`, {0,}    -> 0 or more 
`+`, {1, }   -> 1 or more
`?`, {0, 1}  -> 0 or 1
{n}          -> excatly `n`
{m, n}       -> betn `m` and `n` (inclusive)
{m, }        -> `m` or more
{0, n}       -> atmax `n`
"""

import re

def main():
    """regex quantifier examples:"""
    text = "It is exactly 11:20 am."
    matches = re.finditer(r"\d{2}:\d{2}", text)

    for match in matches:
        print(match)

if __name__ == "__main__":
    main()