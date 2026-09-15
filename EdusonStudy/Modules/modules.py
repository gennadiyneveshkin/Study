# Импорт всего модуля os
import os

# Просмотр текущей директории
print(os.getcwd())

# Импорт только функции date, но не всей библиотеки datetime
from datetime import date

print(date.today())

# Вывод текущего времени с помощью функции datetime модуля datetime
from datetime import datetime

print(datetime.now().time())

# Из модуля импорт сразу нескольких функций
from math import sin, cos

print(sin(1), cos(1))

# Из библиотеки requests импортировать все функции
from requests import *

# Теперь для использования функции в коде, не нужно писать название библиотеки перед точкой
# Не нужно писать requests.post()
# строка ниже закоментирована, потому что без аргументов в скобках выдаст ошибку
# post(), get()

# Присваивание алиасов библиотекам и модулям

# Импортируем библиотеку pandas с алиасом pd
import pandas as pd

# Вызов функции DataFrame библиотеки pandas с помощью присвоенного ей алиаса
print(pd.DataFrame([1, 2, 3]))
