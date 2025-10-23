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
