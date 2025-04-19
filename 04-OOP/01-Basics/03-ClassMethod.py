from datetime import datetime

class Person:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def from_birth_date(cls, name: str, birth_date: str):
        """
        Factory method to create a Person instance from a birth date string.
        """
        birth_year = datetime.strptime(birth_date, "%Y-%m-%d").year
        return cls(name, birth_year)

person1 = Person("Alice", 1990)
print(f"{person1.name} was born in {person1.birth_year}.")

person2 = Person.from_birth_date("Bob", "1985-07-15")
print(f"{person2.name} was born in {person2.birth_year}.")

# Use case of class method:
# - Factory method
