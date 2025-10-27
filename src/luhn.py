

def luhn_check(card_number):
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    control = digits.pop()
    parity = (len(digits)) % 2
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

def utility():
    while True:
        number = input("Введите номер карты: ").strip()
        if number == "-1":
            print("Выход из программы.")
            break
        try:
            if luhn_check(number):
                print("correct")
            else:
                print("incorrect")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

utility()
