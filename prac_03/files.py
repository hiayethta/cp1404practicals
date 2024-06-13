"""
CP1404 - Practical
File reading applications and practice
"""

"""Ask user for name and print to text file"""
FILENAME = 'name.txt'
NUMBERFILE = 'numbers.txt'

out_file = open(FILENAME, 'w')
name = input("Enter name: ").upper()
print(name, file=out_file)
out_file.close()

"""Read text file and print a formatted string"""
out_file = open(FILENAME, 'r')
for line in open(FILENAME):
    print(f"Hi {name}!")
out_file.close()

"""Read first two lines of file and add numbers"""
total = 0
in_file = open(NUMBERFILE, 'r')
for i in range(2):
    line = in_file.readline()
    number = int(line)
    total += number
print(f"Total: {total}")
out_file.close()
