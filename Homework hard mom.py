def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data +=1
            print(f'В {i} записан некорректный тип данных для подсчета суммы')

    return result, incorrect_data

def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)[0]
        lenn = len(numbers)
        answer = summ / lenn
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        answer = None
    except ZeroDivisionError:
            return 0
    return answer


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')




