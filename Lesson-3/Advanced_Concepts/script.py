# This is a Try It Out - Coding Challenge

# Write a program that uses regex to validate user input. Examples:
# Check if a password meets certain criteria (e.g., minimum length, containing uppercase and lowercase letters).

import re

def validate_password(password):
    """
    Validates a password using a single regex pattern.

    Criteria:
    - At least 8 characters long
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character (@, $, !, %, *, ?, &)
    """
    # Regex pattern breakdown:
    # ^               - Start of string
    # (?=.*[a-z])     - Positive lookahead: must contain a lowercase letter
    # (?=.*[A-Z])     - Positive lookahead: must contain an uppercase letter
    # (?=.*\d)        - Positive lookahead: must contain a digit (0-9)
    # (?=.*[@$!%*?&]) - Positive lookahead: must contain one of these special characters
    # . {8,}           - Enforces a minimum length of 8 characters
    # $               - End of string
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

    # Use re.match to check if the complete string fits the criteria
    if re.match(pattern, password):
        return True
    return False


# Example Usage
if __name__ == "__main__":
    print("--- Password Validation System ---")
    user_input = input("Enter a password to test: ")

    if validate_password(user_input):
        print("✅ Password is valid and meets all security criteria!")
    else:
        print("❌ Invalid password.")
        print("Requirements: Minimum 8 characters, 1 uppercase, 1 lowercase, 1 number, and 1 symbol (@$!%*?&).")
