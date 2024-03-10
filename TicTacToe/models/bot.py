from player import Player


class Bot(Player):
    def __init__(self, symbol, difficulty_level):
        super().__init__(symbol)
        self.difficulty_level = difficulty_level

    def play(self):
        # Implementation for bot's play method
        pass

