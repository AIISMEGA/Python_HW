def user_data(name, surname, year_of_birth, accommodation, email, telephone):
    return (
        f'Имя пользователя: {name}, Фамилия пользователя: {surname}, Год рождения пользователя: {year_of_birth}, Город '
        f'проживания пользователя: {accommodation}, Email пользователя: {email}, Телефон пользователя: {telephone}')


name = input('Введите имя пользователя: ')
surname = input('Введите фамилию пользователя: ')
year_of_birth = input('Введите год рождения пользователя пользователя: ')
accommodation = input('Введите город проживания пользователя: ')
email = input('Введите email пользователя: ')
telephone = input('Введите телефон пользователя: ')

print(user_data(name=name, surname=surname, year_of_birth=year_of_birth, accommodation=accommodation, email=email,
                telephone=telephone))

