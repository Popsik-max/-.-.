Pass_1 = int(input('Число первой вставки в промежутке от 3 до 20: ' ))

for num_1 in range (1, 21):
    for num_2 in range (2, 21):
        num_3 = num_1 + num_2
        num_4 = Pass_1 / num_3
        if num_4 - int(num_4) == 0:
            print('Второй пароль: ', num_1, num_2)


        else:
            continue