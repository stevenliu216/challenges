from challenges.challenge12 import fizz_buzz


def test_fizz_buzz(capfd):
    fizz_buzz(15)
    out, err = capfd.readouterr()
    assert out == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"
