"""
CP1404 Practical 04, Task 1
Warm up with evaluating list expressions
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]
= [3]
numbers[-1]
= [2]
numbers[3]
= [1]
numbers[:-1]
= [2, 9, 5, 1, 4, 1, 3], incorrect
= [3, 1, 4, 1, 5, 9]
numbers[3:4]
= [1, 5]
5 in numbers
= True
7 in numbers
= False
"3" in numbers
= False
numbers + [6, 5, 3]
= .... incorrect
= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

# Change first element to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all elements except the first two
numbers[2:]

# Print whether 9 is an element of numbers
9 in numbers

print(numbers)
