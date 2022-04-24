num = str(input('Insert num '))

max_num = 0
pos = 0
while pos < len(num):
    if int(max_num) < int(num[pos]): #cравнение новой переменной max_num c каждым числом
        max_num = num[pos] 
    print(num[pos])
    pos += 1

print(max_num)


