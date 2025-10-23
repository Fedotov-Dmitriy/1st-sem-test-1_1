def fast_pow(number, power):

    result = number

    if power < 0:
        raise InvalidPowerError("Отрицательная степень не поддерживается")

    if not isinstance(power, int):
        raise TypeError("Степень всегда является целым числом")

    if not isinstance(number, int):
        raise TypeError("Число, возводимое в степень должно быть целым")

    while power != 1:
        result *= result
        power = power // 2
    return result
