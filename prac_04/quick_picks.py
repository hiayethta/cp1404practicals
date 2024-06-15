"""
CP1404 Practical
Quick pick lottery ticket generator program
Generate number of line (picked by user) with 6 random numbers
(Numbers between 1 and 45)
"""
import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

"""Print line with 6 random numbers based on user input"""
number_of_picks = int(input("How many quick picks? "))
while number_of_picks < 0:
    print("Invalid input.")
    number_of_picks = int(input("How many quick picks? "))

"""Generate 6 random numbers between min and max values"""
for i in range(number_of_picks):
    quick_picks = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_picks:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_picks.append(number)
    print(" ".join(f"{number:2}" for number in quick_picks))  # lines 23-25 are copied from solution
