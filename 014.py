def merge_list_to_dict(list_1, list_2):
    merge_list_zip = zip(list_1, list_2)
    merge_list_list=list(merge_list_zip)
    merge_list_dict = dict(merge_list_list)
    return merge_list_dict

names_list_1=['Vladislav','Marina','Vadim','Emma']
age_list_2=[48,47,29,15]

result=merge_list_to_dict(names_list_1,age_list_2)

print(result)