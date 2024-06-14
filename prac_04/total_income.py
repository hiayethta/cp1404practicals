"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Print formatted reported of monthly incomes with totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total = calculate_total(income, total)
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def calculate_total(income, total):
    """Calculate monthly income totals"""
    total += income
    return total


main()
