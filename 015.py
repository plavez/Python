def merge_lists_to_dict(names, age):
    merge_lists_zip = zip(names, age)
    merge_lists_dict = dict(merge_lists_zip)

    for key, value in merge_lists_dict.items():

        print(f"{key} - {value}", 'лет')

    return merge_lists_dict


papa_name = input("Напишите имя отца - ")
mother_name = input("Напишите имя Мамы - ")
sonn_name = input("Напишите имя сына - ")
dother_name = input("Напишите имя дочки - ")

papa_age = 48
mother_age = 47
sonn_age = 29
dother_age = 15

out_names = [papa_name, mother_name, sonn_name, dother_name]
out_ages = [papa_age, mother_age, sonn_age, dother_age]

famaly_names_ages = merge_lists_to_dict(out_names, out_ages)
