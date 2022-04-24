usr_sec = int(input('Введите время '))

hh = (usr_sec // 3600)
hh1 = (usr_sec % 3600)

print(hh, hh1)

mm = (hh1 // 60)
ss = (hh1 % 60)

print(mm, ss)

print(str(hh) + ":" + str(mm) + ":" + str(ss))

