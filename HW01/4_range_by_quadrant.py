# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quadrant_no = 0

while not 0 < quadrant_no < 5:
    quadrant_no = int(input('Введите номер квадранта (1-4):'))

if quadrant_no == 1:
    print('Диапаазон: (+∞;+∞)')
elif quadrant_no == 2:
    print('Диапаазон: (-∞;+∞)')
elif quadrant_no == 3:
    print('Диапаазон: (-∞;-∞)')
elif quadrant_no == 4:
    print('Диапаазон: (+∞;-∞)')
