from game import check_the_guess


def test_greater_guess():
    won, msg = check_the_guess(10, 3)
    assert won is False
    assert msg == "your guess is more than number"


def test_greater_less():
    won, msg = check_the_guess(2, 3)
    assert won is False
    assert msg == "your guess is less than number"
