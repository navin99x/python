"""
Guide: Different ways to read a file in Python
"""

# Read the entire file at once
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

# Read all lines into a list
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# Read file line by line using readline()
with open("demo.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.rstrip())
        line = f.readline()

# Read file line by line using iteration
with open("demo.txt", "r") as f:
    for line in f:
        print(line.rstrip())
