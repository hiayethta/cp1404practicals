"""
CP1404/CP5632 Practical
Store user emails and names in dictionary
Extract name from email
"""

EMAIL_TO_NAME = {}
emails = []
email = input("Email: ")
while email != "":
    name = email.split('@')[0]
    email = input("Email: ")
    print(name.title())
