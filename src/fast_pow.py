def fast_pow(number, power):
    if power < 0:
        return 1 / fast_pow(number, -power)
    result = number
    while power != 1:
        result *= result
        power = power // 2
    return result
