from src.fast_pow import fast_pow


def test_two_power_two():
    assert fast_pow(2, 2) == 4

def test_negative():
    assert fast_pow(-1, 4) == 1

def test_kritical():
    assert fast_pow(4, -1) == 0.25
    

