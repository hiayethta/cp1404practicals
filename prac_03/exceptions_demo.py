"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    This will error will occur when the input is not an integer. I.e. '.5', '!', 'a'
2. When will a ZeroDivisionError occur?
    This error will occur when the denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes. Set a default denominator value when this error occurs.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    denominator = 2  # set denominator to default value
print("Finished.")
