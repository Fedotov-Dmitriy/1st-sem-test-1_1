def fast_pow(number, power):
    #проверка степени
    if not isinstance(power, int):
        raise TypeError("power must be an integer")

    # нули
    if power == 0:
        return 1
    if number == 0:
        if power < 0:
            raise ValueError("0 cannot be raised to a negative power")
        return 0
    #отрицательная степень
    if power < 0:
        number = 1 / number
        power = -power

    result = 1
    base = number
    while power > 0:
        if power % 2 == 1:
            result*=base
        base *= base
        power >>= 1
    return result
