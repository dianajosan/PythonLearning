my_list = [10, -4, 34, -3, 3, -5, -1, 4, 4, 5, -5, 5]


def check_sum(my_list):
    count = 0
    for n in range(0, len(my_list)):

        print(my_list[n])
        for n1 in range(n + 1, len(my_list)):
            if my_list[n] + my_list[n1] == 0:
                count += 1
                print(count)
    return count


if check_sum(my_list) > 0:
    print(f"We found {check_sum(my_list)} pairs of 2 numbers with sum 0! ")
else:
    print("No pair of 2 numbers with sum 0 found.")
