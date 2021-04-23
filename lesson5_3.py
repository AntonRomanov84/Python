file = open('lesson5_3.txt', 'r', encoding='utf-8')
lines = file.readlines()
sum = 0
for row in lines:
    line = row.split()
    if (float(line[1]) < 20000):
        print(f'{line[0]} имеет оклад менее 20000руб')
    sum += float(line[1])
print(f'Средний заработок на предприятии: {sum} руб')
file.close()