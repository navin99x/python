import re

def show_word_boundary_matches(text, word):
    print(f"\nText: {text}\nWord/Phrase: '{word}'\n")
    patterns = {
        r"\\b{w}": f"\\b{word}",
        r"{w}\\b": f"{word}\\b",
        r"\\b{w}\\b": f"\\b{word}\\b",
        r"\\B{w}": f"\\B{word}",
        r"{w}\\B": f"{word}\\B",
        r"\\B{w}\\B": f"\\B{word}\\B",
    }
    for desc, pattern in patterns.items():
        print(f"Pattern: r'{pattern}'")
        matches = list(re.finditer(pattern, text))
        if matches:
            for match in matches:
                print(f"  Match: '{match.group()}' at {match.span()}")
        else:
            print("  No matches found.")
        print()

def main():
    """Demonstrate word boundary scenarios with different words and texts"""
    examples = [
        ("The cat sat on the mat, but not in the wildcat.", "cat"),
        ("He is a superman, not just a man.", "man"),
    ]
    for text, word in examples:
        show_word_boundary_matches(text, word)

if __name__ == "__main__":
    main()