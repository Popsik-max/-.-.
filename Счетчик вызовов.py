calls = 0
def count_call():
    global calls
    calls += 1

def string_info(string):
    count_call()
    return ((len(string)), string.upper(), string.lower())


def is_contains (string, list_to_search):
    count_call()
    for i in list_to_search:
        if string.lower() == i.lower():
            result = True
            break
        elif string.lower() != i.lower():
            result = False
            continue

    return result



print(string_info('Университет Урбан'))
print(string_info('Чем дальше, тем сложнее учиться :(, много приходится пользоваться Гуглом '))
print(is_contains('popsik', ['Pupsik', 'Popsik', 'popik'] ))
print(is_contains('AL', ['Popsik', 'Pupsik', 'popik'] ))
print(calls)






