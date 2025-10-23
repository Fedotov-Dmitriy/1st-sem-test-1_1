def luhn_check(card_number):
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    if not digits:
        raise ValueError("номер карты не может быть пустым или содержать буквы")
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


while True:
    card_input = input("Введите номер карты (или '-1' для выхода): ")
    if card_input.lower() == "-1":
        break

    if luhn_check(card_input):
        print("correct")
    else:
        print("incorrect")
