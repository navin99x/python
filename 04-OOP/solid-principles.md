# SOLID Principles of Software Design

The SOLID principles are a set of five design principles that help developers create more maintainable, understandable, scalable, robust, modular, extensible, and flexible object-oriented software.

## Overview of the SOLID Principles

1. **Single Responsibility Principle** (SRP)
2. **Open/Closed Principle** (OCP)
3. **Liskov Substitution Principle** (LSP)
4. **Interface Segregation Principle** (ISP)
5. **Dependency Inversion Principle** (DIP)

Let's explore each principle in detail.

## 1. Single Responsibility Principle (SRP)

> **Statement:** A class should have only one reason to change, meaning it should have only one job or responsibility.

### Violating SRP Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    @classmethod
    def save(cls, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')
    Person.save(p)
```

In this example, the `Person` class performs two different tasks:
1. Managing person information
2. Handling database storage

This violates the Single Responsibility Principle.

### Following SRP Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')

    db = PersonDB()
    db.save(p)
```

Now, each class has a single responsibility:
- `Person` handles person information only
- `PersonDB` manages database operations

## 2. Open/Closed Principle (OCP)

> **Statement:** Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

This principle promotes the use of abstraction and polymorphism to enable adding new functionality without changing existing code.

### Violating OCP Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonDB:
    def save_to_server1(self, person):
        print(f'Save the {person} to the database server 1.')
    
    def save_to_server2(self, person):
        print(f"Save the {person} to the database server 2.")
```

If we need to add a new server (server 3), we would have to modify the `PersonDB` class, violating the OCP.

### Following OCP Example

```python
from abc import ABC, abstractmethod

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

class PersonDB(ABC):
    @abstractmethod
    def save(self, person):
        pass

class Server1(PersonDB):
    def save(self, person):
        print(f'Save the {person} to the database server 1.')

class Server2(PersonDB):
    def save(self, person):
        print(f'Save the {person} to the database server 2.')

class Server3(PersonDB):
    def save(self, person):
        print(f'Save the {person} to the database server 3.')
```

With this design, we can add new servers by creating new classes that extend `PersonDB` without modifying existing code.

## 3. Liskov Substitution Principle (LSP)

> **Statement:** Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

In simpler terms, subclasses should maintain the expected behavior of their parent classes.

### Violating LSP Example

```python
class Server4(PersonDB):
    def save(self, person):
        if person.name == "nigesh":  # Adding a restriction that isn't in the parent class
            raise ValueError("This name is banned!")
        print(f'Save the {person} to the database server 4.')
```

This violates LSP because `Server4` changes the expected behavior of the `save` method by introducing a validation that might cause the method to fail in cases where the parent class's method would succeed.

### Following LSP Example

There are several ways to fix this:

```python
# Option 1: Use a decorator for validation
def validate_person_name(func):
    def wrapper(self, person):
        if person.name.lower() == "nigesh":
            raise ValueError("This name is banned")
        return func(self, person)
    return wrapper

class Server4(PersonDB):
    @validate_person_name
    def save(self, person):
        print(f'Save the {person} to the database server 4.')

# Option 2: Handle validation separately
class PersonValidator:
    @staticmethod
    def validate(person):
        if person.name.lower() == "nigesh":
            raise ValueError("This name is banned")

# Then use the validator before calling save
# validator = PersonValidator()
# validator.validate(person)
# server4.save(person)
```

> **Understanding LSP:** LSP doesn't prevent adding new behaviors to child classes, but it requires that the expected behaviors of the parent class are preserved. You can introduce new methods or properties, but methods defined in the parent class should function in a way that's consistent with their intended behavior.

## 4. Interface Segregation Principle (ISP)

> **Statement:** Client should not be forced to depend on methods it does not use. This means you should split large interfaces into smaller, more specific ones.

### Violating ISP Example

Let's extend our database system to handle different types of database operations:

```python
from abc import ABC, abstractmethod

class PersonDB(ABC):
    @abstractmethod
    def save(self, person):
        pass
    
    @abstractmethod
    def delete(self, person):
        pass
    
    @abstractmethod
    def backup(self):
        pass
    
    @abstractmethod
    def restore(self):
        pass

# Regular server needs all operations
class Server1(PersonDB):
    def save(self, person):
        print(f'Save {person} to server 1')
    
    def delete(self, person):
        print(f'Delete {person} from server 1')
    
    def backup(self):
        print('Backup server 1')
    
    def restore(self):
        print('Restore server 1')

# Read-only server doesn't need save or delete
class ReadOnlyServer(PersonDB):
    def save(self, person):
        # Not applicable for read-only server
        raise NotImplementedError("Cannot save to read-only server")
    
    def delete(self, person):
        # Not applicable for read-only server
        raise NotImplementedError("Cannot delete from read-only server")
    
    def backup(self):
        print('Backup read-only server')
    
    def restore(self):
        print('Restore read-only server')
```

This violates ISP because `ReadOnlyServer` is forced to implement methods like `save` and `delete` that it doesn't need and can't use.

### Following ISP Example

Let's break down the large interface into smaller, more focused interfaces:

```python
from abc import ABC, abstractmethod

class Saveable(ABC):
    @abstractmethod
    def save(self, person):
        pass

class Deletable(ABC):
    @abstractmethod
    def delete(self, person):
        pass

class Backupable(ABC):
    @abstractmethod
    def backup(self):
        pass
    
    @abstractmethod
    def restore(self):
        pass

# Regular server implements all interfaces
class Server1(Saveable, Deletable, Backupable):
    def save(self, person):
        print(f'Save {person} to server 1')
    
    def delete(self, person):
        print(f'Delete {person} from server 1')
    
    def backup(self):
        print('Backup server 1')
    
    def restore(self):
        print('Restore server 1')

# Read-only server only implements the backup interface
class ReadOnlyServer(Backupable):
    def backup(self):
        print('Backup read-only server')
    
    def restore(self):
        print('Restore read-only server')
```

Now each server implementation only needs to implement the interfaces that are relevant to its functionality.

## 5. Dependency Inversion Principle (DIP)

> **Statement:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

### Violating DIP Example

Let's consider an application that manages person data:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

class Server1:
    def save(self, person):
        print(f'Save {person} to server 1')

class PersonManager:
    def __init__(self):
        self.server = Server1()  # Direct dependency on Server1
    
    def save_person(self, person):
        self.server.save(person)
```

Here, `PersonManager` (high-level module) directly depends on `Server1` (low-level module). If we need to switch to a different server, we'd have to modify `PersonManager`.

### Following DIP Example

```python
from abc import ABC, abstractmethod

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass

class Server1(PersonStorage):
    def save(self, person):
        print(f'Save {person} to server 1')

class Server2(PersonStorage):
    def save(self, person):
        print(f'Save {person} to server 2')

class PersonManager:
    def __init__(self, storage):
        self.storage = storage  # Depends on abstraction
    
    def save_person(self, person):
        self.storage.save(person)

# Usage
server = Server1()  # or Server2()
manager = PersonManager(server)
person = Person("John Doe")
manager.save_person(person)
```

Now both the high-level module (`PersonManager`) and the low-level modules (`Server1`, `Server2`) depend on the abstraction (`PersonStorage`). We can easily switch between different storage implementations without modifying `PersonManager`.

## Summary

The SOLID principles provide a solid foundation for creating well-designed object-oriented software:

1. **Single Responsibility Principle**: Each class should have only one reason to change.
2. **Open/Closed Principle**: Software entities should be open for extension but closed for modification.
3. **Liskov Substitution Principle**: Subclasses should be substitutable for their base classes.
4. **Interface Segregation Principle**: Many specific interfaces are better than one general interface.
5. **Dependency Inversion Principle**: Depend on abstractions, not on concrete implementations.

Following these principles leads to code that is more maintainable, flexible, and easier to understand and extend.
