from abc import ABC, abstractmethod

from TicTacToe.models.symbol import Symbol


class Player(ABC):
    def __init__(self, symbol):
        self.symbol = Symbol(symbol)

    @abstractmethod
    def play(self):
        pass
