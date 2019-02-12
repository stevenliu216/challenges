from challenges.challenge18 import exceptions


def test_exceptions():
    assert exceptions(1, 0) == "Error Code: integer division or modulo by zero"
    assert exceptions(2, "$") == "Error Code: invalid literal for int() with base 10: '$'"
    assert exceptions(3, 1) == 3
