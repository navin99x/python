# Blueprint for other classes

from abc import ABC, abstractmethod

class Instrument(ABC):

    @abstractmethod
    def play(self):
        pass

    def silence(self):  # Also works with concrete methods
        print("All instruments stopped playing.")

class Guitar(Instrument):
    def play(self):
        print("Guitar is playing.")

class Harmonia(Instrument):
    def play(self):
        print("Harmonia is playing.")

obj = Guitar()
obj.play()

# @property + @abstractmethod for read-only abstract properties