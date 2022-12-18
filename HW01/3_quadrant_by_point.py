# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = 0
y = 0
quadrant_no = 0

while x == 0:
    x = float(input('Введите Х (не 0): '))
while y == 0:
    y = float(input('Введите Y (не 0): '))

if x > 0 and y > 0:
    quadrant_no = 1
elif x < 0 and y > 0:
    quadrant_no = 2
elif x < 0 and y < 0:
    quadrant_no = 3
elif x > 0 and y < 0:
    quadrant_no = 4

print('Точка находится в {} квадранте'.format(quadrant_no))


