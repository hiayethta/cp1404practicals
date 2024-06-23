"""
Word Occurrences
Program to count the occurrences of each word in a string.
Estimate: 20 minutes
Actual:   32 minutes
"""

PUNCTUATION_MARKS = ".,;:'!?-"

# def main():
#     string = input("Text: ")
#     word_counts = count_words(string)
#     count_words(word_counts)
#
#
# def format_output(word_counts):
#     max_word_length = max(len(word) for word in word_counts.keys())
#     for word in sorted(word_counts.key()):
#         print(f"{word:{max_word_length}} : {word_counts[word]}")
#
#
# def count_words(string):
#     string = string.lower()
#     words = string.split()
#     word_count = {}
#     for word in words:
#         word = word.strip(PUNCTUATION_MARKS)
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#
#     return word_count
#
#
# main()

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
