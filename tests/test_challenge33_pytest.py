from challenges.challenge33 import int_to_roman


def test_int_to_roman():
  assert int_to_roman(3) == "III"
  assert int_to_roman(4) == "IV"
  assert int_to_roman(58) == "LVIII"
  assert int_to_roman(1994) == "MCMXCIV"
