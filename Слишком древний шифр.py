number = int(input('Число первой вставки в промежутке от 3 до 20: ' ))

for i in range (1, number):
    for j in range (i+1,number):
        if number % (i + j) == 0:
            password = (str(i) + str(j))
            print(password,end='')
            continue
        else:
            continue
