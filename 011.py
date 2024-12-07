my_set_1 = {1, 3, 5, 7}
my_set_1.add(9)
my_set_2 = {1, 4, 5, 11}

my_set_united = my_set_1.intersection(my_set_2)

print(my_set_united)

my_list_1 = list(my_set_united)

print(type(my_list_1))
print(my_list_1)
