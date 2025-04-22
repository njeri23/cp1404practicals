"""
Testing code using assert and doctest
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
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence: capitalize first letter and end with a full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("goodbye.")
    'Goodbye.'
    """
    phrase = phrase.strip()
    if not phrase.endswith("."):
        phrase += "."
    return phrase[0].upper() + phrase[1:]


def run_tests():
    """Run the tests on the functions."""
    # 1. Assert test for repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"  # Fixed function to pass this test

    # 2. Car tests
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test default fuel
    default_car = Car()
    assert default_car.fuel == 0, "Default fuel is not 0"

    # Test specific fuel
    fuelled_car = Car(fuel=10)
    assert fuelled_car.fuel == 10, "Car does not set fuel correctly"


run_tests()

# 3. Run doctests
doctest.testmod()
