import random

my_list = [random.randint(1, 1000) for i in range(100)]
result_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]

print(my_list)
print(result_list)
