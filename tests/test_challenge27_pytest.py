from challenges.challenge27 import reach_the_finish


def test_finish_line():
    assert reach_the_finish([2, 3, 1, 1, 4])
    assert reach_the_finish([2, 0, 0])


def test_run_out_of_range():
    assert not reach_the_finish([3, 2, 1, 0, 4])


def test_no_race():
    assert reach_the_finish([0])
