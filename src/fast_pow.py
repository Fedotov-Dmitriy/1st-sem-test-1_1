def fastPow(number, power):
    result = number
    while power != 1:
        result *= result
        power >>= 1
    return result
