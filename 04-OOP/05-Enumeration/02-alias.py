# If you have multiple enum member sharing same value then python doesn't create new member but instead create an alias of existing member.

from enum import Enum

class Status(Enum):
    PASS = 1  # main member
    JUST_PASS = 1  # alias member
    FAIL = 0  # main member

print(Status.PASS is Status.JUST_PASS)  # Output: True
print(Status.PASS is Status.FAIL)  # Output: False

print(Status(1))  # Output: Student.Pass