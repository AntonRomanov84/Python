def salary_1():
    try:
        time = float(input('Выработка в часах - '))
        salary = float(input('Ставка в час, руб. - '))
        bonus = float(input('Премия, руб. - '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника -  {res}')
    except ValueError:
        return print('Введите число!')
salary_1()