"""
CP1404 - Practical
Practice for writing loop programs
"""

# Displays all odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars, using user input
star_number = int(input("Number of stars: "))
for i in range(star_number):
    print('*', end='')
print()

# d. Print n lines of increasing stars
for i in range(1, star_number + 1):
    print('*' * i)
print()
