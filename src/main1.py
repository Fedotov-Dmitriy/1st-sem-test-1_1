def luhn_check(card_number):
    #проверка строки
    if not isinstance(card_number, str):
        raise TypeError("card_number должен быть строкой")
    #проверка на корректный ввод

    digits = []
    #проверка на корректность ввода
    for ch in card_number:
        if ch.isdecimal():
            digits.append(int(ch))
        elif ch in " \t\r\n":
            continue
        else:
            raise ValueError("Кривой ввод")

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



def main()
    print("Введите номер карты (или -1 для выхода):")
    while True:
            try:
                line = input().strip()
            except EOFError:
                return 0
            except KeyboardInterrupt:
                print("\nЗавершение по Ctrl-C.")
                return 0
            if line == "-1":
                return 0
            print("correct" if ok else "incorrect")
if __name__ == "__main__":
    raise SystemExit(main())