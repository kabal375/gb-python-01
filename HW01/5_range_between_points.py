# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

def find_range(ax, ay, bx, by):
    return ((bx - ax)**2 + (by - ay)**2)**0.5

ax = float(input('Введите Ax: '))
ay = float(input('Введите Ay: '))
bx = float(input('Введите Bx: '))
by = float(input('Введите By: '))

print(f'Расстояние между точками: {round(find_range(ax, ay, bx, by), 2)}')