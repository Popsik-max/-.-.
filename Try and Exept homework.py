def add_everything_up(a,b):
    try:
        result = a + b
    except TypeError:
        if isinstance(a,str):
            result_2 = a + str(b)
        else:
            result_2 = str(a)+ b
        return (f'Переданные параметры были разного типа, приводило к ошибке. '
                f'Результат работы except: {result_2}')
    else:
        return (f'Оба переданных параметра одного типа, результат: {result}')
    finally:
        print('Код имеет небольшие отличия, но условия задачи выполняет. Если убрать лишний текст, будет выглядеть лаконичнее.')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
