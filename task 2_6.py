goods = []
features = {'name': '', 'price': '', 'q-ty': '', 'UoM': ''}
analytics = {'name': [], 'price': [], 'q-ty': [], 'UoM': []}

usr_pos = 0

while True:
    if input('For exit press X, press Enter to continue ').upper() == 'X':
        break
    usr_pos += 1
    for k in features.keys():
        info = input(f'Insert data for {k} - ')
        features[k] = int(info) if k in ('price', 'q-ty') else info
        analytics[k].append(features[k])
    goods.append((usr_pos, features.copy()))
    print(f'\nAvailable goods\n{goods}')
    print(f'\nAnalytics on available goods:\n')

    for key, value in analytics.items():
        print(f'{key}: {value}')






