# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

source_list = [randint(-10, 10) for i in range(randint(3, 10))]
odd_sum = sum([source_list[i] for i in range(len(source_list)) if i % 2 == 1])

print(f'Исходный список: {source_list}')
print(odd_sum)
