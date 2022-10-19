usr_month = int(input('Enter month value from 1 to 12 '))


season = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}

for i in season.keys():
    if usr_month in season[i]:
        print(i)















