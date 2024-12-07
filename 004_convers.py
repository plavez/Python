my_dict = {}

key_1 = input("Please enter name of the 1 key: ")
value_1 = int(input("Please enter 1 value: "))
key_2 = input("Please enter name of the 2 key: ")
value_2 = int(input("Please enter 2 value: "))
key_3 = input("Please enter name of the 3 key: ")
value_3 = (input("Please enter 3 value: "))

my_dict = {str.capitalize(key_1): value_1,
           str.capitalize(key_2): value_2,
           str.capitalize(key_3): value_3}

print(len(my_dict))
print(my_dict)

my_dict['Key 4'] = 44
my_dict['Key 5'] = 55

print(len(my_dict))
print(my_dict)

del my_dict[str.capitalize(key_1)]
del my_dict[str.capitalize(key_2)]

print(len(my_dict))
print(my_dict)
