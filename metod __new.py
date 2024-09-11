# print(int.__mro__)      # цепочка наследования данного класса
# print(object)

# class User:
#
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         print('Я в нью')
#         if cls.__instance is None:
#               cls.__instance = super(). __new__(cls)  # метод супер вызывает ссылку на класс
#         return cls.__instance
#
#     def __init__(self,*args, **kwargs):
#         print(('Я в ините'))
#         self.args = args
#         self.kwargs = kwargs
#         self.name = kwargs.get('name')
#         for key,values in kwargs.items():
#             setattr(self,key, values)
#
# other = [1,2,3]
# user = {'name':'Den', 'age':25, 'gender': 'male'}
#
# user1 = User(*other, **user)
# print(user1.args)
# print(user1.name)
# print(user1.age)
# print(user1.gender)

class House():
    houses_history = []

    def __new__(cls, *args,**kwargs):        # cls = созданный класс Дома, при создании обьектов в котором буду аргументы позиционные и именованные
        cls.houses_history.append(args[0])      #  берем класс Дома и в его атрибут добавляем атрибут будущего обекта класса Дома с индексом 0
        return super().__new__(cls)          # ссылаемся на класс созданный (Дома), иначе инит не сработает. Дает в методе нью использовать методы класса Дома

    def __init__(self, name, number_of_floor):  # обьект/экземпляр класса со своими атрибутами
        self.name = name # имя обекта = имя 1 атрибта

    def __del__(self): # деструктор, удаляет при выполнении кода
        print(f'{self.name} снесен, но он останется в истории') #




h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
input()    # чтобы деструктор не сработал автоматически на оставшийся обьект в классе


