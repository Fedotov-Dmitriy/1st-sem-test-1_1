from src.fast_pow import fast_pow


def test_two_power_two():
    assert fast_pow(2, 2) == 4


def test_negative():
    assert fast_pow(-1, 4) == 1


def test_incorrect_power():
    try:
        fast_pow(1, -1)
    except Exception:
        assert True
