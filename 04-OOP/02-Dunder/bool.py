# `__bool__` is used to evaluate truth value of an object.
# If `__bool__` is not defined for a custom class, 
# Python will use `__len__` if implemented, returning `False` for length 0 and `True` for non-zero length.
# If `__len__` is also not defined, object is evaluated to be `True` by default.

import time

class FileUpload:
    def __init__(self, filename: str, total_size: int):
        self.filename = filename
        self.total_size = total_size  # Total file size in bytes
        self.uploaded_size = 0  # Initial bytes uploaded

    def start_upload(self):
        """Simulate uploading a chunk every second."""
        while self.uploaded_size < self.total_size:
            time.sleep(1)
            self.uploaded_size += 1000 # Upload rate of 1Kbps

            if self.uploaded_size > self.total_size:
                self.uploaded_size = self.total_size

            print(f"Uploading... {self.uploaded_size}/{self.total_size} bytes")
        
        print("Upload complete!")

    def __bool__(self):
        """Return True if upload is complete, False otherwise."""
        return self.uploaded_size == self.total_size

    def __repr__(self):
        return (f"FileUpload(filename='{self.filename}', uploaded={self.uploaded_size}/{self.total_size})")

file = FileUpload("python.zip", total_size=10000)  # Uploading file of 10kb
print(f"Starting upload for: {file.filename}")
file.start_upload()

while not file:
    print(file)
    time.sleep(2.5)  # check every 2.5 seconds

# Use case of `__bool__`:
# - Object Validation
# - Flow Control (if...else condition check for object)