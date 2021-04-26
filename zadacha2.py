vr_sec = int(input('Введите время в секундах - '))
hh = vr_sec // 3600
mm = (vr_sec - hh * 3600) // 60
ss = vr_sec - (hh * 3600 + mm * 60)
print(f'Время в чч:мм:сс   {hh} : {mm} : {ss}')