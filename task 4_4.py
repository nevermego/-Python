input_list = [2, 6, 13, 2, 4, 37, 6, 8, 27, 13, 89, 4]

result = [i for i in input_list if input_list.count(i) == 1]
print(result)