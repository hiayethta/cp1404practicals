"""
CP1404 Practical
Program that prompts user for 5 numbers and stores in a list
Then prints first, last, min, max, and average of numbers
"""

numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")

