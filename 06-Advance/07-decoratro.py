"""
A decorator is a function:
- That takes another function as an argument.
- Returns a closure
- The closure then accepts arguments.
- Then it calls original function using its own arguments.
"""

# def final_price(price, discount):
#     return price - price * discount

# def currency(fn):   # decorator function
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f"Rs. {result}"

#     return wrapper

# calclate_price = currency(final_price)
# print(calclate_price(100, 0.2))


# More pythonic way

def currency(fn):   # decorator funciton
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"Rs. {result}"
    return wrapper

@currency
def final_price(price, discount):
    return price - price * discount


print(final_price(100, 0.2))