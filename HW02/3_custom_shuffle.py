# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint

def shuffle_list(source_list):
    new_list = []
    scope = len(source_list) - 1
    for i in range(len(source_list)):
        e_index = randint(0, scope)
        new_list.append(source_list[e_index])
        source_list.remove(source_list[e_index])
        scope -= 1
    return new_list

source_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'Исходный список: {source_list}')
print(f'Перемешанный список: {shuffle_list(source_list)}')

