def luhn_check(card_number):
    digits = [int(d) for d in str(card_number) if d.isdigit()]
    control = digits.pop()
    parity = len(digits) % 2  # delete extra brackets
    total = 0
    for i in range(len(digits)):
        if (
            i % 2 != parity
        ):  # fix error, != instead of == by definition of the algorithm
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]
    return (total + control) % 10 == 0


def main():
    print("Проверка номера карты по алгоритму Луна")
    print("Введите номер карты для проверки")
    print("Для выхода введите -1")
    print()

    while True:
        try:
            user_input = input("Введите номер карты: ").strip()

            if user_input == "-1":
                print("Выход из программы.")
                break

            if not user_input:
                print("Ошибка: Введите номер карты или -1 для выхода")
                continue

            # Проверка по алгоритму Луна
            if luhn_check(user_input):
                print("correct")
            else:
                print("incorrect")

        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
            print("Пожалуйста, попробуйте еще раз")

        print()


if __name__ == "__main__":
    main()
