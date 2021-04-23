def summ():
    try:
        with open('lesson5_5.txt', 'w') as file:
            line = input('Введите цифры через пробел: ')
            file.writelines(line)
            numb = line.split()
            print(sum(map(int, numb)))
    except ValueError:
        print('Необходимо ввести цифры через пробел!')
summ()