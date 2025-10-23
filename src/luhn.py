def luhn_check(card_number):
    #проверка строки
    if not isinstance(card_number, str):
        raise TypeError("card_number должен быть строкой")
    #проверка на корректный ввод





    digits = [int(d) for d in str(card_number) if d.isdigit()]

    if len(digits) < 2:
        raise ValueError("Как минимум 2 цифры.")

    control = digits.pop()
    parity = (len(digits))%2
    total = 0
    for i in range(len(digits)):
        if i % 2 == parity:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]
    return (total + control) % 10 == 0
