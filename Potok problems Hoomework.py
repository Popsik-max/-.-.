import  threading
import time
import random

class Bank():
    def __init__(self,balance):
        self.balance = balance

    def deposit(self):
        operation = 100
        while operation > 0:
            rand = random.randint(50, 500)
            self.balance+= rand
            if self.balance >= 500:
                operation -= 1
                print(f'Пополнение: {rand}. Баланс {self.balance}')
                time.sleep(0.001)
            else:
                operation -= 1
                print(f'Пополнение: {rand}. Баланс {self.balance}')
                time.sleep(0.001)
    def take(self):

        operation2 = 100
        while operation2 > 0:
            rand2 = random.randint(50,500)
            print(f'Запрос на  {rand2}')
            if self.balance >= rand2:
                self.balance -= rand2
                print(f'Снятие:{rand2}.Баланс: {self.balance}')
                operation2 -=1
                time.sleep(0.001)
            else:
                print(f'Запрос отклонен,недостаточно средств')
                operation2 -= 1
                time.sleep(0.001)




bk = Bank(0)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')