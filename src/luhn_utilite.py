from luhn import luhn_check

if __name__ == "__main__":
    while (card := input("Input card number (-1 for exit): ")) != "-1":
        if luhn_check(card):
            print("correct")
        else:
            print("incorrect")
