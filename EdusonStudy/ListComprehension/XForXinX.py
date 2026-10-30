# Списочные выражения (включения)
# List Comprehension

# new list = [expression for item in iterable if condition]
# expression - выражение, которое вычисляется для каждого элемента и становится элементом нового списка
# for item in iterable - цикл, который перебирает каждый элемент исходной коллекции
# if condition - необязательное условие, если оно истинно, элемент добавляется в новый список


# Возведение в квадрат всех четных чисел из списка
my_list = [1, 2, 3, 4]
squares = [x**2 for x in my_list if x % 2 == 0]
print(squares)

# Формирование списка из чисел больше 18
ages = [10, 16, 67, 44, 18, 53]
adults = [adult for adult in ages if adult > 18]
print(adults)


# Применение функции sin к каждой из точек в списке
t = list(range(11))
print(t)
from math import sin
t_sin = [round((sin(ti)),3) for ti in t ]
print(t_sin)

# Создание списка из цифр 5 на основе списка t

# нижнее подчеркивание вместо переменной - это значит, что нам не важно, что это за переменная
# мы ее больше нигде не используем
lst_5 = [5 for _ in t]
print(lst_5)

# Найти длину елементов списка
elems_list = [1, [1, 2], [3, 4, 5], 10]
elems_len = [len(x) if not isinstance(x, int) else 1 for x in elems_list]
print(elems_len)

# НЕСКОЛЬКО ЦИКЛОВ

# Сделать список плоским
lst = [[1, 2, 3], [3, 4], [], [5, 6, 7, 8]]

# for el in lst - внешний цикл, выполняется первым
# for x in el - внутренний цикл, выполняется вторым
# питон начинает с внешнего цикла и берет el из lst
# затем идет во внутренний цикл и переберает все х в el и снова возвращается во внешний цикл за следующим el
lst_thin = [x for el in lst for x in el]


# ГЕНЕРАТОР МНОЖЕСТВ

#  Найти числа, которые делятся на 2
lst = [[1, 2, 3], [], [1, 5, 10], [], [2, 4, 7, 9, 10]]

result = {x for el in lst for x in el if x%2 == 0}
print(result)

# ГЕНЕРАТОР СЛОВАРЕЙ (dict comprehension)

# Пронумеровать список
lst = ['Первая задача', 'Вторая задача', 'Третья задача']
res = {key : value for key, value in enumerate(lst, start = 1)}
print(res)


# Функция zip_longest и list comprehension

nums1 = [1, 2, 3]
nums2 = [1, 2, 3, 4]
nums3 = [1, 2, 3, 4, 5]

from itertools import zip_longest

# zip_longest выводит все значения, не отсекая лишние
# вместо несуществующих элементов в более коротких списках ставит None
for x, y, z in zip_longest(nums1, nums2, nums3):
    print(x, y, z)

# Но можно вместо None поставить 0
for x, y, z in zip_longest(nums1, nums2, nums3, fillvalue=0):
    print(x, y, z)

# Формирование списка из вводимых чисел
numbers = [int(input(f'Введите {i+1} число: ')) for i in range(3)]
print(numbers)