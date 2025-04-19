class Product:
    discount = 0.15  # class attribute

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calcuate_final_price(self):
        return f"The final price for {self.name} is {self.price * self.discount}"

obj1 = Product("apple", 300)
obj2 = Product("mango", 300)

print(obj1.calcuate_final_price())

# custom discount from mango of 30%
obj2.discount = 0.3
print(obj2.calcuate_final_price())

# Explanation:
# Python stores instance variables in the __dict__ attribute of the instance.
# Python finds the variable in the __dict__ attribute of the instance. If it cannot find the variable, it goes up and look it up in the __dict__ attribute of the class.

# Use case of class method:
# - default value
# - Tracking objects
# - class constant