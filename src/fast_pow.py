def fast_pow(number, power):
    result = number
    while power != 1:
        result *= result
        power = power // 2
    return result
