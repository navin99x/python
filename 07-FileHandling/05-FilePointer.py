"""
File Pointer in Python
----------------------------
When reading or writing files, the file pointer determines **where the next read or write will happen**.
Two key methods:
1. tell() → Returns the current position of the file pointer (in bytes)
2. seek(offset, whence=0) → Moves the file pointer to a new position
"""

file_path = "demo.txt"

with open(file_path, "r") as file:
    print(f"Initial file pointer: {file.tell()}")  # Start position
    
    file.seek(5)  # Move pointer to 5th byte from beginning
    print(f"File pointer after seek(5): {file.tell()}")  # Confirm new position
    
    print("Reading from new position:", file.read(10))  # Reads 10 characters


# seek(offset, whence) → whence: 0=start, 1=current, 2=end
