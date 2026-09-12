# Функции
import email


# Функция без аргументов
# Выводит на экран фразу "Hello!"
def fhello():
    print('Hello!')


fhello()


def fhello2():
    print('Hello!')
    print('Hello2!')


fhello2()


# Функция с оператором return
def pow():
    return 5 ** 2  # возвращает в pow() значение 25


a = pow()
print(a)


# Функция с оператором pass
def foonk():
    pass  # ничего не делается, но и ошибка не выдается


def foonk2():
    ...  # то же самое, что и pass


# Функция возведения в степень с аргументами

def pow(x, n):
    return x ** n


a = pow(5, 3)
print(a)


# Аргумент по умолчанию
# Функция возводит любое число в квадрат
def pow(x, n=2):
    return x ** n

# Подаем на вход функции число 100, функция возвращает 1000 - присваиваем это значение переменной а
a = pow(100)
print(a)

a = pow(5, 3)
print(a)


# Позиционные аргументы

def add(a, b, c, d=100):
    return a + b + c + d


s = add(10, 5, 15)  # мы знаем позиции аргументов, поэтому не пишем что а = 10
print(s)


# Именованные аргументы

def add(a, b, c, d=100):
    print(f'1 - {a}\n2 - {b}\n3 - {c}\n4 - {d}')


add(b=10, c=15, a=5)  # задаем аргументы в любом порядке, но указываем их имена


# Позиционные и именованные аргументы в одной функции

def strict_function(e, f, *, g, h=100):  # все аргументы после * должны быть именнованными
    return e * f + g * h


result = strict_function(10, 2, g=3)
print(result)


# Как лучше оформлять код функций

def process(user_code, language, problem_id, company_id, attempts):
    ...


process(
    user_code="select * from users",  # до и после = пробелы не ставим
    language="SQL",
    problem_id=115,
    company_id=1,
    attempts=3,  # в последней строке также ставим запятую, т.к. возможно еще что-то будет добавляться
)

# Функция может принимать на вход неограниченное количество неменованных *args и именованных **kwargs аргументов
def my_function(*args, **kwargs):
    print(args)
    print(kwargs)


# *args - кортеж из позиционных аргументов
# **kwargs - словарь из именованных аргументов

my_function(5, 3, 'string', n=5, d=3, s='string2')


# после * вместо args и после двух звездочек ** после kwargs можно ставить любые символы
# например запись def my_function (*some, **any): тоже будет работать

def get_user_info(num, **kwargs):
    user_name = kwargs.pop('name', 'Без имени')
    # из get_user_info принимаем значение по ключу name и присваиваем его переменной user_name
    # если значение отсутствует, переменной user_name присваиваем значение Без имени

    user_mail = kwargs.pop('mail', 'Без почты')

    print(f'Пользователь номер {num}, имя {user_name}, почта {user_mail} и доп. информацией {kwargs}')


get_user_info(100, name='Андрон', language='Python')


# Локальные и глобальные переменные, область видимости
def my_function(x):
    x += 10
    return x

# Внутри функции x принимает значение 110

x = 100  # Но за ее пределами x = 100
a = my_function(x)
print(a, x)

# Глобальные переменные не теряют свое значение за пределами функций
def my_function (x):
    global a
    a = x + 10
    return a
a = 10
b = my_function(15)
print(a, b)

# Документирование функций
def my_function (x, n=2):
    # Задаем описание функции
    """Функция возводит любое число в любую степень, по умолчанию в квадрат"""
    return x ** n
print(my_function.__doc__) # Если к функции задано описание, его можно посмотреть таким образом
print('число:')
x = int(input())
print('степень:')
n = int(input())
a = my_function(x, n)
print (a)

# Возврат нескольких значений из функции
def process (data):
    flag = 1
    res = 10
    return flag, res
fl, res = process(1)
print (fl, res)
# подаем на вход функции значение data = 1, на выходе получем кортеж из двух значений (1, 10)
# с которыми дальше можем работать
# но это не очень хорошая практика!

