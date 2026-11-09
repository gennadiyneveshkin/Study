# Вывод своей формулировки ошибки
def foo (a, b):
    try:
        res = a/b
        return res
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

print(foo(1, 0))

# Вывод стандартной формулировки ошибки
try:
    1/0

# Отлавливается TODO любая ошибка,
#  которая сохраняется в переменную err
except Exception as err:

    # выводим ошибку на печать
    print(err)

# Отлавливание ошибок различных видов
try:
    eval('''def foo():''')
except ZeroDivisionError as err:
    print(1, err)
except TypeError as err:
    print(2, err)
except Exception as err:
    print(3, err)

# Расширенный вывод текста ошибки (ошибка + описание)
try:
    1/0
except Exception as err:
    print ('Ошибка: ', err)
    print(repr(err))

# Дополнительные условия
try:
    res = 1/1
except Exception as err:
    print(err)
else:
    print(res)
finally:
    print('Этот блок выполнится в любом случае!')

# TRY EXCEPT вместе с RAISE
# raise не «обрабатывает» ошибку, он её создаёт,
# а try/except ее обрабатывает

def divide(a, b):
    if b == 0:

# строка raise ZeroDivisionError(...) это способ сказать:
# «Я не хочу пытаться делить на ноль, я сразу сообщаю: тут ошибка».
# Функция сознательно прерывает работу и выбрасывает исключение.
# Без raise Python сам выбросил бы ZeroDivisionError при a / b, но с raise ты:
# делаешь проверку заранее и даёшь понятное сообщение;
# контролируешь момент и тип исключения (можно даже свой тип ошибки сделать);
# явно показываешь, что это недопустимое состояние по логике твоей программы.
# То есть raise это сигнал об ошибке, но не её обработка.
        raise ZeroDivisionError("Делитель не должен быть нулём")
    return a / b

# Блок try/except нужен, чтобы поймать этот сигнал и не дать программе аварийно завершиться.
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")


