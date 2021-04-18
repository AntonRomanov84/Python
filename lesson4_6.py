from itertools import count, cycle
end = 10
tr = 0
for el in count(int(input('Введите число: '))):
    tr += 1
    print(el)
    if tr == end:
        break
list = input('Введите строку через пробел или q для выхода: ').split()
for el in cycle(list):
    print(el)
    exit = input()
    if exit == 'q':
        break