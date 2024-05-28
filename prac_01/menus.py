"""
CP1404 - Practical
Program for basic menu according to pseudocode:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""


MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter your name: ")
print(MENU_STRING)
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello " + name)
    if choice == 'G':
        print("Goodbye " + name)
    else:
        print("Invalid choice")
    print(MENU_STRING)
    choice = input(">>> ").upper()
print("Finished.")
