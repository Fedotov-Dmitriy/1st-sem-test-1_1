def fast_pow(number, power):
    if power < 1:
        raise ValueError("Степень меньше 1")
    result = 1
    base = number
    while power > 0:
        if power % 2 == 1:
            result *= base
            power -= 1
        base *= base
        power = power // 2
    return result
