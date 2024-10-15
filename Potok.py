import time   #   импорт базу для задержки
from time import sleep
from datetime import datetime  # импорт базы для подсчета времени

time_start = datetime.now()
def write_words(word_count,file_name):
    with open (file_name, 'a', encoding = 'utf8' ) as file:   #открываем файл для добавления в него строк
        for i in range(word_count):                           #   вносим количество строк которое получим в качестве аргумента
            wr_file = file.write(f'Какое то слово № {i} \n')          #   переменная представляет из себя запись в файл строки и номера
            time.sleep(0.1)                                      # задержка 0,1 млск

    print(f'Завершилась запись в файл {file_name}')

write_words(10,'example1txt')
write_words(30,'example2txt')
write_words(200,'example3txt')
write_words(100,'example4txt')
time_end = datetime.now()
time_ = time_end - time_start
print(time_)


from  threading import Thread    # импортируем базу для создания потока
import requests  #
time_start1 = datetime.now()
first = Thread(target=write_words(10,'example5txt')) # создаем обьект класса потоки, где таргет функция необходиая к выполнению
second = Thread(target=write_words(30,'example6txt'))
third = Thread(target=write_words(200,'example7txt'))
four = Thread(target=write_words(100,'example8txt'))


first.start()  # старт потока относительно обьекта класса
first.join()  # останавливает работу программы после завершения работы потока
second.start()
second.join()
third.start()
third.join()
four.start()
four.join()

time_end2 = datetime.now()
time_2 = time_end2 - time_start1
print(time_2)