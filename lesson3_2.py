def person (name, lastname, year, city, email, phone):
    return print(f'Имя: {name}; Фамилия: {lastname}; Год рождения: {year}; Город проживания: {city}; Email: {email};\
    Телефон: {phone}')
person(name=input('Имя - '), lastname=input('Фамилия - '), year=input('Год рождения - '),
       city=input('Город проживания - '), email=input('Email - '), phone=input('Телефон - '))