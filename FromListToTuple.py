my_list = input[34, 82.6, "Darth Vader", 17, "Hannibal"]

# my_tuple = (my_list[0], my_list[len(my_list)-1], len(my_list))
my_tuple = []
if my_list == []:
    print("Null list")
else:
    my_tuple = (my_list[0], my_list[-1], len(my_list))

print("The tuple is: " + str(my_tuple))