#  returns a string representation of an object, replacing non-ASCII characters with escape sequences.

text = "Hello, café!"
print(ascii(text))  # Output: 'Hello, caf\xe9!'

# Working with emojis
emoji_text = "Python 🐍"
print(ascii(emoji_text))  # Output: 'Python \U0001f40d'

# Using ascii() on lists with Unicode elements
mixed_list = ["apple", "mango", "café", "🍕"]
print(ascii(mixed_list))  
# Output: ['apple', 'mango', 'caf\xe9', '\U0001f355']

# Using ascii() on dictionaries
data = {"name": "René", "icon": "✅"}
print(ascii(data))  
# Output: {'name': 'Ren\xe9', 'icon': '\u2705'}

# Using ascii() for debugging function outputs
def greet(name):
    return f"Hello, {name}!"

name_unicode = "Élise"
print(ascii(greet(name_unicode)))  # Output: 'Hello, \xc9lise!'
