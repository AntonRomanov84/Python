my_list = [7, 5, 3, 3, 2]
print(f' Рейтинг - {my_list}')
element = int(input('Введите элемент - '))
while True:
    for el in range(len(my_list)):
        if my_list[el] == element:
            my_list.insert(el + 1, element)
            break
        elif my_list[0] < element:
            my_list.insert(0, element)
        elif my_list[-1] > element:
            my_list.append(element)
        elif my_list[el] > element and my_list[el + 1] < element:
            my_list.insert(el + 1, element)
    print(f' Рейтинг - {my_list}')
    element = int(input('Введите новый элемент - '))