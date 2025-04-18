# converts Unicode value into its corresponding in character

char_A = 'A'
print(f"Unicode for character {char_A}: {ord(char_A)}")  # Output: 65

# Using ord() for special characters
char_dollar = '$'
char_roach = '☃'
print(f"Unicode for character {char_dollar}: {ord(char_dollar)}")  # Output: 36
print(f"Unicode for character {char_roach}: {ord(char_roach)}")  # Output: 9731

# Using ord() to translate emoji
emoji_char = "😀"
print(f"Unicode for emoji {emoji_char}: {ord(emoji_char)}")  # Output: 😀