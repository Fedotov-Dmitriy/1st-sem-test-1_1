from src.fast_pow import fast_pow
import pytest
import random


def test_two_power_two():
    assert fast_pow(2, 2) == 4


def test_negative():
    assert fast_pow(-1, 4) == 1


@pytest.fixture
def random_n():
    return random.randint(1, 100)


def test_negative_power(random_n):
    assert fast_pow(10, -1) == 10 ** (-1)