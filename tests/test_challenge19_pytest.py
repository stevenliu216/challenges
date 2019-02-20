from challenges.challenge19 import list_comp


def test_list_comp():
    assert list_comp(1, 1, 1, 2) == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
