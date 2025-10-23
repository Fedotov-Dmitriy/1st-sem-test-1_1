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
