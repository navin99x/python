# Using @enum.unique property to define enumeration that should have unique alias.

from enum import Enum, unique

@unique
class Response(Enum):
    SUCESS = 1
    ERROR = 0

    # NOT_OKAY = 0  # ValueError