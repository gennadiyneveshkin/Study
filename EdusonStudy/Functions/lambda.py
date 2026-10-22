# Синтаксис: lambda [аргументы]: [тело функции]

# Вовзодит число в квадрат
make_square = lambda x: x**2
print(make_square(5))

# Складывает три числа
adder = lambda a, b, c: a + b + c
print(adder(1, 2, 3))


# LAMBDA + FILTER

# Получить четные числа из списка
lst = [1, 2, 3, 4, 5, 6]

# lambda проверяет соответствие аргумента условию, описанному в теле функции
# lambda x: x % 2 == 0 это просто функция: «дай мне какое‑то значение, я скажу, чётное оно или нет».
# Для lambda x - это просто имя параметра, который придёт «сверху».
# filter применяет lambda к lst
# filter берёт список lst и по очереди подставляет каждый его элемент в эту функцию как аргумент.
# list преобразовывает полученный результат в формат списка

even_lst = list(filter(lambda x: x % 2 == 0, lst))
print(even_lst)


# LAMBDA + MAP
# Возвести в квадрат каждый элемент списка
lst = [1, 2, 3, 4, 5, 6]

# map берет поочередно элементы списка lst и подает их в lambda
square_lst = list(map(lambda x: x**2, lst))
print(square_lst)


# Преобразование списка различных чисел в список целых чисел
lst = [1.5, 1e-5, 1.23e+1, 5, 1.108]
int_lst = list(map(lambda x:int(x), lst))
print(int_lst)

# Преобразование списка различных чисел в список целых чисел
lst = [1.5, 1e-5, 1.23e+1, 5, 1.108]
int_lst = list(map(lambda x:int(x), lst))
print(int_lst)

# УСЛОВИЯ В LAMBDA

# Преобразовать в списке строковые элементы в число
# Остальные элементы оставить без изменений

lst = [1.5, 1e-5, 1.23e+1, 5, 1.108, '100']

# если аргумент x это число, возвращаем его же, если не число, то преобразовываем в число
int_lst = list(map (lambda x: x if isinstance(x, (int, float)) else eval(x), lst))
print(int_lst)


# НЕСКОЛЬКО АРГУМЕНТОВ LAMBDA
lst1 = [1, 2, 3]
lst2 = [3, 2, 1]
result = list(map(lambda x, y: x > y, lst1, lst2))
print(result)

lst = [1, 10, -1, 5, 6, 3]
print(sum(lst))

# ФУНКЦИЯ REDUCE B И LAMBDA

lst = [5, 6, 7]

from functools import reduce

product = reduce(lambda x, y: x*y, lst)
print(product)