def fast_pow(number, power):
    result = number
    if power == 0:
        return 1
    while power != 1:
        if power > 0:
            result *= result
            power = power // 2
        if power < 0:
            return 1 / fast_pow(number, -power)
    return result
