from threading import Thread
import time
import requests

class Knigt(Thread):

    def __init__(self, namee, power):
        self.namee = namee
        self.power = power
        super().__init__()    # обращение к материнскому классу для создания атрибутов

    def run(self):
        days = 0
        agr = 100
        print(f'{self.namee}, на нас напали!')
        while agr > 0:
            agr -= int(self.power)
            time.sleep(1)
            days += 1
            print(f'{self.namee} сражается {days} дней, осталось {agr} воинов')
        print(f'{self.namee} одержал победу спустя {days} дня/дней')

first_knight = Knigt('Sir Lancelot', 10)
second_knight = Knigt("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закочились')
