from challenges.challenge22 import validate_phone_number


def test_validate_phone_number():
    assert validate_phone_number(["3137456281", "1252478965"]) == ["YES", "NO"]
    assert validate_phone_number(["123-456-7890"]) == ["NO"]
