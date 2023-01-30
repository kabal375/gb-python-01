# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, uniform

source_list = [round(uniform(0, 10), randint(1, 3)) for _ in range(randint(3, 10))]

print(f'Исходный список: {source_list}')
#brain damaging list of fractional parts that aren't zeroes creation
fract_parts_list = list(filter(lambda i: i != 0, (map(lambda i: i - int(i), source_list))))

fmin = round(min(fract_parts_list), 3)
fmax = round(max(fract_parts_list), 3)

print(f'Макс. значение: {fmax}, мин. значение: {fmin}')
print(f'Разница: {round(fmax - fmin, 3)}')
