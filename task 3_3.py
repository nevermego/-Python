def my_func(num1, num2, num3):

    if num1 > num2:

        if num2 > num3:
            return num1 + num2
        else:
            return num1 + num3

    else:

        if num1 > num3:
            return num2 + num1
        else:
            return num2 + num3
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))
print("my_func = ", my_func(num1,num2,num3))