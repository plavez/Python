grage_auto_set = {'Mercedes', 'BMW', 'Mini', 'VW', 'Audi'}
garage_moto_set = {'Ducatti', 'Yamaha', 'Huqsvara', 'Suzuki', 'KTM'}

print(grage_auto_set == garage_moto_set)
print(grage_auto_set is garage_moto_set)

print(grage_auto_set)
print('Mercedes' in grage_auto_set)
print(garage_moto_set)
print('Yamaha' in garage_moto_set)
print('Yamaha' not in grage_auto_set)
print('BMW' not in grage_auto_set)
print('Audi' not in garage_moto_set)
