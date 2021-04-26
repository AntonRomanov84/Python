my_txt = open('lesson5_1.txt', 'w', encoding='utf-8')
line = input('Введите любой текст: ')
while line:
    my_txt.writelines(line)
    line = input('Введите любой текст: ')
    if not line:
        break

my_txt.close()