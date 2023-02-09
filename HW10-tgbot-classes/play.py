from game import SweetsGame

class Play:
    games = dict()



    def start_game(cls, player_name: str, player_id: str):
        cls.games[player_id] = SweetsGame(player_name, player_id)
        return cls.get_instance(cls, player_id)

    def stop_game(cls, player_id):
        cls.games.pop(player_id)

    def get_instance(cls, player_id):
        return cls.games.get(player_id)


        