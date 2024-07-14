"""
Word Occurrences
Program to count the occurrences of each word in a string.
Estimate: 20 minutes
Actual:   29 minutes
"""

PUNCTUATION_MARKS = ".,;:'!?-"

string = input("Text: ")
string = string.lower()
words = string.split()
word_count = {}
for word in words:
    word = word.strip(PUNCTUATION_MARKS)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
max_word_length = max(len(word) for word in word_count.keys())
for word in sorted(word_count.keys()):
    print(f"{word:{max_word_length}} : {word_count[word]}")
