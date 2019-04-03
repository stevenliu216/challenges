from challenges.challenge25 import max_profit


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([2, 1, 4, 5, 2, 9, 7]) == 8


def test_no_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_buy_at_end():
    assert max_profit([2, 1, 2, 1, 0, 1, 2]) == 2


def test_min_at_right():
    assert max_profit([2, 4, 1]) == 2


def test_profit_not_at_min():
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4
