# Операции с дробными числами

# Тип данных type и окруление round
p = 3.1415
print(p)
print(type(p))
print(round(p))  # округление до целой части

import math  # импорт модуля math с основными мат функциями, в т.ч sin, cos и др.
from math import ceil, floor  # импорт из math функций округления в меньшую ceil и большую floor сторо

print(ceil(p))  # TODO  округление до большего целого (до потолка)
print(floor(p))  # FIXME  округление до меньшего целого (до пола)
print(math.floor(0.6))  # округление до меньшего целого сразу через math.floor

print(round(p, 2))  # округление до сотых

d = 7e-5
print(d)
d1 = 0.00007
print(d1)
if d == d1:
    print('d = d1')
else:
    print('d is not equals e')

a = 33
b = 200
if b > a:
    print('b is greater than a')

e = 1
print(float(e))  # преобразуем целое число в число с плавающей точкой

f = 3.1415
print(int(f))  # преобразуем число с плавающей точкой в целое число

j = 3.78
print(int(j))  # округление происходит не по математическим правилам(!) а простым отбрасыванием дробной части

# Преобразовываем экспоненциальную запись в десятичную
exponential_num = 1.5e-3
decimal_num = float(exponential_num)