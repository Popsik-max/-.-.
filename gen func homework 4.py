import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
space_func = lambda x, y : x == y  # создаем переменную, которой является результат работы ламбды, а именно сравнение х и у
print(list(map(space_func, first, second))) # мап перебирает 2 строки и производит с их элементами логику работы переменной/функции

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open (file_name, 'a',encoding='utf8') as file:
            for i in data_set:
                file1 = file.write(str(i)+ '\n') # помимо ай в формате строки нужно добавлять перенос строчки

        return file1
    return write_everything
write = get_advanced_writer('example.txt')   # в эту переменную мы заложили выполнение функции и первый ее параметр/переменную
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])   # здесь мы уже вызываем функцию с заложенным параметром и добавляем уже параметры для внутренней функции

class MysticBall():
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        a = random.choice(self.word)  # в качестве аргумента для рандома передается коллекция строк
        return a


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball.__call__())
print(first_ball.__call__())
print(first_ball.__call__())
