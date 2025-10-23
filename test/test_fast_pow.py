from src.fast_pow import fast_pow


def test_base():
    assert fast_pow(2, 10) == 1024

def test_negative_base():
    assert fast_pow(-3, 3) == -27
    assert fast_pow(-3, 4) == 81

def test_zero_base():
    assert fast_pow(2, 0) == 1

def test_two_power_two():
    assert fast_pow(2, 2) == 4

def test_negative_pow():
    assert abs(fast_pow(2, -3) - 0.125) < 1e-15
    assert abs(fast_pow(-2, -3) + 0.125) < 1e-15

def test_negative():
    assert fast_pow(-1, 4) == 1
