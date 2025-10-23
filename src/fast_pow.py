def fastPow(number, power):
    if not isinstance(power, int):
        raise ValueError("Power must be integer")
    if power < 0:
        raise ValueError("Power must be non-negative")
    if power == 0:
        return 1 
    result = 1
    base = number
    while power > 0:
        if power % 2 == 1:
            result *= base
        base *= base
        power = power // 2
    return result