def my_func(arg1, arg2, arg3):
    if arg1 >= arg2 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg3 and arg3 >= arg2:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(my_func(int(input('Введите первое число - ')), int(input('Введите второе число - ')),
              int(input('Введите третье число - '))))