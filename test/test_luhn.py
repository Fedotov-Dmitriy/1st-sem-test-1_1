import pytest

from src.luhn import luhn_check


def test_good():
    assert luhn_check("4561 2612 1234 5467")


def test_bad():
    assert not luhn_check("4561 2612 1234 5463")

def test_wrong_types():
    with pytest.raises(AssertionError):
        luhn_check(True)

def test_wrong_string():
    with pytest.raises(AssertionError):
        luhn_check("blabla")
