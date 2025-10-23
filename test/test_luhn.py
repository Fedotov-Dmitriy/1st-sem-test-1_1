from ..src.luhn import luhn_check


def test_good():
    assert luhn_check("8571 2612 1234 5467")


def test_bad():
    assert not luhn_check("4561 2612 1234 5463")
