# Основные встроенные модули Python

# Модуль для работы с операционной системой
import os

# Список всех файлов директории
print(os.listdir())

# Модуль для работы с математическими функциями
import math

# copysign позволяет определить знак числа + или -
from math import cos, sin, exp, sqrt, pi, log, copysign

# mean - функция расчета среднего значения
from statistics import mean

print(pi)

# Позволяет отбирать файлы в конкретной директории по заданному шаблону имени
import glob
print(glob.glob('*')) # Выведет все файлы в текущей директории, кроме тех, что начинаются с .
print(glob.glob('*.py')) # Выведет все файлы, которые заканчиваются на .py


# Функция работы со временем
from time import time

# Время с момента начала отсчета
print(time())

from time import sleep

def timer():
    sleep(2)

start = time()
timer()

# Время выполнения функции timer
print(time() - start)


# Модуль работы с датой и временем

from datetime import datetime

datetime.now()
print('Текущая дата и время:', datetime.now())


# Другие модули:
# json
# random - работа со случайными числами
# cmath - работа с математическими функциями
# pickle

