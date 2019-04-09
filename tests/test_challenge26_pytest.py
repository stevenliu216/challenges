from challenges.challenge26 import swap_case


def test_swap_case():
    assert (
        swap_case(
            "In February, Seattle was hit with its biggest February snow storm in more than 50 years."
        )
        == "iN fEBRUARY, sEATTLE WAS HIT WITH ITS BIGGEST fEBRUARY SNOW STORM IN MORE THAN 50 YEARS."
    )
