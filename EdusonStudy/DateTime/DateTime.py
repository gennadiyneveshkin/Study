# РАБОТА С ДАТОЙ. МОДУЛЬ date
from datetime import date

from EdusonStudy.Modules.bacic_modules import start

# Создание даты
dt = date(2026, 11, 19)

# Получение даты из переменной dt
print(dt)

# Получение только года из переменной dt
print(dt.year)

# Получение месяца и дне из переменной dt
print(dt.month)
print(dt.day)

# Получение дня недели
# Получим 3 - третий день недели Thursday
print(dt.weekday())

# Получение текущей даты
print(date.today())

# Получение текущего года
print(date.today().year)

print(type(dt))

# Преобразование даты в строку и форматирование с помощью TODO .strftime()
print(dt.strftime('%d/%m/%Y'))

# Выведет текущую дату день/месяц/год
print(date.today().strftime('%d/%m/%Y'))

# Выведет текущий месяц
print(date.today().strftime('%m'))

# РАБОТА С ДАТОЙ И ВРЕМЕНЕМ. МОДУЛЬ datatime
# содержит в себе не только дату (возможности модуля date) но и время

from datetime import datetime
dtm = datetime(2026, 11, 19, 12, 34, 00)
print(dtm)

# Вывод только времени
current_time = datetime.now()
print (current_time.time())
print(f'{current_time.hour}:{current_time.minute}:{current_time.second}')

# Сделать !!!из строки!!!  дату: метод TODO .strptime()
s = '2026-11-19 14:51'
s_parsed = datetime.strptime(s, '%Y-%m-%d %H:%M')
print(s_parsed)

# Была строка, стал объект datetime.datetime
print(type(s_parsed))

print(s_parsed.strftime('%d/%m/%Y'))

# Вывод только даты
print(s_parsed.date())

# Вывод только времени
print(s_parsed.time())

print()
# ДАТЫ И МЕТКИ ВРЕМЕНИ
print(dtm)

# ts - метка времени для объекта dtm
ts = datetime.timestamp(dtm)
print(ts)

# Восстановление по метке ts в читабельном формате даты и времени объекта dtm
# То есть если у нас для объекта dtm есть только метка в формате 1795080840.0
# то по ней мы можем восстановить дату в нормальном формате
rts = datetime.fromtimestamp(ts)
print(rts)

# ЧАСОВЫЕ ПОЯСА
import pytz
print(pytz.all_timezones)
msk = pytz.timezone('Europe/Moscow')
print(msk)

# РАЗНОСТЬ ДАТ
current = datetime.now()
past = datetime(2025, 1, 11, 12, 00, 00)
dif = current - past
print(dif)
print(type(dif))

# timedelta - разница во времени
from datetime import timedelta

# Прибавить к текущей дате 30 дней и посмотреть какая дата будет
future = current + timedelta(days=30)
print(future)

print()
# МОДУЛЬ time (не путать с from datetime import time)
# содержит другие функции нежели time из datetime
import time

# Количество секунд с начала эпохи
t = time.time()
print(t)

# Замерить время, сколько работает код
# Фиксируем начало отсчета
start = time.time()

print('Hello')

# Задержка на 2 сек.
time.sleep(2)

print('OK')

print(f'Итоговое время: {time.time() - start}')