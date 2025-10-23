def luhn_check(card_number: str):
    """
    This is luhn checking algorithm.
    It check whether the card is correct.
    card_number must be a valid string containing digits and spaces.
    It raises ValueError if card_number is invalid.
    """
    if (
        not all(x.isspace() or x.isdigit() for x in card_number)
        or len(card_number) == 0
    ):
        raise ValueError("The luhn algorithm did not receive a card for input.")

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
    """
    This is command line interactive luhn checking algorithm.
    User writes down a credit card and gets whether his card is correct or not.
    """
    while True:
        try:
            user_input = input("Write card number or -1 to quit: ")

            if user_input == "-1":
                break

            if luhn_check(user_input):
                print("Your card is correct.")
            else:
                print("Your card is incorrect.")
        except EOFError:
            break
        except ValueError as e:
            print(e)
    print("Bye bye!")


if __name__ == "__main__":
    luhn_interactive()
