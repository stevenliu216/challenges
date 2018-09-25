from challenges.challenge3 import is_unique


def test_is_unique():
    assert is_unique("alabama") is False
    assert is_unique("Ford") is True
