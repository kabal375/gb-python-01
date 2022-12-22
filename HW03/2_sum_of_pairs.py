# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

source_list = []
res_list = []
res_list_len = 0

for _ in range(randint(3, 10)):
    source_list.append(randint(-10, 10))

print(f'Исходный список: {source_list}')

if len(source_list) % 2 == 0:
    res_list_len = len(source_list) // 2
else:
    res_list_len = len(source_list)//2 + 1

for i in range(res_list_len):
    res_list.append(source_list[i] + source_list[len(source_list) - 1 - i])

print(f'Список сумм: {res_list}')
