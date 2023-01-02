# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def create_factors(n: int) -> dict:
    factors = {}
    for i in range(0, n+1):
        factors[i] = randint(-100, 100)

    return factors


def create_equasion(factors: dict) -> str:
    eq_list = []
    x_part: str
    f_part: str

    for i in range(len(factors) - 1, -1, -1):
        if factors.get(i) != 0:
            if i == 0:
                x_part = ''
            elif i == 1:
                x_part = ' * x'
            else:
                x_part = ' * x**' + str(i)

            if factors.get(i) == 1:
                f_part = ''
                x_part = x_part.replace(' * ', '')
            else:
                f_part = str(factors.get(i))

            eq_list.append(f_part + x_part)


    return (' + '.join(eq_list) + ' = 0').replace('+ -', '- ')

def save2file(filename: str, str2save: str):
    with open(filename, "w") as f:
        f.write(str2save)

n = int(input('Введите N: '))
factors = create_factors(n)
# factors = {0: 12, 1: 50, 2: 59, 3: 0}
eq = create_equasion(factors)
print(eq)
save2file('eq2.txt', eq)