number = input("Enter a value: ")
number = int(number)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)

    return result


print("The factorial of 5 is:  " + str(factorial(number)))
