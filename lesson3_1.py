def func(arg1, arg2):
    try:
        res = arg1 / arg2
    except ZeroDivisionError:
        return 'Ошибка! Нельзя применять 0!'
    return res
print(func(int(input('Введите первое число - ')), int(input('Введите второе число - '))))