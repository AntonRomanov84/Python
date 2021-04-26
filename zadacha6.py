a = int(input('Пробежал в первый день, км,'))
b = int(input('Пробежал всего, км,'))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day = day + 1
print(day)