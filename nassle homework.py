class Animal:    # класс животные
    alive = True   # атрибут класса животные
    fed = False     # атрибут класса животные
    def __init__(self, name):   # инициализирует создание обьектов класса животные с переменной "имя"
        self.name = name

class Predator(Animal):   # класс хищники, имеет материнский класс животные
    def eat(self, food):        # метод, который принимает в качестве аргумента обьект другого класса фууд == обьект класса Растения
        self.food = food.name       # позволяет обратиться к названию обьекта?
        if food.edible == True:      # обращается к атрибуту обьекта фууд. Данный атрибут в этой задаче заложен либо в материнском классе, либо в дочернем.
            Predator.fed = True
            print(f'{self.name} съел {self.food}')
        else:
            Predator.alive = False
            print(f'{self.name} не стал есть {self.food}')
    pass
class Mammal(Animal):
    def eat(self, food):
        self.food = food.name
        if food.edible == True:
            Mammal.fed = True
            print(f'{self.name} съел {self.food}')
        else:
            Mammal.alive = False
            print(f'{self.name} не стал есть {self.food}')

    pass

class Plant:
    edible = False         #  атрибут материнского класса
    def __init__(self, name):        # инициализация обьектов дочерних классов
        self.name = name
class Flower(Plant):           # пустой класс, инициализация происходит за счет инита в материнском классе
    pass
class Fruit(Plant):            # # пустой класс, инициализация происходит за счет инита в материнском классе. + создан внутри класса свой атрибут, точнее перезаписан.
    edible = True
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)    # здесь к обьекту класса животные применяется метод, который берет в качестве атрибута обьект другог класса.
a2.eat(p2)
print(a1.alive)
print(a2.fed)

