def luhn_check(card_number: str):
    digits = [int(d) for d in card_number if d.isdigit()]
    control = digits.pop()
    parity = (len(digits)) % 2
    total = 0
    for i in range(len(digits)):
        if (i + 1) % 2 == parity:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]
    total += control
    return total % 10 == 0 and total // 10 == control


def luhn_interactive():
    def check_valid_card(card):
        return all(x.isspace() or x.isdigit() for x in card)

    while True:
        try:
            user_input = input("Write card number or -1 to quit: ")

            if user_input == "-1":
                break

            if not check_valid_card(user_input):
                raise Exception("You didn't enter a card.")

            if luhn_check(user_input):
                print("Your card is correct.")
            else:
                print("Your card is incorrect.")
        except EOFError:
            break
        except Exception as e:
            print(e)
    print("Bye bye!")


if __name__ == "__main__":
    luhn_interactive()
