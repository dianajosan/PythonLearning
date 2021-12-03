my_list = [10, -14, 26, -3, 13, -4, -1, 5]


def check_sum(my_list):
    for n in range(0, len(my_list)):
        total = 0
        for n1 in range(n, len(my_list)):
            total += my_list[n1]
            if total == 0:
                print("We found the elements with sum zero.")

check_sum(my_list)
