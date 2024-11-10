# Введение в функциональное программирование
# Задача "Вызов разом"

def apply_all_func(int_list, *functions):
    """

    :param int_list:список из чисел (int, float)
    :param functions: неограниченное кол-во функций, которые применимы к спискам, состоящим из чисел
    :return:словарь, где ключом будет название вызванной функции,
     а значением - её результат работы со списком int_list.
    """
    results = { }
    for func in functions:
        results[func.__name__] = func(int_list)
    return  results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

