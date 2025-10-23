class NegativePowerError(Exception):
    pass


def fast_pow(number, power):
    if power < 1:
        raise NegativePowerError
    result = number
    while power != 1:
        result *= result
        power = power // 2
    return result
