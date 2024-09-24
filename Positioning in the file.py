def custom_write(file_name,strings):   # функциям принимает название файла и 'строки'. В качестве строки идет список со строками
    strins_positions = {}   # создаем словарь для добавления ключей и значений
    for i in strings:     # цикл для переборки строк из списка
        file = open(file_name, 'a',encoding='utf8')   # открываем файл в переменной с добавлением - append, добавляем кодировку для русских букв.
        Tell = file.tell()   # определяем позицию курсора, т.к. ничего не записано, будет 0 изначально.
        file.write(i +'\n')   # вносим в файл созданный строку из списка, добавляем перенос строки
        file.close()
        file1 = open(file_name,'r',encoding='utf8')   # # открываем файл в переменной с добавлением - read, добавляем кодировку для русских букв.
        contens = file1.read()     # создаем переменную с текущим значением/информацией в созданном файле
        line_numb = contens.count('\n')    # подсчитываем количество символов переноса строки в переменной
        file.close()
        strins_positions[line_numb,Tell] = i     # добавляем с словарь ключи и значение. Запомни!!!Ключи в квадратных скобках!!!
    return strins_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():           # представляет наш словарь в виде кортежа.
  print(elem)








