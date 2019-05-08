from challenges.challenge29 import letter_combinations


def test_letter_combinations():
    assert letter_combinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert letter_combinations("9") == ["w", "x", "y", "z"]
    assert letter_combinations("") == []
