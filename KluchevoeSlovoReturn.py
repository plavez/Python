# def sum_nums(a, b):
#     sum = a + b
#     # print("Line is not executed")
#     return sum


# name = sum_nums('Golic ', 'Vladislav')
# age = sum_nums(10, 38)
# print(name)
# print(age)
# print(name)


def adress_client(street, house_number, plz, city):
    street_with_number = street, house_number
    plz_nummer = plz
    return street_with_number, plz_nummer
    # return plz_nummer


adress = adress_client('Im Gerstel', 40, 66994, 'Dahn')
print(adress)
