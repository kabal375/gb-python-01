from math import modf
from datetime import datetime

def random_enough() -> float:
    current_time = datetime.now()
    base = float(str(current_time.microsecond)[3:]) / 1000 + 1
    r = base ** 3 + base ** 2 + base

    return modf(r * 1000)[0]

def random_enough_int(n: int) -> int:
    return int(random_enough() * n)

for _ in range(15):
    print(random_enough_int(70))

