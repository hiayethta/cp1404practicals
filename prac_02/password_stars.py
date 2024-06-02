"""
CP1404 Practical
Get password with minimum length and display correlating number of stars
"""

MINIMUM_LENGTH = 4


def main():
    """Get password and print using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, must satisfy minimum length."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))


main()
