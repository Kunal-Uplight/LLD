from abc import ABC, abstractmethod

from TicTacToe.models.board import Board
from TicTacToe.models.cell import Cell
from TicTacToe.models.symbol import Symbol


class Player(ABC):
    def __init__(self, symbol):
        self.symbol = Symbol(symbol)

    @abstractmethod
    def make_move(self, board: Board) -> Cell:
        pass
