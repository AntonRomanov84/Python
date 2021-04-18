def func(x, y):
    for el in range(abs(y - 1)):
        x *= x
        return 1 / x
print(func(5, -7))