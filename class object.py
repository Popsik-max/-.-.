# class Human:
#     def __init__(self, name, age):
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

# den = Human('Денис',22)
# max = Human("Макс",22)
# max.bir()

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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


