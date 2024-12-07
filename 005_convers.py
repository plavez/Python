my_nums = (10, 5, 100, 0, 5, 5)

index_one = my_nums.index(5)
index_two = my_nums.index(5, index_one + 1)
index_three = my_nums.index(5, index_two + 1)


print(index_two)
print(index_three)
