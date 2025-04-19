class Person:
    """
    Represents Person with name and age
    """
    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a Person object
        
        Parameters:
            name(str): Name of the person
            age(int): Age of the person
        """
        self.name = name
        self.age = age

    def eligiblity(self) -> bool:
        "Check if person is eligible to vote."

        return self.age >= 18

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    person = Person(name, age)
    print("You can vote" if person.eligiblity() else "You can't vote")

if __name__ == "__main__":
    main()
