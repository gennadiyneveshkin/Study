# Импорт функции foo из файла mod_test.py, который лежит на том же уровне, в той же папке
# что и файл, с которым мы сейчас работаем
from mod_test import foo
print(foo())


# Импортируем модуль sys который позволяет посмотреть пути к файлам и папкам
# по которым ходим питон в поисках импортируемых файлов
# Импортируем библиотеку os
import os, sys

# Смотрим на текущие пути, по которым ходит питон
print(sys.path)

# Добавляем к списку директорий, по которым ходит питон, нужную нам директорию Functions
sys.path.append(
    os.path.join(os.getcwd(), '..', 'Functions')
)

# Проверяем, что она попала в список
print(sys.path)

# Импорт функции test_function из файла import_test, который лежит в папке Functions
from import_test import test_function
