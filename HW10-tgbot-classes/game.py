from random import randint


class SweetsGame:

    total = 250
    max_n = 25
    is_players_turn = False

    player_name = ''
    player_id = ''

    def __init__(self, name: str, id: str):
        self.player_name = name
        self.player_id = id

        self.total = randint(200, 300)
        self.max_n = randint(15, 30)
        self.is_players_turn = randint(0, 1)

    def get_info(self) -> str:
        return f'Размер кучи конфет: {self.total}, максимум конфет за ход: {self.max_n}'

    def get_total(self) -> int:
        return self.total

    def player_turn(self, n: int) -> bool:
        if (self.total - n) < 0 or n > self.max_n or n <= 0:
            return False
        else:
            self.total -= n
            return True

    def bot_turn(self) -> int:
        if self.total <= self.max_n:
            bot_got = self.total
        else:
            bot_got = randint(1, self.max_n)
        self.total -= bot_got
        return bot_got

    def check_win(self):
        if self.total == 0:
            return True
        else:
            return False

    def __del__(self):
        print(
            f'Instance for {self.player_name} ({self.player_id}) was destroyed')
