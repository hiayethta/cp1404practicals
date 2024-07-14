"""
CP1404 Practical -
Program that stores user's guitars and prints their details

Estimated Completion: 40 minutes
Actual: 28~ minutes
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

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
