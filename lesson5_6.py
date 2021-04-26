subj = {}
with open('lesson5_6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lect, pract, lab = line.split()
        subj[subject] = int(lect) + int(pract) + int(lab)
    print(f'Общее количество часов по предмету: \n {subj}')