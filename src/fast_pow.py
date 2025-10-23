def fast_pow(number, power):
    if power == 0:
        return 1
    if power < 0:
        return 1 / fast_pow(number, -power)
    result = 1
    base = number
    while power > 0:
        if power % 2 == 1:
            result *= base
        base *= base
        power = power // 2
    return result
