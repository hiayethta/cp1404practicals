"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    long_word = False  # Sets the default value
    if len(word) >= length:
        long_word = True
        return long_word
    else:
        return long_word


assert is_long_word("not") == False
assert is_long_word("supercalifrag") == True
assert is_long_word("Python") == True


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car()  # Default value
    assert test_car.fuel == 0


def format_phrase_to_sentence(phrase):
    """
    This will change the format of a phrase into a sentence.
    The sentence will start with a capital and end with a '.'
    >>> format_phrase_to_sentence('hello')
    'Hello.'
    >>> format_phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_to_sentence('this subject is slay  ')
    'This subject is slay.'
    """
    stripped_phrase = phrase.strip()  # Strip any possible whitespace
    sentence = stripped_phrase.capitalize()
    if sentence[-1] != '.':  # Check for a fullstop at the end of the sentence
        sentence += '.'  # Adds a fullstop
    return sentence


run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()
