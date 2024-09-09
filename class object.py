# class Human:
#     def __init__(self, name, age):       # определение атрибутов обьекта
#         self.name = name
#         self.age = age
#         self.say_info()
#
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age}')
#
#     def bir (self):
#         self.age += 1
#         print(f'У меня теперь день рожденья, мне теперь {self.age}')
#
#     def __len__(self): # длина обьекта
#         return self.age
#
#     def __lt__(self,other):  #   сравнение двух обьектов
#         return self.age < other.age
#
#     def __gt__(self, other):         #сравнение двух обьектов
#         return self.age > other.age
#
#     def __eq__(self, other):           # сравнение на равенство двух обектов
#         return self.age == other.age and self.name == other.name
#
#     def __bool__(self):           # проверка истина или не истина
#         return bool(self.age)
#
#     def __str__(self):
#         return f'{self.name}'
#
#
#     def __del__(self):         #
#         print(f'{self.name} ушёл')
#
#
#
# den = Human('Денис',22)
# max = Human("Макс",22)
# a = 6
# print(den)
#

class House():
    def __init__(self,name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self,new_floor):
        self.new_floor = int(new_floor)
        if self.new_floor > self.number_of_floor or self.new_floor < 1:
            print('Такого этажа не существует!')
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return (f'Название:{self.name}, количество этажей: {self.number_of_floor}')

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor # оператор равно

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor # оператор меньше

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor # оператор меньше или равно

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor # оператор больше

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor # оператор больше или равно

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor # оператор не равно

    def __add__(self, value):        #увеличивает количество этажей на переданное значение
        self.number_of_floor += value
        return self.number_of_floor

    def __radd__(self, value):   # вызывает другой метод, но нужно прописать атрибут!!!!!!
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__
h1.__add__(10)# __add__
print(h1)
print(h1 == h2)
h1.__iadd__(10)
print(h1)
h2.__radd__(10)
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__






