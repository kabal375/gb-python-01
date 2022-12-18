# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def expression(x, y, z):
    return not(x and y and z) == (not x) or (not y) or (not z)

print('Результаты выражения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  при различных значениях предикат:')
print('X     Y      Z')
print(f'True, False, False - {expression(True, False, False)}')
print(f'True, True, False - {expression(True, True, False)}')
print(f'True, False, True - {expression(True, False, True)}')
print(f'True, True, True - {expression(True, True, True)}')
print(f'False, True, True - {expression(False, True, True)}')
print(f'False, False, True - {expression(False, False, True)}')
print(f'False, True, False - {expression(False, True, False)}')
print(f'False, False, False - {expression(False, False, False)}')

