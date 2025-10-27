def fast_pow(number, power):
    if power < 0:
        return 1
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= number
        number *=number
        power //= 2
    return result