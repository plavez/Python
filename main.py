my_list = [1, 2]
my_list_2 = []

my_dict = {}
my_dict_2 = {'test': 2}

print(my_list and my_dict)  # {}
print(bool(my_list and my_dict))  # False
print(bool(my_list and my_dict_2))  # True


my_list_2 and print("List is not empty!!!")# ничего потому что ложно.
my_list and print("List is not empty!!!")#List is not empty!!!
