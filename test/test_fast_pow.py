from src.fast_pow import fastPow


def test_two_power_two():
    assert fastPow(2, 2) == 4


def test_negative():
    assert fastPow(-1, 4) == 1

def test_zero_power():
    assert fastPow(5, 0) == 1

def test_negative_power():
    try:
        fastPow(2, -1)
        assert False
    except ValueError:
        pass

def test_invalid_power_type():
    try:
        fastPow(2, 2.5)
        assert False
    except ValueError:
        pass
    
def test_additional_cases():
    assert fastPow(2, 3) == 8
    assert fastPow(1, 100) == 1
    assert fastPow(0, 5) == 0
    assert fastPow(-2, 3) == -8
