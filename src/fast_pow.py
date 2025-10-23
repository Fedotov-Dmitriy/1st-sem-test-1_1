def fastPow(number, power):
    result = number
    while power != 1:
        result *= number
        power = power - 1
        print(result, power)
    return result


