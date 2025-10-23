def luhnСheck(cardNumber):
    digits = [int(d) for d in str(cardNumber) if d.isdigit()]
    parity = (len(digits)) % 2
    control = digits.pop()
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

user_number = []
user_str = str(input("Введите строчку с номером, оканчивающуюся на '-1': "))

def check(str):
    for i in range(len(str) - 1):
        if str[i]+str[i+1] != '-1':
            if str[i] in '0123456789':
                user_number.append(int(str[i]))
            else:
                print("Найден неверный символ: ", str[i])
    if luhnСheck(user_number):
        return "Номер корректен"
    else:
        return "Некорректный номер"
print(check(user_str))