"""
Parameterized decorator is a decorator that accepts arguments.
We need this when the behaviour of decorator needs to be customized or,
parametarized at the time of calling a funciton.
"""

import functools

def permission_required(required_level):
    """
    A decorator factory that returns a decorator.
    The returned decorator checks if the current user has the required_level
    to access the decorated function.
    """
    def decorator(func):
        """
        The actual decorator that wraps the function.
        """
        @functools.wraps(func)
        def wrapper(current_user_level, *args, **kwargs):
            """
            The wrapper function that adds the permission check logic.
            """
            print(f"Checking permission for '{func.__name__}'...")
            print(f"  Required Level: {required_level}, User Level: {current_user_level}")

            if current_user_level >= required_level:
                print(f"  Permission GRANTED for {func.__name__}.")
                return func(current_user_level, *args, **kwargs) # Pass all args including user level
            else:
                print(f"  Permission DENIED for {func.__name__}.")
                raise PermissionError(
                    f"User level {current_user_level} is too low. Required level: {required_level}"
                )
        return wrapper
    return decorator # This is the key: the factory returns the decorator

# --- Example Functions with Parameterized Decorators ---

@permission_required(required_level=1)
def view_public_data(current_user_level):
    """Allows viewing data accessible to everyone (level 1)."""
    return "This is public data accessible to all users."

@permission_required(required_level=5)
def edit_standard_report(current_user_level, report_id):
    """Allows editing standard reports (level 5 needed)."""
    return f"Successfully edited standard report {report_id}."

@permission_required(required_level=10)
def delete_critical_record(current_user_level, record_id):
    """Allows deleting critical records (level 10 needed - admin only)."""
    return f"Successfully deleted critical record {record_id}."

# --- Simulate different user levels ---
if __name__ == "__main__":
    print("--- Demonstrating Decorator Factory (Permission Required) ---\n")

    # Simulate user levels
    USER_LEVEL_GUEST = 1
    USER_LEVEL_REGULAR = 5
    USER_LEVEL_ADMIN = 10

    # Test Case 1: Guest trying to view public data
    print(f"Attempting to view public data with user level {USER_LEVEL_GUEST} (Guest)...")
    try:
        data = view_public_data(USER_LEVEL_GUEST)
        print(f"Result: {data}\n")
    except PermissionError as e:
        print(f"Error: {e}\n")

    # Test Case 2: Guest trying to edit standard report (should fail)
    print(f"Attempting to edit standard report with user level {USER_LEVEL_GUEST} (Guest)...")
    try:
        edit_standard_report(USER_LEVEL_GUEST, "RPT001")
        print("Result: Report edited (should not happen)\n")
    except PermissionError as e:
        print(f"Error: {e}\n")

    # Test Case 3: Regular user trying to edit standard report (should succeed)
    print(f"Attempting to edit standard report with user level {USER_LEVEL_REGULAR} (Regular User)...")
    try:
        result = edit_standard_report(USER_LEVEL_REGULAR, "RPT002")
        print(f"Result: {result}\n")
    except PermissionError as e:
        print(f"Error: {e}\n")

    # Test Case 4: Regular user trying to delete critical record (should fail)
    print(f"Attempting to delete critical record with user level {USER_LEVEL_REGULAR} (Regular User)...")
    try:
        delete_critical_record(USER_LEVEL_REGULAR, "REC999")
        print("Result: Record deleted (should not happen)\n")
    except PermissionError as e:
        print(f"Error: {e}\n")

    # Test Case 5: Admin user trying to delete critical record (should succeed)
    print(f"Attempting to delete critical record with user level {USER_LEVEL_ADMIN} (Admin)...")
    try:
        result = delete_critical_record(USER_LEVEL_ADMIN, "REC123")
        print(f"Result: {result}\n")
    except PermissionError as e:
        print(f"Error: {e}\n")

    print("--- End Demonstration ---")