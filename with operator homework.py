import re
class WordsFinder():

    def __init__(self,*args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:   #цикл для переборки аргументов- названий файлов
            with open (i , encoding = 'utf-8') as file:  #открытие файла под именем file
                file_read = file.read()
                file_lower = file_read.lower()
                non_signs = re.sub(r'[^\w\s]', '', file_lower)
                file_split = non_signs.split()
                all_words[i]= file_split

        return all_words
    def find(self,word):
        result = {}
        self.word = str(word)
        word_lower = self.word.lower()
        all_ = self.get_all_words()
        count1 = 0
        for name, words in all_.items():
            for i in words:
                if i == word_lower:
                    count1 +=1
                    result[name] = count1
                    break
                else:
                    count1 += 1
                    continue
        return result
    def count(self,word):
        result2 = {}
        self.word = str(word)
        word_lower = self.word.lower()
        all_ = self.get_all_words()
        count2 = 0
        for name, words in all_.items():
            for i in words:
                if i == word_lower:
                    count2 +=1
                    continue
                else:
                    continue
            result2[name]= count2


        return result2

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))






