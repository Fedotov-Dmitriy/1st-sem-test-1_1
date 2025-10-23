import pytest

from src.luhn import luhn_check


def test_good():
    assert luhn_check("8571 2612 1234 5467")


def test_bad():
    assert not luhn_check("4561 2612 1234 5463")


@pytest.mark.parametrize(
    ["number", "expected"],
    [
        ("8531462222641434", False),
        ("9245217030", False),
        ("2530643671", False),
        ("2036532071", False),
    ],
)
def test_negative_power(number, expected):
    assert luhn_check(number) == expected
