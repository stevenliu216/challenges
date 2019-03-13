from challenges.challenge21 import replace_spaces_dashes, last_five_lowercase, backwards_skipped


def test_replace_spaces_dashes():
    assert replace_spaces_dashes("Sammy Shark") == "Sammy-Shark"


def test_last_five_lowercase():
    assert last_five_lowercase("Sammy Shark") == "shark"


def test_backwards_skipped():
    assert backwards_skipped("Sammy Shark") == "kaSymS"
