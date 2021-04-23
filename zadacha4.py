num = int(input('Введите число - '))
m = num % 10
a = num // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print('Самая большая цифра - ', m)