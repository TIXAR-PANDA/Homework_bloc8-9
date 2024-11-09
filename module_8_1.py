# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    """
    add_everything_up  складывает числа(int, float) и строки(str)
    :param a:число(int, float) или строка(str)
    :param b:число(int, float) или строка(str)
    :return: a + b , когда a и b окажутся разными типами (числом и строкой),
    то возвращать строковое представление этих двух данных вместе (в том же порядке)
    """

    try:
        return a + b
    except TypeError:

        return str(a)+str(b)


print(add_everything_up(12, 45.3))
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('бла', "бла"))
print(add_everything_up(121, 45))

