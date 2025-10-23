import pytest

from src.fast_pow import fast_pow


def test_two_power_two():
    assert fast_pow(2, 2) == 4

def test_fuzzy():
    for x in range(1, 10):
        for y in range(-10, 10):
            assert fast_pow(x, y) == x**y

def test_negative():
    assert fast_pow(-1, 4) == 1

def test_zero():
    assert all(fast_pow(1, x) == 1 for x in range(1, 100))
    assert all(fast_pow(x, 0) == 1 for x in range(1, 100))
    with pytest.raises(ZeroDivisionError):
        fast_pow(0, -5)
