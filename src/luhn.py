def luhn_check(card_number):
    if not all(x.isdigit() or x.isspace() for x in str(card_number)):
        raise ValueError("card_number should only consist of numbers and whitespace characters")
    spaces = sum(1 for x in str(card_number) if x.isspace())
    if spaces != 0 and spaces != 3:
        raise ValueError("card_number should only have zero or three whitespace characters")

    digits = [int(d) for d in str(card_number) if d.isdigit()]
    if len(digits) != 16:
        raise ValueError("card_number should have exactly 16 digits")

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
