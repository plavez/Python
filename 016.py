def merge_list_to_dict(list_1, list_2):

    return dict(zip(list_1, list_2))


res_one = merge_list_to_dict(list_1=['a', 'b', 'c'], list_2=[10, True, []])
print(res_one)

res_two = merge_list_to_dict(list_2=[{}, True, 100], list_1=['abc'])
print(res_two)

res_three = merge_list_to_dict(['a', True, 100], list_2=['abc'])
print(res_three)

# res_three=merge_list_to_dict(list_2=['abc'],['a',True,100])
# print(res_three)
