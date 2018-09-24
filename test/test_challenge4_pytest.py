from challenges.challenge4 import find_magic_index


def test_find_magic_index():
    assert find_magic_index([-1, 0, 1, 2, 4, 10]) == 4
