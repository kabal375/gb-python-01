# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

source = input('Введите число: ')
sum = 0

for s in source:
    if s.isdigit():
        sum += int(s)

print(sum)