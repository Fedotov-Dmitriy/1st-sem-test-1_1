import pytest

from src.luhn import luhn_check


def test_only_whitespace():
    with pytest.raises(ValueError):
        luhn_check("gnwejkvberiw5245425 4543")


def test_spacing():
    assert luhn_check("8571261212345467")
    assert luhn_check("8571 2612 1234 5467")
    with pytest.raises(ValueError):
        assert luhn_check("857  12612 1  2345467")
        assert luhn_check("8571 2612 123454 67")
        assert luhn_check("85712612 1234 5467")

def test_too_many_digits():
    with pytest.raises(ValueError):
        assert luhn_check("11111111111111111111111111111")

def test_good():
    assert luhn_check("8571 2612 1234 5467")


def test_bad():
    assert not luhn_check("4561 2612 1234 5463")
