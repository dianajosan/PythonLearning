my_list = [20, 9, 51, 81, 50, 42, 77]


def count_low_high(my_list):
    if (len(my_list) == 0):
        return None
    high_list = len([n for n in my_list if n > 50 or n % 3 == 0])
    low_list = len(my_list) - high_list

    return [low_list, high_list]


print(count_low_high(my_list))