def fast_poww(number, power):
    result = number
    if power > 0:
        while power != 1:
            result *= number
            power = power - 1
        return result
    if power < 0:
        while power != 1:
            result /= number
            power = power + 1
        return result
    return 1
