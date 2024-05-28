"""
CP1404 - Practical
Shop calculator program
Allows users to enter number of items with each price
Program checks if discount is valid, and prints total
"""

price_total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    price_total += price
if price_total > 100:
    price_total = price_total * 0.9  # apply 10% discount

print(f"Total price for {number_of_items} items is ${price_total:.2f}")
