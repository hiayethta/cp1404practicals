"""
CP1404/CP5632 - Practical
Program to determine score status
"""

score = float(input("Enter score: "))
while score >= 0:
    if score < 50:
        print("Bad score")
        score = float(input("Enter score: "))
    elif score < 90:
        print("Pass")
        score = float(input("Enter score: "))
    elif score <= 100:
        print("Excellent")
        score = float(input("Enter score: "))
    else:
        print("Invalid score")
        score = float(input("Enter score: "))
else:
    print("Invalid input")
