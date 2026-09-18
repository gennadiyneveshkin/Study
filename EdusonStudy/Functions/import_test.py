def test_function():
    return 'Это первая функция из файла import_test'
print(test_function())

def test_function2():
    return 'Это вторая функция из файла import_test'


# Данная строка отделяет код, который выполняется при прямом запуске скрипта
# от кода, который выполняется при его импорте как модуля
if __name__ == '__main__':
    print(test_function2())