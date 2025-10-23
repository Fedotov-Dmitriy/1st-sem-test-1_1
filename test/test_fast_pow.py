from ..src.fast_pow import fast_poww


def test_two_power_two():
    assert fast_poww(2, 2) == 4


def test_negative():
    assert fast_poww(-1, 4) == 1
    assert fast_poww(2, -4) == 0.0625


def test2():
    assert fast_poww(2, 3) == 8

