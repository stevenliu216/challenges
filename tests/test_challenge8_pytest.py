from challenges.challenge8 import max_area


def test_max_area():
    test_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert max_area(test_height) == 49
