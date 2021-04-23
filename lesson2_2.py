list = [int(i) for i in input('Введите значения через пробел - ').split()]
list_new = list
print(list_new)
j = 0
for i in range(int(len(list_new)/2)):
    list_new[j], list_new[j+1] = list_new[j+1], list_new[j]
    j += 2
    print(list_new)