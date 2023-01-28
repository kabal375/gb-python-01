# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint

def player_turn(max_n: int) -> int:
    n = max_n + 1
    while n > max_n:
        n = int(input(f'Введите количество конфет (меньше {max_n}): '))
    return n

def bot_turn(max_n: int, n: int) -> int:
    print('Ход бота')
    if max_n < n:
        return max_n
    else:
        return randint(1, max_n)

def next_turn(is_player_turn: bool, current_heap: int, n: int):
    if current_heap < n:
        max_n = current_heap
    else:
        max_n = n
    if is_player_turn:
        return player_turn(max_n)
    else:
        return bot_turn(max_n, n)


heap = randint(100, 250)
n = 28
print(f'Количество конфет в куче: {heap}')

print(f'Максимальное количество конфет за ход: {n}')

is_player_turn = bool(randint(0, 1))

while heap > 0:
    heap -= next_turn(is_player_turn, heap, n)
    if heap > 0:
        is_player_turn = not is_player_turn
    print(f'Количество конфет в куче: {heap}')

if is_player_turn:
    print('Победа игрока!')
else:
    print('Победа бота!')

