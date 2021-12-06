input_sample = "[]["


def check_balance(brackets):
    i = 0                    # counter variable for checking if the brackets are opened and also closed
    for bracket in brackets:
        if bracket == '[':
            i += 1
        elif bracket == ']':
            i -= 1
        elif bracket != ']' or bracket != '[':
            print("Invalid data")
            return i == 1
        if i < 0:
            break

    return i == 0


print("Balanced brackets (" + str(check_balance(input_sample)) + ")")
input_keyboard = input("Enter a string to check if the brackets are balanced or not: ")
print("Balanced brackets (" + str(check_balance(input_keyboard)) + ")")
