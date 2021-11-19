n = 7


def fib(n):
    first = 0
    second = 1
    i = 3

    if n == 1:
        return first
    if n == 0:
        return second
    while i <= n:
        fibonnaci_series = first+second
        first = second
        second = fibonnaci_series
        i += 1
    return fibonnaci_series


print(f"The {n}th fibonacci number is: " + str(fib(n)))
# For a number entered from keyboard
m = int(input("Enter a number: "))
print(f"The {m}th fibonacci number is: " + str(fib(m)))


