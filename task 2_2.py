user_list = list(input('Enter list of elements without space between them '))

for i in range(1, len(user_list), 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]

print(user_list)





