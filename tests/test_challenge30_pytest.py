from challenges.challenge30 import runner_up_score


def test_runner_up_score():
    assert runner_up_score([2, 3, 4, 5, 6, 6]) == 5
