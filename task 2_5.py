my_list = [7, 5, 3, 2]
el = int(input('Insert new element '))
i = 0

for n in my_list:
    if el <= n:
        i += 1
    elif el > n:
        break

my_list.insert(i, int(el))
print(my_list)