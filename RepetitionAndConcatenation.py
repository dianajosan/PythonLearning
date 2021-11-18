first_parameter = input("Enter first number: ")
second_parameter = input("Enter the second number: ")


def rep_cat(x, y):
    if x.isdigit() and y.isdigit():
        x = str(x) * 10
        y = str(y) * 5
        result = x + y
        print("The concatenation result between the values is: " + result)

    return result


if first_parameter.isdigit() and second_parameter.isdigit():
    rep_cat(first_parameter, second_parameter)
elif not first_parameter.isdigit():
    print("First value is not a valid number.")
elif not second_parameter.isdigit():
    print("Second value is not a valid number.")

