my_list = []
my_range = range(7, 36, 4)
my_range_2 = range(my_range.start, my_range.stop)

# print(my_range_2)

# for int_2 in my_range_2:
#     print(int_2)
#     my_list_2=list(int_2)

for ineratation_list in my_range:
    my_list = list(my_range)

print(my_list)
print(type(my_list))
