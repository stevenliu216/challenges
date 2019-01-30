from challenges.challenge15 import athlete_sort


def test_athlete_sort():
    arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
    sorted_array = [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]
    assert athlete_sort(1, arr) == sorted_array
