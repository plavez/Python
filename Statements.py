# def you_adress(street, number):
#     adress = street, number
#     return adress


# adress_out_fn = you_adress('Im Gerstel', 40)
# print(adress_out_fn)

def our_house(name_street, number_house, city, plz, country):
    full_adress = name_street, number_house, plz, city, country

    return full_adress


def propeties_car(model_auto, year_production, color_car, type_body_car, type_engine, type_wheel_drive):
    car = model_auto, year_production
    type_car = type_wheel_drive, type_engine
    desig_car = color_car, type_body_car
    return car+type_car+desig_car


car_firm = input('Firm of your car :')
car_type = input('Enter body type of your car :')
car_color = input('Enter color of your car :')
car_whell = input('Enter please type system whel of your car :')
car_engine = input('Enter please which engine have your car :')
car_age = input('Enter production year of your car :')

car_compleate_info = propeties_car(
    car_firm, car_age, car_color, car_type, car_engine, car_whell)
print(car_compleate_info)

streetname = input('Enter name your stree :')
number_your_house = input('Enter number of your house :')
nameofcity = input('Enter name of your City :')
plz_number = input('Please enter number of your PLZ :')
name_country = input('Enter name of your Country :')
adress_complete = our_house(
    streetname, number_your_house, nameofcity,
    plz_number, name_country)


print(adress_complete)
