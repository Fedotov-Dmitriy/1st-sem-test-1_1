def luhn_check(card_number):
    assert isinstance(card_number, str), "Error: card_number must be string"
    card_number = card_number.replace(' ', '')
    assert card_number.isdigit(), "Error: card_number must be string of digits"
    digits = [int(d) for d in card_number]
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
    return total % 10 == 0

if __name__ == "__main__":
    inp = input("Enter card number: ")
    while inp != '-1':
        try:
            res = luhn_check(inp)
            print("correct" if res else "incorrect")
        except AssertionError as ex:
            print(ex)
        finally:
            inp = input("Enter card number: ")

    print("Bye!")
