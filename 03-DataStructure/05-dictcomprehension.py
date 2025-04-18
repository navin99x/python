# Employee sales data
employee_sales = {
    "Alice": 150,
    "Bob": 90,
    "Charlie": 200,
    "Diana": 120,
    "Eve": 75
}

# Performance levels using dictionary comprehension
performance = {
    name: (
        "High" if sales > 130 else "Average" if 100 <= sales <= 130 else "Low"
    )
    for name, sales in employee_sales.items() if sales >= 75  # Filter sales >= 75
}

print(performance)

# Output:
# {'Alice': 'High', 'Bob': 'Low', 'Charlie': 'High', 'Diana': 'Average', 'Eve': 'Low'}