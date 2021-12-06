my_list = [1, 5, 42, 38, 20, 99, 1285, 78, 389]
k = 3

my_list.sort()
print(my_list)

if k > len(my_list) or k <= 0:
    print("Invalid value for k.")
else:
    kth_max = my_list[-k]
    print(f"The largest {k}th number is: " + str(kth_max))

# Enter k from the keyboard
k_keyboard = input("Enter an integer: ")
k_keyboard = int(k_keyboard)

if k_keyboard > len(my_list) or k_keyboard <= 0:
    print("Invalid value for k introduced from keyboard.")
else:
    kth_max_2 = my_list[-k_keyboard]  # k max for the keyboard k
    print(f"The largest {k_keyboard}th number is: " + str(kth_max_2))    # the largest kth number for k from keyboard