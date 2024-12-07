goods_list = ['Kinder schue', 'Herren schue',
              'Sky', 'Brilien', 'Heandphones', 'Notebook',
              'Schampoo', 'Soap', 'Zahepaste']
price_list=[20,65,145,100,34,675,10,4,3]

goods_price_zip=zip(goods_list,price_list)
goods_price_list=list(goods_price_zip)
goods_price_dict=dict(goods_price_list)

print(type(goods_price_list))
print(type(goods_price_dict))

print(goods_price_list)
print()
print(goods_price_dict)