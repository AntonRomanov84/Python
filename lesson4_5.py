from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2

print(f'Список четных значений: {[el for el in range(100, 1001, 2) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка:\
{reduce(my_func, [el for el in range(100, 1001, 2) if el % 2 == 0])}')