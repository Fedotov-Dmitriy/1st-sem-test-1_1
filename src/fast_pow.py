def fast_pow(number, power):
    assert (isinstance(number, int) or isinstance(number, float) \
            and isinstance(power, int)), \
            "Error: number and power must be numbers"

    assert (power > 0 and isinstance(power, int)), "Error: power must be natural number"

    result = 1
    while power > 0:
        if power % 2  == 1:
            result *= number
        number *= number
        power = power // 2
    return result
