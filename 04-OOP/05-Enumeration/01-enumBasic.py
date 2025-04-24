# Enumerations are immutable

from enum import Enum

class Status(Enum):
    COMPLETE = 1
    INCOMPLETE = 0

print(type(Status.COMPLETE))  # Output: <enum 'Status'>
print(isinstance(Status.COMPLETE, Status))  # Output: True

print(Status.COMPLETE.name)  # Output: COMPLETE
print(Status.COMPLETE.value)  # Output: 1

print(Status["COMPLETE"] == Status(1))  # They both returns same member i.e. Status.COMPLETE
