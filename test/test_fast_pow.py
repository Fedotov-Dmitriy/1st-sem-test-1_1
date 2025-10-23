import math
import pytest
from src.fast_pow import fast_pow


def test_positive_integer_power():
    assert fast_pow(2, 3) == 8
    assert fast_pow(5, 0) == 1


def test_zero_power():
    # Любое число в степени 0 равно 1
    assert fast_pow(5, 0) == 1


def test_negative_integer_power():
    assert math.isclose(fast_pow(2, -2), 0.25)
    assert math.isclose(fast_pow(10, -3), 0.001)


def test_fractional_power():
    assert math.isclose(fast_pow(9, 0.5), 3.0)
    assert math.isclose(fast_pow(8, 1 / 3), 2.0)


def test_negative_base_integer_power():
    assert fast_pow(-2, 4) == 16
    assert math.isclose(fast_pow(-2, 3), -8)


def test_negative_base_fractional_power():
    with pytest.raises(ValueError):
        fast_pow(-8, 1 / 3)
