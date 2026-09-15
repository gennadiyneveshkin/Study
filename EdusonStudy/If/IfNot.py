# if not - сочетание условного оператора if и логического оператора not.
# Оператор not инвертирует значение. Если условие истинно, not сделает его ложным и наоборот
from http.cookiejar import domain_match

my_dict = {}
if not my_dict:
    print("Словарь пуст")  # Выполнится, так как словарь пуст

# Отсутствие значения в переменной domain это False. not False это True.
# Т.е. выполнитяся условие if, а не else
domain = ''
if not domain:
    print('Домен не указан')
else:
    print(domain)