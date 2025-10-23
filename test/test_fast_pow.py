from src.fast_pow import fast_pow, NegativePowerException
import pytest
import random


def test_two_power_two():
    assert fast_pow(2, 2) == 4


def test_negative():
    assert fast_pow(-1, 4) == 1


@pytest.fixture
def random_n():
    return random.randint(1, 10)


def test_value_based(random_n):
    assert fast_pow(5, random_n) == 5 ** random_n


@pytest.mark.parametrize(["number", "power"], [(0, 0), (-1, -1), (0, -1), (1, -1), (1, 0)])
@pytest.mark.xfail(raises=NegativePowerException)
def test_negative_power(number, power):
    assert fast_pow(number, power)
