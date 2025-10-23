# Simplistic power implementation for non-negative integer powers
def fast_pow(number, power: int):
    if power == 0:
        if number == 0:
            raise Exception("0^0 is undefined")

        return 1

    if power < 0:
        raise Exception("negative power unsupported")

    result = 1

    while power != 0:
        result *= number
        power -= 1

    return result
