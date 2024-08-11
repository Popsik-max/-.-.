calls = 0
def count_call():
    global calls
    calls += 1

def string_info(string):
    count_call()
    return ((len(string)), string.upper(), string.lower())


def is_contains (string, list_to_search):
    count_call()
    if string.lower() in list_to_search:
        print('Элемент есть в списке:', True)

    else:
        print('Элемента нет в списке:', False)
list_to_search = ['Popsik', 'Pupsik', 'poPIK']
list_lower = [word.lower() for word in list_to_search ]


print(string_info('Университет Урбан'))
print(string_info('Чем дальше, тем сложнее учиться :(, много приходится пользоваться Гуглом '))
(is_contains('popsik', list_lower))
(is_contains('ALMAZ', list_lower))
print(calls)







