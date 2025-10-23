def luhn_check(card_number):
    if not all(x.isdigit() or x.isspace() for x in str(card_number)):
        raise ValueError("card_number should only consist of numbers and whitespace characters")

    spaces = sum(1 for x in str(card_number) if x.isspace())
    if spaces != 0 and spaces != 3:
        raise ValueError("card_number should only have zero or three whitespace characters")
    if spaces != 0 and not all(len(x) == 4 for x in card_number.split()):
        raise ValueError("Each fragment of card_number should contain 4 digits")

    digits = [int(d) for d in str(card_number) if d.isdigit()]
    if len(digits) != 16:
        raise ValueError("card_number should have exactly 16 digits")

    parity = (len(digits))%2
    total = 0
    for i in range(len(digits)):
        digit = digits[i]
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

if __name__ == "__main__":
    while True:
        number = input("Enter card number: ")
        if number == "-1": break
        try:
            result = luhn_check(number)
            if result: print("correct")
            else: print("incorrect")
            break
        except ValueError as e:
            if 'card_number' in str(e):
                print(str(e))
            else:
                raise e
