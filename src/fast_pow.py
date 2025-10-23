class MyException(Exception):
    pass

def fastPow(number, power):
    if power < 0:
        raise MyException("Отрицательная степень")
    if power > 1000000000:
        raise MyException("Слишком большая степень")
    result = 1
    while power != 0:
        result *= number
        power = power - 1
    return result
