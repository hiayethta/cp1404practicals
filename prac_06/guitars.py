"""
CP1404 Practical -
Program that stores user's guitars and prints their details

Estimated Completion: 40 minutes
Actual:
"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    name = input("Name: ")

    guitars = []
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar_entry = Guitar(name, year, cost)
        guitars.append(new_guitar_entry)

        name = input("Name: ")
    else:
        None


main()
