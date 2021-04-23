from itertools import count
from math import factorial
def fact():
    for el in count(1):
        yield factorial(el)
gen = fact()
x = 0
for i in gen:
    if x == 9:
        break
    else:
        x += 1
        print(f'Факториал числа {x} = {i}')
