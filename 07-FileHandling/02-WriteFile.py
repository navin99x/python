"""
Guide: Writing data to a file in Python
"""

# Using write() to overwrite or create a file
with open("demo.txt", "w") as f:
    f.write("Hello world\nHow are you?\n")


# Using writelines() to append multiple lines
lines_to_add = ["Hello Nepal\n", "This is Navin\n"]

with open("demo.txt", "a") as f:
    f.writelines(lines_to_add)
