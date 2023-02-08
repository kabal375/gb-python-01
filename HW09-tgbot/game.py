from random import randint

default_total = 250
default_max_n = 28

total = 250
min_total = 10
max_n = 28
min_n = 1
is_started = False
is_players_turn = False


def set_total(new_total: str) -> bool:
    global total
    try:
        t = int(new_total)
    except ValueError:
        return False
    if t >= min_total:
        total = t
        return True
    else:
        return False

def set_max_n(new_max_n: str) -> bool:
    global max_n
    try:
        n = int(new_max_n)
    except ValueError:
        return False
    if n >= min_total:
        max_n = n
        return True
    else:
        return False


def start_game():
    global is_players_turn
    global is_started

    is_players_turn = randint(0,1)
    is_started = True


def end_game():
    global default_total
    global default_max_n
    global is_started
       
    set_total(str(default_total))
    set_max_n(str(default_max_n))
    is_started = False

#########################
def check_turn(n: int) -> bool:
    global total
    global max_n

    if (total - n) < 0 or n > max_n or n <= 0:
        return False
    else:
        total -= n
        return True

def bot_turn():
    global total
    global max_n
    if total <= max_n:
        total = 0
    else:
        total -= randint(1, max_n)

