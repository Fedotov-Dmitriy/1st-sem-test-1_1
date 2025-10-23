def fast_pow(number, power):
    if power != abs(round(power)) or power <= 0:
        raise Exception("Not natural power.")
    result = number
    while power != 1:
        result *= result
        power = power // 2
    return result
