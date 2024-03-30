from abc import ABC, abstractmethod

from TicTacToe.models.board import Board
from TicTacToe.models.cell import Cell


class PlayingStrategy(ABC):
    @abstractmethod
    def make_move(self, board: Board) -> Cell:
        pass

    @staticmethod
    def get_playing_strategy(difficulty_level):
        pass
