my_str = input('Введите строку через пробел - ')
my_str = my_str.split()
for i, val in enumerate(my_str, start=1):
    if len(str(my_str)) <= 10:
        print(f' {i} - {val}')
    else:
        print(f' {i} - {val [0:10]}')

