a = 1


def check_num(a):
    if a < 5:
        return 'Маленькое число'
    elif a < 10:
        return 'Среднее число'
    elif a < 20:
        return 'Большое число'
    else:
        return 'Очень бошьшое число'


print(check_num(a))

# Комбинирование условий

a = 10
b = 100
c = 50
d = 1000

# Проверяем выполнение всех условий
if a > 5 and b > 10 and c > 15:
    print('Все числа большие')

else:
    print('False')

# Проверяем выполнение хотя бы одного условия
if a > 5 or b > 10 or c > 15:
    print('Хотя бы одно число большое')
else:
    print('False')

# Проверяем выполнение условий в порядке очередности

if a > 5 and b > 10 or c > 100 and d < 50:
    print('True')
else:
    print('False')


# Возведение в степень обычным способом
def pow(a, n):
    if n:
        return a ** n
    else:
        return a


print(pow(5, 2))


# Возведение в степень лаконичный вариант без else
# Можно использовать если одиночный if и возврачает либо 1 либо 2 условие
def pow(a, n):
    if n:
        return a ** n
    return a


print(pow(5, 2))


# Возведение в степень с помощью тернарного оператора
def pow(a, n):
    # Если n задано возвращаем а в степени n, если не задано, возвращаем а
    return a ** n if n else a  # Тернарный оператор


print(pow(5, 2))


# ОПТИМИЗАЦИЯ КОДА

# МЕТОДИКА РАННЕГО ПРЕРЫВАНИЯ

# Это упрощенный пример, без выполнения проверок внутри функций
# Просто возвращаем True, если переменные не пусты

# Магазин работает?
def check_shop_is_opened(shop):
    # Если передано хоть какое-то значение переменной shop, возвращаем True - магазин открыт
    if shop:
        return True


# В магазине есть нужный товар?
def check_is_unit_in_shop(unit, shop):
    # Если переменные shop и unit не пусты, возвращаем True
    if shop and unit:
        return True


# У покупателя есть деньги на покупку данного товара?
def check_customer_can_afford_unit(unit, customer):
    # Если переменные customer и unit не пусты, возвращаем True
    if unit and customer:
        return True


shop = 'Магазин 1'
unit = 'Компьютер'
customer = 'Алексей'


# Сложный и громоздкий вариант

def make_purchase():
    # Поочередно проверяем что каждое условие True, если все True, возвращаем в функцию 'Покупка успешна'

    if check_shop_is_opened(shop):  # Если верно, то проверяем следующее условие
        if check_is_unit_in_shop(unit, shop):  # Если верно, то проверяем следующее условие
            if check_customer_can_afford_unit(unit, customer):  # Если верно, то возвращаем в функцию
                return 'Покупка успешна'
            else:
                raise Exception('Не достаточно денег')
        else:
            raise Exception('Товара нет в магазине')
    else:
        raise Exception('Магазин закрыт')


print(make_purchase())


# Лаконичный и читабельный вариант с ранним прерыванием

def make_purchase():
    if not check_shop_is_opened(shop):  # Если shop == False
        raise Exception('Магазин закрыт')  # Возвращаем 'Магазин закрыт' и дальше проверка не идет

    if not check_is_unit_in_shop(unit, shop):  # Если unit == False
        raise Exception('Товара нет в магазине')  # Возвращаем 'Товара нет' и дальше проверка не идет

    if not check_customer_can_afford_unit(unit, customer):  # Если customer == False
        raise Exception('Не достаточно денег')  # Возвращаем 'Нет денег' и дальше проверка не идет

    return 'Покупка успешна'  # Если все 3 условия выше == True, возвращаем 'Покупка успешна'


# Альтернативный вариант

if (check_shop_is_opened(shop)
        and check_customer_can_afford_unit(unit, customer)
        and check_customer_can_afford_unit(unit, customer)):
    print('Покупка успешна!')
else:
    print('Не удалось совершить покупку')


# ИЗБЕГАЕМ ДЛИНЫХ УСЛОВИЙ

class Competition:  # Класс Конкурс
    is_active = True  # Конкурс действует?
    vacancies = 10  # Осталось вакансий


