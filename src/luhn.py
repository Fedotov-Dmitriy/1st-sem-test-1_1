import sys


def luhn_check(card_namber):
    digits = [int(d) for d in str(card_namber) if d.isdigit()]
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


if __name__ == "__main__":
    input_number = sys.argv[1]
    if luhn_check(input_number):
        print("correct")
    else:
        print("incorrect")