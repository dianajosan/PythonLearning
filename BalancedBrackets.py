input = "[[[[][]]]]"


def check_balance(brackets):
    i = 0                    # counter variable for checking if the brackets are opened and also closed
    for bracket in brackets:
        if bracket == '[':
            i += 1
        elif bracket == ']':
            i -= 1
        if i < 0:
            break

    return i == 0


print("Balanced brackets (" + str(check_balance(input)) + ")")