class Person:  # Класс Учасник
    age = 18
    level = 5


comp = Competition
per = Person

if comp.is_active and comp.vacancies > 0 and per.age > 15 and per.level > 3:  # Очень длинно!
    print('OK')  # выполняется какой-то код по начислению баллов
else:
    print('Извините, вы не соответствуете условию начисления баллов')


# Альтернативный вариант с помощью инкапсуляции

class Competition:  # Класс Конкурс
    is_active = True  # Конкурс действует?
    vacancies = 10  # Осталось вакансий

    @property
    def is_actual(self):  # Проверка актуальности конкурса
        if self.is_active and self.vacancies > 0:
            return True
        return False


class Person:
    age = 18
    level = 5

    @property
    def match_conditions(self):  # Проверка соответствия участника
        if self.age > 15 and self.level > 3:
            return True
        return False


comp = Competition()
per = Person()

# TODO В Python запись if comp.is_actual and per.match_conditions: уже является полноценной проверкой на True, потому что сам if ожидает булево значение. Добавлять == True избыточно и может даже навредить, так как вы сравниваете булево значение с True — это лишнее действие.
if comp.is_actual and per.match_conditions:
    print('Вам начислены баллы')  # выполняется какой-то код по начислению баллов
else:
    print('Извините, вы не соответствуете условию начисления баллов')

print(comp.is_actual)
print(per.match_conditions)


# Как это будет выглядеть без @property
class Competition:
    is_active = True
    vacancies = 10

    def is_actual(self):
        if self.is_active and self.vacancies > 0:
            return True
        return False


class Person:
    age = 18
    level = 5

    def match_conditions(self):
        if self.age > 15 and self.level > 3:
            return True
        return False


comp = Competition()
per = Person()

# Если убрать декоратор @property и превратить эти методы в обычные функции, то запись для print будет следующей:
# print(comp.is_actual()) # со скобками, как вызов метода
# print(per.match_conditions())
# Но важно: если вы просто уберёте @property, не поменяв сами методы, код if comp.is_actual and per.match_conditions перестанет работать, потому что теперь is_actual и match_conditions — это методы, а не свойства. Их нужно вызывать со скобками:
# if comp.is_actual() and per.match_conditions():
# print('OK')
# То есть либо вы оставляете @property и пишете без скобок (и в print, и в if), либо убираете @property и везде добавляете скобки. Смешивать эти два подхода нельзя — код либо сломается, либо даст неверный результат. Рекомендую оставить @property, так как именно для этого он и предназначен — чтобы обращаться к методам как к атрибутам, делая код чище и короче.

if comp.is_actual() and per.match_conditions():
    print('Вам начислены баллы*')  # выполняется какой-то код по начислению баллов
else:
    print('Извините, вы не соответствуете условию начисления баллов*')

print('\n')

# Как избегать дублирования кода

def login(username, email, password):
   print('Пользоваетль залогинен')


def create_user(username, email, password, company_id):
    print('Пользоваетль создан')


user = 1
username = 'Андрон'
email = 'mail@mail.ru'
password = 'abcde'
company_id = 100

if not user:
    # запусти функцию create_user и передай ей текущие значения переменных
    # Слева от = - имя аргумента функции, справа - переменная, из которой берётся значение
    create_user(
        username=username,
        email=email,
        password=password,
        company_id=company_id,
    )
else:
    # запусти функцию login и передай ей текущие значения переменных
    login(
        username=username,
        email=email,
        password=password,
    )

# Упрощение кода

if not user:
    # Присваиваем переменной auth_func значение функции create_user
    auth_func = create_user

    # Словарь extra_args будет содержать пары ключ-значение с параметрами, которые
    # имеют отношение только при регистрации нового пользователя
    extra_args = {
        'company_id': company_id
    }
else:
    auth_func = login

    # Пустой словарь (в который возможно добавить элементы, кторые относятся только к регистрации)
    extra_args = {}

# auth_func содержит общие аргументы для create_user и login

auth_func (
    username=username,
    email=email,
    password=password,
)
