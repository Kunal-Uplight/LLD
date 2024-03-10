from player import Player
from TicTacToe.models.symbol import Symbol
from user import User


class HumanPlayer(Player):
    def __init__(self, symbol: Symbol, user: User):
        super().__init__(symbol)
        self.user = user

    def play(self):
        # Implementation for human player's play method
        pass
