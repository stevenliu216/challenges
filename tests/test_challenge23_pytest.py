from challenges.challenge23 import name_format


def test_name_format():
    assert name_format(
        [
            ["Zion", "Williamson", "20", "M"],
            ["Ja", "Morant", "19", "M"],
            ["Macy", "Miller", "22", "F"],
        ]
    ) == ["Mr. Ja Morant", "Mr. Zion Williamson", "Ms. Macy Miller"]
