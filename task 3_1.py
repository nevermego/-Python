def my_func():
    try:
        num = int(input('Введите числитель '))
        denomin = int(input('Введите знаменатель '))

    except denomin == 0:
        return print("Деление на ноль невозможно")
    divis = num / denomin
    return divis

print(my_func())