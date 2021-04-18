proceeds = float(input('Введите значение выручки Вашей компании -'))
cost = float(input('Введите значение издержек Вашей компании -'))
if proceeds > cost:
    profit = proceeds - cost
    print(f'Поздравляем! Ваша компания работает с прибылью! Ваша прибыль составляет - {profit}. Рентабельность прибыли составляет - {profit / proceeds}')
else:
    print(f'Очнитесь! Ваша компания работает в убыток! Убыток составляет - {proceeds - cost}')
workers = int(input('Введите количество сотрудников -'))
if proceeds > cost:
    print(f'Прибыль Вашей компании в расчете на одного сотрудника составляет - {profit / workers}')