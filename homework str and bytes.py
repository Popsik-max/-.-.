class Shop():
    def __init__(self,__file_name = 'products.txt'):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name,'r')
        info = file.read()   # с помощью этой переменной мы получаем актуальный список в файл нейм, т.е. продакт txt
        file.close()
        return  info


    def add(self,*products):
        cur_info = self.get_products()
        file1 = open(self.__file_name, 'a')
        for i in products:
            if i.name in cur_info:
                print(f'Продукт {i} уже есть в магазине')
            else:

                file1.write(f'{i}\n')
        file1.close()

class Product():
    def __init__(self, name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2.__str__())
s1.add(p1, p2, p3)
print(s1.get_products())

