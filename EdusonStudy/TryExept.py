def foo (a, b):
    try:
        res = a/b
        return res
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

print(foo(1, 0))


