def luhn_check(card_number):
    digits_str = "".join(filter(str.isdigit, str(card_number)))
    if not digits_str:
        return False
    digits = [int(d) for d in digits_str]
    control = digits.pop()
    digits.reverse()

    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit
    total += control
    return total % 10 == 0


def main():
    print("Введите номер карты")
    while True:
        user_input = input("Введите номер карты: ").strip()
        if user_input == "-1":
            print("Выход из программы.")
            break
        try:
            if luhn_check(user_input):
                print("correct")
            else:
                print("incorrect")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
