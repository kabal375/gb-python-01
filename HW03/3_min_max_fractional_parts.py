# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, uniform
from unicodedata import decimal

source_list = []
# source_list = [1.1, 1.2, 3.1, 5, 10.01]

for _ in range(randint(3, 10)):
    fract_part = randint(0, 3)
    source_list.append(round(uniform(0, 10), fract_part))

print(f'Исходный список: {source_list}')

fmin = None
fmax = None

for i in source_list:
    f = (i - int(i))
    if f != 0:
        if (fmin is None) or (fmin > f):
            fmin = f
        if (fmax is None) or (fmax < f):
            fmax = f

print(round(fmax - fmin, 3))

