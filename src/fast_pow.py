def fastPow(number, power):
    result = 1
    base = number
    while power > 0:
        if power % 2 == 1:
            result*=base
        base *= base
        power >>= 1
    return result
