my_list = [12, 23, 31, 48, 67]

print(my_list)

del my_list[3]
# temp_list_index = my_list.pop(3)

print(len(my_list))
# print(temp_list_index)

my_list.reverse()

print(my_list)

second_my_list = [20, 56]

print(second_my_list)
my_list.extend(second_my_list)
# big_list = my_list+second_my_list

print(my_list)
print()
