import pytest
from src.luhn import luhn_check


def test_good():
    assert luhn_check("8571 2612 1234 5466")
    assert luhn_check("4  5  6  1     2  6  1  2     1  2  3  4     5  5  6  6")


def test_bad():
    assert not luhn_check("4561 2612 1234 5463")
    assert not luhn_check("4  5  6  1     2  6  1  2     1  2  3  4     5  4  6  4")
    assert not luhn_check("4  5  6  1     2  6  1  2     1  2  3  4     5  4  6  7")


def test_invalid():
    with pytest.raises(ValueError):
        luhn_check("abc")

    with pytest.raises(ValueError):
        luhn_check("451abc")

    with pytest.raises(ValueError):
        luhn_check("")
