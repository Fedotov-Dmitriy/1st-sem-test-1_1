import pytest

from src.luhn import luhn_check


def less_than_two():
    with pytest.raises(Exception) as e:
        luhn_check("1")
        assert e == "less than two digits"


def test_good():
    assert luhn_check("17893729974")


def test_bad():
    assert not luhn_check("17893729970")
