my_list = [10, -14, 26, 5, -3, 13, -5]


def check_sum(my_list):
    for n in range(0, len(my_list)):
        for n1 in range(n + 1, len(my_list)):
            if my_list[n] + my_list[n1] == 0:
                return True

    return False


print("We have 2 numbers in the list with sum zero. (" + str(check_sum(my_list)) + ")")
