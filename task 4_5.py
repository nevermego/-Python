from functools import reduce

input_list = [i for i in range(100, 1000) if i % 2 == 0]

def mult(accum, el):
    return accum * el

print(reduce(mult, input_list, 1))

