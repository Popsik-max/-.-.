class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']     # список с вариантами цветов
    _COLOR_LOWER = [x.lower() for x in _COLOR_VARIANTS ]            #перевод всех элементов списка в нижний регистр или верхний, неважно.
    def __init__(self, owner,__model, __engine_power, __color):            # атрибуты обьекта класса транспорт
        self.owner = owner              #  инициализиция атрибутов
        self.__model = __model          #инициализиция атрибутов
        self.__engine_power = __engine_power           #инициализиция атрибутов
        self.__color = __color              #инициализиция атрибутов

    def get_model(self):                       # метод для модели, селф это будущий созданный обьект с атрибутами
        return (f'Модель: {self.__model}')
    def get_horse_powers(self):                 # метод для мощности, селф это будущий созданный обьект с атрибутами
        return (f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):                        # метод для цвета, селф это будущий созданный обьект с атрибутами
        return (f'Цвет автомобиля: {self.__color}')
    def print_info(self,car):               # метод для инвы авто, в качестве атрибута использует обьект класса ( по сути ссылается сам на себя при выхове метода)
        self.car = car
        print(self.car.get_model())           # все методы вызываются в 1 методе, работают для переданного обьекта
        print(self.car.get_horse_powers())             # все методы вызываются в 1 методе, работают для переданного обьекта
        print(self.car.get_color())               # все методы вызываются в 1 методе, работают для переданного обьекта
        print(f'Владелец {self.owner}')  # все методы вызываются в 1 методе, работают для переданного обьекта

    def set_color(self,new_color):               # метод для смены цвета авто
        self.new_color = new_color
        if self.new_color.lower() in Vehicle._COLOR_LOWER:       # ищем новый цвет в атрибуте класса(список). Обращаемся к нему через название класса. Список перевели в нижний регистр.
            self.__color = self.new_color                  # перезаписываем значение атрибута
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info(vehicle1)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info(vehicle1)