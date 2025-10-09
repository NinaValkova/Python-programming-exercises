from player import Player

class Team:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @property
    def players(self):
        return self.__players
    

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.players.append(player)

        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                player_temp = player
                self.__players.remove(player)
                return player_temp

        return f"Player {player_name} not found"
