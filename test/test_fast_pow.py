from src.fast_pow import fast_pow


def test_two_power_two():
    assert fast_pow(2, 2) == 4


def test_negative():
    assert fast_pow(-1, 4) == 1


def test_negative_pover():
    assert fast_pow(2, -1) == 1 / 2


def test_pover_zero():
    assert fast_pow(2, 0) == 1
