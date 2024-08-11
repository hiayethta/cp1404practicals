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

prompt = input("Enter a phrase or title: ").strip()
while prompt != "":
    try:
        search_result_page = wikipedia.page(prompt, auto_suggest=False)
        print(f"{search_result_page.prompt}\n{search_result_page.summary}\n{search_result_page.url}\n")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f'We need a more specific title. Try one of the following, or a new search:')
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'Page id "{prompt}" does not match any pages. Try another id! .')
    prompt = input("Enter a phrase or title: ").strip()
print("Program finished.")
