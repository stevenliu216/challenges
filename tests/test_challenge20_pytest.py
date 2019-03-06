from challenges.challenge20 import print_rangoli


def test_print_rangoli():
    assert print_rangoli(3) == "----c----\n--c-b-c--\nc-b-a-b-c\n--c-b-c--\n----c----\n"
