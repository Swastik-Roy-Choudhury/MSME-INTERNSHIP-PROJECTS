import re

def check_password_strength(password):
    """Checks the strength of a password based on various criteria.

    Args:
        password: The password to be checked.

    Returns:
        A string indicating the password strength (e.g., "Strong", "Medium", "Weak").
    """

    # Define regular expressions for different character types
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_number = re.search(r'\d', password)
    has_special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Calculate password strength based on criteria
    strength = 0
    if len(password) >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_number:
        strength += 1
    if has_special_char:
        strength += 1

    # Determine password strength rating
    if strength >= 4:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"

def main():
    while True:
        password = input("Enter a password: ")
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")

        if input("Would you like to check another password? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()