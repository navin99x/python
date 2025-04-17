def calculate_average(numbers):
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    This function takes a list of numerical values and returns their average.
    If the list is empty, it raises a ValueError to prevent division by zero.

    Args:
        numbers (list of float or int): A list of numeric values.

    Returns:
        float: The arithmetic mean of the input numbers.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> calculate_average([10, 20, 30])
        20.0
        >>> calculate_average([1.5, 2.5, 3.5])
        2.5
        >>> calculate_average([])
        Traceback (most recent call last):
            ...
        ValueError: The list is empty. Cannot compute average.

    Notes:
        - This function uses simple arithmetic mean calculation.
        - It does not handle cases where the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("The list is empty. Cannot compute average.")

    return sum(numbers) / len(numbers)


print(calculate_average([10, 20, 30]))  # Output: 20.0