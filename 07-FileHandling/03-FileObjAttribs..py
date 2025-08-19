with open("demo.txt", "r") as f:
    print("File name:", f.name)
    print("File closed?:", f.closed)
    print("File encoding:", f.encoding)
    print("File mode:", f.mode)

print("File closed after 'with' block?:", f.closed)
