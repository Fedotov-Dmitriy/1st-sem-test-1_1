import pytest

from src.fast_pow import fast_pow


def test_two_power_two():
    assert fast_pow(2, 2) == 4

def test_five_power_five():
    assert fast_pow(5, 5) == 3125

def test_negative():
    with pytest.raises(AssertionError):
        fast_pow(5, -2)

def test_not_natural():
    with pytest.raises(AssertionError):
        fast_pow(6, 1.5)

def test_zero():
    with pytest.raises(AssertionError):
        fast_pow(3, 0)

def test_wrong_types():
    with pytest.raises(AssertionError):
        fast_pow("foo", "bar")
