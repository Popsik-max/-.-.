# class Human:
#     def __init__(self, name, group):
#         self.name = name
#         super().__init__(group)  # через метод супер обращаемся уже в материнском классе к следующему в очереди наследованию классу. В данном случае студенческая группа
#         super().about()
#
#     def info(self):
#         print(f'Hi, my name is {self.name}')
#
#
# class StudentGroup:
#     def __init__(self, group):
#         self.group = group
#
#     def about(self):
#         print(f'{self.name} in {self.group}')
#
# class Student(Human, StudentGroup):
#     def __init__(self, name, place, group):
#         super().__init__(name, group)             # через метод супер обращаемся к материнскому классу
#         self.place = place
#         super().info()

# # human = Human('Denis')
# # print((human.name ))
# student = Student('Denis', 'Urban', 'p1')
#
# print(Student.mro())  # c помощью mro вызываем цепочку наследования класса студенты


# HOME WORK

class Horse:
    def __init__(self, x_distance = 0, sound = 'Frrr', y_distance = 0 ):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)
    def run(self, dx):
         self.x_distance += dx
         return self.x_distance

class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):
    def __init__(self,x_distance, sound, y_distance ):
        super().__init__(x_distance, sound ,y_distance)

    def move(self, dx,dy):
        self.dx = super().run(dx)
        self.dy = super().fly(dy)

    def get_pos(self):
        return (self.x_distance , self.y_distance)

    def voice(self):
        print(f'{self.sound}')

p1 = Pegasus(0,'Frrr',0)
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move( -5,20)
print(p1.get_pos())
p1.voice()




