def fastPow(number, power):
    result = number
    deg = 1
    while deg * 2 < power:
        result *= result
        deg *= 2
    while deg < power:
        result *= number
        deg += 1
    return result