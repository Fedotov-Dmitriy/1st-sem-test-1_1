def luhnСheck(cardNumber):
    digits = [int(d) for d in str(cardNumber) if d.isdigit()]
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


def utility(cardNumber):
    cardNumber = input('Введите номер карты(или -1, чтобы выйти)')
    flag = False
    while cardNumber != "-1":
        if flag:
            print("Вы неправильно ввели номер карты, будте внимательны")
            cardNumber = input('Введите номер карты(или -1, чтобы выйти):')
        for i in range(len(cardNumber)):
            if i % 4 == 0:
                if cardNumber != " ":
                    flag = True
            else:
                if cardNumber[i] not in '1234567890':
                    flag = True
        if not flag:
            if luhnСheck(cardNumber):
                print("Correct")
            else:
                print("Incorect")
            cardNumber = input('Введите номер карты(или -1, чтобы выйти):')
