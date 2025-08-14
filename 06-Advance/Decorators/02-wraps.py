"""
When decorating a funciton, 
you will loose original function signature & documentation.
To fix this, we can use functools.wraps decorator
to preserver original function metadata (name, documentation.)
"""

from functools import wraps

def unit_converter(func):
    """Decorator to convert result from km to m."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wraps original function to apply unit conversion."""
        result = func(*args, **kwargs)
        return result * 1000
    
    return wrapper

@unit_converter
def calculate_distance(speed: float | int, time: float | int) -> float:
    """
    Calculates distance covered based on given speed and time taken

    Args:
        speed (float|int): speed int km/hr
        time (float|int) : time taken in hours

    Returns:
        float: distance travelled in kilometers
    """

    return float(speed) * float(time)

def main():
    speed = 24  # 25 km/hr
    time = 1.5  # 1 and half hours
    distance = calculate_distance(speed, time)
    print(f"Total distance travelled: {distance:.2f}m.")

"""
    # Without using functools.wraps
    print(calculate_distance.__name__)  # Output: wrapper
    print(calculate_distance.__doc__)   # prints docstring of wrapper() function

    # Perks of using functools.wraps
    print(calculate_distance.__name__)  # Output: calculate_distance
    print(calculate_distance.__doc__)   # prints docstring of calculate_distance() function
"""

if __name__ == "__main__":
    main()