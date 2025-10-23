def luhn_check(number):
    digits = [int(d) for d in str(number) if d.isdigit()]

    if len(digits) < 2:
        raise Exception("less than two digits")

    control = digits.pop()
    parity = (len(digits) - 1) % 2
    total = 0

    for i in reversed(range(len(digits))):
        value = digits[i]

        if i % 2 == parity:
            value = digits[i] * 2
            if value > 9:
                value -= 9

        total += value

    return (10 - (total % 10)) % 10 == control


if __name__ == "__main__":
    response = ["incorrect", "correct"]
    prompt = int(input())

    while prompt != -1:
        print(response[int(luhn_check(prompt))])
        prompt = int(input())
