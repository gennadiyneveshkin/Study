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

# Формирование списка из вводимых чисел
numbers = [int(input(f'Введите {i+1} число: ')) for i in range(3)]
print(numbers)