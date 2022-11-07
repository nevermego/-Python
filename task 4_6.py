from itertools import cycle

start = 8
it1 = (i for i in range(start, start+10))

print([i for i in it1])


list_before = [6, 28, 4, 17, 33, 22, 11]
list_it = cycle(list_before)
it2 = (next(list_it) for _ in range(10))
print([i for i in it2])
