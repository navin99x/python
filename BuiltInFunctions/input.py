# used to accept user input from the keyboard

name = input("Enter your name: ")
print(f"Hello, {name}!")

# 1. Handling empty input with default values
color = input("Enter your favorite color (press Enter to skip): ") or "Unknown"
print(f"Favorite color: {color}")
# If user presses Enter, output is "Favorite color: Unknown"