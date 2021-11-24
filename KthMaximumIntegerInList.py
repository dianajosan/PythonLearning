my_list = [1, 5, 42, 38, 20, 99, 1285, 78, 389]
k = 3

# Enter k from the keyboard
k_keyboard = input("Enter an integer: ")
k_keyboard = int(k_keyboard)

my_list.sort()
print(my_list)

kth_max = my_list[-k]
kth_max_2 = my_list[-k_keyboard]      # k max for the keyboard k

print(f"The largest {k}th number is: " + str(kth_max))
print(f"The largest {k_keyboard}th number is: " + str(kth_max_2))    # the largest kth number for k from keyboard