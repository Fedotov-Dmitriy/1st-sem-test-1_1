from src.fast_pow import fastPow, MyException
from pytest import raises


def test_two_power_two():
    assert fastPow(2, 2) == 4


def test_negative():
    assert fastPow(-1, 4) == 1

def test_errors_under_zero():
    try:
        fastPow(3, -1)
        assert False
    except MyException as e:
        assert isinstance(e, MyException)
        assert str(e) == "Отрицательная степень"


def test_errors_too_much():
    try:
        fastPow(3, 10000000000000)
        assert False
    except MyException as e:
        assert isinstance(e, MyException)
        assert str(e) == "Слишком большая степень"
