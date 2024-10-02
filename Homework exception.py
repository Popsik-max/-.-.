class Car:
    def __init__(self, model,__vin,__numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(__vin)   # при создании атрибута, вызываем методы класса
        self.__numbers = self.__is_valid_numbers(__numbers)    # при создании атрибута, вызываем методы класса

    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        cor_vin = isinstance(self.vin_number,int)  #  переменная для вина
        cor_vin2 = self.vin_number in range(100000,9999999)  #  #  переменная для вина
        if cor_vin == False:
            raise IncorrectVinNumber('Некорректный тип vin номера')
        elif cor_vin2 == False:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self,numbers):
        self.numbers = numbers
        cor_num = isinstance(self.numbers,str)   #  переменная для номера
        cor_num2 = len(self.numbers)    #  переменная для номера
        if cor_num == False:
            raise IncorrectCarNumbers('Некорректный тип данных для номера')  # ссылается на класс с ошибкой
        elif cor_num2 != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

class IncorrectVinNumber(Exception):        # класс для райса с атрибутом в виде переменной сообщения
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):     # класс для райса с атрибутом в виде переменной сообщения
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
