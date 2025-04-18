# opens files for reading, writing, or modifying.

with open("demo.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Writing to a file (overwrites existing content)
with open("demo.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling in Python is powerful!")

# Appending data to a file
with open("demo.txt", "a") as file:
    file.write("\nAppending this new line.")

# Using binary mode for reading a file
with open("image.jpg", "rb") as file:
    binary_data = file.read()
    print("Binary data:", binary_data[:10])  # Show first 10 bytes

# Open file with using different encodings
with open("demo_utf8.txt", "r", encoding="utf-8") as file:
    print("UTF-8 file content:", file.read())
