from itertools import product

import pytest

from src.fast_pow import fast_pow


def test_positive_power():
    for n, p in product(range(-1000, 1000), range(1, 100)):
        assert fast_pow(n, p) == n**p


def test_negative_power():
    for n, p in product(range(-1000, 1000), range(1, 100)):
        with pytest.raises(Exception) as e:
            fast_pow(n, -p)
            assert e == "negative power unsupported"


def test_zero_power():
    for n in range(-1000, 100):
        if n == 0:
            continue  # tested separately

        assert fast_pow(n, 0) == 1


def test_0_pow_0():
    with pytest.raises(Exception) as e:
        fast_pow(0, 0)
        assert e == "0^0 is undefined"
