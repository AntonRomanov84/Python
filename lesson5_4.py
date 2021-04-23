dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('lesson5_4.txt', 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()
    print(lines)
with open('lesson5_4_new.txt', 'a', encoding='utf-8') as file_write:
    for line in lines:
        row = line.split()
        row[0] = dict[row[0]]
        print(' '.join(row), file=file_write)