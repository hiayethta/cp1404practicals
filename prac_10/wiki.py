"""
CP1404/CP5632 Practical
Using the wikipedia package to create a program
that asks the user to input a phrase or title, then print its
details.

Estimated time to complete: 30 minutes
Actual:
"""
import wikipedia
from wikipedia import DisambiguationError

prompt = input("Enter a phrase or title: ")
while prompt != "":
    try:
        search_results = wikipedia.search(prompt)
        first_page_results = wikipedia.page(search_results[0])
        for results in range(1):
            print(first_page_results.summary)
            break
    except DisambiguationError:
        print("Unable to get summary. Please enter a new prompt.")
        prompt = input("Enter a phrase or title: ")
    prompt = input("Enter a phrase or title: ")
print("Program finished.")
