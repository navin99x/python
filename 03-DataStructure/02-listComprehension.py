# [expression for item in iterable if condition]
orders = [
    {"order_id": 101, "customer": "Alice", "items": 3, "total_cost": 120.5},
    {"order_id": 102, "customer": "Bob", "items": 1, "total_cost": 50.0},
    {"order_id": 103, "customer": "Charlie", "items": 5, "total_cost": 180.75},
    {"order_id": 104, "customer": "Diana", "items": 2, "total_cost": 90.0},
    {"order_id": 105, "customer": "Eve", "items": 4, "total_cost": 250.0},
]

# Using list comprehension for filtering, extracting, and formatting
high_value_orders = [
    f"Order #{order['order_id']} by {order['customer']} (${order['total_cost']:.2f})"
    for order in orders
    if order["total_cost"] > 100
]

print(high_value_orders)

# Output: 
# ['Order #101 by Alice ($120.50)', 'Order #103 by Charlie ($180.75)', 'Order #105 by Eve ($250.00)']