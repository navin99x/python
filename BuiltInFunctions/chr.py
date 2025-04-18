# converts an integer into its corresponding Unicode character
# throws `ValueError` if input is out of unicode range (1,114,111)

unicode_65 = 65
print(f"Character for Unicode {unicode_65}: {chr(unicode_65)}")  # Output: A

# Using chr() for special characters
unicode_36 = 36  
unicode_9731 = 9731 
print(f"Character for Unicode {unicode_36}: {chr(unicode_36)}")  # Output: $
print(f"Character for Unicode {unicode_9731}: {chr(unicode_9731)}")  # Output: ☃

# Using chr() to generate emojis
emoji_unicode = 128512
print(f"Emoji for Unicode {emoji_unicode}: {chr(emoji_unicode)}")  # Output: 😀