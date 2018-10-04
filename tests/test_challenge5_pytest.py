from challenges.challenge5 import pick_bball_game


def test_pick_bball_game():
    assert pick_bball_game(0.9) == 2
    assert pick_bball_game(0) == 0
    assert pick_bball_game(1) == 0
    assert pick_bball_game(0.5) == 0
    assert pick_bball_game(0.4) == 1
    assert pick_bball_game(0.51) == 2
    assert pick_bball_game(0.49) == 1
