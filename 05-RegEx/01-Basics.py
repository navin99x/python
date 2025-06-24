"""
Basic usage of Python's re (regular expression) module.
Demonstrates common functions and match object methods.
"""

import re

# Common re module functions:
# re.compile(pattern)         -> Compiles a regex pattern into a Pattern object
# re.search(pattern, string) -> Searches for the first occurrence of pattern in string
# re.match(pattern, string)  -> Checks for a match only at the beginning of string
# re.fullmatch(pattern, string) -> Checks if the whole string matches the pattern
# re.findall(pattern, string) -> Returns all non-overlapping matches as a list
# re.finditer(pattern, string)  -> Returns iterator that yeilds Match object
# re.split(pattern, string)  -> Splits string by the occurrences of pattern

# Match object methods:
# group()  -> Returns the matched string
# start()  -> Returns the start index of the match
# end()    -> Returns the end index of the match
# span()   -> Returns a tuple (start, end) of the match


def main():
    """Example usage of re.search and match object methods."""
    text = "Python 3.10 was released on October 04, 2021."
    pattern = r"\d{4}"  # Matches the first sequence of 4 digits
    match = re.search(pattern, text)
    print(f"Type of match object: {type(match)}")
    if match:
        print(f"Matched string: {match.group()}")
        print(f"Start index: {match.start()}")
        print(f"End index: {match.end()}")
        print(f"Span: {match.span()}")
    else:
        print("No match found.")


if __name__ == "__main__":
    main()