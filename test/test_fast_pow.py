from src.fast_pow import fast_pow


def test_two_power_two():
    assert fast_pow(2, 2) == 4


def test_negative():
    assert fast_pow(-1, 4) == 1
    assert fast_pow(-2, 3) == -8


def test_negative_power():
    epsilon = 1e-8

    assert fast_pow(5, -1) - 0.2 <= epsilon
    assert fast_pow(10, -2) - 0.01 <= epsilon
    assert fast_pow(77, -5) - 77 ** (-5) <= epsilon

    assert fast_pow(-0.2, -2) - 25 <= epsilon
    assert fast_pow(-0.2, -1) - 5 <= epsilon


def test_edge_cases():
    assert fast_pow(1100101, 0) == 1
    assert fast_pow(-13, 0) == 1
    assert fast_pow(111, 0) == 1


def test_roots():
    assert fast_pow(9, 0.5) == 3
    assert fast_pow(8, 1 / 3) == 2
    assert fast_pow(64, 1 / 6) == 2
