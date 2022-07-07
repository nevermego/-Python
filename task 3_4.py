def task_4_a(x, y):

    return x ** y

def task_4_b(x, y):

    pow = 1.0
    for i in range(0, y, -1):
        pow /= x

    return pow
x = int(input('Insert x = '))
y = int(input('Insert y = '))
print("Task 4 a", task_4_a(x, y), " task b ", task_4_b(x, y))