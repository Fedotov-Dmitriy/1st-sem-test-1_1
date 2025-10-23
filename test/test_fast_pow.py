import pytest
from fast_pow import fastPow

def test_two_power_two():
    assert fastPow(2, 2) == 4

def test_negative():
    assert fastPow(256, 0) == 1

def test_neg():
    assert fastPow(2, -4) == 1
