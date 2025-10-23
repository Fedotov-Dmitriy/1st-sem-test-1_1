def fastPow(number, power):
    result = 1
    while power != 0:
        result *= number
        power = power - 1
    return result

