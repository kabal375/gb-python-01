# Задайте список из n чисел последовательности (1 + 1/n)^n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введите N: '))

elements = []
sum = 0

for i in range(1, n+1):
    elements.append(round((1 + 1/i)**i, 3))
    sum += elements[i-1]

print(elements)
print('Сумма элементов: {}'.format(sum))