def fast_pow(number, power):
    # Обработка отрицательной степени
    if power < 0:
        number = 1 / number
        power = -power

    result = 1.0
    base = float(number)
    exp = int(power)

    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2

    return result
