def user_data(name, surname, birth_year, city, email, phone):
    print("User data:", name, surname, birth_year, city, email, phone)

ins_name = input("Ведите Имя ")
ins_surname = input('Введите Фамилию ')
b_year = input('Введите год рождения ')
ins_city = input('Введите город ')
ins_mail = input('Введите электронную почту ')
ins_phone = input('Введите телефон ')

user_data(name=ins_name, surname=ins_surname, birth_year=b_year, city=ins_city, email=ins_mail, phone=ins_phone)