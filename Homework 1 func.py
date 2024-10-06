def apply_all_func(int_list,*functions):
    result = {}
    for func in functions:
        res = func(int_list)
        result[func.__name__] = res
    return result
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# min - принимает список, возвращает минимальное значение из него.
# max - принимает список, возвращает максимальное значение из него.
# len - принимает список, возвращает кол-во элементов в нём.
# sum - принимает список, возвращает сумму его элементов.
# sorted - принимает список, возвращает новый отсортированный список на основе переданного.