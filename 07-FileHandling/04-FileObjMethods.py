with open("demo.txt",'a') as file:
    print("Is file readable?: ",file.readable())
    print("Is file writeable?: ",file.writable())
    
    # Move file pointer to byte 10
    file.seek(10)
    
    # Truncate file at current pointer
    file.truncate() 

"""
- If size is not specified or is set to None, it truncates the file at the current position. 
- If size is specified and greater than the current size, the file is padded with null bytes to the specified size.
- If size is less than the current size, it truncates the file to the specified size.
"""
