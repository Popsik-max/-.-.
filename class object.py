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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1.__str__())
print(h2.__str__())

print(h1.__len__())
print(h2.__len__())
