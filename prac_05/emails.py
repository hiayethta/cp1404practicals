"""
CP1404/CP5632 Practical
Store user emails and names in dictionary
Extract name from email
"""


def main():
    """Ask user for email and name and store into dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if name_confirmation != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")  # Print every name w/ corresponding email


def extract_name_from_email(email):
    """Extract name from email."""
    full_name = email.split("@")[-0]
    parts = full_name.split('.')
    name = " ".join(parts).title()  # Join first and last name w/ first letter as uppercase
    return name


main()
