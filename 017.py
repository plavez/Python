def update_car_info(**car):
    car['is_available'] = True

    return car

# result_1=update_car_info(is_available=True)
# print(result_1)


result_2 = update_car_info(brand='Mercedes', price=37000)

print(result_2)
