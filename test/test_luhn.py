from src.luhn import luhn_check


def test_good():
    assert luhn_check("8571 2612 1234 5467")

def test_incorrect_input():
    try:
        luhn_check("7")  # слишком коротко
    except ValueError:
        pass
    else:
        raise AssertionError("Ошибка недостатка цифр.")

def test_incorrect_input_2():
    try:
        luhn_check("4111 11X")
    except ValueError:
        pass
    else:
        raise AssertionError("Value error.")

def test_bad():
    assert not luhn_check("4561 2612 1234 5463")