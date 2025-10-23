def fastPow(number, power):
    if power == 0:
        return 1
    if number == 0:
        if power < 0:
            return "0 cannot be raised to a negative power"
        return 0

    result = 1
    base = number
    while power > 0:
        if power % 2 == 1:
            result*=base
        base *= base
        power >>= 1
    return result
